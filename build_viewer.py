#!/usr/bin/env python3
# v2.0.0 2026-05-06 Notion-style HTML course viewer with embedded images

import json, re, base64
from pathlib import Path

BASE = Path(__file__).parent

COURSES = {
    "GitHub 官方課程": [
        {"id": "api",    "title": "API Fundamentals",                    "dir": "01_api_fundamentals",    "emoji": "🔑"},
        {"id": "pe",     "title": "Prompt Engineering Tutorial",          "dir": "02_prompt_engineering",  "emoji": "✍️"},
        {"id": "rwp",    "title": "Real World Prompting",                 "dir": "03_real_world_prompting","emoji": "🌍"},
        {"id": "eval",   "title": "Prompt Evaluations",                   "dir": "04_prompt_evaluations",  "emoji": "📊"},
        {"id": "tool",   "title": "Tool Use",                             "dir": "05_tool_use",            "emoji": "🔧"},
    ],
    "Skilljar 影片課程": [
        {"id": "s01", "title": "Claude 101",                              "file": "01_claude_101.md",            "emoji": "👋"},
        {"id": "s02", "title": "Claude Code 101",                         "file": "02_claude_code_101.md",       "emoji": "💻"},
        {"id": "s03", "title": "Introduction to Claude Cowork",           "file": "03_claude_cowork.md",         "emoji": "🤝"},
        {"id": "s04", "title": "Claude Code in Action",                   "file": "04_claude_code_in_action.md", "emoji": "⚡"},
        {"id": "s05", "title": "AI Fluency: Framework & Foundations",     "file": "05_ai_fluency_framework.md",  "emoji": "🧠"},
        {"id": "s06", "title": "Building with the Claude API",            "file": "06_building_with_api.md",     "emoji": "🏗️"},
        {"id": "s07", "title": "Introduction to MCP",                     "file": "07_intro_mcp.md",             "emoji": "🔌"},
        {"id": "s08", "title": "AI Fluency for Educators",                "file": "08_ai_fluency_educators.md",  "emoji": "🏫"},
        {"id": "s09", "title": "AI Fluency for Students",                 "file": "09_ai_fluency_students.md",   "emoji": "🎓"},
        {"id": "s10", "title": "MCP Advanced Topics",                     "file": "10_mcp_advanced.md",          "emoji": "⚙️"},
        {"id": "s11", "title": "Claude with Amazon Bedrock",              "file": "11_claude_bedrock.md",        "emoji": "☁️"},
        {"id": "s12", "title": "Claude with Google Vertex AI",            "file": "12_claude_vertex.md",         "emoji": "🌐"},
        {"id": "s13", "title": "Enterprise Train the Trainer",            "file": "13_enterprise_train.md",      "emoji": "🏢"},
        {"id": "s14", "title": "AI Fluency for Nonprofits",               "file": "14_ai_fluency_nonprofits.md", "emoji": "💚"},
        {"id": "s15", "title": "Introduction to Agent Skills",            "file": "15_agent_skills.md",          "emoji": "🤖"},
        {"id": "s16", "title": "Introduction to Subagents",               "file": "16_subagents.md",             "emoji": "👥"},
        {"id": "s17", "title": "AI Capabilities and Limitations",         "file": "17_ai_capabilities.md",       "emoji": "⚖️"},
    ],
}

def load_md(path):
    try:
        return path.read_text(encoding="utf-8")
    except:
        return f"# {path.name}\n\n*(file not found)*"

def build_content_map():
    content = {}
    for group, courses in COURSES.items():
        for c in courses:
            if "dir" in c:
                d = BASE / c["dir"]
                files = sorted(f for f in d.glob("*.md") if not f.name.startswith("00_README"))
                combined = "\n\n---\n\n".join(load_md(f) for f in files)
                content[c["id"]] = combined
            else:
                content[c["id"]] = load_md(BASE / "00_skilljar_full" / c["file"])
    return content

