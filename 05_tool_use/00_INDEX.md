# Anthropic Tool Use Course — Lesson Index

> Source: [anthropics/courses](https://github.com/anthropics/courses/tree/master/tool_use) on GitHub
> Converted from Jupyter notebooks to Markdown.

---

## Lessons

| # | File | Title | Description |
|---|------|-------|-------------|
| 00 | [00_README.md](./00_README.md) | README | Course overview and table of contents |
| 01 | [01_tool_use_overview.md](./01_tool_use_overview.md) | Tool Use Basics | Conceptual introduction to tool use (function calling): what it is, why it matters, key use cases, and a high-level walkthrough of the 4-step request/response workflow |
| 02 | [02_your_first_simple_tool.md](./02_your_first_simple_tool.md) | Your First Simple Tool | Hands-on implementation of a basic calculator tool; covers defining a tool schema, sending it with a prompt, and extracting the tool-use response from Claude |
| 03 | [03_structured_outputs.md](./03_structured_outputs.md) | Forcing JSON with Tool Use | Technique for using a "dummy" tool definition to force Claude to return perfectly structured JSON output — useful for entity extraction, summarisation, and sentiment analysis |
| 04 | [04_complete_workflow.md](./04_complete_workflow.md) | The Complete Tool Use Workflow | Full 4-step agentic loop: sending tools + prompt → Claude calls a tool → client executes code → result returned to Claude → Claude formulates final answer |
| 05 | [05_tool_choice.md](./05_tool_choice.md) | Tool Choice | How to control which tool Claude selects using the `tool_choice` parameter (`auto`, `any`, `tool`) and when each option is appropriate |
| 06 | [06_chatbot_with_multiple_tools.md](./06_chatbot_with_multiple_tools.md) | Chatbot with Multiple Tools | Building a multi-turn customer support chatbot (TechNova) that can select from a suite of tools: `get_user`, `get_order_by_id`, `get_customer_orders`, and `cancel_order` |

---

## Key Concepts Covered

- **Tool schema definition** — `name`, `description`, `input_schema` (JSON Schema)
- **4-step tool use loop** — prompt → `tool_use` stop reason → execute → `tool_result`
- **Structured JSON output** via tool definitions
- **`tool_choice` parameter** — `auto` / `any` / specific tool name
- **Multi-tool chatbots** — routing logic, multi-turn conversation state
- **Error handling** in tool results
