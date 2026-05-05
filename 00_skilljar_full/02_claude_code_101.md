# Claude Code 101

> Source: https://anthropic.skilljar.com/claude-code-101


---

## My Profile

> https://anthropic.skilljar.com/accounts/profile/?next=/claude-code-101

# My Profile

![Robin Hsu's Avatar](https://www.gravatar.com/avatar/84e7c24c2183ec02600cd77eeec4a925/?s=194&d=mm)

For best results, use a square image

Avatar:

#### Registrations

![Add to LinkedIn Profile](https://s3.amazonaws.com/everpath-course-content/media/en-us/images/btn-linkedin-add-to-profile.png)

![Add to LinkedIn Profile](https://s3.amazonaws.com/everpath-course-content/media/en-us/images/btn-linkedin-add-to-profile.png)

#### Registrations

![Add to LinkedIn Profile](https://s3.amazonaws.com/everpath-course-content/media/en-us/images/btn-linkedin-add-to-profile.png)

![Add to LinkedIn Profile](https://s3.amazonaws.com/everpath-course-content/media/en-us/images/btn-linkedin-add-to-profile.png)

## Data and Privacy

Skilljar is a learning management system that hosts our educational content. You're logging into it to access the Anthropic course materials. This separate platform allows us to provide interactive learning experiences, track your progress, and ensure you have access to all course resources in an organized way.

Skilljar collects basic learning analytics such as course progress, lesson completion status, quiz scores, and time spent on materials. This data helps us understand how you're progressing through the course and allows us to provide you with completion certificates. All data collection is focused on improving your learning experience, and is subject to Skilljar's Privacy Policy.

Skilljar only tracks your learning progress within this course platform, while your Anthropic account manages your access to the Anthropic Console and/or Claude AI services.

Yes, Skilljar employs industry-standard security measures including data encryption, secure hosting, and regular security audits. Your learning data is stored on secure servers with appropriate access controls. Skilljar is SOC 2 compliant and follows best practices for data protection to ensure your information remains safe and private.

To request deletion of your learning data or account, email academy-support@anthropic.com. Your request will be processed in accordance with applicable privacy laws and our data retention policies. Note that some data may need to be retained for legitimate business purposes, such as compliance or security, but we'll delete all personal information where legally permissible.

No, you don't need an Anthropic account to access this learning content. The course is hosted on Skilljar and only requires a Skilljar account for access. However, if you want to use Claude AI services after completing the course, you would need to create a separate Anthropic account at claude.ai.

---

## Resume

> https://anthropic.skilljar.com/claude-code-101/resume

## Course quiz

# Claude Code 101 Quiz

---

## What is Claude Code?

> https://anthropic.skilljar.com/claude-code-101/469788

## What is Claude Code?

### Video

> 📹 **[What is Claude Code?](https://www.youtube.com/watch?v=fl1DSmwQKKY)**

> [![影片縮圖](https://img.youtube.com/vi/fl1DSmwQKKY/hqdefault.jpg)](https://www.youtube.com/watch?v=fl1DSmwQKKY)

### What is Claude Code?

Claude Code is an agentic coding tool that understands your codebase, edits your files, runs commands, and integrates with your existing developer tools to help you get things done faster. It's available in your terminal, Visual Studio Code, the Claude Desktop app, on the web, and in JetBrains IDEs.

## What Separates Claude Code from Claude?

If you've used Claude.ai before, you might be wondering what makes Claude Code different. Unlike Claude.ai, Claude Code has direct access to your files, your terminal, and your entire codebase. Instead of copying and pasting code back and forth, it goes in and does the work itself.

The key differentiator is that Claude Code works as an AI Agent.

## What is an Agent?

An AI Agent is software that can interact with its environment and perform actions to complete a defined goal. At its core, this works by having a large language model operating in a loop in real time. AI Agents can have access to tools, external services, or even other AI Agents to help reach their goals.

## What Can Claude Code Actually Do?

Here's what that looks like in practice:

- Read and understand your codebase. You can ask Claude Code to explain a feature or trace a bug throughout your code.
- Edit files across your project. Claude Code can refactor a function and update every file that references it.
- Run terminal commands. It can execute your build script, run your tests, install packages, and use the output to decide what to do next.
- Search the web. If it needs documentation or the latest API references, it can look that up for you.

## Using Claude Code Effectively

To use Claude Code effectively, keep these three concepts in mind:

The context window. Think of this as Claude's working memory. It can hold a lot, but not everything at once. This is where the "agentic" aspect comes in — Claude finds strategic ways to locate answers within your codebase without loading the entire thing into context.

It asks for permission. By default, Claude Code will ask you before running commands or making changes. You're always in control, whether you prefer a hands-on or hands-off approach.

It can make mistakes. Just like any tool, Claude Code isn't perfect. It might misunderstand your intent, introduce a bug, or over-engineer a solution. Staying in the loop helps you catch these early.

## Recap

Claude Code is an agentic coding tool. It reads your codebase, edits your files, runs commands, and connects to external tools to help you ship faster. You can use it today in your terminal, VS Code, JetBrains, and the Claude Desktop app.

---

## How Claude Code works

> https://anthropic.skilljar.com/claude-code-101/469789

## How Claude Code works

### Video

> 📹 **[How Claude Code Works](https://www.youtube.com/watch?v=6bs5b4FltCU)**

> [![影片縮圖](https://img.youtube.com/vi/6bs5b4FltCU/hqdefault.jpg)](https://www.youtube.com/watch?v=6bs5b4FltCU)

### How Claude Code Works

Claude Code is different from typical chat applications. Understanding how it works under the hood will help you use it more effectively.

## The Agentic Loop

Claude Code is best explained through the agentic loop:

- You enter a prompt into Claude Code.
- Claude gathers the context it needs by interacting with the model, which returns text or a tool call that Claude Code can execute.
- It takes action — for example, editing a file or running a command.
- It verifies the results and determines whether they achieve what your prompt set out to do.
- If they do, Claude finishes and waits for the next prompt. If they don't, it loops back and tries again until the results are complete and verifiable.
Throughout this loop, you can add context, interrupt, or steer the model to help guide it toward your goal.

![Diagram of the agentic loop: Your prompt flows into the loop of Gather context, Take action, and Verify results, with the ability to interrupt, steer, or add context at any point](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686365%2Fagenticloop.1775686365141.jpg)

## Context

Claude has a context window that determines how much of your conversation, file contents, command outputs, and more it can store and reference. Once you reach that limit, Claude Code compacts your conversation — automatically determining what it can remove or summarize to bring the context window back down to a usable size.

## Tools

Tools are the backbone of how agents work. Most AI assistants simply take text in and return text out. Tools let Claude Code determine when to execute code to get closer to completing a task. This could be a file-reading tool, a web search tool, or any number of other capabilities. Claude Code uses semantic understanding to determine when to call a tool and how to use the output.

## Permissions

Claude Code has several permission modes:

- Default behavior: Claude asks for explicit permission before editing a file or running a shell command.
- Auto-accept: Files are edited without asking, but commands still require approval.
- Plan mode: Uses read-only tools to compile a plan of action before starting any work.

![Claude Code asking for permission before running a bash command](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686376%2Fvideo2ask.1775686376586.jpg)

All of this can be configured in your settings file. Be cautious when skipping permissions — giving Claude Code free rein to run commands means a mistake could be harder to catch before it happens.

## Recap

Claude Code combines several agentic concepts: an agentic loop, a managed context window, tools, and configurable permissions — all inside your terminal. It can read your codebase, take action, and verify its own work. That's what makes it fundamentally different from a chat window.

---

## Installing Claude Code

> https://anthropic.skilljar.com/claude-code-101/469790

## Installing Claude Code

### Video

> 📹 **[Installing Claude Code](https://www.youtube.com/watch?v=0kILa02vKuI)**

> [![影片縮圖](https://img.youtube.com/vi/0kILa02vKuI/hqdefault.jpg)](https://www.youtube.com/watch?v=0kILa02vKuI)

### Installing Claude Code

Claude Code is simple to install whether you want to use it in your terminal, on the web, or in your IDE.

## Terminal

On macOS, Linux, or WSL, use the curl command to install it in one go. If you prefer Homebrew, you can also use brew install, but note that this method doesn't support auto-updates.

```
brew install
```

On Windows, there are a few options. In PowerShell, use the Invoke-RestMethod command. In CMD, use the curl command. There's also a winget command available, though like Homebrew, it won't auto-update.

```
Invoke-RestMethod
```

![Terminal showing Claude Code successfully installed via curl](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686381%2Fvideo3terminalinstall.1775686380887.jpg)

After installation, you should be able to run the claude command. If not, restart your terminal. Navigate to your project directory and run:

```
claude
```

```
claude
```

```
claude
```

You'll go through some initial setup steps like choosing your color theme and signing in with your Claude account (Pro, Max, or Enterprise) or using an API key. If your organization has a Claude Enterprise account, be sure to select that option.

![Claude Code login method selection: subscription, API, or third-party platform](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686379%2Fvideo3claudeinitaccounts.1775686379767.jpg)

Whatever directory you run claude in, it will have access to that directory and all of its subfolders.

```
claude
```

## Visual Studio Code

Open your Extensions panel and search for "Claude Code." Look for the extension by Anthropic with the blue verification check. Hit install.

After installation, you may need to restart VS Code. Once it's running, open the command palette with Ctrl/Cmd + Shift + P and search for "Claude Code Open in New Tab." You can also click the Claude logo if it's visible in your sidebar.

```
Ctrl/Cmd + Shift + P
```

![Claude Code extension page in VS Code marketplace](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686378%2Fvideo3claudecodevscode.1775686378631.jpg)

The VS Code extension provides a very similar experience to the terminal. You can also opt out of the UI and use the terminal experience directly in your settings.

## JetBrains

Install the Claude Code plugin from the JetBrains Marketplace. After installation, restart your IDE. When you reopen it, you'll see the Claude logo. Clicking it opens a pane with the terminal experience that works alongside your editor.

![Claude Code plugin in the JetBrains Marketplace](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686367%2Fclaudecodejetbrainsvideo3.1775686367876.jpg)

## Desktop

After installing and signing into Claude Desktop, you'll see a toggle at the top labeled "Code." The look and feel is similar to the chat side of things, but it lets you work in a specific folder, change permissions, and even work in a cloud environment.

![Claude Desktop Code view showing recent project folders](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686367%2Fclaudecodedesktopvideo3github.1775686366970.jpg)

## Web

On the web, access Claude Code by going to claude.ai/code, or by clicking the "Code" label in the sidebar of the chat app. This works similarly to the desktop app, but you're restricted to GitHub repositories.

```
claude.ai/code
```

![Claude Code on the web at claude.ai/code with repository selection](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686365%2Fclaudeaislashcodevideo3.1775686365598.jpg)

## Which One Should I Use?

If you want to stay on the cutting edge, the terminal is your best bet — features ship there first. The IDE integrations offer a nearly identical experience if you prefer Claude Code to feel more intertwined with your code editor.

Desktop is great for letting Claude run in the background while you handle other tasks.

Claude Code on the web is a solid option if you want to remotely work on projects through a GitHub repository.

However you want to use Claude Code is up to you.

---

## Your first prompt

> https://anthropic.skilljar.com/claude-code-101/469791

## Your first prompt

### Video

> 📹 **[Your first Claude Code prompt](https://www.youtube.com/watch?v=gbetp6D7J_Q)**

> [![影片縮圖](https://img.youtube.com/vi/gbetp6D7J_Q/hqdefault.jpg)](https://www.youtube.com/watch?v=gbetp6D7J_Q)

### Your First Prompt

You talk to Claude Code like you would any AI assistant. When entering your prompt, here are some things to consider that can both protect you and make things easier.

## Auto-Accept vs. Approval

You can choose whether Claude auto-accepts every file change it suggests, or whether it asks for your explicit permission each time. Press Shift + Tab to cycle between modes.

```
Shift + Tab
```

- Approval mode: Claude asks permission each time it wants to edit a file or run a command.
- Auto-accept mode: File edits are automatically approved, but commands still require your permission.
There's no right or wrong answer — it's whatever you're comfortable with.

![Claude Code in auto-accept mode, reading files and working through a task](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686381%2Fvideo4autoaccept.1775686381332.jpg)

## Plan Mode

Within the Shift + Tab menu is Plan Mode. Plan mode takes your prompt and uses read-only tools to analyze your codebase and research your suggested implementation. It will ask clarifying questions along the way, then return a detailed plan it can execute.

```
Shift + Tab
```

Plan mode is great for planning complex changes or doing a safe code review. Many times you'll be asking Claude to handle multi-step implementations toward a feature, and this is exactly where Plan Mode excels.

![Claude Code with plan mode on, showing the status bar indicator](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686384%2Fvideo4planmode.1775686383837.jpg)

## Example: Add a Dark Mode Toggle

Let's walk through an example. Say you have an application that needs a dark mode toggle. Open the root directory of your project and run claude. Press Shift + Tab a couple of times to enter Plan Mode, then write a prompt like:

```
claude
```

```
Shift + Tab
```

```
My app needs a dark mode implemented across the entire app. Can you create a toggle switch on the header that allows a user to toggle between light mode and dark mode? I need you to find a good contrast color that works based on my existing light theme.
```

```
My app needs a dark mode implemented across the entire app. Can you create a toggle switch on the header that allows a user to toggle between light mode and dark mode? I need you to find a good contrast color that works based on my existing light theme.
```

![Entering the dark mode prompt in Claude Code with plan mode enabled](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686383%2Fvideo4demoenteringpromptinplanmode.1775686382790.jpg)

Let Claude plan it out. After reviewing the plan, if it looks good, accept it and let Claude ask you for approval at each step. At the end, you can see exactly what Claude did and how it reached its conclusions.

## Recap

When using Claude Code, try to be as descriptive as possible with your prompt. If you want to stay in the loop at every step, you can. Use Plan Mode to let Claude dig into the details of what you want to achieve before executing on any code.

---

## The explore → plan → code → commit workflow

> https://anthropic.skilljar.com/claude-code-101/469792

## The explore → plan → code → commit workflow

### Video

> 📹 **[The Explore → Plan → Code → Commit workflow in Claude Code](https://www.youtube.com/watch?v=xJQuF02NAK8)**

> [![影片縮圖](https://img.youtube.com/vi/xJQuF02NAK8/hqdefault.jpg)](https://www.youtube.com/watch?v=xJQuF02NAK8)

### The Explore → Plan → Code → Commit Workflow

If you take one thing away from this course, let it be this workflow: Explore, Plan, Code, and Commit. Without it, most people jump straight to asking Claude to write code — which means more course-correcting later on.

## Explore and Plan

The fastest way to handle these first two steps is with Plan Mode. In plan mode, Claude can't edit files — it just reads files to gather information about how it will tackle the implementation.

To enter plan mode, press Shift + Tab until you see "Plan Mode" under the text input. Then write a prompt like:

```
Shift + Tab
```

![Claude Code status bar showing plan mode on with shift+tab to cycle](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686390%2Fvideo5planmodeshifttab.1775686390450.jpg)

```
I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it.
```

```
I need to add WebP conversion to our image upload pipeline. Figure out where in the pipeline it should happen, whether we need new dependencies, and how to approach it.
```

Claude will read relevant files, run some web searches, and give you a plan of action. Review it and decide if it meets your criteria. If not, ask it to revise specific areas.

![Claude Code presenting the plan with options to approve, revise areas, or ask questions](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686389%2Fvideo5planmodereviseareas.1775686389692.jpg)

This is the best place to course-correct because it's before any code is written. You can also run the explore subagent without being in plan mode if you just want a general summary of your codebase without intending to make changes afterward.

## Code

Once the plan looks good, select "approve" to accept it and let Claude work through the list items. You can choose whether Claude auto-accepts file edits or asks you each time.

Claude will do its best to troubleshoot before considering the plan "finished," but at times you'll need to step in. This is the benefit of working with Plan Mode — after execution, you also have the context of how you got to the results, which helps guide Claude's next decisions.

A few tips to make the coding phase smoother:

- Define a success criteria. For Claude to be confident in its results, it needs to be clear on what "correct" looks like. Make this explicit when writing your plan.
- Add tools. Tools that help Claude complete its goals remove a lot of back and forth. For example, if you're building web UIs, install the Claude in Chrome extension so Claude Code can control a browser tab and test the UI directly.

![The Claude in Chrome extension page in the Chrome Web Store](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686387%2Fvideo5claudeinchromeextension.1775686387012.jpg)

- Include a test suite. Give Claude a test suite it can continuously validate against. Claude can even write tests for you. Before handing this off, make sure the tests are a reliable source of truth to avoid false positives.
Quick tip: If you find Claude keeps running into the same issues, ask it to save the solution to its CLAUDE.md file.

## Commit

Once you've tested the changes yourself and are happy with the results, it's time to push your code. Before you commit, run a subagent code reviewer to look at your work. A subagent gets a fresh pair of eyes on the codebase — it doesn't carry the bias the main agent might have from the session.

![A code-reviewer subagent running in Claude Code, reading files and reviewing recent changes](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686388%2Fvideo5claudesubagentcodereviewer.1775686387773.jpg)

Then get Claude to generate a commit message in your style. Rinse and repeat.

## Recap

To be effective with Claude Code, follow the Explore, Plan, Code, and Commit workflow:

- Explore gives Claude the relevant context it needs for your project.
- Plan creates a plan of action that Claude uses to measure success.
- Code is the back and forth between you and Claude before settling on the final outcome.
- Commit helps you review and push your code so you can start on your next feature.

---

## Context management

> https://anthropic.skilljar.com/claude-code-101/469793

## Context management

### Video

> 📹 **[Context Management in Claude Code](https://www.youtube.com/watch?v=eW3oTyfeWZ0)**

> [![影片縮圖](https://img.youtube.com/vi/eW3oTyfeWZ0/hqdefault.jpg)](https://www.youtube.com/watch?v=eW3oTyfeWZ0)

### Context Management

Context is Claude's working memory. Every file it reads, every command it runs, every message you send — it all takes up space in the context window.

## What is the Context Window?

Think of the context window as the amount of space Claude can hold in its memory. Whenever you enter a prompt, Claude reads a file, runs a tool call, or receives a tool call result, it's all adding to the context window. Since there's a finite amount of space, it becomes important to optimize how you use it.

![Diagram showing the context window as a grid of tokens — some taken, most available](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686395%2Fvideo6contextwindowdiagram.1775686395676.jpg)

## What Happens When Context Fills Up

When you approach the limit, the context window is automatically compacted. Compaction summarizes important details and removes unnecessary tool call results to free up space. Note that this process can potentially lose details.

![Claude Code showing 'Compacting conversation...' as it summarizes the context](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686393%2Fvideo6compactingcontext.1775686393619.jpg)

![Claude Code displaying a compact summary of the previous conversation including key technical concepts and files](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686394%2Fvideo6compactingsummary.1775686394575.jpg)

## Commands

You can run compaction manually with the /compact command. This compacts everything up to that point. It's handy when you want to free up context space while keeping a memory of what you previously worked on.

```
/compact
```

![The /compact command in Claude Code's autocomplete menu](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686393%2Fvideo6compactcommand.1775686392964.jpg)

If you want to completely start from scratch with no memory of the previous session, run /clear. This removes everything.

```
/clear
```

![Running /clear in Claude Code to start a fresh session](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686392%2Fvideo6clearcommand.1775686392379.jpg)

To check the state of your context, run the /context command. You'll get a high-level overview of your context size, the categories taking up the most space, and a visual graphic showing the breakdown.

```
/context
```

![Output of the /context command showing context usage breakdown with a visual bar chart](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686364%2FVideo_2_01_01_11_11.1775686364258.jpg)

## When to Use Which

A general rule of thumb:

- Use /compact when you're working on a specific feature and running up against the context limit but need to continue. Keeping the context relevant to your current feature is important.

```
/compact
```

- Use /clear when you want to start a new feature. You don't want the previous conversation to introduce bias into something new. For things you want Claude to remember across sessions, put them in your CLAUDE.md file so it doesn't have to rediscover things from scratch.

```
/clear
```

![A CLAUDE.md file with commands, important notes, and architecture sections](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686391%2Fvideo6claudemdfile.1775686391669.jpg)

## Tips for Saving Context Space

Be specific. A vague prompt might seem smaller, but it actually costs more context in the long run. Without clear instructions, Claude is forced to explore your codebase more and do its own reasoning — which takes up far more context space than a detailed prompt would.

Manage your MCP servers. MCP servers load all of their available tools into context by default, even when you're not using them. If you have servers configured for things unrelated to the current project, consider turning them off. You can also try "Skills," which work similarly to MCP servers but don't load everything into context upfront.

Use subagents. Subagents run in parallel with your main agent but have a completely separate context window. For tasks where you only need the answer — like "where are the authentication endpoints located?" — a subagent does the work and returns just a summary to your main agent, keeping your primary context clean.

## Recap

Managing context within Claude Code is crucial. Use /compact to summarize long sessions and /clear to start fresh. To use your context window effectively: be specific with your prompts, check what's consuming your current context, and use subagents to delegate tasks where you only need the result.

```
/compact
```

```
/clear
```

---

## Code review

> https://anthropic.skilljar.com/claude-code-101/469794

## Code review

### Video

> 📹 **[Introducing Code Review](https://www.youtube.com/watch?v=RKsADl0ZC3Y)**

> [![影片縮圖](https://img.youtube.com/vi/RKsADl0ZC3Y/hqdefault.jpg)](https://www.youtube.com/watch?v=RKsADl0ZC3Y)

### Code Review

Claude Code has a few built-in features that make your git workflow faster. Let's go through them.

## Review with a Subagent

Before you push a PR, ask Claude to use a subagent to review your changes. The subagent runs in its own context window with fresh eyes — it doesn't carry the bias of the main agent that just spent the session writing the code.

When creating a code-reviewer subagent, restrict it to read-only tools. A reviewer should flag issues, not edit files. Check the subagent configuration into your repo so your whole team uses the same reviewer.

## The /commit-push-pr Skill

The /commit-push-pr skill handles the commit, push, and PR creation all in one step. Instead of doing each manually, just run the skill and Claude takes care of it.

```
/commit-push-pr
```

If you have a Slack MCP server configured with channels listed in your CLAUDE.md, it will automatically post the PR link to your team's channel.

## Session Linking with --from-pr

When Claude creates a PR through gh pr create, the session gets linked to that PR automatically. If you need to come back to it later — maybe to address review comments or fix a failing build — run:

```
gh pr create
```

```
claude --from-pr <PR_NUMBER>
```

```
claude --from-pr <PR_NUMBER>
```

This picks up right where you left off.

## Recap

Use a subagent for an unbiased code review before pushing. Use /commit-push-pr to handle the full commit-to-PR flow in one step. And use --from-pr to resume work on a PR later. These are small features, but they remove a lot of friction from your daily workflow.

```
/commit-push-pr
```

```
--from-pr
```

---

## The CLAUDE.md file

> https://anthropic.skilljar.com/claude-code-101/469795

## The CLAUDE.md file

### Video

> 📹 **[The CLAUDE.md file](https://www.youtube.com/watch?v=O0FGCxkHM-U)**

> [![影片縮圖](https://img.youtube.com/vi/O0FGCxkHM-U/hqdefault.jpg)](https://www.youtube.com/watch?v=O0FGCxkHM-U)

### The CLAUDE.md File

One of the most useful features in Claude Code is the CLAUDE.md file. It gives Claude Code persistent memory about your project.

## The Problem It Solves

When you open Claude Code without a CLAUDE.md file, it starts fresh every time. It has to re-explore your codebase, figure out what dependencies are needed, and understand what features are already implemented. Sometimes it makes assumptions, which makes it harder to steer Claude in the right direction.

CLAUDE.md solves this. It's a Markdown file you add to the root of your project, and Claude Code reads it automatically every time you start a session. Think of it as an onboarding script for your codebase. The contents of the CLAUDE.md file are appended to your prompt.

## An Example

Here's what a typical CLAUDE.md file looks like:

```
# Project

This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM.

# Commands
- Dev server: `pnpm dev`
- Run tests: `pnpm test`
- Lint: `pnpm lint`

# Code Style
- Use 2-space indentation
- Prefer named exports
- All API routes go in app/api/
- Use server actions instead of API routes where possible
```

```
# Project

This is a Next.js 15 app using the App Router, Tailwind, and Drizzle ORM.

# Commands
- Dev server: `pnpm dev`
- Run tests: `pnpm test`
- Lint: `pnpm lint`

# Code Style
- Use 2-space indentation
- Prefer named exports
- All API routes go in app/api/
- Use server actions instead of API routes where possible
```

It's straightforward. Now if you ask Claude Code to create a React component, it already knows to use Tailwind for styling and to follow your code conventions.

![A CLAUDE.md file open in VS Code showing project info, commands, and code style rules](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686400%2Fvideo8claudemdexample.1775686400069.jpg)

## CLAUDE.md is for Teams

You can (and should) commit your CLAUDE.md to version control so your team benefits from it. There's actually a hierarchy of memory files depending on who they're for:

- Project-level CLAUDE.md lives in the root directory of your project. Shared with the team.
- User-level CLAUDE.md lives in your configuration folder. This one is just for you and applies across all your projects. Put your personal preferences here.

## Tips

Save corrections to memory. If you find yourself correcting Claude repeatedly — like telling it to always use server actions instead of API routes — explicitly ask Claude to save that rule to memory. Next time you open the project, it'll know.

![Asking Claude to save a rule to the CLAUDE.md file — always use server actions instead of API routes](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686399%2Fvideo8Askingclaudetoputinmemory.1775686399417.jpg)

Reference project docs. If you have documentation in your project that you want Claude to reference, use the @ symbol with the file path:

```
@
```

```
## README.md

Please read if you need more info: @README.md
```

```
## README.md

Please read if you need more info: @README.md
```

Start without one. We recommend starting a project without a CLAUDE.md file so you can see where you constantly have to course-correct the model. This keeps your CLAUDE.md compact and focused on only the necessary information. When you're ready, run /init to have Claude generate one for you.

```
/init
```

## Recap

The difference between a frustrating Claude Code session and a productive one often comes down to context — and the CLAUDE.md file is how you provide that context. Start with your stack, your preferences, and your commands, then build from there as you go.

---

## Subagents

> https://anthropic.skilljar.com/claude-code-101/469796

## Subagents

### Video

> 📹 **[What are subagents?](https://www.youtube.com/watch?v=jKErNxuxPXg)**

> [![影片縮圖](https://img.youtube.com/vi/jKErNxuxPXg/hqdefault.jpg)](https://www.youtube.com/watch?v=jKErNxuxPXg)

### Subagents

Claude can delegate tasks to subagents that break them down and run component tasks in parallel, improving your context management. Each subagent operates in its own isolated context window.

## How It Works

Managing context in Claude Code is important. A lot of the context window gets consumed by things like tool calls exploring your codebase or running web searches for research. What Claude discovers during that exploration isn't always relevant to the main feature you're developing.

This is where subagents come in. Claude spawns a subagent to handle a task like "explore this codebase for me." The subagent runs in parallel with its own context window, does all the exploration work, and once finished, summarizes its findings and returns that summary back to Claude.

The result: you get the answer you were looking for, without the entire journey it took to get there cluttering your main context.

## Creating Your Own Subagent

Subagents are defined in Markdown files with YAML frontmatter. The easiest way to get started is to let Claude generate one for you. Run:

```
/agents
```

```
/agents
```

Then select "Create new agent." You'll walk through steps including choosing the scope of the agent, defining its purpose, selecting the tools it has access to, and even picking a color for it.

Claude will generate a name, description, and prompt for the subagent. This also tells Claude when to call the subagent based on the prompts you give it.

## Further Customization

Subagents can be customized further. Here are some highlights:

- Persistent memory lets your subagent retain memory across conversations. This is great if you're using it consistently on the same projects.
- Preload skills into subagents by adding the skill key and listing skills by name. Note that unlike skills in your main conversation, the entire skill is loaded into context here.

```
skill
```

## Recap

Keeping your context window clean is one of the best ways to stay productive with Claude Code. With subagents, you can run an agent in the background to handle the heavy lifting and return just the answer to your main context window.

Want to go deeper? Check out our dedicated course: Introduction to subagents

---

## Skills

> https://anthropic.skilljar.com/claude-code-101/469848

## Skills

### Video

> 📹 **[What are skills?](https://www.youtube.com/watch?v=bjdBVZa66oU)**

> [![影片縮圖](https://img.youtube.com/vi/bjdBVZa66oU/hqdefault.jpg)](https://www.youtube.com/watch?v=bjdBVZa66oU)

### Article

Want to go deeper? Check out our dedicated course: Introduction to agent skills

---

## Hooks

> https://anthropic.skilljar.com/claude-code-101/469798

## Hooks

### Video

> 📹 **[Hooks in Claude Code](https://www.youtube.com/watch?v=IkaPHiMDazM)**

> [![影片縮圖](https://img.youtube.com/vi/IkaPHiMDazM/hqdefault.jpg)](https://www.youtube.com/watch?v=IkaPHiMDazM)

### Hooks

Hooks let you run commands at specific points in Claude Code's lifecycle. The key difference between hooks and everything else covered in this course is that hooks are deterministic — they always run.

## Why Use Hooks

You can tell Claude in your CLAUDE.md to run Prettier after every file edit. Most of the time it will. But sometimes it won't. A hook makes it happen every single time, no exceptions.

Common use cases include:

- Auto-formatting after file edits
- Logging all executed commands for compliance
- Blocking dangerous operations like modifying production files
- Sending yourself notifications when Claude finishes a task

## How They Work

Hooks are configured in your settings.json. You pick an event, optionally set a matcher for which tools it applies to, and provide a command to run. The available events are:

```
settings.json
```

- PreToolUse — runs before a tool call
- PostToolUse — runs after a tool call completes
- UserPromptSubmit — runs when you submit a prompt, before Claude processes it
- Stop — runs when Claude finishes responding
- Notification — runs when Claude sends a notification
You configure them through the /hooks command inside Claude Code, or by editing settings.json directly.

```
/hooks
```

```
settings.json
```

![The settings.json file inside the .claude directory with hooks configuration](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686375%2Fvideo11settingsjsonfile.1775686375582.jpg)

## A Practical Example

The most common hook: auto-formatting after edits. Set a PostToolUse hook with a matcher of "Edit|MultiEdit|Write" so it fires whenever Claude modifies a file. The command checks the file extension and runs the appropriate formatter — Prettier for TypeScript, gofmt for Go, whatever your project uses.

```
"Edit|MultiEdit|Write"
```

## Blocking with PreToolUse

PreToolUse hooks can block tool calls before they execute. Your hook receives the tool name and input as JSON on stdin. The exit code determines the behavior:

- Exit code 0 — proceed normally.
- Exit code 2 — block the action. The stderr message gets fed back to Claude as feedback so it knows why it was blocked and can adjust.
- Any other exit code — a non-blocking error that gets shown to you but doesn't stop anything.
This is how you enforce hard rules. Block writes to a production config directory. Block bash commands that contain rm -rf. Block commits to main. Whatever your team needs to be guaranteed, not suggested.

```
rm -rf
```

![A settings.json file showing PreToolUse and PostToolUse hooks with matchers and commands](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686375%2Fvideo11hooksblock.1775686375002.jpg)

## Sharing Hooks with Your Team

Hooks configured in .claude/settings.json are project-level and can be checked into your repo. This means your entire team gets the same hooks automatically. Use the CLAUDE_PROJECT_DIR environment variable in your commands to reference scripts stored in your project, so they work regardless of Claude's current working directory.

```
.claude/settings.json
```

```
CLAUDE_PROJECT_DIR
```

## Recap

Hooks give you deterministic control over Claude Code's behavior. Use PostToolUse for auto-formatting and logging. Use PreToolUse to block dangerous operations. Configure them with /hooks or in settings.json. And check them into your repo so your team gets them too.

```
/hooks
```

```
settings.json
```

If something needs to happen every time without fail, don't put it in a prompt. Put it in a hook.

---

## Course quiz

> https://anthropic.skilljar.com/claude-code-101/469849

## Course quiz

# Claude Code 101 Quiz