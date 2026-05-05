#!/usr/bin/env python3
# v5.0.0 2026-05-06 Fix: capture YouTube embeds + inline images

import os, re, time, json
from pathlib import Path
from playwright.sync_api import sync_playwright

EMAIL    = os.environ.get("SKILLJAR_EMAIL", "")
PASSWORD = os.environ.get("SKILLJAR_PASS", "")
SESSION_FILE = Path(__file__).parent / ".skilljar_session.json"
OUTPUT_DIR   = Path(__file__).parent / "00_skilljar_full"
OUTPUT_DIR.mkdir(exist_ok=True)

COURSES = [
    ("01_claude_101",            "https://anthropic.skilljar.com/claude-101"),
    ("02_claude_code_101",       "https://anthropic.skilljar.com/claude-code-101"),
    ("03_claude_cowork",         "https://anthropic.skilljar.com/introduction-to-claude-cowork"),
    ("04_claude_code_in_action", "https://anthropic.skilljar.com/claude-code-in-action"),
    ("05_ai_fluency_framework",  "https://anthropic.skilljar.com/ai-fluency-framework-foundations"),
    ("06_building_with_api",     "https://anthropic.skilljar.com/claude-with-the-anthropic-api"),
    ("07_intro_mcp",             "https://anthropic.skilljar.com/introduction-to-model-context-protocol"),
    ("08_ai_fluency_educators",  "https://anthropic.skilljar.com/ai-fluency-for-educators"),
    ("09_ai_fluency_students",   "https://anthropic.skilljar.com/ai-fluency-for-students"),
    ("10_mcp_advanced",          "https://anthropic.skilljar.com/model-context-protocol-advanced-topics"),
    ("11_claude_bedrock",        "https://anthropic.skilljar.com/claude-in-amazon-bedrock"),
    ("12_claude_vertex",         "https://anthropic.skilljar.com/claude-with-google-vertex"),
    ("13_enterprise_train",      "https://anthropic.skilljar.com/enterprise-train-the-trainer"),
    ("14_ai_fluency_nonprofits", "https://anthropic.skilljar.com/ai-fluency-for-nonprofits"),
    ("15_agent_skills",          "https://anthropic.skilljar.com/introduction-to-agent-skills"),
    ("16_subagents",             "https://anthropic.skilljar.com/introduction-to-subagents"),
    ("17_ai_capabilities",       "https://anthropic.skilljar.com/ai-capabilities-and-limitations"),
]


