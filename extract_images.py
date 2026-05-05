#!/usr/bin/env python3
# v1.0.0 2026-05-05 Extract base64 images from GitHub .ipynb files

import json, base64, subprocess, re
from pathlib import Path

BASE = Path(__file__).parent
IMG_DIR = BASE / "images"
IMG_DIR.mkdir(exist_ok=True)

# GitHub repo: anthropics/courses — map folder → local md dir
REPO_DIRS = [
    ("anthropic_api_fundamentals",          BASE / "01_api_fundamentals"),
    ("prompt_engineering_interactive_tutorial", BASE / "02_prompt_engineering"),
    ("real_world_prompting",                BASE / "03_real_world_prompting"),
    ("prompt_evaluations",                  BASE / "04_prompt_evaluations"),
    ("tool_use",                            BASE / "05_tool_use"),
]

def gh_list_files(path):
    """List all files in a GitHub repo path recursively (BFS)."""
    result = []
    queue = [path]
    while queue:
        p = queue.pop(0)
        r = subprocess.run(
            ["gh", "api", f"repos/anthropics/courses/contents/{p}",
             "--jq", "[.[] | {name: .name, path: .path, type: .type, download_url: .download_url}]"],
            capture_output=True, text=True
        )
        if r.returncode != 0:
            print(f"  ⚠️  {p}: {r.stderr.strip()}")
            continue
        items = json.loads(r.stdout)
        for item in items:
            if item["type"] == "dir":
                queue.append(item["path"])
            elif item["name"].endswith(".ipynb"):
                result.append(item)
    return result

def download_ipynb(download_url):
    """Download .ipynb file content via curl."""
    r = subprocess.run(["curl", "-sL", download_url], capture_output=True)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except:
        return None

def extract_attachments(nb_data, notebook_name):
    """Extract all attachment images from notebook cells."""
    saved = {}
    cells = nb_data.get("cells", [])
    for cell in cells:
        attachments = cell.get("attachments", {})
        for filename, mime_dict in attachments.items():
            for mime_type, b64_data in mime_dict.items():
                if isinstance(b64_data, str):
                    img_bytes = base64.b64decode(b64_data)
                    out_path = IMG_DIR / filename
                    out_path.write_bytes(img_bytes)
                    saved[filename] = str(out_path)
                    print(f"    ✅ {filename} ({len(img_bytes)//1024}KB)")
    return saved

def update_md_references(md_dir):
    """Replace attachment:xxx.png with images/xxx.png in all .md files."""
    count = 0
    for md_file in md_dir.glob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        new_text = re.sub(r'\(attachment:([^)]+)\)', r'(images/\1)', text)
        if new_text != text:
            md_file.write_text(new_text, encoding="utf-8")
            changes = text.count("attachment:")
            print(f"  📝 {md_file.name}: replaced {changes} attachment refs")
            count += changes
    return count

def main():
    all_saved = {}

    for repo_dir, local_dir in REPO_DIRS:
        print(f"\n📂 {repo_dir}")
        files = gh_list_files(repo_dir)
        print(f"   Found {len(files)} .ipynb files")

        for f in files:
            print(f"  ⬇️  {f['path']}")
            nb = download_ipynb(f["download_url"])
            if nb is None:
                print(f"    ❌ Failed to download")
                continue
            saved = extract_attachments(nb, f["name"])
            all_saved.update(saved)

    print(f"\n📸 Total images extracted: {len(all_saved)}")

    print("\n🔗 Updating MD file references...")
    total_refs = 0
    for _, local_dir in REPO_DIRS:
        total_refs += update_md_references(local_dir)
    print(f"   Total references updated: {total_refs}")

    print(f"\n✅ Done! Images saved to: {IMG_DIR}")

if __name__ == "__main__":
    main()