def build_image_map():
    """Encode all images as base64 data URIs for self-contained HTML."""
    img_dir = BASE / "images"
    img_map = {}
    if not img_dir.exists():
        return img_map
    for f in img_dir.iterdir():
        ext = f.suffix.lower()
        mime = {
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".gif": "image/gif",
            ".svg": "image/svg+xml",
            ".webp": "image/webp",
        }.get(ext, "image/png")
        b64 = base64.b64encode(f.read_bytes()).decode()
        img_map[f.name] = f"data:{mime};base64,{b64}"
    return img_map

def build_sidebar():
    lines = []
    for group, courses in COURSES.items():
        lines.append(f'<div class="group-label">{group}</div>')
        for c in courses:
            lines.append(
                f'<div class="course-item" onclick="showCourse(\'{c["id"]}\')" id="nav-{c["id"]}">'
                f'<span class="course-emoji">{c["emoji"]}</span>'
                f'<span class="course-name">{c["title"]}</span></div>'
            )
    return "\n".join(lines)

def main():
    print("📦 Loading course content...")
    content_map = build_content_map()
    total_kb = sum(len(v) for v in content_map.values()) // 1024
    print(f"   {len(content_map)} courses, ~{total_kb} KB text")

    print("🖼️  Encoding images...")
    img_map = build_image_map()
    img_kb = sum(len(v) for v in img_map.values()) // 1024
    print(f"   {len(img_map)} images, ~{img_kb} KB encoded")

    sidebar_html = build_sidebar()
    content_json = json.dumps(content_map, ensure_ascii=False)
    img_json = json.dumps(img_map, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Anthropic Academy — 課程庫</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  :root {{
    --bg: #ffffff;
    --bg-sidebar: #f7f7f5;
    --bg-hover: #efefed;
    --bg-active: #e9e9e7;
    --bg-code: #f1f1ef;
    --bg-code-block: #f7f6f3;
    --border: #e9e9e7;
    --border-light: #f0f0ee;
    --text: #37352f;
    --text-muted: #9b9a97;
    --text-light: #6b6966;
    --text-sidebar: #37352f;
    --accent: #e8590c;
    --accent-bg: #fff3ee;
    --link: #2383e2;
    --heading: #37352f;
    --code-text: #e83e8c;
    --shadow: 0 1px 3px rgba(0,0,0,.06);
    --radius: 4px;
  }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: var(--bg);
    color: var(--text);
    display: flex;
    height: 100vh;
    overflow: hidden;
    font-size: 15px;
    line-height: 1.6;
  }}

  /* ── Sidebar ── */
  #sidebar {{
    width: 260px;
    min-width: 260px;
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }}

  #sidebar-header {{
    padding: 16px 14px 10px;
    border-bottom: 1px solid var(--border);
  }}

  .brand {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .brand-icon {{
    width: 28px;
    height: 28px;
    background: var(--text);
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 14px;
    font-weight: 700;
    flex-shrink: 0;
  }}

  .brand-text h1 {{
    font-size: 14px;
    font-weight: 600;
    color: var(--text);
    line-height: 1.2;
  }}

  .brand-text p {{
    font-size: 11px;
    color: var(--text-muted);
    margin-top: 1px;
  }}

  #search-wrap {{
    padding: 8px 10px;
    border-bottom: 1px solid var(--border);
  }}

  #search {{
    width: 100%;
    padding: 6px 10px;
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    color: var(--text);
    font-size: 13px;
    font-family: inherit;
    outline: none;
    transition: border-color .15s;
  }}

  #search::placeholder {{ color: var(--text-muted); }}
  #search:focus {{ border-color: #aaa; }}

  #nav {{ overflow-y: auto; flex: 1; padding: 6px 0 12px; }}

  .group-label {{
    padding: 8px 14px 4px;
    font-size: 11px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: .06em;
    user-select: none;
  }}

  .course-item {{
    display: flex;
    align-items: center;
    gap: 7px;
    padding: 5px 12px 5px 14px;
    cursor: pointer;
    border-radius: var(--radius);
    margin: 0 6px;
    transition: background .1s;
    user-select: none;
  }}

  .course-item:hover {{ background: var(--bg-hover); }}
  .course-item.active {{ background: var(--bg-active); }}

  .course-emoji {{ font-size: 14px; flex-shrink: 0; width: 20px; text-align: center; }}
  .course-name {{ font-size: 13px; color: var(--text-sidebar); line-height: 1.4; }}
  .course-item.active .course-name {{ font-weight: 500; }}

  /* ── Main ── */
  #main {{
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: var(--bg);
  }}

  #topbar {{
    padding: 0 32px;
    height: 45px;
    display: flex;
    align-items: center;
    border-bottom: 1px solid var(--border);
    gap: 12px;
    flex-shrink: 0;
  }}

  #breadcrumb {{
    font-size: 13px;
    color: var(--text-muted);
    flex: 1;
  }}

  #breadcrumb span {{
    color: var(--text);
    font-weight: 500;
  }}

  #toc-btn {{
    font-size: 12px;
    padding: 4px 10px;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    background: var(--bg);
    color: var(--text-light);
    cursor: pointer;
    font-family: inherit;
    transition: all .15s;
  }}

  #toc-btn:hover {{ background: var(--bg-hover); border-color: #ccc; color: var(--text); }}

  #content-wrap {{ flex: 1; display: flex; overflow: hidden; }}

  /* ── TOC ── */
  #toc {{
    width: 200px;
    min-width: 200px;
    background: var(--bg-sidebar);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    padding: 16px 0;
    display: none;
  }}

  #toc .toc-title {{
    font-size: 11px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: .06em;
    padding: 0 14px 8px;
  }}

  #toc a {{
    display: block;
    padding: 3px 14px;
    font-size: 12.5px;
    color: var(--text-light);
    text-decoration: none;
    line-height: 1.5;
    border-left: 2px solid transparent;
    transition: all .1s;
  }}

  #toc a:hover {{ color: var(--text); background: var(--bg-hover); }}
  #toc a.active {{ color: var(--accent); border-left-color: var(--accent); }}
  #toc a.h3 {{ padding-left: 24px; font-size: 12px; }}
  #toc a.h4 {{ padding-left: 34px; font-size: 11.5px; }}

  /* ── Content ── */
  #content-scroll {{
    flex: 1;
    overflow-y: auto;
    padding: 40px 80px 80px;
  }}

  #content {{
    max-width: 720px;
    margin: 0 auto;
  }}

  /* Notion-style typography */
  #content h1 {{
    font-size: 30px;
    font-weight: 700;
    color: var(--heading);
    margin: 0 0 6px;
    line-height: 1.3;
    letter-spacing: -.02em;
  }}

  #content h2 {{
    font-size: 20px;
    font-weight: 600;
    color: var(--heading);
    margin: 36px 0 8px;
    letter-spacing: -.01em;
    line-height: 1.35;
  }}

  #content h3 {{
    font-size: 17px;
    font-weight: 600;
    color: var(--heading);
    margin: 24px 0 6px;
    line-height: 1.4;
  }}

  #content h4 {{
    font-size: 15px;
    font-weight: 600;
    color: var(--heading);
    margin: 18px 0 4px;
  }}

  #content p {{
    font-size: 15px;
    line-height: 1.75;
    color: var(--text);
    margin-bottom: 10px;
  }}

  #content ul, #content ol {{
    padding-left: 24px;
    margin-bottom: 10px;
  }}

  #content li {{
    font-size: 15px;
    line-height: 1.7;
    color: var(--text);
    margin-bottom: 3px;
  }}

  #content li > ul, #content li > ol {{
    margin-top: 4px;
    margin-bottom: 4px;
  }}

  #content strong {{ font-weight: 600; color: var(--text); }}

  #content em {{ color: var(--text-light); }}

  #content code {{
    background: var(--bg-code);
    color: var(--code-text);
    padding: 1px 5px;
    border-radius: 3px;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 13px;
    border: 1px solid var(--border);
  }}

  #content pre {{
    background: var(--bg-code-block);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 18px 20px;
    margin: 14px 0;
    overflow-x: auto;
  }}

  #content pre code {{
    background: none;
    color: #37352f;
    padding: 0;
    border: none;
    font-size: 13px;
    line-height: 1.65;
  }}

  #content blockquote {{
    border-left: 3px solid var(--border);
    padding: 8px 16px;
    margin: 12px 0;
    color: var(--text-light);
    background: var(--bg-sidebar);
    border-radius: 0 4px 4px 0;
  }}

  #content blockquote p {{ color: var(--text-light); margin: 0; }}

  #content hr {{
    border: none;
    border-top: 1px solid var(--border);
    margin: 32px 0;
  }}

  #content a {{
    color: var(--link);
    text-decoration: underline;
    text-underline-offset: 2px;
  }}

  #content a:hover {{ text-decoration: none; }}

  #content img {{
    max-width: 100%;
    border-radius: 6px;
    border: 1px solid var(--border);
    margin: 12px 0;
    display: block;
  }}

  /* YouTube thumbnail links */
  #content a img {{
    border: none;
    transition: opacity .15s;
  }}
  #content a img:hover {{ opacity: .85; }}
  #content blockquote a img {{
    border-radius: 8px;
    max-width: 480px;
    width: 100%;
  }}

  #content table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    margin: 14px 0;
  }}

  #content th {{
    background: var(--bg-code-block);
    padding: 8px 12px;
    text-align: left;
    font-weight: 600;
    border: 1px solid var(--border);
    font-size: 13px;
  }}

  #content td {{
    padding: 7px 12px;
    border: 1px solid var(--border);
    vertical-align: top;
  }}

  #content tr:nth-child(even) td {{ background: var(--bg-sidebar); }}

  /* Welcome screen */
  #welcome {{
    text-align: center;
    padding: 80px 20px;
    color: var(--text-muted);
  }}

  .welcome-icon {{
    font-size: 48px;
    margin-bottom: 20px;
    display: block;
  }}

  #welcome h2 {{
    font-size: 24px;
    color: var(--text);
    font-weight: 600;
    margin-bottom: 10px;
  }}

  #welcome p {{
    font-size: 14px;
    line-height: 1.8;
    color: var(--text-muted);
  }}

  .welcome-stats {{
    display: flex;
    gap: 24px;
    justify-content: center;
    margin: 24px 0;
  }}

  .stat-box {{
    background: var(--bg-sidebar);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 20px;
    text-align: center;
  }}

  .stat-box .num {{
    font-size: 22px;
    font-weight: 700;
    color: var(--text);
    display: block;
  }}

  .stat-box .label {{
    font-size: 12px;
    color: var(--text-muted);
    margin-top: 2px;
  }}

  /* Scrollbar */
  ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
  ::-webkit-scrollbar-track {{ background: transparent; }}
  ::-webkit-scrollbar-thumb {{ background: #d9d9d7; border-radius: 3px; }}
  ::-webkit-scrollbar-thumb:hover {{ background: #bbb; }}

  /* Dark mode */
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #191919;
      --bg-sidebar: #1f1f1f;
      --bg-hover: #2a2a2a;
      --bg-active: #2e2e2e;
      --bg-code: #282828;
      --bg-code-block: #222222;
      --border: #2e2e2e;
      --border-light: #282828;
      --text: #e6e3de;
      --text-muted: #6b6866;
      --text-light: #9b9893;
      --text-sidebar: #e6e3de;
      --accent: #f4a261;
      --accent-bg: #2a1f14;
      --link: #6fb3e8;
      --heading: #e6e3de;
      --code-text: #f06292;
      --shadow: 0 1px 3px rgba(0,0,0,.3);
    }}
    .brand-icon {{ background: #e6e3de; color: #191919; }}
    #content pre code {{ color: #d4d0cb; }}
  }}
</style>
</head>
<body>

<div id="sidebar">
  <div id="sidebar-header">
    <div class="brand">
      <div class="brand-icon">A</div>
      <div class="brand-text">
        <h1>Anthropic Academy</h1>
        <p>22 courses · GitHub + Skilljar</p>
      </div>
    </div>
  </div>
  <div id="search-wrap">
    <input id="search" type="text" placeholder="搜尋課程..." oninput="filterCourses(this.value)">
  </div>
  <div id="nav">
    {sidebar_html}
  </div>
</div>

<div id="main">
  <div id="topbar">
    <div id="breadcrumb">Anthropic Academy &nbsp;/&nbsp; <span id="course-title-span">選擇課程</span></div>
    <button id="toc-btn" onclick="toggleToc()">目錄</button>
  </div>
  <div id="content-wrap">
    <div id="toc"><div class="toc-title">目錄</div></div>
    <div id="content-scroll">
      <div id="content">
        <div id="welcome">
          <span class="welcome-icon">📚</span>
          <h2>Anthropic Academy 課程庫</h2>
          <div class="welcome-stats">
            <div class="stat-box"><span class="num">22</span><div class="label">門課程</div></div>
            <div class="stat-box"><span class="num">5</span><div class="label">GitHub 課程</div></div>
            <div class="stat-box"><span class="num">17</span><div class="label">Skilljar 課程</div></div>
          </div>
          <p>點擊左側課程開始閱讀</p>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
const COURSES = {content_json};
const IMAGES = {img_json};

marked.setOptions({{
  breaks: true,
  gfm: true,
}});

// Custom renderer to replace image paths with base64 data URIs
const renderer = new marked.Renderer();
renderer.image = function(href, title, text) {{
  // href could be an object in newer marked versions
  let src = (typeof href === 'object' && href !== null) ? (href.href || href) : href;
  // Extract filename from path like "images/foo.png"
  const filename = String(src).split('/').pop();
  const dataUri = IMAGES[filename];
  if (dataUri) src = dataUri;
  const titleAttr = title ? ` title="${{title}}"` : '';
  const altAttr = text ? ` alt="${{text}}"` : '';
  return `<img src="${{src}}"${{altAttr}}${{titleAttr}}>`;
}};

marked.use({{ renderer }});

function showCourse(id) {{
  document.querySelectorAll('.course-item').forEach(el => el.classList.remove('active'));
  const nav = document.getElementById('nav-' + id);
  if (nav) nav.classList.add('active');

  const md = COURSES[id] || '*(no content)*';
  const html = marked.parse(md);
  const content = document.getElementById('content');
  content.innerHTML = html;

  const scroll = document.getElementById('content-scroll');
  scroll.scrollTop = 0;

  const title = nav ? nav.querySelector('.course-name').innerText : id;
  document.getElementById('course-title-span').textContent = title;

  buildToc();
}}

function buildToc() {{
  const toc = document.getElementById('toc');
  const headings = document.getElementById('content').querySelectorAll('h1,h2,h3,h4');
  toc.innerHTML = '<div class="toc-title">目錄</div>';
  if (headings.length < 3) return;

  headings.forEach((h, i) => {{
    const id = 'h-' + i;
    h.id = id;
    const cls = h.tagName.toLowerCase();
    const a = document.createElement('a');
    a.href = '#' + id;
    a.className = cls;
    a.textContent = h.textContent.slice(0, 55);
    a.onclick = (e) => {{
      e.preventDefault();
      h.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
    }};
    toc.appendChild(a);
  }});
}}

function toggleToc() {{
  const toc = document.getElementById('toc');
  toc.style.display = toc.style.display === 'block' ? 'none' : 'block';
}}

function filterCourses(q) {{
  q = q.toLowerCase();
  document.querySelectorAll('.course-item').forEach(el => {{
    el.style.display = el.querySelector('.course-name').innerText.toLowerCase().includes(q) ? '' : 'none';
  }});
  document.querySelectorAll('.group-label').forEach(el => {{
    const siblings = [];
    let next = el.nextElementSibling;
    while (next && next.classList.contains('course-item')) {{
      siblings.push(next);
      next = next.nextElementSibling;
    }}
    el.style.display = siblings.some(s => s.style.display !== 'none') ? '' : 'none';
  }});
}}
</script>
</body>
</html>"""

    out = BASE / "index.html"
    out.write_text(html, encoding="utf-8")
    size_kb = out.stat().st_size // 1024
    size_mb = size_kb / 1024
    print(f"✅ index.html 生成完成 ({size_mb:.1f} MB)")
    print(f"   open {out}")

if __name__ == "__main__":
    main()