def do_login(page):
    print("🔐 Logging in...")
    # 必須從這個 URL 進入，才會帶 t= d= 參數到 accounts.skilljar.com
    page.goto("https://anthropic.skilljar.com/auth/login?next=%2F", wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(3000)
    print(f"  Redirect → {page.url}")
    page.fill('input[name="login"]', EMAIL)
    page.fill('input[name="password"]', PASSWORD)
    page.click('button[type="submit"], input[type="submit"], button:has-text("Sign In")')
    page.wait_for_timeout(5000)
    print(f"  After login → {page.url}")


def is_logged_in(page):
    page.goto("https://anthropic.skilljar.com/", wait_until="domcontentloaded", timeout=20000)
    page.wait_for_timeout(2000)
    text = page.inner_text("body")
    # Logged in = no "Sign In" link, or shows user menu / profile
    return "sign in" not in text[:500].lower() and "accounts.skilljar.com" not in page.url


def enroll_if_needed(page, course_url):
    """Click Register/Enroll button if present."""
    page.goto(course_url, wait_until="domcontentloaded", timeout=30000)
    page.wait_for_timeout(2500)
    try:
        btn = page.query_selector('a:has-text("Enroll"), a:has-text("Register"), button:has-text("Enroll"), button:has-text("Register")')
        if btn:
            btn.click()
            page.wait_for_timeout(3000)
            print("    → Enrolled")
    except:
        pass


def get_lesson_urls(page, course_url):
    """After enrollment, find all lesson/step links in the course sidebar."""
    enroll_if_needed(page, course_url)

    links = page.evaluate("""() => {
        const results = [];
        const seen = new Set();
        document.querySelectorAll('a[href]').forEach(a => {
            const href = a.href;
            const text = a.innerText.trim();
            if (
                href.includes('anthropic.skilljar.com') &&
                !seen.has(href) &&
                text.length > 3 &&
                !href.includes('/auth/') &&
                !href.includes('/logout') &&
                href !== window.location.href &&
                (
                    href.includes('/path/') ||
                    href.includes('/course/') ||
                    href.includes('/lesson/') ||
                    href.includes('/module/') ||
                    href.match(/anthropic\\.skilljar\\.com\\/[a-z0-9-]+\\/[a-z0-9-]/)
                )
            ) {
                seen.add(href);
                results.push({ title: text, url: href });
            }
        });
        return results;
    }""")
    return links


def page_to_md(page):
    return page.evaluate("""() => {
        // Step 1: Convert YouTube iframes → placeholder <p> BEFORE removal
        const seenYT = new Set();
        document.querySelectorAll('iframe').forEach(iframe => {
            const src = iframe.src || iframe.getAttribute('data-src') || '';
            const ytMatch = src.match(/youtube(?:-nocookie)?\\.com\\/embed\\/([a-zA-Z0-9_-]+)/);
            if (ytMatch) {
                const videoId = ytMatch[1];
                if (seenYT.has(videoId)) {
                    iframe.remove();
                    return;
                }
                seenYT.add(videoId);
                // Try to get real title from sibling/parent text context
                let title = '';
                const parent = iframe.closest('section, div, article, .lesson-content, .video-wrapper');
                if (parent) {
                    const heading = parent.querySelector('h1,h2,h3,h4,h5,h6');
                    if (heading) title = heading.innerText.trim();
                }
                if (!title) title = iframe.title || iframe.getAttribute('aria-label') || '';
                if (!title || title === 'YouTube video player') title = 'Video';
                title = title.replace(/::/g, ' ');
                const p = document.createElement('p');
                p.textContent = 'YOUTUBE_EMBED::' + videoId + '::' + title;
                iframe.parentNode.replaceChild(p, iframe);
            }
        });

        // Step 2: Remove unwanted elements (iframes that weren't YouTube are now gone too)
        ['script','style','nav','header','footer','aside','iframe',
         '[class*="sidebar"]','[class*="breadcrumb"]'].forEach(sel => {
            document.querySelectorAll(sel).forEach(e => e.remove());
        });

        const main = document.querySelector(
            'main, article, [class*="lesson-content"], [class*="content-body"], ' +
            '[class*="course-content"], [class*="step-content"], body'
        );
        if (!main) return document.body.innerText;

        const parts = [];
        main.querySelectorAll('h1,h2,h3,h4,h5,h6,p,li,pre,code,blockquote,img').forEach(el => {
            const tag = el.tagName.toLowerCase();

            // Images
            if (tag === 'img') {
                const src = el.src || el.getAttribute('src') || '';
                const alt = el.alt || 'image';
                // Skip tiny icons / tracking pixels / data URIs
                if (src && !src.startsWith('data:') && !src.includes('tracker') &&
                    (el.naturalWidth || 0) > 60) {
                    parts.push('\\n![' + alt + '](' + src + ')\\n');
                }
                return;
            }

            const text = el.textContent?.trim();
            if (!text) return;

            // YouTube placeholder — skip if this element's parent is also selected (avoid dupe)
            if (text.startsWith('YOUTUBE_EMBED::')) {
                const parent = el.parentElement;
                if (parent && (parent.tagName === 'BLOCKQUOTE' || parent.tagName === 'LI')) return;
                const parts2 = text.split('::');
                const videoId = parts2[1] || '';
                const title   = parts2[2] || 'Video';
                if (videoId) {
                    parts.push('\\n> 📹 **[' + title + '](https://www.youtube.com/watch?v=' + videoId + ')**\\n');
                    parts.push('> [![影片縮圖](https://img.youtube.com/vi/' + videoId + '/hqdefault.jpg)](https://www.youtube.com/watch?v=' + videoId + ')\\n');
                }
                return;
            }

            if (tag==='h1') parts.push('\\n# '+text+'\\n');
            else if (tag==='h2') parts.push('\\n## '+text+'\\n');
            else if (tag==='h3') parts.push('\\n### '+text+'\\n');
            else if (tag==='h4'||tag==='h5'||tag==='h6') parts.push('\\n#### '+text+'\\n');
            else if (tag==='pre'||tag==='code') parts.push('\\n```\\n'+text+'\\n```\\n');
            else if (tag==='li') parts.push('- '+text);
            else if (tag==='p') parts.push(text+'\\n');
            else if (tag==='blockquote') parts.push('> '+text+'\\n');
        });
        return parts.join('\\n').replace(/\\n{3,}/g, '\\n\\n').trim();
    }""")


def scrape_course(page, name, url):
    print(f"\n📚 {name}")
    try:
        lessons = get_lesson_urls(page, url)
        title = page.evaluate("() => document.querySelector('h1')?.innerText?.trim() || ''") or name
        print(f"  {len(lessons)} lessons | title: {title[:50]}")

        md = [f"# {title}\n\n> Source: {url}\n"]

        if not lessons:
            md.append(page_to_md(page))
        else:
            for i, lesson in enumerate(lessons):
                print(f"  [{i+1}/{len(lessons)}] {lesson['title'][:60]}")
                try:
                    page.goto(lesson["url"], wait_until="domcontentloaded", timeout=45000)
                    page.wait_for_timeout(2000)
                    content = page_to_md(page)
                    md.append(f"\n---\n\n## {lesson['title']}\n\n> {lesson['url']}\n\n{content}")
                except Exception as le:
                    print(f"    ⚠️  skip: {str(le)[:60]}")
                    md.append(f"\n---\n\n## {lesson['title']}\n\n> {lesson['url']}\n\n*(load error)*")
                time.sleep(0.5)

        out = OUTPUT_DIR / f"{name}.md"
        out.write_text("\n".join(md), encoding="utf-8")
        print(f"  ✅ {out.name} ({out.stat().st_size//1024} KB)")
        return True
    except Exception as e:
        print(f"  ❌ {e}")
        return False


def main():
    # 清除舊 session
    if SESSION_FILE.exists():
        SESSION_FILE.unlink()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context()
        page = ctx.new_page()

        # 強制重新登入
        do_login(page)

        # 確認登入狀態
        if not is_logged_in(page):
            print("❌ Login failed. Check email/password.")
            browser.close()
            return

        print("✅ Logged in!\n")

        # 儲存 session 供後續使用
        SESSION_FILE.write_text(json.dumps(ctx.storage_state()))

        import sys
        only = sys.argv[1] if len(sys.argv) > 1 else None
        ok = 0
        for name, url in COURSES:
            if only and only not in name:
                continue
            if scrape_course(page, name, url):
                ok += 1

        browser.close()

    print(f"\n✅ {ok} courses scraped → {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
