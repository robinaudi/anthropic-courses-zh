# Claude with Google Cloud's Vertex AI

> Source: https://anthropic.skilljar.com/claude-with-google-vertex


---

## My Profile

> https://anthropic.skilljar.com/accounts/profile/?next=/claude-with-google-vertex

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

> https://anthropic.skilljar.com/claude-with-google-vertex/resume

## Quiz on prompt engineering techniques

# Quiz on Prompt Engineering Techniques

---

## Welcome to the course

> https://anthropic.skilljar.com/claude-with-google-vertex/289145

## Welcome to the course

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Overview of Claude models

> https://anthropic.skilljar.com/claude-with-google-vertex/289146

## Overview of Claude models

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Accessing the API

> https://anthropic.skilljar.com/claude-with-google-vertex/289151

details

## Accessing the API

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building applications with Claude, understanding the complete request lifecycle helps you architect better systems and debug issues more effectively. Let's walk through what happens when a user sends a message to your AI-powered chat application.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619446%2F03_-_001_-_Accessing_the_API_01.1748619446474.png)

## The Complete Request Flow

The journey from user input to AI response involves five distinct steps: Request to Server, Request to Vertex, Model Processing, Response to Server, and Response to Client. Each step plays a crucial role in delivering that "magical" response users expect.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619447%2F03_-_001_-_Accessing_the_API_03.1748619446886.png)

## Why You Need a Server

Never make API requests directly from client-side code. Here's why:

- API requests require secret credentials that must stay secure
- Exposing credentials in client code makes them visible to anyone
- Your server acts as a secure intermediary between your app and Vertex
Always route requests through your own server that you control and secure.

## Making the API Request

Your server communicates with Vertex using either Anthropic's SDKs or Google's official Vertex SDKs. Anthropic provides official SDKs for Python, TypeScript, Go, and Ruby.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619447%2F03_-_001_-_Accessing_the_API_05.1748619447285.png)

Every request must include these key fields:

- API Key - Identifies your request to Anthropic
- Model - Name of the specific model to use
- Messages - List containing the user's input text
- Max Tokens - Limits how many tokens the model can generate
The user's input gets placed inside a "user" message, which then goes into a list of messages sent to the API.

## Inside Claude: Text Generation Process

Once Vertex receives your request, Claude processes it through four stages: Tokenization, Embedding, Contextualization, and Generation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619448%2F03_-_001_-_Accessing_the_API_07.1748619448446.png)

### Tokenization

Claude first breaks down the input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

### Embedding

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as number-based definitions.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619449%2F03_-_001_-_Accessing_the_API_09.1748619448923.png)

### Contextualization

Since words can have multiple meanings, Claude uses context to determine the right interpretation. The word "quantum" could refer to physics, computing, or just mean "very small" - context from surrounding words clarifies the intended meaning.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619449%2F03_-_001_-_Accessing_the_API_10.1748619449353.png)

During contextualization, each embedding gets adjusted based on its neighbors, highlighting the meaning that makes most sense given the context.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619450%2F03_-_001_-_Accessing_the_API_11.1748619449882.png)

### Generation

The contextualized embeddings pass through an output layer that produces probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and randomness to create more natural, varied responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619450%2F03_-_001_-_Accessing_the_API_13.1748619450513.png)

After selecting a word, Claude adds it to the sequence and repeats the entire process for the next word.

## When Generation Stops

After generating each token, Claude checks several conditions to decide whether to continue:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619451%2F03_-_001_-_Accessing_the_API_15.1748619451060.png)

- Max tokens reached - Has it hit the limit you specified?
- Natural ending - Did it generate an end-of-sequence token?
- Stop sequence - Did it encounter a predefined stop phrase?
The end-of-sequence token is a special signal (not visible text) that Claude uses to indicate it has reached a natural conclusion.

## The Response

Once generation completes, Vertex sends a response back to your server containing:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619451%2F03_-_001_-_Accessing_the_API_17.1748619451445.png)

- Message - The generated text
- Usage - Count of input and output tokens
- Stop Reason - Why the model stopped generating
Your server then forwards the generated text to your client application, where it appears in the chat interface.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619452%2F03_-_001_-_Accessing_the_API_18.1748619452060.png)

## The Complete Picture

This entire process - from user input through tokenization, embedding, contextualization, generation, and back to the user - happens in seconds. Understanding this flow helps you build more robust applications and troubleshoot issues when they arise.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619452%2F03_-_001_-_Accessing_the_API_19.1748619452534.png)

The key takeaway: always use a server as an intermediary, understand that text generation is an iterative process, and pay attention to the response metadata to monitor usage and understand model behavior.

---

## Vertex AI Setup

> https://anthropic.skilljar.com/claude-with-google-vertex/307525

## Vertex AI Setup

In the next video we will be making a request to Vertex AI in order to call a Claude model. To do so, you need to go through a little bit of setup.

#### Step One: Ensure Anthropic models are enabled in Vertex

- In your browser, navigate to https://console.cloud.google.com/vertex-ai/dashboard
- In the left hand nav, click on 'Model Garden'

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1751930983%2F1.1751930983608.png)

- In the 'Search models' box, enter 'Anthropic'

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1751931014%2F2.1751931013945.png)

- Click on the model that you want to use.

#### Step Two: Enable the Model

- Once you've found the model you want to use, you may need to enable it. On the model information page, click the 'Enable' button
- If you don't see an 'Enable' button then you already have access to the model

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1751931033%2F3.1751931033360.png)

#### Step Three: Install the gcloud CLI

If you don't already have the gcloud CLI installed, follow the directions here to install and authenticate with the CLI: https://cloud.google.com/sdk/docs/install

#### Step Four: Login and set up authentication with the gcloud CLI

If you have not already logged in to the gcloud CLI, do so by running:

```
gcloud init
gcloud auth login
```

```
gcloud init
gcloud auth login
```

Then, set your project ID and set your default credentials:

```
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

```
gcloud config set project YOUR_PROJECT_ID
gcloud auth application-default login
```

That's it! The Anthropic SDK will automatically use these credentials when attempting to access Vertex.

---

## Making a request

> https://anthropic.skilljar.com/claude-with-google-vertex/289155

details

## Making a request

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now it's time to get hands-on with the Anthropic Python SDK and make your first request to Claude through Vertex AI. We'll walk through three essential steps: installing the SDK, creating a client, and making your first API call.

## Installing the Anthropic Python SDK

First, you'll need to install the Anthropic SDK with Vertex AI support. In your Jupyter notebook, run this magic command:

```
%pip install "anthropic[vertex]"
```

```
%pip install "anthropic[vertex]"
```

The [vertex] part ensures you get the specific components needed to connect to Google Cloud's Vertex AI platform.

```
[vertex]
```

## Creating an API Client

Next, import and create a client instance specifically designed for Vertex AI:

```
from anthropic import AnthropicVertex

client = AnthropicVertex(region="global", project_id="your-project-id")
model = "claude-sonnet-4@20250514"
```

```
from anthropic import AnthropicVertex

client = AnthropicVertex(region="global", project_id="your-project-id")
model = "claude-sonnet-4@20250514"
```

You'll need to replace "your-project-id" with your actual Google Cloud project ID, which you can find in the Google Cloud Console's project selector. Setting the model as a variable saves you from typing it repeatedly throughout your notebooks.

```
"your-project-id"
```

## Understanding the Create Function

The core of making requests to Claude is the create function, which requires three key parameters:

```
create
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619440%2F03_-_003_-_Making_a_Request_08.1748619440458.png)

- model - The name of the Claude model you want to use
- max_tokens - A safety limit on response length (Claude won't try to hit this target, it just won't exceed it)
- messages - The conversation history you're sending to Claude
Think of max_tokens as a budget rather than a goal. If you set it to 1000, Claude will write whatever response it thinks is appropriate, but stop if it would exceed 1000 tokens.

```
max_tokens
```

## Understanding Messages

Messages represent the back-and-forth conversation between you and Claude, just like in a chat application:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619441%2F03_-_003_-_Making_a_Request_12.1748619440992.png)

There are two types of messages:

- User messages - Content written by humans that you want to feed into Claude
- Assistant messages - Content that Claude has generated and sent back to you

## Making Your First Request

Here's how to structure a basic request:

```
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
```

```
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
```

Each message is a dictionary with a role (either "user" or "assistant") and content (the actual text).

```
role
```

```
content
```

## Extracting the Response

When you run the request, you'll get back a complex response object with lots of metadata. To get just the text that Claude generated, use:

```
message.content[0].text
```

```
message.content[0].text
```

This gives you clean, readable output instead of the full response object with all its technical details. You'll use this pattern frequently when working with Claude's responses.

---

## Multi-turn conversations

> https://anthropic.skilljar.com/claude-with-google-vertex/289156

details

## Multi-turn conversations

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with the Anthropic API and Claude, there's a crucial concept you need to understand: Claude doesn't store any of your conversation history. Each request you make is completely independent, with no memory of previous exchanges.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619440%2F03_-_004_-_Multi-Turn_Conversations_01.1748619440499.png)

This means if you want to have a multi-turn conversation where Claude remembers context from earlier messages, you need to handle the conversation state yourself.

## The Problem with Stateless Conversations

Let's say you ask Claude "What is quantum computing?" and get a good response. Then you follow up with "Write another sentence" - Claude has no idea what you're referring to. It will write a sentence about something completely random because it has no memory of the quantum computing discussion.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619441%2F03_-_004_-_Multi-Turn_Conversations_02.1748619441159.png)

## How Multi-Turn Conversations Work

To maintain conversation context, you need to do two things:

- Manually maintain a list of all messages in your code
- Send the complete message history with every request

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619441%2F03_-_004_-_Multi-Turn_Conversations_05.1748619441704.png)

Here's the flow that actually works:

- Send your initial user message to Claude
- Take Claude's response and add it to your message list as an assistant message
- Add your follow-up question as another user message
- Send the entire conversation history to Claude

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619442%2F03_-_004_-_Multi-Turn_Conversations_08.1748619442168.png)

## Building Helper Functions

To make conversation management easier, you can create three helper functions:

```
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
```

```
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
```

## Putting It All Together

Here's how you use these functions to maintain a conversation:

```
# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(messages)
```

```
# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(messages)
```

Now Claude will understand that "Write another sentence" refers to expanding on the quantum computing definition, because you've provided the complete conversation context.

## Key Takeaways

Remember that every API call to Claude is independent. If you want conversational context, you must:

- Store all messages locally in your application
- Send the complete message history with each request
- Properly format messages with "user" and "assistant" roles
These helper functions will be essential throughout your work with Claude, making it much easier to build applications that feel like natural conversations rather than isolated question-and-answer exchanges.

---

## Chat exercise

> https://anthropic.skilljar.com/claude-with-google-vertex/289150

## Chat exercise

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## System prompts

> https://anthropic.skilljar.com/claude-with-google-vertex/289153

details

## System prompts

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

System prompts are a powerful way to customize how Claude responds to user input. Instead of getting generic answers, you can shape Claude's tone, style, and approach to match your specific use case.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619444%2F03_-_006_-_System_Prompts_00.1748619444467.png)

## Why System Prompts Matter

Consider building a math tutor chatbot. When a student asks "How do I solve 5x + 2 = 3 for x?", you want Claude to act like a real tutor, not just spit out the answer. A good math tutor should:

- Initially give hints rather than complete solutions
- Patiently walk students through problems step by step
- Show solutions for similar problems as examples
You definitely don't want Claude to:

- Immediately give direct answers
- Tell students to just use a calculator

## How System Prompts Work

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619445%2F03_-_006_-_System_Prompts_05.1748619444941.png)

System prompts provide Claude with guidance on how to respond. You define them as plain strings and pass them into the create function call. The key benefits are:

- System prompts provide Claude guidance on how to respond
- Claude will try to respond in the same way someone in the specified role would respond
- Helps keep Claude on task
Here's the basic structure:

```
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
    model=model,
    messages=messages,
    max_tokens=1000,
    system=system_prompt
)
```

```
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
    model=model,
    messages=messages,
    max_tokens=1000,
    system=system_prompt
)
```

## Seeing the Difference

Without a system prompt, Claude gives a complete step-by-step solution immediately. This might be helpful, but it doesn't encourage the student to think through the problem themselves.

With the math tutor system prompt, Claude's response changes dramatically. Instead of providing the full solution, Claude asks guiding questions like "What do you think would be a good first step to isolate x? Consider what operation we might need to perform on both sides to start moving terms around."

## Building a Flexible Chat Function

Rather than hard-coding system prompts, you can make your chat function more reusable by accepting system prompts as parameters:

```
def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```

```
def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```

This approach handles an important detail: Claude's API doesn't accept system=None, so you need to conditionally include the system parameter only when it's provided.

```
system=None
```

Now you can call your chat function with or without a system prompt:

```
# Without system prompt
answer = chat(messages)

# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)
```

```
# Without system prompt
answer = chat(messages)

# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)
```

System prompts are essential for creating AI applications that behave consistently and appropriately for their intended purpose. They transform generic AI responses into specialized, role-appropriate interactions.

---

## System prompts exercise

> https://anthropic.skilljar.com/claude-with-google-vertex/289157

## System prompts exercise

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Temperature

> https://anthropic.skilljar.com/claude-with-google-vertex/289154

details

## Temperature

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Temperature is a powerful parameter that controls how predictable or creative Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications.

## How Claude Generates Text

Before diving into temperature, it's helpful to understand Claude's text generation process. When you send Claude a prompt like "What do you think?", it goes through three main steps:

- Tokenization - Breaking your input into smaller chunks
- Prediction - Calculating probabilities for possible next words
- Sampling - Choosing a token based on those probabilities

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619496%2F03_-_008_-_Temperature_00.1748619496769.png)

In this example, Claude might assign a 30% probability to "about", 20% to "would", 10% to "of", and so on. The model then selects one token and repeats this process to build complete responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619497%2F03_-_008_-_Temperature_05.1748619497297.png)

## What Temperature Does

Temperature is a decimal value between 0 and 1 that directly influences these selection probabilities. It's like adjusting the "creativity dial" on Claude's responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619497%2F03_-_008_-_Temperature_06.1748619497674.png)

At low temperatures (near 0), Claude becomes very deterministic - it almost always picks the highest probability token. At high temperatures (near 1), Claude distributes probability more evenly across options, leading to more varied and creative outputs.

## Temperature Ranges and Use Cases

Different tasks call for different temperature settings:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619499%2F03_-_008_-_Temperature_10.1748619499025.png)

### Low Temperature (0.0 - 0.3)

- Factual responses
- Coding assistance
- Data extraction
- Content moderation

### Medium Temperature (0.4 - 0.7)

- Summarization
- Educational content
- Problem-solving
- Creative writing with constraints

### High Temperature (0.8 - 1.0)

- Brainstorming
- Creative writing
- Marketing content
- Joke generation

## Implementing Temperature in Code

Adding temperature support to your chat function is straightforward. Here's how to modify your existing function:

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```

The key changes are adding temperature=1.0 as a parameter and including "temperature": temperature in the params dictionary.

```
temperature=1.0
```

```
"temperature": temperature
```

## Testing Temperature Effects

To see temperature in action, try generating movie ideas with different settings:

```
# Low temperature - more predictable
answer = chat(messages, temperature=0.0)

# High temperature - more creative  
answer = chat(messages, temperature=1.0)
```

```
# Low temperature - more predictable
answer = chat(messages, temperature=0.0)

# High temperature - more creative  
answer = chat(messages, temperature=1.0)
```

With temperature=0.0, you might consistently get responses like "A time-traveling archaeologist must prevent ancient artifacts from being stolen." With temperature=1.0, you'll see much more variety in the creative concepts generated.

## Key Takeaways

Remember that temperature doesn't guarantee different outputs - it just changes the probability of getting them. Even at high temperatures, Claude might occasionally produce similar responses. The key is matching your temperature setting to your task:

- Use low temperatures when you need consistent, factual responses
- Use high temperatures when you want creativity and variety
- Experiment with different values to find what works best for your specific use case
Temperature is one of the most practical parameters for fine-tuning Claude's behavior, making it an essential tool in your AI development toolkit.

---

## Course satisfaction survey

> https://anthropic.skilljar.com/claude-with-google-vertex/297285

## Course satisfaction survey

# Course Satisfaction Survey - Google Vertex

---

## Response streaming

> https://anthropic.skilljar.com/claude-with-google-vertex/289162

details

## Response streaming

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building chat applications with Claude, there's a significant user experience challenge: responses can take 10-30 seconds to generate, leaving users staring at a loading spinner. The solution is response streaming, which lets users see text appear chunk by chunk as Claude generates it, creating a much more responsive feel.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619503%2F03_-_009_-_Response_Streaming_00.1748619503472.png)

## The Problem with Standard Responses

In a typical chat setup, your server sends a user message to Claude and waits for the complete response before sending anything back to the client. This creates an awkward delay where users have no feedback that anything is happening.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619504%2F03_-_009_-_Response_Streaming_02.1748619503994.png)

## How Streaming Works

With streaming enabled, Claude immediately sends back an initial response indicating it has received your request and is starting to generate text. Then you receive a series of events, each containing a small piece of the overall response.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619504%2F03_-_009_-_Response_Streaming_03.1748619504478.png)

Your server can forward these text chunks to your client application as they arrive, allowing users to see the response building up word by word. All of these events are part of a single request to Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619505%2F03_-_009_-_Response_Streaming_04.1748619504964.png)

## Understanding Stream Events

When you enable streaming, Claude sends back several types of events:

- MessageStart - A new message is being sent
- ContentBlockStart - Start of a new block containing text, tool use, or other content
- ContentBlockDelta - Chunks of the actual generated text
- ContentBlockStop - The current content block has been completed
- MessageDelta - The current message is complete
- MessageStop - End of information about the current message

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619505%2F03_-_009_-_Response_Streaming_11.1748619505385.png)

The ContentBlockDelta events contain the actual generated text that you'll want to display to users.

```
ContentBlockDelta
```

## Basic Streaming Implementation

To enable streaming, add stream=True to your messages.create call:

```
stream=True
```

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)
```

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619506%2F03_-_009_-_Response_Streaming_12.1748619505920.png)

## Simplified Text Streaming

Rather than manually parsing events, you can use the SDK's simplified streaming interface that extracts just the text content:

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")
```

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")
```

This approach automatically filters out everything except the actual text content, which is usually what you need for displaying responses to users.

## Getting the Final Message

While streaming is great for user experience, you often need the complete message for storage or further processing. After streaming completes, you can get the assembled final message:

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        pass  # Send to client in real application
    
    final_message = stream.get_final_message()
```

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        pass  # Send to client in real application
    
    final_message = stream.get_final_message()
```

This gives you both the streaming capability for user experience and the complete message object for database storage or conversation history.

## Practical Considerations

Each text chunk in the stream can contain multiple words or even complete sentences - you're not guaranteed to receive exactly one word per event. The chunk size depends on how quickly Claude generates each portion of text.

In production applications, you'll typically forward these text chunks immediately to your client application through WebSockets or Server-Sent Events, allowing users to see responses appear in real-time while maintaining the complete conversation history on your server.

---

## Controlling model output

> https://anthropic.skilljar.com/claude-with-google-vertex/289160

details

## Controlling model output

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Beyond crafting better prompts, there are two powerful techniques for controlling Claude's output: prefilled assistant messages and stop sequences. These methods give you precise control over how Claude responds and when it stops generating text.

## Prefilled Assistant Messages

Message prefilling lets you provide the beginning of Claude's response, which it will then continue from that starting point. This technique is incredibly useful for steering Claude in a specific direction.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619499%2F03_-_010_-_Controlling_Model_Output_01.1748619499244.png)

Here's how it works: instead of just sending a user message, you add an assistant message at the end of your message list. Claude sees this assistant message and thinks "I've already started responding to this question, so I should continue from where I left off."

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619499%2F03_-_010_-_Controlling_Model_Output_05.1748619499761.png)

For example, if you ask "Is tea or coffee better at breakfast?" without prefilling, Claude typically gives a balanced response mentioning both options. But if you add an assistant message saying "Coffee is better because", Claude will continue from there and build a case for coffee.

The key thing to understand is that Claude continues from exactly where your prefilled text ends. If you write "Coffee is better because", Claude won't repeat that text - it will pick up right after "because" and complete the thought.

Here's the code structure:

```
messages = []
add_user_message(messages, "Is tea or coffee better at breakfast?")
add_assistant_message(messages, "Coffee is better because")
answer = chat(messages)
```

```
messages = []
add_user_message(messages, "Is tea or coffee better at breakfast?")
add_assistant_message(messages, "Coffee is better because")
answer = chat(messages)
```

You can steer Claude in any direction using this technique:

- Favor coffee: "Coffee is better because"
- Favor tea: "Tea is better because"
- Take a contrarian stance: "Neither is very good because"

## Stop Sequences

Stop sequences force Claude to end its response as soon as it generates a specific string of characters. This is perfect for controlling the length or endpoint of responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619500%2F03_-_010_-_Controlling_Model_Output_15.1748619500461.png)

The concept is straightforward: you provide a list of strings, and when Claude generates any of those strings, it immediately stops and returns whatever it has generated up to that point.

For example, if you ask Claude to "Count from 1 to 10" with a stop sequence of "5", you'll get:

```
add_user_message(messages, "Count from 1 to 10")
answer = chat(messages, stop_sequences=["5"])
```

```
add_user_message(messages, "Count from 1 to 10")
answer = chat(messages, stop_sequences=["5"])
```

This returns: "1, 2, 3, 4, " - stopping right before the "5" is included in the output.

You can be more precise with your stop sequences. If you want to avoid the trailing comma and space, use stop_sequences=[", 5"] instead. This will give you a cleaner result: "1, 2, 3, 4".

```
stop_sequences=[", 5"]
```

Stop sequences are particularly useful for:

- Limiting list lengths
- Stopping at specific markers or delimiters
- Creating consistent output formats
- Preventing overly long responses
Both techniques give you fine-grained control over Claude's behavior, allowing you to create more predictable and targeted responses for your applications.

---

## Structured data

> https://anthropic.skilljar.com/claude-with-google-vertex/289158

details

## Structured data

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you need Claude to generate structured data like JSON, Python code, or bulleted lists, you'll often run into a common problem: Claude wants to be helpful and add explanatory text around your content. While this is usually great, sometimes you need just the raw data with nothing else.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619492%2F03_-_011_-_Structured_Data_02.1748619492360.png)

Consider building a web app that generates AWS EventBridge rules. Users enter a description, click generate, and expect to see clean JSON they can immediately copy and use. If Claude returns the JSON wrapped in markdown code blocks with explanatory headers and footers, users can't simply hit "copy all" - they'd have to manually select just the JSON portion.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619493%2F03_-_011_-_Structured_Data_05.1748619492885.png)

This pattern shows up whenever you're generating structured data. Claude naturally wants to explain its work, but in many cases, you want only the content you're asking for and nothing else.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619493%2F03_-_011_-_Structured_Data_06.1748619493294.png)

## Combining Stop Sequences with Assistant Message Prefilling

The solution combines two techniques we've covered: stop sequences and assistant message prefilling. Here's how it works in practice:

```
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
```

```
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
```

When you run this code, you get back just the JSON content without any markdown formatting or additional commentary.

## How It Works Behind the Scenes

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619493%2F03_-_011_-_Structured_Data_15.1748619493726.png)

Here's what happens when Claude processes your request:

- Claude reads your user message and thinks "I need to write a full rule and probably describe it"
- It sees the prefilled assistant message and assumes it already started writing the JSON markdown block
- Claude thinks "Oh, I've already started the JSON part, so I just need to write the actual JSON content"
- It generates the JSON content
- When Claude tries to close the markdown block with ```, it hits the stop sequence and generation stops immediately

```
```
```

The result is that you get everything between the prefilled start and the stop sequence - exactly the content you wanted.

## Cleaning Up the Output

The returned text might have some extra newlines, but you can easily clean this up:

```
import json

# Parse as JSON to validate and format
parsed_json = json.loads(text.strip())
```

```
import json

# Parse as JSON to validate and format
parsed_json = json.loads(text.strip())
```

This technique works for any structured data format, not just JSON. Whether you're generating Python code, bulleted lists, or any other specific content format, you can use assistant message prefilling to start the response and stop sequences to end it exactly where you want.

This approach gives you precise control over Claude's output format, ensuring your applications get clean, usable data without extra formatting or commentary that might interfere with downstream processing.

---

## Structured data exercise

> https://anthropic.skilljar.com/claude-with-google-vertex/289152

## Structured data exercise

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Quiz on accessing Claude with the API

> https://anthropic.skilljar.com/claude-with-google-vertex/289281

## Quiz on accessing Claude with the API

# Quiz on Accessing Claude with the API

---

## Prompt evaluation

> https://anthropic.skilljar.com/claude-with-google-vertex/289159

details

## Prompt evaluation

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques to write better prompts, while prompt evaluation helps you measure how well those prompts actually work.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619540%2F04_-_001_-_Prompt_Evaluation_00.1748619540294.png)

## Prompt Engineering vs Prompt Evaluation

Prompt engineering is your toolkit for writing and improving prompts. It's a set of best practices that help Claude understand exactly what you're asking for and how you want it to respond. Think of it as the craft of prompt writing - techniques like multishot prompting, structuring with XML tags, and many other approaches we'll explore.

Prompt evaluation, on the other hand, is about measurement. It's automated testing that gives you objective metrics on whether your prompts are actually effective. Instead of guessing if your prompt works well, evaluation lets you:

- Test against expected answers
- Compare different versions of the same prompt
- Review outputs for errors

## The Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619541%2F04_-_001_-_Prompt_Evaluation_10.1748619541009.png)

Option 1: Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

Option 2: Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

Option 3: Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective data. This requires more work and cost upfront, but gives you much more confidence in your prompt's reliability.

## Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are traps that all engineers fall into - myself included. It's natural to write a prompt, test it a couple times with your own inputs, and think "this looks good enough." But when you're building serious applications, this approach often leads to problems in production.

The issue is that you can't predict all the ways users will interact with your prompt. What seems to work perfectly in your limited testing might fail completely when faced with real-world usage patterns.

## The Value of Systematic Evaluation

Option 3 - running your prompt through an evaluation pipeline - gives you objective data about performance. Instead of relying on gut feelings or limited manual testing, you get measurable scores that tell you how well your prompt handles a variety of inputs.

This approach lets you iterate confidently. You can make changes to your prompt and immediately see whether those changes improve or hurt performance. It's the difference between guessing and knowing whether your prompt improvements actually work.

While evaluation requires more upfront investment in time and resources, it pays dividends when you need reliable, production-ready prompts that work consistently across diverse user inputs.

---

## A typical eval workflow

> https://anthropic.skilljar.com/claude-with-google-vertex/289161

details

## A typical eval workflow

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619547%2F04_-_002_-_A_Typical_Eval_Workflow_00.1748619547713.png)

## Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

```
prompt = f"""
Please answer the user's question:

{question}
"""
```

```
prompt = f"""
Please answer the user's question:

{question}
"""
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619548%2F04_-_002_-_A_Typical_Eval_Workflow_04.1748619548527.png)

This basic prompt will serve as our baseline for testing and improvement.

## Step 2: Create an Evaluation Dataset

Your evaluation dataset contains sample inputs that you'll feed into your prompt. Since our prompt only has one input (the user's question), we need a collection of different questions to test with.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619549%2F04_-_002_-_A_Typical_Eval_Workflow_06.1748619549029.png)

The dataset contains questions that we will merge with our prompt. You can assemble these datasets by hand or generate them using Claude. In real-world evaluations, you might have tens, hundreds, or even thousands of different records, but we'll start with just three questions for this example:

- What's 2+2?
- How do I make oatmeal?
- How far away is the Moon?

## Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude and collect the responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619549%2F04_-_002_-_A_Typical_Eval_Workflow_08.1748619549492.png)

For example, the first question becomes a complete prompt that Claude processes and returns an answer like "2 + 2 = 4". You repeat this process for all questions in your dataset, building a collection of question-answer pairs.

## Step 4: Feed Through a Grader

Now comes the crucial step of objectively measuring the quality of Claude's responses. You take each question-answer pair and feed them into a grader that scores the responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619550%2F04_-_002_-_A_Typical_Eval_Workflow_11.1748619549867.png)

The grader assigns scores (typically 1-10) based on answer quality:

- 10 = Perfect answer with no room for improvement
- 4 = Adequate but definitely room for improvement
- Lower scores indicate poor responses
After scoring all responses, you average the scores together. In our example, scores of 10, 4, and 9 average to 7.66, giving you an objective measurement of your prompt's performance.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619550%2F04_-_002_-_A_Typical_Eval_Workflow_14.1748619550433.png)

## Step 5: Change Prompt and Repeat

With your baseline score established, you can now modify your prompt and run the entire process again to see if your changes improve performance.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619551%2F04_-_002_-_A_Typical_Eval_Workflow_15.1748619550921.png)

For example, you might enhance the original prompt by adding more specific instructions:

```
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

```
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

## Prompt Scoring

The power of this workflow lies in getting objective measurements of prompt performance. You can compare scores between different prompt versions to determine which performs better.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619551%2F04_-_002_-_A_Typical_Eval_Workflow_17.1748619551452.png)

In our example:

- Prompt v1 scored 7.66
- Prompt v2 scored 8.7
The higher score for v2 provides objective evidence that adding "Answer the question with ample detail" improved the prompt's performance. You can then use the better-performing version or continue iterating to achieve even higher scores.

This systematic approach removes guesswork from prompt improvement and gives you a reliable framework for optimization. While there's complexity in implementing effective graders, this workflow provides a solid foundation for building your own evaluation system.

---

## Generating test datasets

> https://anthropic.skilljar.com/claude-with-google-vertex/289163

details

1
                                    download

## Generating test datasets

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building a custom prompt evaluation workflow starts with creating a solid prompt and then generating test data to see how well it performs. Let's walk through setting up an evaluation system for a prompt that helps users write AWS-specific code.

## Setting Up the Goal

Our prompt needs to assist users in writing three specific types of output for AWS use cases:

- Python code
- JSON configuration files
- Regular expressions
The key requirement is that when a user requests help with a task, we return clean output in one of these formats without any extra explanations, headers, or footers.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619548%2F04_-_003_-_Generating_Test_Datasets_01.1748619548328.png)

Here's our initial prompt template:

```
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

```
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

## Creating an Evaluation Dataset

An evaluation dataset contains inputs that we'll feed into our prompt to test its performance. For our case, we need an array of JSON objects where each object has a "task" property describing what we want Claude to accomplish.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619548%2F04_-_003_-_Generating_Test_Datasets_05.1748619548824.png)

You can create datasets in two ways:

- Assemble them manually
- Generate them automatically using Claude
For automatic generation, using a faster model like Haiku makes sense since we're generating test data rather than production output.

## Generating Test Data with Code

Let's build a function that asks Claude to generate test cases for us. The function will create a comprehensive prompt that requests specific types of AWS-related tasks.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619549%2F04_-_003_-_Generating_Test_Datasets_09.1748619549203.png)

Here's the core function structure:

```
def generate_dataset():
    prompt = """
    Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts 
    that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of objects, 
    each representing task that requires Python, JSON, or a Regex to complete.
    
    Example output:
    ```json
    [
        {
            "task": "Description of task",
        },
        ...additional
    ]
    ```
    
    * Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
    * Focus on tasks that do not require writing much code
    
    Please generate 3 objects.
    """
```

```
def generate_dataset():
    prompt = """
    Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts 
    that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of objects, 
    each representing task that requires Python, JSON, or a Regex to complete.
    
    Example output:
    ```json
    [
        {
            "task": "Description of task",
        },
        ...additional
    ]
    ```
    
    * Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
    * Focus on tasks that do not require writing much code
    
    Please generate 3 objects.
    """
```

## Implementing the Generation Logic

To get clean JSON output from Claude, we'll use the pre-filling technique with stop sequences:

```
messages = []
add_user_message(messages, prompt)
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
return json.loads(text)
```

```
messages = []
add_user_message(messages, prompt)
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
return json.loads(text)
```

This approach ensures Claude starts its response with properly formatted JSON and stops at the closing markdown fence.

## Testing and Saving the Dataset

After running the generation function, you should get back realistic test cases like:

- Create a Python function to extract the AWS region from an ARN
- Write a JSON configuration for an AWS Lambda function
- Develop a regular expression to validate an AWS S3 bucket name

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619549%2F04_-_003_-_Generating_Test_Datasets_16.1748619549748.png)

Save your generated dataset to a file for easy reuse:

```
dataset = generate_dataset()

with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=2)
```

```
dataset = generate_dataset()

with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=2)
```

This creates a dataset.json file in your notebook directory containing all your test cases, ready to use for prompt evaluation in the next steps of your workflow.

```
dataset.json
```

#### Downloads

- 001_prompt_evals.ipynb
                                                (opens in new tab)

---

## Running the eval

> https://anthropic.skilljar.com/claude-with-google-vertex/289166

details

## Running the eval

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we have our evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619554%2F04_-_004_-_Running_the_Eval_00.1748619554019.png)

The evaluation process follows a clear workflow: we take our dataset of test cases, combine each one with our prompt template, send it to Claude for processing, and then evaluate the output using a grader system.

## Building the Core Functions

The evaluation pipeline consists of three main functions, each with a specific responsibility. Let's start with the simplest one - the function that handles individual prompts.

## The run_prompt Function

This function takes a test case and merges it with our prompt template:

```
def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""
    
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output
```

```
def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""
    
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output
```

Right now, we're keeping the prompt extremely simple. We're not including any formatting instructions, so Claude will likely return more verbose output than we need. We'll refine this later as we iterate on our prompt design.

## The run_test_case Function

This function orchestrates running a single test case and grading the result:

```
def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)
    
    # TODO - Grading
    score = 10
    
    return {
        "output": output,
        "test_case": test_case,
        "score": score
    }
```

```
def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)
    
    # TODO - Grading
    score = 10
    
    return {
        "output": output,
        "test_case": test_case,
        "score": score
    }
```

For now, we're using a hardcoded score of 10. The grading logic is where we'll spend significant time in upcoming sections, but this placeholder lets us test the overall pipeline.

## The run_eval Function

This function coordinates the entire evaluation process:

```
def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    return results
```

```
def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    return results
```

This function processes every test case in our dataset and collects all the results into a single list.

## Running the Evaluation

To execute our evaluation pipeline, we load our dataset and run it through our functions:

```
with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)
```

```
with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)
```

The first time you run this, expect it to take some time - even with Claude Haiku, it can take around 30 seconds to process a full dataset. We'll cover optimization techniques later.

## Examining the Results

The evaluation returns a structured JSON array where each object represents one test case result:

```
print(json.dumps(results, indent=2))
```

```
print(json.dumps(results, indent=2))
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619554%2F04_-_004_-_Running_the_Eval_18.1748619554611.png)

Each result contains three key pieces of information:

- output: The complete response from Claude
- test_case: The original test case that was processed
- score: The evaluation score (currently hardcoded)
As you can see in the output, Claude generates quite verbose responses since we haven't provided specific formatting instructions yet. This is exactly the kind of issue we'll address as we refine our prompts.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619555%2F04_-_004_-_Running_the_Eval_01.1748619555038.png)

## What We've Accomplished

At this point, we've successfully built the core evaluation pipeline. We can take our dataset, process it through Claude, and collect structured results. The major missing piece is the grading system - that hardcoded score of 10 needs to be replaced with actual evaluation logic.

This pipeline represents the foundation of most AI evaluation systems. While it may seem simple, you've just built the majority of what an eval pipeline actually does. The complexity comes in the details - better prompts, sophisticated grading, and performance optimizations.

Next, we'll dive into the critical topic of graders, which will transform our hardcoded scores into meaningful evaluations of Claude's performance.

---

## Model based grading

> https://anthropic.skilljar.com/claude-with-google-vertex/289168

details

1
                                    download

## Model based grading

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building prompt evaluation workflows, grading systems provide objective signals about output quality. A grader takes model output and returns some kind of measurable feedback - typically a number between 1 and 10, where 10 represents high quality and 1 represents poor quality.

## Types of Graders

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619610%2F04_-_005_-_Model_Based_Grading_03.1748619610196.png)

There are three main approaches to grading model outputs:

- Code graders - Programmatically evaluate outputs using custom code
- Model graders - Use another AI model to assess the quality
- Human graders - Have people manually review and score outputs

### Code Graders

Code graders let you implement any programmatic check you can imagine. Common uses include:

- Checking output length
- Verifying output does or doesn't contain certain words
- Syntax validation for JSON, Python, or regex
- Readability scores to ensure appropriate reading levels

### Model Graders

Model graders offer tremendous flexibility by using an additional API call to evaluate outputs. They're useful for assessing:

- Response quality
- Quality of instruction following
- Completeness
- Helpfulness
- Safety

### Human Graders

Human graders provide the most flexibility but come with significant downsides. While humans can evaluate responses for any criteria imaginable, the process is time-consuming and tedious.

## Defining Evaluation Criteria

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619610%2F04_-_005_-_Model_Based_Grading_06.1748619610723.png)

Before implementing any grader, you need clear evaluation criteria. For a code generation prompt, you might focus on:

- Format - Should return only Python, JSON, or Regex without explanation
- Valid Syntax - Produced code should have valid syntax
- Task Following - Response should directly address the user's task with accurate code

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619611%2F04_-_005_-_Model_Based_Grading_07.1748619611291.png)

The first two criteria work well with code graders, while task following is better suited for model graders due to their flexibility.

## Implementing a Model Grader

Model graders are often the easiest to implement. Here's a basic structure:

```
def grade_by_model(test_case, output):
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
```

```
def grade_by_model(test_case, output):
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619612%2F04_-_005_-_Model_Based_Grading_11.1748619611803.png)

The grading prompt should be comprehensive and include:

- Clear role definition for the grader
- The original task
- The AI-generated solution to evaluate
- Specific output format requirements
Ask for more than just a score. Request strengths, weaknesses, and reasoning alongside the numerical score. This prevents the model from defaulting to middling scores like 6 and forces more thoughtful evaluation.

## Integrating Graders into Your Workflow

Once you have a grader function, integrate it into your test case runner:

```
def run_test_case(test_case):
    output = run_prompt(test_case)
    
    # Call the model grader
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]
    
    return {
        "output": output, 
        "test_case": test_case, 
        "score": score,
        "reasoning": reasoning
    }
```

```
def run_test_case(test_case):
    output = run_prompt(test_case)
    
    # Call the model grader
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]
    
    return {
        "output": output, 
        "test_case": test_case, 
        "score": score,
        "reasoning": reasoning
    }
```

After running all test cases, calculate an average score to get an objective metric for your prompt's performance:

```
from statistics import mean

def run_eval(dataset):
    results = []
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")
    
    return results
```

```
from statistics import mean

def run_eval(dataset):
    results = []
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")
    
    return results
```

This gives you a concrete number to focus on improving. While model graders can be somewhat capricious and might benefit from better guidance, they provide a starting point for objective evaluation that you can iterate on and improve.

#### Downloads

- 001_prompt_evals_grader.ipynb
                                                (opens in new tab)

---

## Code based grading

> https://anthropic.skilljar.com/claude-with-google-vertex/289167

details

1
                                    download

## Code based grading

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When evaluating AI models that generate code, you need more than just checking if the response makes sense. You also need to verify that the generated code actually has valid syntax and follows the correct format. This is where code-based grading comes in.

## How Code Grading Works

Code grading validates two key aspects of AI-generated responses:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619603%2F04_-_006_-_Code_Based_Grading_00.1748619603473.png)

- Format - The response should return only the requested code type (Python, JSON, or Regex) without explanations
- Valid Syntax - The generated code should actually parse correctly as the intended language
- Task Following - The response should directly address what was asked and be accurate
The first two criteria are handled by the code grader, while task following is evaluated by the model grader. Together, they provide a comprehensive evaluation.

## Syntax Validation Functions

To check if generated code has valid syntax, you can create three helper functions that attempt to parse the output:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619604%2F04_-_006_-_Code_Based_Grading_02.1748619604039.png)

```
def validate_json(text):
    try:
        json.loads(text.strip())
        return 10
    except json.JSONDecodeError:
        return 0

def validate_python(text):
    try:
        ast.parse(text.strip())
        return 10
    except SyntaxError:
        return 0

def validate_regex(text):
    try:
        re.compile(text.strip())
        return 10
    except re.error:
        return 0
```

```
def validate_json(text):
    try:
        json.loads(text.strip())
        return 10
    except json.JSONDecodeError:
        return 0

def validate_python(text):
    try:
        ast.parse(text.strip())
        return 10
    except SyntaxError:
        return 0

def validate_regex(text):
    try:
        re.compile(text.strip())
        return 10
    except re.error:
        return 0
```

Each function tries to parse the text as its respective format. If parsing succeeds, it returns a perfect score of 10. If it fails with an error, the syntax is invalid and returns 0.

## Dataset Format Requirements

For the code grader to know which validator to use, your test cases need to specify the expected output format:

```
{
    "task": "Create a Python function to validate an AWS IAM username",
    "format": "python"
}
```

```
{
    "task": "Create a Python function to validate an AWS IAM username",
    "format": "python"
}
```

You can update your dataset generation prompt to automatically include this format field by adding it to the example output structure.

## Improving Prompt Clarity

To get better results from your AI model, make your prompt instructions more specific about the expected output format:

```
* Respond only with Python, JSON, or a plain Regex
* Do not add any comments or commentary or explanation
```

```
* Respond only with Python, JSON, or a plain Regex
* Do not add any comments or commentary or explanation
```

You can also use a pre-filled assistant message with code blocks to encourage the model to return just the raw code:

```
add_assistant_message(messages, "```code")
```

```
add_assistant_message(messages, "```code")
```

This tells Claude to start generating code content without having to specify whether it's Python, JSON, or Regex upfront.

## Combining Scores

The final step is merging the model grader score with the code grader score. A simple approach is to average them:

```
model_grade = grade_by_model(test_case, output)
model_score = model_grade["score"]
syntax_score = grade_syntax(output, test_case)

score = (model_score + syntax_score) / 2
```

```
model_grade = grade_by_model(test_case, output)
model_score = model_grade["score"]
syntax_score = grade_syntax(output, test_case)

score = (model_score + syntax_score) / 2
```

This gives equal weight to both content quality and technical correctness. You might adjust these weights based on what matters more for your specific use case.

## Testing Your Implementation

Once you've implemented code grading, run your evaluation to get a baseline score. The score itself isn't inherently good or bad - what matters is whether you can improve it by refining your prompts. This gives you a quantitative way to measure prompt engineering progress rather than relying on subjective assessment.

#### Downloads

- 001_prompt_evals_fns.ipynb
                                                (opens in new tab)

---

## Exercise on prompt evals

> https://anthropic.skilljar.com/claude-with-google-vertex/289164

details

1
                                    download

## Exercise on prompt evals

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Downloads

- 001_prompt_evals_complete.ipynb
                                                (opens in new tab)

---

## Quiz on prompt evaluation

> https://anthropic.skilljar.com/claude-with-google-vertex/289279

## Quiz on prompt evaluation

# Quiz on Prompt Evaluation

---

## Prompt engineering

> https://anthropic.skilljar.com/claude-with-google-vertex/289169

details

2
                                    download

## Prompt engineering

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt engineering is about taking a prompt you've written and improving it to get more reliable, higher-quality outputs. This process involves iterative refinement - starting with a basic prompt, evaluating its performance, then systematically applying engineering techniques to improve it.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619608%2F05_-_001_-_Prompt_Engineering_00.1748619608702.png)

## The Iterative Improvement Process

The approach follows a clear cycle that you can repeat until you achieve your desired results:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619609%2F05_-_001_-_Prompt_Engineering_01.1748619609168.png)

- Set a goal - Define what you want your prompt to accomplish
- Write an initial prompt - Create a basic first attempt
- Evaluate the prompt - Test it against your criteria
- Apply prompt engineering techniques - Use specific methods to improve performance
- Re-evaluate - Verify that your changes actually improved the results
You repeat the last two steps until you're satisfied with the performance. Each iteration should show measurable improvement in your evaluation scores.

## Example: Meal Planning for Athletes

Let's walk through a practical example. The goal is to create a prompt that generates a one-day meal plan for athletes based on their physical characteristics and requirements.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619609%2F05_-_001_-_Prompt_Engineering_04.1748619609611.png)

The prompt takes these inputs and should produce a comprehensive meal plan with caloric totals, macronutrient breakdowns, and specific meal details with portions and timing.

## Setting Up the Evaluation Framework

To measure improvement systematically, you need a robust evaluation setup. The framework includes:

- Dataset generation - Create test cases that represent real-world scenarios
- Automated scoring - Use consistent criteria to evaluate outputs
- Performance tracking - Monitor improvements across iterations
When setting up your evaluator, be mindful of API rate limits. Start with low concurrency (1-3 concurrent requests) and only increase if you don't encounter rate limiting errors.

## Creating Your Initial Prompt

Start with something simple, even if you know it's not great. Here's an example of a basic first attempt:

```
What should this person eat?

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}  
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
```

```
What should this person eat?

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}  
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
```

This prompt is intentionally basic and will likely produce poor results. That's exactly what you want - a clear baseline to improve from.

## Establishing Evaluation Criteria

Define specific criteria that your prompt should meet. For the meal planning example, good output should include:

- Daily caloric total
- Macronutrient breakdown
- Meals with exact foods, portions, and timing
These criteria help the evaluation model grade outputs consistently and give you clear targets for improvement.

## Measuring Baseline Performance

Run your initial prompt through the evaluation framework. Don't be discouraged by low scores - a score of 2.3 out of 10 is actually perfect for a starting point. It gives you plenty of room to demonstrate improvement.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619610%2F05_-_001_-_Prompt_Engineering_18.1748619610284.png)

## Analyzing Results

Most evaluation frameworks generate detailed reports showing how each test case performed. These reports typically include:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619611%2F05_-_001_-_Prompt_Engineering_19.1748619611159.png)

- Individual test case results - See exactly what the model produced
- Scoring breakdown - Understand why certain outputs scored poorly
- Reasoning - Get feedback on what's missing or incorrect
Use this detailed feedback to identify specific areas where your prompt needs improvement. Look for patterns across multiple test cases to understand systematic issues rather than one-off problems.

## Next Steps

With your baseline established and evaluation framework in place, you're ready to start applying specific prompt engineering techniques. Each technique you apply should result in measurable improvement in your evaluation scores, moving you closer to your ideal output quality.

The key is to make one change at a time, evaluate the impact, then decide whether to keep the change or try a different approach. This systematic process ensures you understand which techniques work best for your specific use case.

#### Downloads

- 001_prompting.ipynb
                                                (opens in new tab)
- 002_prompting_completed.ipynb
                                                (opens in new tab)

---

## Being clear and direct

> https://anthropic.skilljar.com/claude-with-google-vertex/289170

details

## Being clear and direct

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The first line of your prompt is the most important part of your entire request. This is where you set the stage for everything that follows, and getting it right can dramatically improve your results.

## Being Clear and Direct

When crafting that crucial first line, you want to focus on two key principles: clarity and directness. This means using simple language that leaves no room for ambiguity about what you want Claude to do.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619590%2F05_-_002_-_Being_Clear_and_Direct_02.1748619589874.png)

## Clear Communication

Being "clear" means:

- Use simple language that anyone can understand
- State exactly what you want without beating around the bush
- Lead with a straightforward statement of Claude's task
Instead of writing something vague like "I need to know about those things people put on their roofs that use sun - those solar panel things, I think they're called," be direct and write: "Write three paragraphs about how solar panels work."

## Direct Instructions

Being "direct" focuses on how you structure your request:

- Use instructions, not questions
- Start with direct action verbs like "Write," "Create," or "Generate"
Rather than asking "I was reading about renewable energy and geothermal energy sounds neat. What countries use it?" try: "Identify three countries that use geothermal energy. Include generation stats for each."

## Putting It Into Practice

Let's see this technique in action. Starting with a weak prompt that simply asked "What should this person eat?" we can apply our clear and direct approach.

The improved version becomes: Generate a one-day meal plan for an athlete that meets their dietary restrictions.

```
Generate a one-day meal plan for an athlete that meets their dietary restrictions.
```

This revision immediately tells Claude:

- What action to take (generate)
- What to create (a meal plan)
- Key constraints (one day, for an athlete, meeting dietary restrictions)

## Results Matter

This simple change can make a significant difference in output quality. In our example, the evaluation score jumped from 2.32 to 3.92 - a substantial improvement from just restructuring that opening line.

The key takeaway: start strong with a clear, direct statement that uses an action verb and explicitly defines the task. This sets Claude up for success and gives you much better results right from the start.

---

## Being specific

> https://anthropic.skilljar.com/claude-with-google-vertex/289165

details

## Being specific

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," Claude could go in countless directions. The story might be 200 words or 2,000 words. It might have one character or five. It might focus on comedy or drama. Without guidance, you're rolling the dice on what you'll get.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619654%2F05_-_003_-_Being_Specific_00.1748619653960.png)

## Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see them used together in professional applications.

### Quality Guidelines

The first type focuses on listing qualities that your output should have. These guidelines control attributes like:

- Length constraints (keep under 1,000 words)
- Structural requirements (include a clear action that reveals the character's talent)
- Content specifications (include at least one supporting character)

### Process Steps

The second type provides specific steps for the model to follow. This approach makes Claude think through different options and considerations before generating the final response. For example:

- Brainstorm 3 talents that would create dramatic tension
- Pick the most interesting talent
- Outline a pivotal scene that reveals the talent
- Brainstorm 3 supporting character types that could increase the impact of this discovery

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619654%2F05_-_003_-_Being_Specific_05.1748619654657.png)

## Real-World Results

The impact of being specific can be dramatic. In testing a meal planning prompt, adding guidelines improved the evaluation score from 3.92 to 7.86 - more than doubling the quality of the output. Here's what that looked like in practice:

```
Generate a one-day meal plan for an athlete that meets their dietary restrictions.

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}

Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
```

```
Generate a one-day meal plan for an athlete that meets their dietary restrictions.

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}

Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
```

## When to Use Each Approach

Quality guidelines work well for almost any prompt you write. They're your baseline for ensuring consistent, useful output.

Process steps are particularly valuable when you're dealing with:

- Troubleshooting complex problems
- Decision making scenarios
- Critical thinking tasks
- Situations where you want Claude to consider multiple perspectives
For example, if you're asking Claude to analyze why a sales team's performance dropped 30% last quarter, you might want to force it to consider market conditions, individual performance, organizational changes, and customer feedback - areas it might not naturally explore without specific direction.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619655%2F05_-_003_-_Being_Specific_18.1748619655213.png)

The key is recognizing that Claude, like any tool, works better when you give it clear instructions about both what you want and how to get there. Being specific isn't about micromanaging the AI - it's about setting up the conditions for success.

---

## Structure with XML tags

> https://anthropic.skilljar.com/claude-with-google-vertex/289171

details

## Structure with XML tags

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you're building prompts that include a lot of content, Claude can sometimes struggle to understand which pieces of text belong together or what different sections are supposed to represent. XML tags provide a simple way to add structure and clarity to your prompts, especially when you're interpolating large amounts of data.

## Why Structure Matters

Consider a prompt where you need to analyze 20 pages of sales records. Without clear boundaries, Claude might have trouble distinguishing between your instructions and the actual data you want analyzed.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619655%2F05_-_004_-_Structure_with_XML_Tags_00.1748619655719.png)

The example above shows how unclear boundaries can make it difficult for Claude to parse your intent. By wrapping different content sections in XML tags, you create clear delimiters that help Claude understand the structure of your prompt.

## Using XML Tags for Clarity

XML tags act as containers that separate distinct portions of your prompt. You can create custom tag names that describe the content they contain:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619656%2F05_-_004_-_Structure_with_XML_Tags_06.1748619656342.png)

In this case, wrapping the sales data in <sales_records> tags makes it immediately clear what that content represents. The tag name itself provides context about the data type.

```
<sales_records>
```

## A Practical Example

Here's a more dramatic example that shows why structure matters. On the left, you have a debugging request with mixed code and documentation:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619656%2F05_-_004_-_Structure_with_XML_Tags_10.1748619656864.png)

Without clear boundaries, Claude has to guess which parts are the buggy code and which parts are documentation. The improved version on the right uses XML tags to separate these concerns:

```
<my_code>
from datavortex import Pipeline, DataSource

def process_data(input_file, output_file):
    pipeline = Pipeline()
    source = DataSource.from_csv(input_file)
</my_code>

<docs>
# Creating a data source from data vortex
csv_source = DataSource.from_csv("data.csv")
</docs>
```

```
<my_code>
from datavortex import Pipeline, DataSource

def process_data(input_file, output_file):
    pipeline = Pipeline()
    source = DataSource.from_csv(input_file)
</my_code>

<docs>
# Creating a data source from data vortex
csv_source = DataSource.from_csv("data.csv")
</docs>
```

Now Claude can easily identify what needs debugging versus what serves as reference material.

## Applying Structure to Your Prompts

Even when your interpolated content isn't massive, XML tags can still improve clarity. For example, when generating meal plans, you might group athlete information together:

```
<athlete_information>
- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
</athlete_information>
```

```
<athlete_information>
- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
</athlete_information>
```

This makes it explicit that these values represent external input about the athlete, rather than part of your instructions.

## Key Benefits

- Most useful when including large amounts of context or data
- Help serve as clear delimiters for Claude to parse different content types
- Improve Claude's ability to understand the relationship between different parts of your prompt
- Make your prompts more maintainable and easier to debug
XML tags are particularly valuable when you're working with complex prompts that mix instructions, data, examples, and other content types. The clearer you can make the structure, the better Claude can understand and respond to your specific needs.

---

## Providing examples

> https://anthropic.skilljar.com/claude-with-google-vertex/289177

details

## Providing examples

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Providing examples in your prompts is one of the most effective prompt engineering techniques you'll use. This approach, known as "one-shot" or "multi-shot" prompting, involves giving Claude sample input/output pairs to guide its responses.

## How Examples Work

Let's look at a sentiment analysis example. Say you want Claude to categorize whether a tweet is positive or negative:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619655%2F05_-_005_-_Providing_Examples_00.1748619655115.png)

The challenge here is sarcasm. A tweet like "Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'" appears positive on the surface, but it's actually sarcastic and negative (Plan 9 is famously terrible).

## Adding Examples to Your Prompt

To handle this, you can add examples that show Claude how to respond correctly:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619655%2F05_-_005_-_Providing_Examples_04.1748619655529.png)

The key elements are:

- Clear introduction: "Here is a example input with an ideal response"
- XML tags for structure: <sample_input> and <ideal_output>

```
<sample_input>
```

```
<ideal_output>
```

- Concrete examples that demonstrate the desired behavior

## Handling Corner Cases

Multi-shot prompting shines when dealing with edge cases. For the sarcasm problem, you might add:

```
Be especially careful with tweets that contain sarcasm.
For example:
<sample_input>
Oh yeah, I really needed a flight delay tonight! Excellent!
</sample_input>
<ideal_output>
Negative
</ideal_output>
```

```
Be especially careful with tweets that contain sarcasm.
For example:
<sample_input>
Oh yeah, I really needed a flight delay tonight! Excellent!
</sample_input>
<ideal_output>
Negative
</ideal_output>
```

This gives Claude a clear pattern to recognize sarcastic content that might otherwise be misclassified.

## Complex Output Formats

Examples are especially valuable when you need Claude to produce structured output like JSON objects or detailed reports. Instead of just describing the format, you show exactly what good output looks like.

## Finding Good Examples from Evaluations

When running prompt evaluations, look for your highest-scoring outputs in the HTML report:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619656%2F05_-_005_-_Providing_Examples_12.1748619655959.png)

Find examples that scored 10 (or your highest available score) and use those input/output pairs as examples in your prompt. This helps Claude understand what "perfect" looks like for your specific task.

## Adding Context to Examples

For even better results, explain why an example is ideal. After showing the sample output, add a brief explanation:

```
</ideal_output>
This meal plan is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
```

```
</ideal_output>
This meal plan is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
```

This reinforces the specific qualities that make the output valuable.

## Best Practices

- Use XML tags to clearly structure your examples
- Start simple with one-shot prompting, then add more examples as needed
- Focus on edge cases that Claude might struggle with
- Include reasoning about why examples are good when possible
- Test iteratively - add examples based on evaluation results
Examples are particularly powerful because they show rather than tell. Instead of trying to describe every nuance of what you want, you demonstrate it directly. This makes your prompts more reliable and helps Claude understand complex requirements that might be difficult to explain in words alone.

---

## Exercise on prompting

> https://anthropic.skilljar.com/claude-with-google-vertex/289173

details

1
                                    download

## Exercise on prompting

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Downloads

- 003_exercise.ipynb
                                                (opens in new tab)

---

## Quiz on prompt engineering techniques

> https://anthropic.skilljar.com/claude-with-google-vertex/289278

## Quiz on prompt engineering techniques

# Quiz on Prompt Engineering Techniques

---

## Introducing tool use

> https://anthropic.skilljar.com/claude-with-google-vertex/289172

details

## Introducing tool use

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Tools allow Claude to access information from the outside world, extending its capabilities beyond what it learned during training. By default, Claude only knows information from its training data and can't access current events, real-time data, or external systems. Tool use solves this limitation by creating a structured way for Claude to request and receive fresh information.

## The Problem Without Tools

When users ask Claude for current information, it hits a wall. For example, if someone asks "What's the weather in San Francisco, California?" Claude has to respond with something like "I'm sorry, but I don't have access to up-to-date weather information."

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619646%2F06_-_001_-_Introducing_Tool_Use_05.1748619646201.png)

This creates a frustrating user experience when people need real-time data that Claude could theoretically help with if it just had access to current information.

## How Tool Use Works

Tool use follows a specific back-and-forth pattern between your application and Claude. Here's the complete flow:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619646%2F06_-_001_-_Introducing_Tool_Use_07.1748619646784.png)

- Initial Request: You send Claude a question along with instructions on how to get extra data from external sources
- Tool Request: Claude analyzes the question and decides it needs additional information, then asks for specific details about what data it needs
- Data Retrieval: Your server runs code to fetch the requested information from external APIs or databases
- Final Response: You send the retrieved data back to Claude, which then generates a complete response using both the original question and the fresh data

## Weather Example in Practice

Let's see how this works with the weather question. The process becomes much more specific:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619647%2F06_-_001_-_Introducing_Tool_Use_14.1748619647322.png)

When a user asks about current weather, you include details in your prompt about how to retrieve weather data. Claude recognizes it needs current information and requests weather data for the specific location. Your server then calls a weather API to get real-time conditions and sends that data back to Claude. Finally, Claude combines the fresh weather data with the user's question to provide an accurate, current response.

## Key Benefits

- Real-time Information: Access current data that wasn't available during Claude's training
- External System Integration: Connect Claude to databases, APIs, and other services
- Dynamic Responses: Provide answers based on the most up-to-date information available
- Structured Interaction: Claude knows exactly what information it needs and how to ask for it
Tool use transforms Claude from a static knowledge base into a dynamic assistant that can work with live data and external systems. This opens up possibilities for building applications that need both AI reasoning and access to current information.

---

## Project overview

> https://anthropic.skilljar.com/claude-with-google-vertex/289175

details

## Project overview

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

We're going to build a practical project that teaches Claude how to set reminders for future dates. This might sound simple at first, but it reveals several interesting challenges that we'll solve using custom tools.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619691%2F06_-_002_-_Project_Overview_00.1748619691746.png)

The goal is to have a conversation like this: you tell Claude "Set a reminder for my doctor's appointment. It's a week from Thursday," and Claude responds "OK, I will remind you." To make this work, we need to understand why this is actually harder than it looks.

## Why This Is Challenging

Claude has some built-in knowledge about dates and times, but it also has some significant limitations:

- Claude might know the current date, but not the exact time
- Claude doesn't always handle time-based addition well, especially if looking many days into the future
- Claude doesn't know how to set a reminder!

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619692%2F06_-_002_-_Project_Overview_08.1748619692245.png)

These limitations mean that even a simple request like "set a reminder for 24 hours from now" becomes problematic. Claude doesn't know what "24 hours from now" actually means without knowing the current time. And even if it could calculate the right date, it has no mechanism to actually create a reminder.

## Tools We Need

To solve these problems, we'll create three custom tools that work together:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619693%2F06_-_002_-_Project_Overview_17.1748619693561.png)

## Get the Current Date Time

This is our starting tool - it gives Claude access to both the current date and the exact time. This solves the problem of Claude not knowing when "now" actually is.

## Add Duration to Date Time

This tool handles the math of adding time periods to dates. Instead of relying on Claude to correctly calculate "what date is 379 days from January 13th, 1973," we give it a reliable tool that can handle these calculations accurately.

## Set a Reminder

Finally, we need a way for Claude to actually create reminders. This tool will provide the mechanism that Claude lacks for setting up future notifications.

We'll implement these tools one at a time, starting with the datetime tool to understand how tool calling works, then building up to the more complex functionality. By the end, Claude will be able to handle natural language requests about setting reminders and convert them into actual scheduled notifications.

---

## Tool functions

> https://anthropic.skilljar.com/claude-with-google-vertex/289176

details

1
                                    download

## Tool functions

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building AI applications with Claude, you'll often need to give it access to real-time information or the ability to perform actions. This is where tool functions come in - they're Python functions that Claude can call when it needs additional data to help users.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619700%2F06_-_003_-_Tool_Functions_00.1748619699839.png)

The image above shows three essential tools we'll be implementing: getting the current date/time, adding duration to dates, and setting reminders. Let's start with the first one.

## What Are Tool Functions?

A tool function is a plain Python function that gets executed automatically when Claude determines it needs extra information to complete a task. For example, if a user asks "What time is it?", Claude would call your date/time tool to get the current time.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619700%2F06_-_003_-_Tool_Functions_06.1748619700490.png)

Here's an example of a weather tool function. Notice how it validates inputs and provides clear error messages - these are key best practices we'll follow.

## Best Practices for Tool Functions

When writing tool functions, keep these guidelines in mind:

- Use descriptive names: Both your function name and parameter names should clearly indicate their purpose
- Validate inputs: Always check that required parameters are present and valid
- Provide meaningful error messages: If Claude gets an error, it might try calling your function again with corrected parameters
The error handling is particularly important because Claude can learn from failures. If you return a clear error message like "Location cannot be empty", Claude might retry the function call with a proper location value.

## Building Your First Tool Function

Let's create a function to get the current date and time. This function will accept a format string to control how the date appears:

```
def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)
```

```
def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    if not date_format:
        raise ValueError("date_format cannot be empty")
    return datetime.now().strftime(date_format)
```

The default format string "%Y-%m-%d %H:%M:%S" produces output like "2024-03-15 14:30:45". You can customize this by passing different format strings:

```
"%Y-%m-%d %H:%M:%S"
```

```
# Get just the time
get_current_datetime("%H:%M")  # Returns "14:30"

# Get a different date format  
get_current_datetime("%B %d, %Y")  # Returns "March 15, 2024"
```

```
# Get just the time
get_current_datetime("%H:%M")  # Returns "14:30"

# Get a different date format  
get_current_datetime("%B %d, %Y")  # Returns "March 15, 2024"
```

## Input Validation

The validation check if not date_format: ensures we don't try to format a date with an empty string. While Claude rarely makes this mistake, providing clear error messages helps the AI understand what went wrong and how to fix it.

```
if not date_format:
```

When Claude encounters an error, it sees the exact error message. This feedback loop allows Claude to adjust its approach and try again with corrected parameters.

## Next Steps

This tool function is just the first step. Next, you'll need to create a JSON schema that describes this function to Claude, then integrate it into your chat system. The function itself is straightforward Python - the complexity comes in properly connecting it to Claude's tool-calling system.

#### Downloads

- 001_tools.ipynb
                                                (opens in new tab)

---

## Tool schemas

> https://anthropic.skilljar.com/claude-with-google-vertex/289174

details

## Tool schemas

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

After writing your tool function, the next step is creating a JSON schema that tells Claude what arguments your function expects and how to use it. This schema acts as documentation that Claude reads to understand when and how to call your tools.

## Understanding JSON Schema

JSON Schema isn't specific to AI or tool calling - it's a widely-used data validation specification that's been around for years. The AI community adopted it because it's a convenient way to describe function parameters and validate data.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619697%2F06_-_004_-_Tool_Schemas_01.1748619697769.png)

The complete tool specification has three main parts:

- name - The function name (like "get_weather")
- description - What the tool does and when to use it
- input_schema - The actual JSON schema describing the arguments

## Writing Effective Descriptions

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619698%2F06_-_004_-_Tool_Schemas_02.1748619698251.png)

The description field is crucial for helping Claude understand your tool. Follow these best practices:

- Explain what the tool does, when to use it, and what it returns
- Aim for 3-4 sentences
- Provide detailed descriptions for each argument as well
The input_schema section describes your function's parameters using standard JSON Schema format, including type information and detailed descriptions for each argument.

## The Easy Way: Let Claude Write Your Schema

Instead of writing JSON schemas from scratch, you can use Claude itself to generate them. Here's the process:

- Copy your tool function
- Go to Claude and ask it to write a JSON schema for tool calling
- Include the Anthropic documentation on tool use as context
- Let Claude generate a properly formatted schema following best practices

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619699%2F06_-_004_-_Tool_Schemas_13.1748619699594.png)

The prompt should be something like: "Write a valid JSON schema spec for the purposes of tool calling for this function. Follow the best practices listed in the attached documentation."

## Implementing the Schema in Code

Once Claude generates your schema, copy it into your code file. Use a consistent naming pattern like function_name_schema to keep things organized:

```
function_name_schema
```

```
get_current_datetime_schema = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    "input_schema": {
        "type": "object",
        "properties": {
            "date_format": {
                "type": "string",
                "description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
                "default": "%Y-%m-%d %H:%M:%S"
            }
        },
        "required": []
    }
}
```

```
get_current_datetime_schema = {
    "name": "get_current_datetime",
    "description": "Returns the current date and time formatted according to the specified format",
    "input_schema": {
        "type": "object",
        "properties": {
            "date_format": {
                "type": "string",
                "description": "A string specifying the format of the returned datetime. Uses Python's strftime format codes.",
                "default": "%Y-%m-%d %H:%M:%S"
            }
        },
        "required": []
    }
}
```

## Adding Type Safety

For better type checking, import and use the ToolParam type from the Anthropic library:

```
ToolParam
```

```
from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
    # your schema dictionary here
})
```

```
from anthropic.types import ToolParam

get_current_datetime_schema = ToolParam({
    # your schema dictionary here
})
```

This isn't strictly necessary for functionality, but it prevents type errors when you use the schema later in your code.

The combination of a well-written tool function and a detailed JSON schema gives Claude everything it needs to understand and properly use your tools in conversations.

---

## Handling message blocks

> https://anthropic.skilljar.com/claude-with-google-vertex/289179

details

## Handling message blocks

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with Claude's tool functionality, you'll encounter a new type of response structure that's different from the simple text responses you've seen before. Instead of just getting back a single text block, Claude can now return multi-block messages that contain both text and tool usage information.

## Making Tool-Enabled API Calls

To enable Claude to use tools, you need to include a tools parameter in your API call. Here's how to structure the request:

```
tools
```

```
messages = []
messages.append({
    "role": "user",
    "content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    tools=[get_current_datetime_schema],
)
```

```
messages = []
messages.append({
    "role": "user",
    "content": "What is the exact time, formatted as HH:MM:SS?"
})

response = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    tools=[get_current_datetime_schema],
)
```

The tools parameter takes a list of JSON schemas that describe the available functions Claude can call.

```
tools
```

## Understanding Multi-Block Messages

When Claude decides to use a tool, it returns an assistant message with multiple blocks in the content list. This is a significant change from the simple text-only responses you've worked with before.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619699%2F06_-_005_-_Handling_Message_Blocks_08.1748619699629.png)

A multi-block message typically contains:

- Text Block - Human-readable text explaining what Claude is doing (like "I can help you find out the current time. Let me find that information for you")
- ToolUse Block - Instructions for your code about which tool to call and what parameters to use
The ToolUse block includes:

- An ID for tracking the tool call
- The name of the function to call (like "get_current_datetime")
- Input parameters formatted according to your JSON schema
- The type designation "tool_use"

## Handling Message History with Multi-Block Content

Here's the critical part: Claude doesn't store conversation history, so you must manage it manually. When working with tool responses, you need to preserve the entire content structure, including all blocks.

Instead of just extracting text, you need to append the complete response content:

```
messages.append({
    "role": "assistant",
    "content": response.content
})
```

```
messages.append({
    "role": "assistant",
    "content": response.content
})
```

This preserves both the text block and the tool use block, maintaining the full conversation context for future API calls.

## The Complete Flow

The tool usage process follows this pattern:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619700%2F06_-_005_-_Handling_Message_Blocks_15.1748619700334.png)

- Send user message with tool schema to Claude
- Receive multi-block assistant message (text + tool use)
- Extract tool call information and execute the function
- Send tool result back to Claude with complete message history
- Receive final response from Claude
Each step requires careful handling of the message structure to maintain conversation continuity. The key insight is that tool-enabled conversations involve more complex message formats, but the fundamental principle of maintaining complete message history remains the same.

## Updating Helper Functions

If you've been using helper functions like add_user_message and add_assistant_message, you'll need to update them to handle multi-block content. The current versions likely only support single text blocks, but now they need to accommodate the more complex content structures that include tool use blocks.

```
add_user_message
```

```
add_assistant_message
```

---

## Sending tool results

> https://anthropic.skilljar.com/claude-with-google-vertex/289184

details

## Sending tool results

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

After Claude requests a tool call, you need to execute the function and send the results back. This completes the tool use workflow by providing Claude with the information it requested.

## Running the Tool Function

When Claude responds with a tool use block, you extract the input parameters and call your function. Here's how to access the tool parameters:

```
// Access the tool use block
tool_use_block = response.content[1]

// Get the input parameters
input_params = tool_use_block.input

// Call your function with the parameters
result = get_current_datetime(**input_params)
```

```
// Access the tool use block
tool_use_block = response.content[1]

// Get the input parameters
input_params = tool_use_block.input

// Call your function with the parameters
result = get_current_datetime(**input_params)
```

The double asterisk (**) unpacks the dictionary into keyword arguments that your function expects.

```
**
```

## Tool Result Block

After running the tool, you send the results back to Claude using a tool result block. This block has several important properties:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619950%2F06_-_006_-_Sending_Tool_Results_05.1748619949924.png)

- tool_use_id - Must match the ID from the original tool use block
- content - The output from your tool function, converted to a string
- is_error - Set to true if an error occurred during execution

## Handling Multiple Tool Calls

Claude can request multiple tool calls in a single response. For example, if a user asks "What's 10 + 10 and what's 30 + 30?", Claude might send two separate tool use blocks:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619951%2F06_-_006_-_Sending_Tool_Results_07.1748619950833.png)

Each tool use block gets a unique ID, and you must match these IDs when sending back results:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619951%2F06_-_006_-_Sending_Tool_Results_08.1748619951478.png)

This ID system ensures Claude can correctly match each result with its corresponding request, even if the results arrive in a different order.

## Sending the Follow-up Request

Your follow-up request to Claude must include the complete conversation history plus the new tool result:

```
messages.append({
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": response.content[1].id,
        "content": result,
        "is_error": False
    }]
})
```

```
messages.append({
    "role": "user",
    "content": [{
        "type": "tool_result",
        "tool_use_id": response.content[1].id,
        "content": result,
        "is_error": False
    }]
})
```

The conversation flow looks like this:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619952%2F06_-_006_-_Sending_Tool_Results_04.1748619952295.png)

Remember to include the tool schema in your follow-up request, even though Claude probably won't need to call tools again. Claude needs the schema to understand the tool references in the conversation history.

## Complete Workflow

Here's the full process:

- User asks a question requiring tool use
- Claude responds with a tool use block
- You execute the requested tool function
- You send a follow-up request with the tool result
- Claude provides a final answer using the tool output
The final request includes your complete message history, the tool result block, and the tool schema. Claude then responds with a regular text message that incorporates the information from your tool execution.

---

## Multi-turn conversations with tools

> https://anthropic.skilljar.com/claude-with-google-vertex/289178

details

1
                                    download

## Multi-turn conversations with tools

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building applications with multiple tools, you need to handle scenarios where Claude might need to call several tools in sequence to answer a single user question. For example, if a user asks "What day is 103 days from today?", Claude needs to first get the current date, then add 103 days to it.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619954%2F06_-_007_-_Multi-Turn_Conversations_with_Tools_02.1748619954762.png)

This creates a multi-turn conversation pattern where Claude makes multiple tool requests before providing a final answer. Your application needs to handle this automatically.

## The Multi-Turn Tool Pattern

Here's what happens behind the scenes when Claude needs multiple tools:

- User asks: "What day is 103 days from today?"
- Claude responds with a tool use block requesting get_current_datetime

```
get_current_datetime
```

- Your server calls the function and returns the result
- Claude realizes it needs more information and requests add_duration_to_datetime

```
add_duration_to_datetime
```

- Your server calls that function and returns the result
- Claude now has enough information to provide the final answer

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619955%2F06_-_007_-_Multi-Turn_Conversations_with_Tools_03.1748619955529.png)

## Building a Conversation Loop

To handle this pattern, you need a conversation loop that continues until Claude stops requesting tools:

```
def run_conversation(messages):
    while True:
        response = chat(messages)

        add_assistant_message(messages, response)

        # Pseudo code
        if response isn't asking for a tool:
            break

        tool_result_blocks = run_tools(response)
        add_user_message(messages, tool_result_blocks)
        
    return messages
```

```
def run_conversation(messages):
    while True:
        response = chat(messages)

        add_assistant_message(messages, response)

        # Pseudo code
        if response isn't asking for a tool:
            break

        tool_result_blocks = run_tools(response)
        add_user_message(messages, tool_result_blocks)
        
    return messages
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619956%2F06_-_007_-_Multi-Turn_Conversations_with_Tools_05.1748619956267.png)

## Refactoring Helper Functions

Before implementing the conversation loop, you need to update your helper functions to handle multiple message blocks properly.

### Updating Message Handlers

Your add_user_message and add_assistant_message functions currently assume they're always working with plain text. Update them to handle full message objects:

```
add_user_message
```

```
add_assistant_message
```

```
from anthropic.types import Message

def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message
    }
    messages.append(user_message)
```

```
from anthropic.types import Message

def add_user_message(messages, message):
    user_message = {
        "role": "user",
        "content": message.content if isinstance(message, Message) else message
    }
    messages.append(user_message)
```

This allows you to pass in either a string, a list of blocks, or a complete message object.

### Updating the Chat Function

Modify your chat function to accept a list of tools and return the full message instead of just text:

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }
    
    if tools:
        params["tools"] = tools
        
    if system:
        params["system"] = system
        
    message = client.messages.create(**params)
    return message
```

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
        "stop_sequences": stop_sequences,
    }
    
    if tools:
        params["tools"] = tools
        
    if system:
        params["system"] = system
        
    message = client.messages.create(**params)
    return message
```

### Extracting Text from Messages

Since the chat function now returns full messages instead of just text, add a helper to extract text when needed:

```
def text_from_message(message):
    return "\n".join(
        [block.text for block in message.content if block.type == "text"]
    )
```

```
def text_from_message(message):
    return "\n".join(
        [block.text for block in message.content if block.type == "text"]
    )
```

This function finds all text blocks in a message and joins them together, which is useful when you need to display the final response to users.

## Why These Changes Matter

These refactoring steps prepare your code for the reality of tool-enabled conversations:

- Multiple blocks per message - Claude's responses can contain both text and tool use blocks
- Flexible message handling - Your functions can now work with various message formats
- Full message preservation - You maintain all the information Claude provides, not just the text portions
- Tool list support - Your chat function can now receive and use multiple tools
With these foundations in place, you're ready to implement the full conversation loop that handles multiple tool calls automatically, creating a seamless experience where Claude can use whatever tools it needs to answer user questions completely.

#### Downloads

- 001_tools_007.ipynb
                                                (opens in new tab)

---

## Implementing multiple turns

> https://anthropic.skilljar.com/claude-with-google-vertex/289182

details

1
                                    download

## Implementing multiple turns

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building a conversation system with tools requires implementing a loop that keeps calling Claude until it stops requesting tool usage. When Claude no longer asks for tools, that signals it has a final response ready for the user.

## Detecting Tool Requests

The key to knowing whether Claude wants to use a tool lies in the stop_reason field of the response message. When Claude decides it needs to call a tool, this field gets set to "tool_use". This gives us a clean way to check if we need to continue the conversation loop:

```
stop_reason
```

```
"tool_use"
```

```
if response.stop_reason != "tool_use":
    break  # Claude is done, no more tools needed
```

```
if response.stop_reason != "tool_use":
    break  # Claude is done, no more tools needed
```

## The Conversation Loop

The main conversation function follows a simple pattern:

```
def run_conversation(messages):
    while True:
        response = chat(messages, tools=[get_current_datetime_schema])
        add_assistant_message(messages, response)
        print(text_from_message(response))
        
        if response.stop_reason != "tool_use":
            break
            
        tool_results = run_tools(response)
        add_user_message(messages, tool_results)
    
    return messages
```

```
def run_conversation(messages):
    while True:
        response = chat(messages, tools=[get_current_datetime_schema])
        add_assistant_message(messages, response)
        print(text_from_message(response))
        
        if response.stop_reason != "tool_use":
            break
            
        tool_results = run_tools(response)
        add_user_message(messages, tool_results)
    
    return messages
```

This loop continues until Claude provides a final answer without requesting any tools.

## Handling Multiple Tool Calls

Claude can request multiple tools in a single response. The message content contains a list of blocks, and we need to process each tool use block separately:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619959%2F06_-_008_-_Implementing_Multiple_Turns_05.1748619959308.png)

The run_tools function handles this by filtering for tool use blocks and processing each one:

```
run_tools
```

```
def run_tools(message):
    tool_requests = [
        block for block in message.content if block.type == "tool_use"
    ]
    tool_result_blocks = []
    
    for tool_request in tool_requests:
        # Process each tool request...
```

```
def run_tools(message):
    tool_requests = [
        block for block in message.content if block.type == "tool_use"
    ]
    tool_result_blocks = []
    
    for tool_request in tool_requests:
        # Process each tool request...
```

## Tool Result Blocks

For each tool use block, we need to create a corresponding tool result block. These blocks have specific required fields:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619960%2F06_-_008_-_Implementing_Multiple_Turns_10.1748619960197.png)

The tool result block must include the same ID as the original tool use block, but in the tool_use_id field:

```
tool_use_id
```

```
tool_result_block = {
    "type": "tool_result",
    "tool_use_id": tool_request.id,
    "content": json.dumps(tool_output),
    "is_error": False
}
```

```
tool_result_block = {
    "type": "tool_result",
    "tool_use_id": tool_request.id,
    "content": json.dumps(tool_output),
    "is_error": False
}
```

## Error Handling

Robust tool execution requires handling potential errors. When a tool fails, we still need to return a tool result block, but with error information:

```
try:
    tool_output = run_tool(tool_request.name, tool_request.input)
    tool_result_block = {
        "type": "tool_result",
        "tool_use_id": tool_request.id,
        "content": json.dumps(tool_output),
        "is_error": False
    }
except Exception as e:
    tool_result_block = {
        "type": "tool_result", 
        "tool_use_id": tool_request.id,
        "content": f"Error: {e}",
        "is_error": True
    }
```

```
try:
    tool_output = run_tool(tool_request.name, tool_request.input)
    tool_result_block = {
        "type": "tool_result",
        "tool_use_id": tool_request.id,
        "content": json.dumps(tool_output),
        "is_error": False
    }
except Exception as e:
    tool_result_block = {
        "type": "tool_result", 
        "tool_use_id": tool_request.id,
        "content": f"Error: {e}",
        "is_error": True
    }
```

## Scalable Tool Routing

To support multiple tools, create a separate routing function instead of hardcoding tool names:

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "other_tool":
        return other_tool_function(**tool_input)
    # Add more tools as needed
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "other_tool":
        return other_tool_function(**tool_input)
    # Add more tools as needed
```

This approach makes it easy to add new tools without modifying the core conversation logic.

## Complete Workflow

The complete multi-turn conversation works like this:

- Send user message to Claude with available tools
- Claude responds with text and/or tool use blocks
- Execute any requested tools and create tool result blocks
- Send tool results back to Claude as a user message
- Repeat until Claude provides a final response without tool requests
This creates a seamless experience where Claude can make multiple tool calls across several conversation turns to gather all the information needed before providing a comprehensive final answer to the user.

#### Downloads

- 001_tools_008.ipynb
                                                (opens in new tab)

---

## Using multiple tools

> https://anthropic.skilljar.com/claude-with-google-vertex/289185

details

1
                                    download

## Using multiple tools

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Adding multiple tools to your Claude implementation becomes straightforward once you have the core tool-handling infrastructure in place. This tutorial shows how to integrate additional tools by following a simple pattern.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619943%2F06_-_009_-_Using_Multiple_Tools_00.1748619943580.png)

## The Tools We're Adding

We need three main capabilities for our reminder system:

- Get current date time - Claude needs to know the current date and time
- Add duration to date time - Claude isn't perfect with date time addition
- Set a reminder - Need a way to set a reminder
The good news is that most of the implementation work is already done. The add_duration_to_datetime function handles various time units (seconds, minutes, hours, days, weeks, months) and returns properly formatted datetime strings.

```
add_duration_to_datetime
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619944%2F06_-_009_-_Using_Multiple_Tools_03.1748619944451.png)

The set_reminder function is a simple placeholder that prints out confirmation details rather than actually setting system reminders.

```
set_reminder
```

## Adding Tools to the Conversation

The process follows the same pattern we established earlier. First, update the run_conversation function to include the new tool schemas:

```
run_conversation
```

```
response = chat(messages, tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
])
```

```
response = chat(messages, tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
])
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619945%2F06_-_009_-_Using_Multiple_Tools_07.1748619945276.png)

This tells Claude about all available tools it can use during the conversation.

## Handling Tool Execution

Next, update the run_tool function to handle the new tool calls:

```
run_tool
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619946%2F06_-_009_-_Using_Multiple_Tools_10.1748619945988.png)

The pattern is consistent: check the tool name, call the corresponding function with the provided input, and return the result.

## Testing Multiple Tool Usage

Let's test with a complex request that requires multiple tools: "Set a reminder for my doctors appointment. Its 177 days after Jan 1st, 2050."

This request forces Claude to:

- Calculate the date 177 days after January 1st, 2050
- Set a reminder for that calculated date

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619946%2F06_-_009_-_Using_Multiple_Tools_15.1748619946641.png)

Claude handles this by first explaining what it needs to do, then using the add_duration_to_datetime tool to calculate June 27, 2050, and finally calling set_reminder with the correct date.

```
add_duration_to_datetime
```

```
set_reminder
```

## Understanding the Message Flow

Looking at the conversation history reveals how Claude manages multiple tools in a single response. The assistant message contains both a text block explaining the process and a tool use block for the first calculation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748619947%2F06_-_009_-_Using_Multiple_Tools_17.1748619947288.png)

After receiving the tool result, Claude continues with another message containing both text and another tool use block for setting the reminder. This demonstrates how Claude can chain multiple tool calls together to complete complex tasks.

## Key Takeaways

Once you have the basic tool infrastructure set up, adding new tools follows a simple three-step process:

- Add the tool schema to the tools list in run_conversation

```
run_conversation
```

- Add a case for the new tool in the run_tool function

```
run_tool
```

- Implement the actual tool function
The framework handles all the message passing, tool result formatting, and conversation flow automatically. This makes it easy to build sophisticated AI assistants that can perform multiple related tasks in sequence.

#### Downloads

- 001_tools_009.ipynb
                                                (opens in new tab)

---

## The batch tool

> https://anthropic.skilljar.com/claude-with-google-vertex/289189

details

## The batch tool

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with Claude's tool calling capabilities, you might notice that Claude can include multiple tool use blocks in a single assistant message. This allows Claude to run several tools in parallel rather than making separate requests for each one. However, getting Claude to actually do this consistently can be challenging in practice.

## The Problem with Multiple Tool Calls

Let's say you ask Claude to set two reminders for the same date. Theoretically, Claude should be able to send back a single response containing two tool use blocks - one for each reminder. But in reality, Claude often sends separate responses instead.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620029%2F06_-_010_-_The_Batch_Tool_04.1748620029736.png)

What typically happens is Claude makes the first tool call, waits for the result, then makes the second tool call in a follow-up message. This creates unnecessary back-and-forth communication when the operations could have been done simultaneously.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620031%2F06_-_010_-_The_Batch_Tool_05.1748620030815.png)

## The Batch Tool Solution

The solution is to implement a "batch tool" - a special tool that accepts a list of other tool calls to execute simultaneously. This is essentially a workaround that tricks Claude into making multiple tool calls at once.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620031%2F06_-_010_-_The_Batch_Tool_06.1748620031536.png)

Here's how it works:

- You define a batch tool schema that tells Claude it can run multiple other tools in parallel
- Instead of calling tools directly, Claude calls the batch tool with a list of tool invocations
- Your code processes this list and executes each tool call
- You return the combined results back to Claude

## Implementing the Batch Tool Schema

The batch tool schema defines how Claude should structure its requests when it wants to run multiple tools:

```
batch_tool_schema = {
    "name": "batch_tool",
    "description": "Invoke multiple other tool calls simultaneously",
    "input_schema": {
        "type": "object",
        "properties": {
            "invocations": {
                "type": "array",
                "description": "The tool calls to invoke",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the tool to invoke"
                        },
                        "arguments": {
                            "type": "object",
                            "description": "The arguments to pass to the tool"
                        }
                    }
                }
            }
        }
    }
}
```

```
batch_tool_schema = {
    "name": "batch_tool",
    "description": "Invoke multiple other tool calls simultaneously",
    "input_schema": {
        "type": "object",
        "properties": {
            "invocations": {
                "type": "array",
                "description": "The tool calls to invoke",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The name of the tool to invoke"
                        },
                        "arguments": {
                            "type": "object",
                            "description": "The arguments to pass to the tool"
                        }
                    }
                }
            }
        }
    }
}
```

## Processing Batch Tool Calls

When Claude uses the batch tool, you need to process the list of invocations and execute each one. Here's the implementation:

```
def run_batch(invocations=[]):
    batch_output = []
    
    for invocation in invocations:
        name = invocation["name"]
        args = json.loads(invocation["arguments"])
        
        tool_output = run_tool(name, args)
        
        batch_output.append({
            "tool_name": name,
            "output": tool_output
        })
    
    return batch_output
```

```
def run_batch(invocations=[]):
    batch_output = []
    
    for invocation in invocations:
        name = invocation["name"]
        args = json.loads(invocation["arguments"])
        
        tool_output = run_tool(name, args)
        
        batch_output.append({
            "tool_name": name,
            "output": tool_output
        })
    
    return batch_output
```

You'll also need to update your main tool routing function to handle batch tool calls:

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
    elif tool_name == "batch_tool":
        return run_batch(**tool_input)
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
    elif tool_name == "batch_tool":
        return run_batch(**tool_input)
```

## Results

With the batch tool implemented, Claude is much more likely to group related operations together. Instead of making separate requests for each reminder, Claude will use the batch tool to set both reminders simultaneously.

The conversation flow becomes much cleaner - one request from the user, one response from Claude with the batch tool call, and one follow-up with all the results. This reduces latency and makes your application more efficient.

While it might seem like a workaround (and it is), the batch tool pattern is an effective way to encourage Claude to think about operations that can be parallelized and execute them more efficiently.

---

## Tools for structured data

> https://anthropic.skilljar.com/claude-with-google-vertex/289181

details

2
                                    download

## Tools for structured data

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you need structured data from Claude, you have two main approaches: prompt-based techniques using message prefills and stop sequences, or a more robust method using tools. While the prompt-based approach is simpler to set up, tools provide more reliable output at the cost of additional complexity.

## Tools for Structured Data

The tool-based approach works by creating a JSON schema that defines the exact structure of data you want to extract. Instead of hoping Claude formats its response correctly, you're essentially giving Claude a function to call with specific parameters that match your desired output structure.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620028%2F06_-_011_-_Tools_for_Structured_Data_03.1748620028103.png)

Here's how the process works:

- Write a schema that describes the structure of data you're looking for
- Force Claude to use a tool with the tool_choice parameter

```
tool_choice
```

- Extract the structured data from the tool use response
- No need to provide a follow-up response - you're done once you get the data
For example, if you want to extract a financial balance and key insights from a statement, your schema would define those as an integer and array of strings respectively.

## Controlling Tool Use

A critical part of this technique is ensuring Claude actually calls your tool. You can control this behavior using the tool_choice parameter:

```
tool_choice
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620029%2F06_-_011_-_Tools_for_Structured_Data_09.1748620028978.png)

- {"type": "auto"} - Model decides if it needs to use a tool (default)

```
{"type": "auto"}
```

- {"type": "any"} - Model must use a tool, but can choose which one

```
{"type": "any"}
```

- {"type": "tool", "name": "TOOL_NAME"} - Model must use the specified tool

```
{"type": "tool", "name": "TOOL_NAME"}
```

For structured data extraction, you'll typically want the third option to guarantee Claude calls your specific schema tool.

## Implementation Example

Let's say you want to extract a title, author, and key insights from an article. First, you'd create a tool schema:

```
article_summary_schema = {
    "name": "article_summary",
    "description": "Extracts structured data from articles",
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "key_insights": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
    }
}
```

```
article_summary_schema = {
    "name": "article_summary",
    "description": "Extracts structured data from articles",
    "input_schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "key_insights": {
                "type": "array",
                "items": {"type": "string"}
            }
        }
    }
}
```

Then you'd call Claude with the tool and force its use:

```
response = chat(
    messages,
    tools=[article_summary_schema],
    tool_choice={"type": "tool", "name": "article_summary"}
)
```

```
response = chat(
    messages,
    tools=[article_summary_schema],
    tool_choice={"type": "tool", "name": "article_summary"}
)
```

The response will contain a tool use block with your structured data in the input field. You can access it directly:

```
input
```

```
structured_data = response.content[0].input
```

```
structured_data = response.content[0].input
```

## When to Use Each Approach

Choose prompt-based structured output when you need something quick and simple. Use tools when you need guaranteed reliability and can handle the extra setup complexity. Both techniques are valuable depending on your specific use case and requirements.

#### Downloads

- 002_structured_data_completed.ipynb
                                                (opens in new tab)
- 002_structured_data.ipynb
                                                (opens in new tab)

---

## The text edit tool

> https://anthropic.skilljar.com/claude-with-google-vertex/289180

details

1
                                    download

## The text edit tool

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Important Note: Tool version strings can for all model versions can be found here: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/text-editor-tool

Claude comes with one built-in tool that you don't need to create from scratch: the text editor tool. This tool gives Claude the ability to work with files and directories just like you would in a standard text editor.

## What the Text Editor Tool Can Do

The text editor tool provides Claude with a comprehensive set of file manipulation capabilities:

- View file or directory contents
- View specific ranges of lines in a file
- Replace text in a file
- Create new files
- Insert text at specific lines in a file
- Undo recent edits to files

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620032%2F06_-_012_-_The_Text_Edit_Tool_00.1748620032281.png)

This dramatically expands Claude's abilities and essentially gives it the power to act as a software engineer right out of the gate.

## Understanding the Implementation Requirements

Here's where things get a bit confusing: while the tool schema is built into Claude, you still need to provide the actual implementation. Think of it this way - Claude knows how to ask for file operations, but you need to write the code that actually performs those operations.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620033%2F06_-_012_-_The_Text_Edit_Tool_04.1748620032972.png)

When you use custom tools, you typically write both the JSON schema and the function implementation. With the text editor tool, Claude provides the schema knowledge, but you must write functions to handle Claude's requests to create files, read directories, replace text, and so on.

## Schema Versions

You do need to include a small schema stub when using the text editor tool, and the exact schema depends on which Claude model you're using:

```
def get_text_edit_schema(model):
    if model.startswith("claude-3-7-sonnet"):
        return {
            "type": "text_editor_20250124",
            "name": "str_replace_editor",
        }
    elif model.startswith("claude-3-5-sonnet"):
        return {
            "type": "text_editor_20241022", 
            "name": "str_replace_editor",
        }
```

```
def get_text_edit_schema(model):
    if model.startswith("claude-3-7-sonnet"):
        return {
            "type": "text_editor_20250124",
            "name": "str_replace_editor",
        }
    elif model.startswith("claude-3-5-sonnet"):
        return {
            "type": "text_editor_20241022", 
            "name": "str_replace_editor",
        }
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620033%2F06_-_012_-_The_Text_Edit_Tool_11.1748620033628.png)

Claude automatically expands this small schema into a much larger, detailed specification that includes all the parameters and operations available.

## Practical Example

Let's see the text editor tool in action. When you ask Claude to work with files, it will use the tool to read, modify, and create files as needed.

For example, if you ask Claude to "Open the ./main.py file and summarize its contents", Claude will:

- Use the text editor tool to view the file
- Read the contents
- Provide you with a summary
You can take this further and ask Claude to modify files. For instance: "Open the ./main.py file and write out a function to calculate pi to the 5th digit. Then create a ./test.py file to test your implementation."

Claude will:

- View the existing main.py file
- Replace its contents with a new implementation including the pi calculation function
- Create a new test.py file with appropriate unit tests

## Why Use the Text Editor Tool?

You might wonder why this tool exists when modern code editors already have AI assistants built in. The text editor tool becomes valuable in scenarios where:

- You're building applications that need to programmatically edit files
- You're working in environments without access to full-featured code editors
- You want to integrate file editing capabilities directly into your Claude-powered applications
Essentially, the text editor tool lets you replicate much of the functionality of a fancy AI-powered code editor within your own applications, giving Claude the ability to be a true coding assistant that can read, write, and modify files on your file system.

#### Downloads

- 005_text_editor_tool.ipynb
                                                (opens in new tab)

---

## The web search tool

> https://anthropic.skilljar.com/claude-with-google-vertex/289183

details

2
                                    download

## The web search tool

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude includes a built-in web search tool that lets it search the internet for current or specialized information to answer user questions. Unlike other tools where you need to provide the implementation, Claude handles the entire search process automatically - you just need to provide a simple schema to enable it.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620026%2F06_-_013_-_The_Web_Search_Tool_00.1748620026281.png)

## Setting Up the Web Search Tool

To use the web search tool, you create a schema object with these required fields:

```
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search", 
    "max_uses": 5
}
```

```
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search", 
    "max_uses": 5
}
```

The max_uses field limits how many searches Claude can perform. Claude might do follow-up searches based on initial results, so this prevents excessive API calls.

```
max_uses
```

## How It Works

When you include the web search schema in your tools list, Claude will automatically decide when to search based on your question. For example, asking "What's the best exercise for gaining leg muscle?" might trigger a search for current fitness research.

The response contains several types of blocks:

- TextBlock - Claude's explanation of what it's doing
- ServerToolUseBlock - Shows the exact search query Claude used
- WebSearchToolResultBlock - Contains the search results
- WebSearchResultBlock - Individual search results with titles and URLs
- CitationsWebSearchResultLocation - Specific text citations supporting Claude's statements

## Restricting Search Domains

You can limit searches to specific domains using the allowed_domains field. This is particularly useful when you want authoritative sources:

```
allowed_domains
```

```
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5,
    "allowed_domains": ["nih.gov"]
}
```

```
web_search_schema = {
    "type": "web_search_20250305",
    "name": "web_search",
    "max_uses": 5,
    "allowed_domains": ["nih.gov"]
}
```

This ensures Claude only searches trusted domains like government health sites instead of random fitness blogs with potentially unreliable information.

## Rendering Search Results

The response structure is designed for rich UI rendering. You typically:

- Display text blocks as regular content
- Show web search results as a reference list at the top
- Render citations inline with links back to source material
- Highlight cited text to show how Claude supports its statements
This creates a transparent experience where users can verify Claude's sources and understand how it arrived at its conclusions. The citation system helps build trust by showing the evidence behind Claude's responses.

#### Downloads

- 006_web_search_complete.ipynb
                                                (opens in new tab)
- 006_web_search.ipynb
                                                (opens in new tab)

---

## Quiz on tool use with Claude

> https://anthropic.skilljar.com/claude-with-google-vertex/289280

## Quiz on tool use with Claude

# Quiz on Tool Use with Claude

---

## Introducing Retrieval Augmented Generation

> https://anthropic.skilljar.com/claude-with-google-vertex/289191

details

## Introducing Retrieval Augmented Generation

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Retrieval Augmented Generation (RAG) is a technique that helps you work with large documents when using Claude. Instead of cramming an entire 800-page financial report into a single prompt, RAG lets you intelligently find and include only the most relevant sections for each question.

## The Problem with Large Documents

Imagine you have a massive financial document and want to ask Claude specific questions about it, like "What risk factors does this company have?" You face a fundamental challenge: how do you get the right information from the document into Claude so it can answer your question effectively?

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620800%2F07_-_001_-_Introducing_Retrieval_Augmented_Generation_01.1748620800500.png)

## Option 1: Include Everything in the Prompt

The first approach seems straightforward - extract all the text from the document and stuff it directly into your prompt along with the user's question.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620801%2F07_-_001_-_Introducing_Retrieval_Augmented_Generation_04.1748620801389.png)

This approach has several problems:

- There's a hard limit on how much text Claude can process - your document might be too long
- Claude becomes less effective with very long prompts
- Larger prompts cost more money and take longer to process

## Option 2: Break Documents into Chunks

The second approach is more sophisticated. You break the document into smaller chunks during a preprocessing step, then find and include only the chunks relevant to each user question.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620802%2F07_-_001_-_Introducing_Retrieval_Augmented_Generation_08.1748620802112.png)

Here's how it works: when a user asks "What risks does this company face?", you search through your chunks to find the one about "Risk Factors" and include only that section in your prompt to Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620802%2F07_-_001_-_Introducing_Retrieval_Augmented_Generation_09.1748620802784.png)

## Benefits of the Chunking Approach

- Claude can focus on only the most relevant content
- Scales up to very large documents
- Works with multiple documents
- Smaller prompts cost less and run faster

## Challenges with Chunking

- Requires a preprocessing step to split documents
- Need a searching mechanism to find "relevant" chunks
- Included chunks might not contain all the context Claude needs
- Many ways to chunk text - which approach is best?
For example, if you only include the "Risk Factors" section, you might miss important context from the "Strategy Outlook" section that addresses how the company plans to handle those risks.

## This is RAG

Option 2 is Retrieval Augmented Generation. Despite its complexity, RAG offers significant advantages for working with large documents, but it comes with technical challenges that require careful consideration.

The key components of RAG are:

- Document preprocessing and chunking
- A search mechanism to find relevant chunks
- Intelligent selection of which chunks to include in prompts
When considering RAG for your application, you need to evaluate whether the benefits outweigh the additional complexity for your specific use case. The technique shines when working with large document collections where you need precise, contextual answers, but it requires more upfront engineering work than simply including entire documents in prompts.

---

## Text chunking strategies

> https://anthropic.skilljar.com/claude-with-google-vertex/289208

details

2
                                    download

## Text chunking strategies

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Text chunking is one of the most critical steps in building a RAG (Retrieval Augmented Generation) pipeline. How you break up your documents directly impacts the quality of your entire system. A poor chunking strategy can lead to irrelevant context being inserted into your prompts, causing your AI to give completely wrong answers.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620820%2F07_-_002_-_Text_Chunking_Strategies_01.1748620819902.png)

Consider this example: you have a document with sections on medical research and software engineering. If you chunk poorly, a user asking "How many bugs did engineers fix this year?" might get information about medical research instead of software engineering, simply because the medical section happened to contain the word "bug" in a different context.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620820%2F07_-_002_-_Text_Chunking_Strategies_03.1748620820757.png)

This demonstrates why chunking strategy matters so much. The goal is to create chunks that maintain semantic coherence and provide meaningful context when retrieved.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620821%2F07_-_002_-_Text_Chunking_Strategies_04.1748620821630.png)

## Three Main Chunking Strategies

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620822%2F07_-_002_-_Text_Chunking_Strategies_05.1748620822407.png)

There are three primary approaches to chunking text, each with distinct advantages and trade-offs:

- Size-based: Divide text into strings of equal length
- Structure-based: Split based on document structure (headers, paragraphs, sections)
- Semantic-based: Group related sentences or sections using NLP techniques

## Size-Based Chunking

Size-based chunking is the most straightforward approach. You simply divide your document into chunks of approximately equal character or word count. It's easy to implement and works reliably across different document types.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620823%2F07_-_002_-_Text_Chunking_Strategies_06.1748620823143.png)

However, this approach has clear downsides. Words get cut off mid-sentence, and chunks lose important context. For example, a chunk might not include the section header that would explain what the content is actually about.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620824%2F07_-_002_-_Text_Chunking_Strategies_07.1748620823862.png)

The solution is to add overlap between chunks. Each chunk includes some characters from neighboring chunks, ensuring better context preservation and avoiding abrupt cutoffs.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620824%2F07_-_002_-_Text_Chunking_Strategies_08.1748620824409.png)

Here's a basic implementation of character-based chunking with overlap:

```
def chunk_by_char(text, chunk_size=150, chunk_overlap=20):
    chunks = []
    start_idx = 0
    
    while start_idx < len(text):
        end_idx = min(start_idx + chunk_size, len(text))
        chunk_text = text[start_idx:end_idx]
        chunks.append(chunk_text)
        
        start_idx = (
            end_idx - chunk_overlap if end_idx < len(text) else len(text)
        )
    
    return chunks
```

```
def chunk_by_char(text, chunk_size=150, chunk_overlap=20):
    chunks = []
    start_idx = 0
    
    while start_idx < len(text):
        end_idx = min(start_idx + chunk_size, len(text))
        chunk_text = text[start_idx:end_idx]
        chunks.append(chunk_text)
        
        start_idx = (
            end_idx - chunk_overlap if end_idx < len(text) else len(text)
        )
    
    return chunks
```

## Structure-Based Chunking

Structure-based chunking leverages the natural organization of your documents. If you're working with markdown files, you can split on headers. For other formats, you might split on paragraphs or other structural elements.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620825%2F07_-_002_-_Text_Chunking_Strategies_09.1748620825351.png)

This approach works beautifully when you have guarantees about document structure. For markdown documents, you can split on section headers:

```
def chunk_by_section(document_text):
    pattern = r'\n## '
    return re.split(pattern, document_text)
```

```
def chunk_by_section(document_text):
    pattern = r'\n## '
    return re.split(pattern, document_text)
```

The major limitation is that many documents don't have consistent structure. Plain text files, PDFs, or user-uploaded documents might not have clear structural markers to split on.

## Semantic-Based Chunking

Semantic-based chunking is the most sophisticated approach. It analyzes the meaning and relationships between sentences to group related content together. This typically involves:

- Breaking text into sentences
- Using NLP techniques to measure semantic similarity
- Grouping related sentences into coherent chunks
While this can produce the highest quality chunks, it's computationally expensive and more complex to implement. For most applications, the simpler approaches work well enough.

## Practical Implementation

Here's a sentence-based chunking function that offers a good middle ground:

```
def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    start_idx = 0
    
    while start_idx < len(sentences):
        end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
        current_chunk = sentences[start_idx:end_idx]
        chunks.append(' '.join(current_chunk))
        
        start_idx += max_sentences_per_chunk - overlap_sentences
        
        if start_idx < 0:
            start_idx = 0
    
    return chunks
```

```
def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    start_idx = 0
    
    while start_idx < len(sentences):
        end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
        current_chunk = sentences[start_idx:end_idx]
        chunks.append(' '.join(current_chunk))
        
        start_idx += max_sentences_per_chunk - overlap_sentences
        
        if start_idx < 0:
            start_idx = 0
    
    return chunks
```

## Choosing the Right Strategy

Your choice of chunking strategy depends entirely on your specific use case:

- Consistent document structure: Use structure-based chunking for the cleanest results
- Mixed document types: Sentence-based chunking often works well
- Code or technical content: Character-based chunking is most reliable
- Unknown document formats: Character-based chunking is your safest bet
Remember that chunking is often an iterative process. Start with a simple approach, test it with your specific documents and use cases, then refine based on the results. The "best" chunking strategy is the one that works reliably for your particular data and requirements.

#### Downloads

- 001_chunking.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Text embeddings

> https://anthropic.skilljar.com/claude-with-google-vertex/289188

details

1
                                    download

## Text embeddings

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

After extracting text chunks from a document, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is essentially a search problem - you need to look through all your chunks and identify the ones that relate to what the user is asking about.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620795%2F07_-_003_-_Text_Embeddings_00.1748620795671.png)

## Semantic Search

The most common approach for finding relevant chunks is semantic search. Unlike traditional keyword-based search, semantic search uses text embeddings to understand the actual meaning of both the user's question and each text chunk. This allows the system to find conceptually related content even when the exact words don't match.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620796%2F07_-_003_-_Text_Embeddings_04.1748620796821.png)

## What Are Text Embeddings?

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620797%2F07_-_003_-_Text_Embeddings_06.1748620797380.png)

Here's how the process works:

- You feed text into an embedding model
- The model outputs a long list of numbers (the embedding)
- Each number ranges from -1 to +1
- These numbers represent different qualities or features of the input text

## Understanding the Numbers

Each number in an embedding is essentially a "score" for some quality of the input text. However, here's the important caveat: we don't actually know what each specific number represents.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620798%2F07_-_003_-_Text_Embeddings_08.1748620798019.png)

While it's helpful to imagine that one number might represent "how happy the text is" and another might represent "how much the text talks about oceans," these are just conceptual examples. The embedding model learns these features during training, but they're not explicitly labeled or interpretable to us.

Despite this opacity, embeddings are incredibly powerful because they capture semantic meaning in a way that allows for mathematical comparison between different pieces of text.

## Embeddings on Vertex AI

Claude can't generate embeddings directly. Instead, you need to use a specialized embedding model. On Vertex AI, the model we'll use is called text-embedding-005.

```
text-embedding-005
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620799%2F07_-_003_-_Text_Embeddings_13.1748620799354.png)

## Implementation

To work with embeddings on Vertex AI, you'll need to install the Google GenAI SDK:

```
pip install google-genai
```

```
pip install google-genai
```

Here's the basic setup for generating embeddings:

```
from google import genai

client = genai.Client(
    project="YOUR_PROJECT_ID", 
    location="global", 
    vertexai=True
)

def generate_embedding(text):
    response = client.models.embed_content(
        model="text-embedding-005", 
        contents=text
    )
    
    if not response.embeddings:
        return []
    
    return [e.values for e in response.embeddings]
```

```
from google import genai

client = genai.Client(
    project="YOUR_PROJECT_ID", 
    location="global", 
    vertexai=True
)

def generate_embedding(text):
    response = client.models.embed_content(
        model="text-embedding-005", 
        contents=text
    )
    
    if not response.embeddings:
        return []
    
    return [e.values for e in response.embeddings]
```

When you run this function with a text chunk, you'll get back a list of floating-point numbers representing the semantic meaning of that text. These embeddings form the foundation for implementing semantic search in your RAG system.

The next step is understanding how to use these embeddings to actually find the most relevant chunks for a user's question, which involves comparing embeddings mathematically to determine similarity.

#### Downloads

- 002_embeddings.ipynb
                                                (opens in new tab)

---

## The full RAG flow

> https://anthropic.skilljar.com/claude-with-google-vertex/289190

details

## The full RAG flow

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we've covered the basics of RAG, text chunking, and embeddings, let's walk through the complete RAG pipeline step by step. This detailed example will show you exactly how all the pieces fit together in a real implementation.

## Step 1: Chunk Your Source Text

First, we take our source document and break it into manageable chunks. For this example, we'll use two simple text sections:

- Section 1: Medical Research - "This year saw significant strides in our understanding of XDR-47, a 'bug' we have not seen before."
- Section 2: Software Engineering - "This division dedicated significant effort to studying various infection vectors in our distributed systems"

## Step 2: Generate Embeddings

Next, we convert each text chunk into numerical embeddings. To make this easier to understand, let's imagine we have a perfect embedding model that always returns exactly two numbers, and we know what each number represents:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620811%2F07_-_004_-_The_Full_RAG_Flow_02.1748620811676.png)

In our imaginary model:

- First number: How much the text talks about medicine
- Second number: How much the text talks about software engineering
So our medical research section gets [0.97, 0.34] - very medical, somewhat software-related due to the word "bug". The software engineering section gets [0.30, 0.97] - very software-focused, but "infection vectors" has medical connotations.

```
[0.97, 0.34]
```

```
[0.30, 0.97]
```

## Normalization

Before storing these embeddings, they go through a normalization process that scales each vector to have a magnitude of 1.0. This is typically handled automatically by your embedding API, but it's important to understand it happens.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620812%2F07_-_004_-_The_Full_RAG_Flow_07.1748620812576.png)

After normalization, our embeddings become [0.944, 0.331] and [0.295, 0.955]. We can visualize these on a unit circle where both points lie exactly on the circle's edge.

```
[0.944, 0.331]
```

```
[0.295, 0.955]
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620813%2F07_-_004_-_The_Full_RAG_Flow_08.1748620813144.png)

## Step 3: Store in Vector Database

The normalized embeddings get stored in a vector database - a specialized database optimized for storing, comparing, and searching through long lists of numbers like our embeddings.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620814%2F07_-_004_-_The_Full_RAG_Flow_09.1748620813871.png)

At this point, we pause. All the work so far has been preprocessing that happens ahead of time. Now we wait for a user to submit a query.

## Step 4: Process User Query

When a user asks a question like "I'm curious about the company. In particular, what did the software engineering dept do this year?", we run their query through the same embedding model.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620814%2F07_-_004_-_The_Full_RAG_Flow_10.1748620814524.png)

This query gets embedded as [0.1, 0.89] - low medical score, high software engineering score. After normalization, it becomes [0.112, 0.993].

```
[0.1, 0.89]
```

```
[0.112, 0.993]
```

## Step 5: Find Similar Embeddings

Now we ask the vector database: "Find the stored embedding that's closest to this user query embedding." The database returns the software engineering section because it's the most similar.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620816%2F07_-_004_-_The_Full_RAG_Flow_12.1748620815972.png)

But how does the database determine "closest"? It uses cosine similarity.

## Cosine Similarity

The vector database calculates the cosine of the angle between vectors to measure similarity. This gives us a number between -1 and 1:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620816%2F07_-_004_-_The_Full_RAG_Flow_15.1748620816527.png)

- 1.0 = vectors point in exactly the same direction (very similar)
- 0.0 = vectors are perpendicular (unrelated)
- -1.0 = vectors point in opposite directions (very different)
In our example:

- User query vs Software Engineering: cosine similarity = 0.983 (very similar!)
- User query vs Medical Research: cosine similarity = 0.398 (less similar)

## Cosine Distance

You'll often see "cosine distance" in vector database documentation. This is simply 1 - cosine similarity, which flips the scale so that smaller numbers mean more similar:

```
1 - cosine similarity
```

- 0.0 = very similar
- 1.0 = perpendicular
- 2.0 = completely opposite

## Step 6: Build the Final Prompt

Finally, we take the user's question and the most relevant text chunk (software engineering section) and combine them into a prompt for Claude:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620817%2F07_-_004_-_The_Full_RAG_Flow_19.1748620817301.png)

```
Answer the user's question about the financial document.

<user_question>
How many bugs did engineers fix this year?
</user_question>

<report>
## Section 2: Software Engineering
This division dedicated significant effort to studying various infection vectors in our distributed systems
</report>
```

```
Answer the user's question about the financial document.

<user_question>
How many bugs did engineers fix this year?
</user_question>

<report>
## Section 2: Software Engineering
This division dedicated significant effort to studying various infection vectors in our distributed systems
</report>
```

And that's the complete RAG pipeline! The system successfully found the most relevant context for the user's software engineering question and provided it to Claude for generating an informed response.

This process happens automatically every time a user submits a query, allowing Claude to answer questions based on your specific documents rather than just its general training knowledge.

---

## Implementing the RAG flow

> https://anthropic.skilljar.com/claude-with-google-vertex/289186

details

2
                                    download

## Implementing the RAG flow

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we understand the RAG flow conceptually, let's implement it step by step using a practical example. We'll work through all five stages of the RAG process, from chunking text to finding relevant documents for user queries.

## Setting Up the Vector Database

For this implementation, we'll use a custom VectorIndex class that provides the basic functionality we need for storing and searching embeddings. The class handles vector storage, distance calculations (using cosine similarity), and document retrieval.

## The Five-Step RAG Implementation

Let's walk through each step of the RAG process:

### Step 1: Chunk the Text by Section

First, we need to break our source document into manageable chunks. We'll use the same section-based chunking approach from earlier:

```
chunks = chunk_by_section(text)
```

```
chunks = chunk_by_section(text)
```

This splits our report.md file into logical sections that we can process individually.

### Step 2: Generate Embeddings for Each Chunk

Next, we convert each text chunk into a numerical embedding that captures its semantic meaning:

```
embeddings = generate_embedding(chunks)
```

```
embeddings = generate_embedding(chunks)
```

These embeddings allow us to perform mathematical comparisons between different pieces of text.

### Step 3: Store Embeddings in the Vector Database

Now we create our vector store and populate it with our embeddings and their associated text:

```
store = VectorIndex()

for embedding, chunk in zip(embeddings, chunks):
    store.add_vector(embedding, {"content": chunk})
```

```
store = VectorIndex()

for embedding, chunk in zip(embeddings, chunks):
    store.add_vector(embedding, {"content": chunk})
```

Notice that we store both the embedding and the original text content. This is crucial because when we retrieve similar embeddings later, we need access to the actual text, not just the numerical vectors. The embedding alone isn't useful to us as developers - we need the human-readable content it represents.

### Step 4: Generate an Embedding for the User Query

When a user asks a question, we need to convert their query into the same embedding space as our stored documents:

```
user_embedding = generate_embedding("What did the software engineering dept do last year?")
```

```
user_embedding = generate_embedding("What did the software engineering dept do last year?")
```

### Step 5: Search for Relevant Documents

Finally, we search our vector store to find the most relevant chunks:

```
results = store.search(user_embedding, 2)

for doc, distance in results:
    print(distance, "\n", doc["content"][0:200], "\n")
```

```
results = store.search(user_embedding, 2)

for doc, distance in results:
    print(distance, "\n", doc["content"][0:200], "\n")
```

This returns the two most similar chunks along with their cosine distance scores.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620875%2F07_-_005_-_Implementing_the_Rag_Flow_10.1748620875517.png)

The diagram above illustrates how the vector database processes a user query. When we ask a question, it gets converted to an embedding vector, and the database finds the stored vectors that are "closest" to it in the high-dimensional space.

## Understanding the Results

When we run this example with the query about the software engineering department, we get back two relevant sections:

- Section 2: Software Engineering - Project Phoenix Stability Enhancements (distance: 0.71)
- Methodology section (distance: 0.72)
The lower the distance score, the more similar the content is to our query. Both results are relevant to our question about what the software engineering department accomplished.

## Why Store Content with Embeddings

You might wonder why we store the original text alongside each embedding. The reason is practical: embeddings are just arrays of numbers that have no direct meaning to humans. When our search returns the most similar embeddings, we need the actual text content to understand what was found and to use it in generating responses.

Some implementations store just an ID that points back to the original text, but for simplicity, we're storing the content directly with each vector.

## What's Next

This implementation covers the core RAG workflow, but there are still improvements we can make. In real-world applications, you might encounter scenarios where this basic approach doesn't work as expected, and we'll explore those refinements in upcoming sections.

#### Downloads

- 003_vectordb.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## BM25 lexical search

> https://anthropic.skilljar.com/claude-with-google-vertex/289195

details

2
                                    download

## BM25 lexical search

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building a RAG pipeline, you'll quickly discover that semantic search alone doesn't always return the best results. Sometimes you need exact term matches that semantic search might miss. The solution is to combine semantic search with lexical search using a technique called BM25.

## The Problem with Semantic Search Alone

Let's say you're searching for a specific incident ID like "INC-2023-Q4-011" in a document. While this exact term appears multiple times in relevant sections, semantic search might return unrelated sections that are semantically similar but don't actually contain the specific term you're looking for.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620882%2F07_-_006_-_BM25_Lexical_Search_04.1748620882308.png)

This happens because semantic search focuses on meaning rather than exact matches. When you need precise term matching, you need a different approach.

## Hybrid Search Strategy

The solution is to run two searches in parallel and merge the results:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620883%2F07_-_006_-_BM25_Lexical_Search_05.1748620883219.png)

- Semantic Search - Uses embeddings and vector databases for meaning-based matching
- Lexical Search - Uses classic text search for exact term matching
- Merge Results - Combines both result sets for better coverage

## How BM25 Works

BM25 (Best Match 25) is a popular algorithm for lexical search in RAG pipelines. Here's how it processes a search query:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620884%2F07_-_006_-_BM25_Lexical_Search_07.1748620884013.png)

The algorithm follows these key steps:

- Tokenize the query - Break the user's question into individual terms
- Count term frequency - See how often each term appears across all documents
- Weight terms by rarity - Terms used less frequently get higher importance scores
- Find best matches - Return chunks that contain more instances of the higher-weighted terms
The key insight is that rare terms like "INC-2023-Q4-011" are much more important for search than common words like "a" or "the".

## Implementing BM25 Search

Here's how to set up a BM25 search system:

```
# Create a BM25 store
store = BM25Index()

# Add documents to the store
for chunk in chunks:
    store.add_document({"content": chunk})

# Search the store
results = store.search("What happened with INC-2023-Q4-011?", 3)
```

```
# Create a BM25 store
store = BM25Index()

# Add documents to the store
for chunk in chunks:
    store.add_document({"content": chunk})

# Search the store
results = store.search("What happened with INC-2023-Q4-011?", 3)
```

The BM25 implementation provides the same API as your semantic search system - both have add_document() and search() methods, making them easy to use together.

```
add_document()
```

```
search()
```

## Better Search Results

When you run the same query through BM25 that failed with semantic search alone, you get much better results. Instead of returning irrelevant sections, BM25 prioritizes the sections that actually contain your specific search terms.

The algorithm correctly identifies that "INC-2023-Q4-011" is a rare, important term and ranks documents containing it much higher than documents with only common words from the query.

## Next Steps

Now that you have both semantic and lexical search systems working independently, the next step is merging their results. This hybrid approach gives you the best of both worlds - the contextual understanding of semantic search combined with the precision of exact term matching from lexical search.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620884%2F07_-_006_-_BM25_Lexical_Search_19.1748620884731.png)

Both search systems use similar APIs, making it straightforward to query both in parallel and combine their results into a single, more comprehensive result set.

#### Downloads

- 004_bm25.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## A Multi-index RAG pipeline

> https://anthropic.skilljar.com/claude-with-google-vertex/289193

details

2
                                    download

## A Multi-index RAG pipeline

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you have both semantic search (vector embeddings) and lexical search (BM25) working independently, the next step is combining them into a unified search pipeline. This hybrid approach leverages the strengths of both methods to deliver more accurate results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620887%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_00.1748620887431.png)

## Creating a Unified Interface

Both search implementations share nearly identical APIs - they both have add_document() and search() methods that work the same way. This consistency makes it straightforward to wrap them in a single Retriever class.

```
add_document()
```

```
search()
```

```
Retriever
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620888%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_01.1748620888208.png)

The Retriever acts as a coordinator that forwards user queries to both indexes, collects their results, and merges them into a single ranked list.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620889%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_02.1748620888938.png)

## Reciprocal Rank Fusion

The challenge is merging results from different search methods that use different scoring systems. Vector search returns cosine similarity scores, while BM25 returns relevance scores - you can't simply combine these numbers directly.

Instead, we use a technique called Reciprocal Rank Fusion (RRF). This method focuses on the rank position of results rather than their raw scores.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620889%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_04.1748620889568.png)

Here's how it works with an example. Say your vector search returns sections 2, 7, and 6 in that order, while BM25 returns sections 6, 2, and 7. To merge these:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620890%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_05.1748620890357.png)

First, create a table showing each text chunk and its rank from both search methods:

- Section 2: Rank 1 from vector, rank 2 from BM25
- Section 7: Rank 2 from vector, rank 3 from BM25
- Section 6: Rank 3 from vector, rank 1 from BM25

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620891%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_06.1748620890893.png)

Then apply the RRF formula to calculate a combined score for each chunk:

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

Where k is a constant (typically 60, but we'll use 1 for clearer results) and rank_i(d) is the rank of document d in the i-th search result.

```
k
```

```
rank_i(d)
```

```
d
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620891%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_07.1748620891653.png)

For our example:

- Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
- Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
- Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620893%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_08.1748620893017.png)

The final ranking becomes: Section 2 (0.833), Section 6 (0.75), Section 7 (0.583). This makes intuitive sense - Section 2 performed well in both searches, Section 6 had mixed results, and Section 7 ranked lower overall.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620894%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_09.1748620894616.png)

## Implementation

The Retriever class implementation is straightforward:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620895%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_11.1748620895209.png)

```
class Retriever:
    def __init__(self, *indexes):
        self._indexes = list(indexes)
    
    def add_document(self, document):
        for index in self._indexes:
            index.add_document(document)
    
    def search(self, query_text, k=1, k_rrf=60):
        # Get results from all indexes
        all_results = [index.search(query_text, k) for index in self._indexes]
        
        # Apply reciprocal rank fusion
        # ... merge logic here ...
```

```
class Retriever:
    def __init__(self, *indexes):
        self._indexes = list(indexes)
    
    def add_document(self, document):
        for index in self._indexes:
            index.add_document(document)
    
    def search(self, query_text, k=1, k_rrf=60):
        # Get results from all indexes
        all_results = [index.search(query_text, k) for index in self._indexes]
        
        # Apply reciprocal rank fusion
        # ... merge logic here ...
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620896%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_12.1748620895862.png)

The merge logic tracks document ranks across all search results, calculates RRF scores, and returns the top-k documents sorted by their combined scores.

## Testing the Hybrid Approach

When testing with the query "what happened with INC-2023-Q4-011?", the hybrid approach delivers much better results than vector search alone:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620897%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_14.1748620896778.png)

The results now correctly prioritize:

- Section 10: Cybersecurity Analysis (the actual incident report)
- Section 2: Software Engineering (relevant context)
- Section 5: Legal Developments (less relevant but still related)

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620897%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_16.1748620897641.png)

## Benefits of the Hybrid Architecture

This design offers several advantages:

- Modular design: Each search index is implemented independently with the same API
- Easy extensibility: You can add new search methods by implementing the same search() and add_document() interface

```
search()
```

```
add_document()
```

- Better accuracy: Combines semantic understanding with exact keyword matching
- Flexible fusion: The RRF algorithm works regardless of how many search indexes you combine

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620898%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_18.1748620898355.png)

The consistent API means you could easily add a third search index - perhaps one that specializes in named entity recognition or handles specific document types - and the Retriever would automatically incorporate its results into the final ranking.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620899%2F07_-_007_-_A_Multi-Index_Rag_Pipeline_17.1748620899059.png)

This hybrid search foundation provides significantly more robust retrieval than either method alone, setting up your RAG pipeline for better performance across a wider range of query types.

#### Downloads

- report.md
                                                (opens in new tab)
- 005_hybrid.ipynb
                                                (opens in new tab)

---

## Reranking results

> https://anthropic.skilljar.com/claude-with-google-vertex/289192

details

2
                                    download

## Reranking results

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The hybrid retrieval approach we've built works well, but it still has some rough edges. When we search for "what did the eng team do with INC-2023-Q4-011?", we'd expect the Software Engineering section to rank higher since it specifically mentions the engineering team and the incident. However, the Cybersecurity section still comes first.

This is where re-ranking comes in - a post-processing technique that can significantly improve retrieval accuracy.

## How Re-ranking Works

Re-ranking adds an extra step after your hybrid search process. Instead of just returning the merged results from your vector and BM25 indexes, you pass those results through an LLM for intelligent reordering.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620879%2F07_-_008_-_Reranking_Results_05.1748620879658.png)

The process is straightforward:

- Run your existing hybrid search (vector + BM25)
- Merge the results as before
- Send the merged results to Claude with a re-ranking prompt
- Get back a reordered list of the most relevant documents

## The Re-ranking Prompt

The prompt structure is simple but effective. You provide Claude with the user's question and all the candidate documents, then ask it to return the most relevant ones in order of decreasing relevance.

```
You are about to be given a set of documents, along with an id of each.
Your task is to select the {k} most relevant documents to answer the user's question.

Here is the user's question:
<question>
{query_text}
</question>

Here are the documents to select from:
<documents>
{joined_docs}
</documents>

Respond in the following format:
```json
{
  "document_ids": str[] # List document ids, {k} elements long, sorted in order of decreasing relevance
}
```
```

```
You are about to be given a set of documents, along with an id of each.
Your task is to select the {k} most relevant documents to answer the user's question.

Here is the user's question:
<question>
{query_text}
</question>

Here are the documents to select from:
<documents>
{joined_docs}
</documents>

Respond in the following format:
```json
{
  "document_ids": str[] # List document ids, {k} elements long, sorted in order of decreasing relevance
}
```
```

## Efficiency Considerations

A key optimization is using document IDs instead of asking Claude to return full text chunks. If you asked Claude to return the complete text of each relevant document, you'd waste time waiting for it to copy large amounts of text.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620880%2F07_-_008_-_Reranking_Results_14.1748620880511.png)

Instead, assign each text chunk a unique ID ahead of time, then ask Claude to return just those IDs in the preferred order. This makes the re-ranking process much faster while still giving you the reordered results you need.

## Implementation

The re-ranker function gets called automatically after your initial hybrid search completes. Here's the basic structure:

```
def reranker_fn(docs, query_text, k):
    joined_docs = "\n".join([
        f"""
        <document>
        <document_id>{doc["id"]}</document_id>
        <document_content>{doc["content"]}</document_content>
        </document>
        """
        for doc in docs
    ])
    
    # Build prompt with user question and documents
    # Send to Claude with JSON response format
    # Parse and return reordered document IDs
```

```
def reranker_fn(docs, query_text, k):
    joined_docs = "\n".join([
        f"""
        <document>
        <document_id>{doc["id"]}</document_id>
        <document_content>{doc["content"]}</document_content>
        </document>
        """
        for doc in docs
    ])
    
    # Build prompt with user question and documents
    # Send to Claude with JSON response format
    # Parse and return reordered document IDs
```

You can integrate this into your retriever by passing the re-ranker function as a parameter:

```
retriever = Retriever(bm25_index, vector_index, reranker_fn=reranker_fn)
```

```
retriever = Retriever(bm25_index, vector_index, reranker_fn=reranker_fn)
```

## Results

The re-ranking approach shows clear improvements. When testing the query "what did the eng team do with INC-2023-Q4-011?", the Software Engineering section now correctly appears first, ahead of the Cybersecurity section. Claude successfully identified that the user was specifically asking about the engineering team's involvement with the incident.

## Trade-offs

Re-ranking comes with trade-offs to consider:

- Increased latency: You now need to wait for an additional LLM call to complete
- Improved accuracy: The LLM can understand context and intent better than pure similarity scores
- Cost considerations: Each search now requires an LLM API call
For many applications, the accuracy improvement justifies the additional latency and cost, especially when precise retrieval is critical for your use case.

#### Downloads

- 006_reranking.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Contextual retrieval

> https://anthropic.skilljar.com/claude-with-google-vertex/289187

details

2
                                    download

## Contextual retrieval

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Contextual retrieval is a technique that improves RAG pipeline accuracy by solving a fundamental problem: when you split a document into chunks, each chunk loses its connection to the broader document context.

## The Problem with Standard Chunking

When you take a source document and break it into chunks for your vector database, each individual piece no longer knows where it came from or how it relates to the rest of the document. This can hurt retrieval accuracy because the chunks lack important contextual information.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620944%2F07_-_009_-_Contextual_Retrieval_00.1748620943971.png)

## How Contextual Retrieval Works

Contextual retrieval adds a preprocessing step before inserting chunks into your retriever database. Here's the process:

- Take each individual chunk and the original source document
- Send both to Claude with a specific prompt asking it to add context
- Claude generates a short snippet that "situates" the chunk within the larger document
- Combine this context with the original chunk to create a "contextualized chunk"
- Use the contextualized chunk in your vector and BM25 indexes

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620945%2F07_-_009_-_Contextual_Retrieval_04.1748620945450.png)

For example, if you have a section about software engineering that mentions a 2023 incident, Claude might generate context like: "This section is from a larger report about a cross-discipline group. It includes mention of INC-2023-04-011, which is also mentioned in the Cybersecurity Analysis section."

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620947%2F07_-_009_-_Contextual_Retrieval_05.1748620946965.png)

## Handling Large Documents

A common problem is when your source document is too large to fit into Claude's context window. You can still use contextual retrieval by providing a reduced set of context:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748620947%2F07_-_009_-_Contextual_Retrieval_07.1748620947609.png)

Instead of including the entire document, provide:

- A few chunks from the start of the document (often containing summaries or abstracts)
- Chunks immediately before the chunk you're contextualizing
This approach gives Claude enough information to understand the document structure and immediate context without overwhelming the prompt.

## Implementation Example

Here's a basic function for adding context to chunks:

```
def add_context(text_chunk, source_text):
    prompt = """
Write a short and succinct snippet of text to situate this chunk within the
overall source document for the purposes of improving search retrieval of the chunk.

Here is the original source document:
<document>
{source_text}
</document>

Here is the chunk we want to situate within the whole document:
<chunk>
{text_chunk}
</chunk>

Answer only with the succinct context and nothing else.
"""
    
    messages = []
    add_user_message(messages, prompt)
    result = chat(messages)
    
    return result["text"] + "\n" + text_chunk
```

```
def add_context(text_chunk, source_text):
    prompt = """
Write a short and succinct snippet of text to situate this chunk within the
overall source document for the purposes of improving search retrieval of the chunk.

Here is the original source document:
<document>
{source_text}
</document>

Here is the chunk we want to situate within the whole document:
<chunk>
{text_chunk}
</chunk>

Answer only with the succinct context and nothing else.
"""
    
    messages = []
    add_user_message(messages, prompt)
    result = chat(messages)
    
    return result["text"] + "\n" + text_chunk
```

For large documents, you can implement a strategy that selects relevant context chunks:

```
# Add context to each chunk, then add to the retriever
num_start_chunks = 2
num_prev_chunks = 2

for i, chunk in enumerate(chunks):
    context_parts = []
    
    # Initial set of chunks from the start of the doc
    context_parts.extend(chunks[: min(num_start_chunks, len(chunks))])
    
    # Additional chunks ahead of the current chunk we're contextualizing
    start_idx = max(0, i - num_prev_chunks)
    context_parts.extend(chunks[start_idx:i])
    
    context = "\n".join(context_parts)
    
    contextualized_chunk = add_context(chunk, context)
    retriever.add_document({"content": contextualized_chunk})
```

```
# Add context to each chunk, then add to the retriever
num_start_chunks = 2
num_prev_chunks = 2

for i, chunk in enumerate(chunks):
    context_parts = []
    
    # Initial set of chunks from the start of the doc
    context_parts.extend(chunks[: min(num_start_chunks, len(chunks))])
    
    # Additional chunks ahead of the current chunk we're contextualizing
    start_idx = max(0, i - num_prev_chunks)
    context_parts.extend(chunks[start_idx:i])
    
    context = "\n".join(context_parts)
    
    contextualized_chunk = add_context(chunk, context)
    retriever.add_document({"content": contextualized_chunk})
```

## When to Use Contextual Retrieval

This technique is most valuable when:

- Your documents have complex internal relationships between sections
- Chunks reference concepts defined elsewhere in the document
- Understanding the document structure is important for accurate retrieval
- You're working with technical documents, reports, or academic papers
While contextual retrieval adds processing time and cost (since you're making additional API calls), it can significantly improve retrieval accuracy for complex documents where context matters.

#### Downloads

- 007_contextual.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Quiz on Retrieval Augmented Generation

> https://anthropic.skilljar.com/claude-with-google-vertex/289277

## Quiz on Retrieval Augmented Generation

# Quiz on Retrieval Augmented Generation

---

## Extended thinking

> https://anthropic.skilljar.com/claude-with-google-vertex/289197

details

2
                                    download

## Extended thinking

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Extended thinking is Claude's advanced reasoning feature that gives the model time to think through complex problems before generating a response. When enabled, Claude produces a visible thinking process that users can examine to understand how the model approached their query.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621012%2F08_-_001_-_Extended_Thinking_01.1748621012415.png)

This feature significantly improves Claude's ability to handle complex tasks with greater accuracy, but it comes with important trade-offs. You'll be charged for all tokens generated during the thinking phase, and the additional processing time increases response latency. The key is knowing when the improved intelligence justifies the extra cost and wait time.

## When to Use Extended Thinking

The decision to enable extended thinking should be driven by your prompt evaluations. Here's the recommended approach:

- Write and test your prompt without extended thinking first
- Run evaluations to measure accuracy
- If results aren't meeting your standards after prompt optimization efforts
- Then consider enabling extended thinking as a solution

## How Extended Thinking Changes Responses

Without extended thinking, Claude's response flow is straightforward - you send a user message with a text block and receive an assistant message with a text block in return.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621013%2F08_-_001_-_Extended_Thinking_03.1748621013540.png)

With extended thinking enabled, the response structure changes significantly. You'll receive an assistant message containing two distinct blocks:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621014%2F08_-_001_-_Extended_Thinking_04.1748621014052.png)

- A thinking block containing Claude's reasoning process

```
thinking
```

- A text block with the final response

```
text
```

## The Signature System

Each thinking block includes a cryptographic signature that serves an important security purpose. This signature ensures that the thinking text hasn't been modified when you include the message in future conversation turns.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621015%2F08_-_001_-_Extended_Thinking_05.1748621014974.png)

Claude relies heavily on the thinking content for response generation, so preventing tampering is crucial for maintaining safe and consistent behavior. If you modify the thinking text, the signature validation will fail.

## Redacted Thinking

Sometimes Claude's thinking process gets flagged by internal safety systems. When this happens, you'll receive a redacted thinking block instead of the raw thinking text.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621016%2F08_-_001_-_Extended_Thinking_07.1748621015793.png)

The redacted content contains the actual thinking text in encrypted form. While you can't read it, you can still include this block in future conversation turns so Claude doesn't lose context from its previous reasoning.

## Implementation

To enable extended thinking in your code, you'll need to modify your chat function with two new parameters:

```
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    thinking=False,
    thinking_budget=1024
):
```

```
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    thinking=False,
    thinking_budget=1024
):
```

The thinking budget represents the maximum tokens Claude can use for reasoning. The minimum allowed value is 1024 tokens. Importantly, your max_tokens parameter must exceed your thinking budget - if you set a thinking budget of 1024, max_tokens must be at least 1025.

```
max_tokens
```

```
max_tokens
```

In practice, you'll want a much larger buffer. For example, with a thinking budget of 1024 and max_tokens of 4000, Claude can use up to 1024 tokens for thinking and up to 2976 tokens for the actual response.

```
max_tokens
```

Add the thinking configuration to your API parameters when the feature is enabled:

```
if thinking:
    params["thinking"] = {
        "type": "enabled",
        "budget": thinking_budget
    }
```

```
if thinking:
    params["thinking"] = {
        "type": "enabled",
        "budget": thinking_budget
    }
```

## Testing Redacted Responses

During development, you may want to test how your application handles redacted thinking blocks. You can force Claude to return a redacted response by including this special trigger string in your message:

```
TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB
```

```
TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB
```

This ensures your error handling works correctly when encountering redacted content in production.

#### Downloads

- 001_thinking_complete.ipynb
                                                (opens in new tab)
- 001_thinking.ipynb
                                                (opens in new tab)

---

## Image support

> https://anthropic.skilljar.com/claude-with-google-vertex/289203

details

2
                                    download

## Image support

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude's vision capabilities let you include images in your messages and ask Claude to analyze them in sophisticated ways. You can ask Claude to describe image contents, compare multiple images, count objects, or perform complex visual analysis tasks.

## Image Handling Basics

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621025%2F08_-_002_-_Image_Support_01.1748621025480.png)

When working with images in Claude, you need to understand several key limitations:

- Up to 100 images across all messages in a single request
- Max size of 5MB per image
- When sending one image: max height/width of 8000px
- When sending multiple images: max height/width of 2000px
- Images can be included as base64 encoding or a URL to the image
- Each image counts as tokens based on dimensions: tokens = (width px × height px) / 750

```
tokens = (width px × height px) / 750
```

To include an image, you add an image block to your user message alongside text blocks. Here's the structure:

```
with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(
        f.read()
    ).decode("utf-8")

add_user_message(messages, [
    # Image Block
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "What do you see in this image?"
    }
])
```

```
with open("image.png", "rb") as f:
    image_bytes = base64.standard_b64encode(
        f.read()
    ).decode("utf-8")

add_user_message(messages, [
    # Image Block
    {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image_bytes,
        }
    },
    # Text Block
    {
        "type": "text",
        "text": "What do you see in this image?"
    }
])
```

## Message Flow

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621026%2F08_-_002_-_Image_Support_02.1748621026421.png)

The conversation works just like text-only interactions. Your server sends a user message containing both image and text blocks to Claude, and Claude responds with a text message analyzing the image.

## Prompting Techniques

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621027%2F08_-_002_-_Image_Support_04.1748621027248.png)

The most important thing to understand about Claude's vision capabilities is that good prompting techniques are absolutely critical. Simple prompts often produce poor results, even with clear images.

For example, asking "How many marbles are in this image?" with an image containing 12 marbles might return an incorrect count of 13. You can dramatically improve accuracy by applying the same prompting engineering techniques you'd use for text:

- Providing detailed guidelines and analysis steps
- Using one-shot or multi-shot examples
- Breaking down complex tasks into smaller steps

### Step-by-Step Analysis

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621028%2F08_-_002_-_Image_Support_05.1748621027972.png)

Instead of a simple question, provide Claude with a methodology:

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
```

```
Analyze this image of marbles and determine the exact count using this methodology:
1. Begin by identifying each unique marble one at a time. Assign each a number as you identify it.
2. Verify your result by counting with a different method. Start from the bottom-left corner and work row by row, from left to right.

What is the exact, verified number of marbles in this image?
```

This structured approach helps Claude get the correct count of 12 marbles.

### One-Shot Examples

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621029%2F08_-_002_-_Image_Support_07.1748621028745.png)

You can also use one-shot prompting by including multiple image-text pairs in a single message:

```
[Image of 11 marbles]
The image above has 11 marbles in it.

[Image of 12 marbles]  
How many marbles are in this image?
```

```
[Image of 11 marbles]
The image above has 11 marbles in it.

[Image of 12 marbles]  
How many marbles are in this image?
```

Providing an example significantly improves Claude's accuracy on the target image.

## Real-World Example: Fire Risk Assessment

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621030%2F08_-_002_-_Image_Support_08.1748621030403.png)

Here's a practical application: automating fire risk assessments for home insurance. Insurance companies often require homeowners to trim trees around their property to reduce wildfire risk. Instead of sending inspectors to each property, you can use satellite imagery with Claude.

The system analyzes satellite images to identify:

- Dense, close-packed trees near the residence
- Difficult access routes for emergency services
- Branches overhanging the residence
Rather than a simple prompt like "provide a fire risk score," you create a detailed analysis framework:

```
Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:
   - The largest roofed structure
   - Typical residential features (driveway connection, regular geometry)
   - Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:
   - Identify any trees whose canopy extends directly over any portion of the roof
   - Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
   - Note particularly dense areas of overhang

3. Fire risk assessment: For any overhanging trees, evaluate:
   - Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
   - Proximity to chimneys, vents, or other roof openings if visible
   - Areas where branches create a "bridge" between wildland vegetation and the structure

4. Defensible space identification: Assess the property's overall vegetative structure:
   - Identify if trees connect to form a continuous canopy over or near the home
   - Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:
   - Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around
   - Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
   - Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple points of vulnerability
   - Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item above (1-5), write one sentence summarizing your findings, with your final response being the numerical rating.
```

```
Analyze the attached satellite image of a property with these specific steps:

1. Residence identification: Locate the primary residence on the property by looking for:
   - The largest roofed structure
   - Typical residential features (driveway connection, regular geometry)
   - Distinction from other structures (garages, sheds, pools)

2. Tree overhang analysis: Examine all trees near the primary residence:
   - Identify any trees whose canopy extends directly over any portion of the roof
   - Estimate the percentage of roof covered by overhanging branches (0-25%, 25-50%, 50-75%, 75%+)
   - Note particularly dense areas of overhang

3. Fire risk assessment: For any overhanging trees, evaluate:
   - Potential wildfire vulnerability (ember catch points, continuous fuel paths to structure)
   - Proximity to chimneys, vents, or other roof openings if visible
   - Areas where branches create a "bridge" between wildland vegetation and the structure

4. Defensible space identification: Assess the property's overall vegetative structure:
   - Identify if trees connect to form a continuous canopy over or near the home
   - Note any obvious fuel ladders (vegetation that can carry fire from ground to tree to roof)

5. Fire risk rating: Based on your analysis, assign a Fire Risk Rating from 1-4:
   - Rating 1 (Low Risk): No tree branches overhanging the roof, good defensible space around
   - Rating 2 (Moderate Risk): Minimal overhang (<25% of roof), some separation between tree canopies
   - Rating 3 (High Risk): Significant overhang (25-50% of roof), connected tree canopies, multiple points of vulnerability
   - Rating 4 (Severe Risk): Extensive overhang (>50% of roof), dense vegetation against structure

For each item above (1-5), write one sentence summarizing your findings, with your final response being the numerical rating.
```

This comprehensive prompt guides Claude through a systematic analysis, resulting in accurate and actionable fire risk assessments. When tested with a heavily tree-covered property, Claude correctly identified it as a "3 (High Risk)" due to significant tree overhang and connected canopies around the structure.

The key takeaway is that Claude's vision capabilities are powerful, but they require the same careful prompt engineering you'd use for any complex task. Invest time in creating detailed, structured prompts rather than relying on simple questions.

#### Downloads

- 002_images.ipynb
                                                (opens in new tab)
- images.zip
                                                (opens in new tab)

---

## PDF support

> https://anthropic.skilljar.com/claude-with-google-vertex/289198

details

1
                                    download

## PDF support

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Downloads

- earth.pdf
                                                (opens in new tab)

---

## Citations

> https://anthropic.skilljar.com/claude-with-google-vertex/289202

details

2
                                    download

## Citations

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When Claude answers questions based on documents you provide, users might assume it's just pulling information from its training data. But what if Claude is actually citing specific sources? The citations feature lets you show users exactly where Claude found its information, building trust and transparency into your AI applications.

## Why Citations Matter

Without citations, users see Claude's responses as coming from memory. They have no way to verify the information or understand that it's based on specific documents you provided. Citations solve this by showing users the exact source material Claude used to generate each part of its response.

## Enabling Citations

To enable citations, add two fields to your document message:

```
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": file_bytes,
  },
  "title": "earth.pdf",
  "citations": { "enabled": True }
}
```

```
{
  "type": "document",
  "source": {
    "type": "base64",
    "media_type": "application/pdf",
    "data": file_bytes,
  },
  "title": "earth.pdf",
  "citations": { "enabled": True }
}
```

The title field gives your document a name that appears in citations. The citations field with enabled: True tells Claude to track where it finds information.

```
title
```

```
citations
```

```
enabled: True
```

## Citation Structure

When citations are enabled, Claude's response becomes more complex. Instead of simple text, you get structured content with citation information:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621005%2F08_-_004_-_Citations_09.1748621004785.png)

Each citation contains:

- cited_text - The exact text Claude is referencing from your document
- document_index - Which document (if you provided multiple)
- document_title - The title you assigned to the document
- start_page_number - Where the cited text begins
- end_page_number - Where the cited text ends

## Building Citation Interfaces

The real power of citations comes from building user interfaces that display them. You can create numbered references in the text that link to detailed citation information:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621005%2F08_-_004_-_Citations_12.1748621005614.png)

When users hover over or click citation numbers, they see exactly which document and pages Claude referenced. This transparency helps users verify information and builds confidence in Claude's responses.

## Citations with Plain Text

Citations aren't limited to PDFs. You can also use them with plain text documents:

```
{
  "type": "document", 
  "source": {
    "type": "text",
    "media_type": "text/plain",
    "data": article_text,
  },
  "title": "earth article",
  "citations": { "enabled": True }
}
```

```
{
  "type": "document", 
  "source": {
    "type": "text",
    "media_type": "text/plain",
    "data": article_text,
  },
  "title": "earth article",
  "citations": { "enabled": True }
}
```

With plain text, you get CitationCharLocation objects instead of page locations. These provide character positions within the text, allowing you to highlight the exact sentences or paragraphs Claude referenced.

```
CitationCharLocation
```

## When to Use Citations

Citations are essential when:

- Users need to verify information accuracy
- You're working with sensitive or important documents
- Transparency about sources builds trust in your application
- Users might want to read the original source material
By implementing citations, you transform Claude from a "black box" that gives answers into a transparent system that shows its work, making your AI applications more trustworthy and verifiable.

#### Downloads

- earth.pdf
                                                (opens in new tab)
- 002_citations_complete.ipynb
                                                (opens in new tab)

---

## Prompt caching

> https://anthropic.skilljar.com/claude-with-google-vertex/289196

details

## Prompt caching

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. Instead of throwing away all the processing work after each request, Claude can save and reuse it when you send similar content again.

## How Claude Normally Processes Requests

To understand prompt caching, let's first look at what happens during a typical request without caching enabled.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621075%2F08_-_005_-_Prompt_Caching_01.1748621075646.png)

When you send a message to Claude, it doesn't immediately start generating a response. Instead, Claude performs extensive preprocessing work on your input:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621077%2F08_-_005_-_Prompt_Caching_04.1748621077221.png)

- Tokenizes the prompt (breaks text into smaller units)
- Creates embeddings for each token (mathematical representations)
- Adds context based on surrounding text
- Only then generates the actual output text

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621078%2F08_-_005_-_Prompt_Caching_06.1748621078185.png)

After sending you the response, Claude discards all this computational work. Everything gets thrown away, and Claude declares itself ready for the next request.

## The Problem with Repeated Content

Here's where things get inefficient. Imagine you're having a conversation with Claude, so your follow-up request includes:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621079%2F08_-_005_-_Prompt_Caching_08.1748621078850.png)

- The same original user message from before
- Claude's previous response
- Your new follow-up message

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621079%2F08_-_005_-_Prompt_Caching_10.1748621079419.png)

Claude has to reprocess that original message all over again, even though it just analyzed the exact same content moments earlier. As Claude might think: "I just processed that message and threw away all the work I did. I could have reused it!"

## How Prompt Caching Solves This

Prompt caching changes this wasteful process. Instead of discarding the preprocessing work, Claude saves it in a cache.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621080%2F08_-_005_-_Prompt_Caching_14.1748621079978.png)

Here's how it works:

- Initial request: Claude processes your message and writes the computational work to a cache
- Follow-up requests: When Claude sees the same content again, it reads the previously processed work from the cache instead of starting over

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621080%2F08_-_005_-_Prompt_Caching_16.1748621080605.png)

The cache acts like a lookup table: "If I ever see this message again, I'll reuse this work I already did."

## Key Benefits and Limitations

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621081%2F08_-_005_-_Prompt_Caching_18.1748621081213.png)

Prompt caching offers several advantages:

- Faster responses: Requests using cached content execute more quickly
- Lower costs: You pay less for processing that reuses cached work
- Automatic optimization: The initial request writes to cache, follow-up requests read from it
However, there are important limitations to keep in mind:

- Short lifespan: Cache only lives for 5 minutes
- Exact matches required: Only useful when you're repeatedly sending the same content
- Common use case: This happens extremely frequently in conversational applications and document analysis workflows
Prompt caching is particularly valuable for applications where users frequently reference the same documents, continue conversations, or iterate on similar prompts within a short timeframe.

---

## Rules of prompt caching

> https://anthropic.skilljar.com/claude-with-google-vertex/289194

details

## Rules of prompt caching

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt caching in Claude works by storing the computational work done on messages so it can be reused in follow-up requests. This makes requests that use cached content both cheaper and faster to execute.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621081%2F08_-_006_-_Rules_of_Prompt_Caching_00.1748621080824.png)

The process follows a simple pattern: your initial request will write to the cache, and follow-up requests can read from the cache. The cache lives for 5 minutes, so this feature is only useful if you're repeatedly sending the same content - but this happens extremely frequently in real applications.

## Cache Breakpoints

Work done on messages is not cached automatically. We have to manually add a 'cache breakpoint' to a block. Work done for everything before the breakpoint will be cached, and the cache will only be used on follow-up requests if the content up to and including the breakpoint is identical.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621081%2F08_-_006_-_Rules_of_Prompt_Caching_03.1748621081646.png)

When you need to add cache breakpoints, you must use the longhand form for writing text blocks instead of the shorthand. Here's the difference:

```
// Shorthand - can't add cache breakpoints
user_message = {
  "role": "user",
  "content": "Hi there!"
}

// Longhand - required for cache breakpoints
user_message = {
  "role": "user", 
  "content": [
    {
      "type": "text",
      "text": "",
      "cache_control": {
        "type": "ephemeral"
      }
    }
  ]
}
```

```
// Shorthand - can't add cache breakpoints
user_message = {
  "role": "user",
  "content": "Hi there!"
}

// Longhand - required for cache breakpoints
user_message = {
  "role": "user", 
  "content": [
    {
      "type": "text",
      "text": "",
      "cache_control": {
        "type": "ephemeral"
      }
    }
  ]
}
```

## How Cache Breakpoints Work

Cache breakpoints span messages and can cache assistant messages too. When you place a breakpoint, everything up to that point gets cached. Remember, content must be identical to use the cache!

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621082%2F08_-_006_-_Rules_of_Prompt_Caching_09.1748621082421.png)

In a follow-up request, Claude reads the previously processed work from the cache instead of reprocessing it:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621083%2F08_-_006_-_Rules_of_Prompt_Caching_11.1748621083185.png)

## Breakpoint Location

You're not restricted to text blocks! You can add cache breakpoints to system prompts and tool definitions. These are actually the most common caching opportunities since they rarely change between requests.

```
// Tool definitions with cache breakpoint
tools = [
  add_duration_to_datetime_schema,
  get_current_datetime_schema,
  {
    "name": "set_reminder",
    "description": "Sets a reminder...",
    "input_schema": { ... },
    "cache_control": {"type": "ephemeral"}
  }
]

// System prompt with cache breakpoint  
system = [
  {
    "type": "text",
    "text": "You are a senior software...",
    "cache_control": {"type": "ephemeral"}
  }
]
```

```
// Tool definitions with cache breakpoint
tools = [
  add_duration_to_datetime_schema,
  get_current_datetime_schema,
  {
    "name": "set_reminder",
    "description": "Sets a reminder...",
    "input_schema": { ... },
    "cache_control": {"type": "ephemeral"}
  }
]

// System prompt with cache breakpoint  
system = [
  {
    "type": "text",
    "text": "You are a senior software...",
    "cache_control": {"type": "ephemeral"}
  }
]
```

## Cache Ordering

Behind the scenes, tools, system prompts, and messages get joined together in that specific order when fed into Claude. This affects how your cache breakpoints work.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621084%2F08_-_006_-_Rules_of_Prompt_Caching_14.1748621083854.png)

You can add up to four cache breakpoints total. If you place a breakpoint on your last tool, everything up to that tool gets cached, but the system prompt and messages won't be. This gives you fine-grained control over what gets cached based on what changes in your application.

## Minimum Content Length

Content must be at least 1024 tokens long to be cached (sum of all messages/blocks you're trying to cache). A simple "Hi there!" message won't meet this threshold, but if you duplicate that text 500 times, you'll have enough tokens to cache.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621084%2F08_-_006_-_Rules_of_Prompt_Caching_19.1748621084576.png)

The key to effective prompt caching is identifying the parts of your requests that stay consistent - usually your system prompts and tool definitions - and placing breakpoints strategically to maximize cache hits while minimizing reprocessing.

---

## Prompt caching in action

> https://anthropic.skilljar.com/claude-with-google-vertex/289200

details

1
                                    download

## Prompt caching in action

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt caching is a powerful optimization feature that makes requests cheaper and faster when you're repeatedly sending the same content to Claude. The initial request writes to the cache, and follow-up requests can read from it. The cache lives for 5 minutes and is extremely useful since many applications send identical tool schemas, system prompts, or message histories repeatedly.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621082%2F08_-_007_-_Prompt_Caching_in_Action_19.1748621082240.png)

## How Prompt Caching Works

When you mark content for caching, Claude processes it once and stores the result. Subsequent requests that include the exact same content can skip the processing step and read directly from the cache. This only works if the cached content is identical - even a single character change invalidates the cache.

You can set multiple cache breakpoints in a single request. The caching order follows this sequence:

- Tool schemas
- System prompt
- Message history

## Setting Up Tool Schema Caching

To cache tool schemas, you need to add a cache_control field to the last tool in your list. Here's the proper way to do it without modifying your original tool schemas:

```
cache_control
```

```
if tools:
    tools_clone = tools.copy()
    last_tool = tools_clone[-1].copy()
    last_tool["cache_control"] = {"type": "ephemeral"}
    tools_clone[-1] = last_tool
    params["tools"] = tools_clone
```

```
if tools:
    tools_clone = tools.copy()
    last_tool = tools_clone[-1].copy()
    last_tool["cache_control"] = {"type": "ephemeral"}
    tools_clone[-1] = last_tool
    params["tools"] = tools_clone
```

This approach creates copies of both the tools list and the last tool schema before adding the cache control field. This prevents accidentally modifying your original tool definitions, which could cause issues if you reorder tools later.

## System Prompt Caching

For system prompts, you need to structure the system parameter as a list with a text block that includes the cache control field:

```
if system:
    params["system"] = [
        {
            "type": "text",
            "text": system,
            "cache_control": {"type": "ephemeral"}
        }
    ]
```

```
if system:
    params["system"] = [
        {
            "type": "text",
            "text": system,
            "cache_control": {"type": "ephemeral"}
        }
    ]
```

## Understanding Cache Behavior

When you make your first request with cacheable content, you'll see cache_creation_input_tokens in the usage field. This shows how many tokens Claude wrote to the cache. On subsequent requests with identical content, you'll see cache_read_input_tokens instead.

```
cache_creation_input_tokens
```

```
cache_read_input_tokens
```

If you have both cached and new content in the same request, you might see both cache reads and cache writes. For example, if you keep the same tool schemas but change the system prompt, you'll read the tools from cache while writing the new system prompt to cache.

## Cache Invalidation

The cache is extremely sensitive to changes. Modifying even a single character in your tool schema description, system prompt, or any cached content will invalidate that cache entry. When this happens, Claude treats it as completely new content and creates a fresh cache entry.

This sensitivity means you should be thoughtful about what you cache. Tool schemas and system prompts that remain stable across many requests are ideal candidates. Dynamic content that changes frequently won't benefit from caching.

## Practical Implementation

In practice, you'll want to build caching into your chat functions by default. Most applications use the same tool schemas and system prompts across multiple requests, making them perfect for caching. The performance and cost benefits are significant when you're making many requests with similar content.

Remember that caching is most valuable when you're repeatedly sending the same content. Since this happens extremely frequently in real applications - especially with tool schemas and system prompts - implementing caching early in your development process will pay dividends as your application scales.

#### Downloads

- 003_caching.ipynb
                                                (opens in new tab)

---

## Quiz on features of Claude

> https://anthropic.skilljar.com/claude-with-google-vertex/289275

## Quiz on features of Claude

# Quiz on Features of Claude

---

## Introducing MCP

> https://anthropic.skilljar.com/claude-with-google-vertex/289201

details

## Introducing MCP

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Instead of building every tool function yourself, MCP shifts that burden to specialized servers that handle the heavy lifting.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621139%2F09_-_001_-_Introducing_MCP_01.1748621139100.png)

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connects to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to outside services like GitHub, AWS, or databases.

## The Problem MCP Solves

Let's say you're building a chat interface where users can ask Claude about their GitHub data. A user might ask "What open pull requests are there across all my repositories?" To answer this, Claude needs tools that can access GitHub's API.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621140%2F09_-_001_-_Introducing_MCP_03.1748621139961.png)

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. To handle all of GitHub's features, you'd need to create an incredible number of tool schemas and functions:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621140%2F09_-_001_-_Introducing_MCP_05.1748621140571.png)

This means writing, testing, and maintaining a lot of code for functions like:

- get_repos()

```
get_repos()
```

- list_repos()

```
list_repos()
```

- create_repos()

```
create_repos()
```

- search_issues()

```
search_issues()
```

- update_issue()

```
update_issue()
```

- create_issue()

```
create_issue()
```

- get_issue()

```
get_issue()
```

- create_file()

```
create_file()
```

## How MCP Changes This

MCP shifts the burden of tool definitions and execution from your server to MCP Servers. Instead of you writing all those GitHub integration tools, someone else creates an MCP Server for GitHub that contains all the necessary tools and functions.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621141%2F09_-_001_-_Introducing_MCP_08.1748621141166.png)

The MCP Server acts as a wrapper around the outside service, providing pre-built tools that you can use immediately. Your server becomes an MCP Client that connects to these specialized servers.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621141%2F09_-_001_-_Introducing_MCP_09.1748621141761.png)

## Who Creates MCP Servers

Anyone can create an MCP Server implementation. Often, service providers themselves will create official MCP implementations. For example, AWS might release their own official MCP Server with tools for their various services.

You can also create your own MCP Server to wrap access to any service you need to integrate with.

## Common Questions

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621143%2F09_-_001_-_Introducing_MCP_12.1748621142800.png)

How is using an MCP Server different from calling a service's API directly?

MCP Servers provide tool schemas and functions already defined for you. If you call an API directly, you'll be writing those tool definitions yourself. MCP saves you that implementation work.

Aren't MCP Servers and tool use the same thing?

This is a common misconception. MCP Servers and tool use are complementary but different concepts. MCP Servers provide pre-built tool schemas and functions, while tool use is about how Claude actually calls those tools. MCP is really about who does the work of creating and maintaining the tool implementations.

The key benefit is that MCP Servers give you access to sophisticated integrations without having to build and maintain all that code yourself. You get the power of tool use with much less development overhead.

---

## MCP clients

> https://anthropic.skilljar.com/claude-with-google-vertex/289204

details

## MCP clients

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external functionality, the client handles all the message passing and protocol details for you.

## Transport Agnostic Communication

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621140%2F09_-_002_-_MCP_Clients_01.1748621139846.png)

But you're not limited to that approach. MCP clients and servers can also connect over:

- HTTP
- WebSockets
- Various other network protocols

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621140%2F09_-_002_-_MCP_Clients_03.1748621140776.png)

## Message Types

Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621141%2F09_-_002_-_MCP_Clients_04.1748621141280.png)

ListToolsRequest/ListToolsResult: The client asks the server "what tools do you provide?" and gets back a complete list of available functionality.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621142%2F09_-_002_-_MCP_Clients_05.1748621141878.png)

CallToolRequest/CallToolResult: The client tells the server "run this specific tool with these arguments" and receives the execution results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621142%2F09_-_002_-_MCP_Clients_06.1748621142450.png)

## Real-World Example Flow

Let's walk through a complete example to see how all these pieces work together. Imagine a user asks "What repositories do I have?" - here's the entire communication chain:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621143%2F09_-_002_-_MCP_Clients_08.1748621143061.png)

The process starts when a user submits their question to your server. Your server realizes it needs to provide Claude with available tools before making the AI request.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621143%2F09_-_002_-_MCP_Clients_09.1748621143612.png)

Your server asks the MCP client for a tool list, which triggers a ListToolsRequest to the MCP server. The server responds with ListToolsResult containing all available tools.

```
ListToolsRequest
```

```
ListToolsResult
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621144%2F09_-_002_-_MCP_Clients_11.1748621144300.png)

Now your server has everything needed to make the initial Claude request: the user's question plus the available tools. Claude analyzes the tools and decides it needs to call one to answer the question properly.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621145%2F09_-_002_-_MCP_Clients_12.1748621144842.png)

Claude responds with a tool use request. Your server recognizes this and asks the MCP client to execute the tool with Claude's specified arguments.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621145%2F09_-_002_-_MCP_Clients_13.1748621145569.png)

The MCP client sends a CallToolRequest to the MCP server, which then makes the actual API call to GitHub to fetch the user's repositories.

```
CallToolRequest
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621147%2F09_-_002_-_MCP_Clients_15.1748621147033.png)

GitHub returns the repository data, which the MCP server wraps in a CallToolResult and sends back through the chain. Your server receives this data and can now make a follow-up request to Claude.

```
CallToolResult
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621148%2F09_-_002_-_MCP_Clients_16.1748621147911.png)

The final step sends the tool results to Claude as part of a user message. Claude now has all the information needed to formulate a complete response about the user's repositories.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621148%2F09_-_002_-_MCP_Clients_18.1748621148672.png)

Yes, this flow involves many steps, but understanding it prepares you for implementing your own MCP clients and servers. Each component has a specific role, and the standardized message types ensure everything works together smoothly regardless of the underlying transport mechanism.

---

## Project setup

> https://anthropic.skilljar.com/claude-with-google-vertex/289199

details

2
                                    download

## Project setup

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

We're going to build a CLI-based chatbot that demonstrates how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.

## What We're Building

Our chatbot will allow users to interact with a collection of documents through natural language. The system consists of two main components:

- An MCP client that handles user interactions and communicates with Claude
- An MCP server that provides tools for reading and updating documents

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621130%2F09_-_003_-_Project_Setup_04.1748621130536.png)

The server will expose two tools to Claude:

- Tool to read a document's contents
- Tool to update a document's contents
All documents are stored in memory for simplicity - they include files like document.pdf, spreadsheet.xlsx, report.txt, and spec.md.

## Important Architecture Note

In real-world projects, you typically implement either an MCP client or an MCP server, not both. You might build:

- Just an MCP server to expose your service's capabilities to AI models
- Just an MCP client to connect to existing MCP servers built by other developers

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621131%2F09_-_003_-_Project_Setup_07.1748621131329.png)

We're building both components in this project purely for educational purposes - to understand how they communicate and work together.

## Project Setup

Download the CLI_project.zip file attached to this video and extract it to your preferred development directory. Open your code editor in the project folder.

## Configuration

The project includes a README.md file with detailed setup instructions. You'll need to:

- Add your Anthropic API key to the .env file
- Install dependencies using either UV (recommended) or pip

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621132%2F09_-_003_-_Project_Setup_14.1748621131900.png)

The .env file should contain:

```
ANTHROPIC_API_KEY="your-api-key-here"
```

```
ANTHROPIC_API_KEY="your-api-key-here"
```

## Running the Project

Once setup is complete, navigate to your project directory in the terminal and run:

```
# If using UV (recommended)
uv run main.py

# If using standard Python
python main.py
```

```
# If using UV (recommended)
uv run main.py

# If using standard Python
python main.py
```

You should see a chat prompt appear. Test it by asking a simple question like "what's 1+1?" to verify everything is working correctly.

The starter project already includes basic chat functionality with Claude. In the following videos, we'll add MCP server capabilities and document management features to create a fully functional document-aware chatbot.

#### Downloads

- cli_project.zip
                                                (opens in new tab)
- cli_project_COMPLETE.zip
                                                (opens in new tab)

---

## Defining tools with MCP

> https://anthropic.skilljar.com/claude-with-google-vertex/289235

details

## Defining tools with MCP

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building an MCP server becomes much simpler when you use the official Python SDK. Instead of writing complex JSON schemas by hand, you can define tools with decorators and let the SDK handle the heavy lifting.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621145%2F09_-_004_-_Defining_Tools_with_MCP_00.1748621145257.png)

In this example, we're creating a document management server with two core tools: one to read documents and another to update them. All documents exist in memory as a simple dictionary where keys are document IDs and values are the content.

## Setting Up the MCP Server

The Python MCP SDK makes server creation straightforward. You can initialize a server with just one line:

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")
```

```
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", log_level="ERROR")
```

This creates a fully functional MCP server that can handle tool definitions, client connections, and message routing.

## Tool Definition with Decorators

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621146%2F09_-_004_-_Defining_Tools_with_MCP_05.1748621146306.png)

The SDK's decorator approach eliminates the need for manual JSON schema writing. Here's how you define a simple tool:

```
@mcp.tool(
    name="add_ints",
    description="Add two integers together",
)
def tool_fn(
    a=Field(description="First number to add"),
    b=Field(description="Second number to add"),
) -> int:
    return a + b
```

```
@mcp.tool(
    name="add_ints",
    description="Add two integers together",
)
def tool_fn(
    a=Field(description="First number to add"),
    b=Field(description="Second number to add"),
) -> int:
    return a + b
```

Behind the scenes, MCP generates the complete tool schema that Claude needs to understand when and how to use your tool.

## Building the Document Reader Tool

The first tool reads document contents by ID. It takes a document identifier and returns the corresponding content from our in-memory dictionary:

```
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]
```

```
@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string."
)
def read_document(
    doc_id: str = Field(description="Id of the document to read")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    return docs[doc_id]
```

The function includes basic error handling to catch requests for non-existent documents. When Claude calls this tool with a valid document ID, it receives the full document content as a string.

## Creating the Document Editor Tool

The second tool performs simple find-and-replace operations on documents. It requires three parameters: the document ID, the text to find, and the replacement text:

```
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including white space."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
```

```
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including white space."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
```

This implementation uses Python's built-in string replace method, which requires exact matches including whitespace. The tool modifies the document in place within our dictionary.

## Key Benefits of the SDK Approach

- No manual JSON schema writing required
- Type hints provide automatic parameter validation
- Field descriptions help Claude understand tool usage
- Error handling integrates naturally with Python exceptions
- Tool registration happens automatically through decorators
The MCP Python SDK transforms tool creation from a complex schema-writing exercise into straightforward Python function definitions. Your tools become more maintainable and easier to test, while Claude gets all the metadata it needs to use them effectively.

---

## The server inspector

> https://anthropic.skilljar.com/claude-with-google-vertex/289207

details

## The server inspector

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building MCP servers, you need a way to test your functionality without connecting to a full application. The Python MCP SDK includes a built-in browser-based inspector that lets you debug and test your server in real-time.

## Starting the Inspector

First, make sure your Python environment is activated (check your project's README for the exact command). Then run the inspector with:

```
mcp dev mcp_server.py
```

```
mcp dev mcp_server.py
```

This starts a development server and gives you a local URL (typically on port 6277) to access the inspector in your browser.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621191%2F09_-_005_-_The_Server_Inspector_04.1748621191338.png)

## Using the Inspector Interface

The MCP inspector is actively being developed, so the interface may look different when you use it. However, the core functionality remains consistent.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621192%2F09_-_005_-_The_Server_Inspector_05.1748621192207.png)

After clicking "Connect" to start your MCP server, you'll see a navigation bar with sections for:

- Resources
- Prompts
- Tools
- Other server capabilities

## Testing Your Tools

The Tools section is where you'll spend most of your debugging time. Click "List Tools" to see all the tools your server provides.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621193%2F09_-_005_-_The_Server_Inspector_09.1748621192855.png)

When you select a tool, the right panel shows its details and provides input fields for testing. For example, to test the read_doc_contents tool:

```
read_doc_contents
```

- Select the tool from the list
- Enter a document ID (like "deposition.md")
- Click "Run Tool"
- Check the results for success and expected output

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621193%2F09_-_005_-_The_Server_Inspector_10.1748621193404.png)

## Testing Tool Interactions

You can test multiple tools in sequence to verify they work together correctly. For instance, after using the edit_document tool to modify content:

```
edit_document
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621194%2F09_-_005_-_The_Server_Inspector_16.1748621194137.png)

Run the read_doc_contents tool again with the same document ID to confirm your changes were applied:

```
read_doc_contents
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621195%2F09_-_005_-_The_Server_Inspector_17.1748621195581.png)

## Development Workflow

The inspector creates an efficient development loop:

- Make changes to your MCP server code
- Test individual tools with various inputs
- Verify tool interactions work as expected
- Debug issues without needing a full application setup
This browser-based testing environment is essential for MCP server development. It saves time by letting you catch issues early and verify functionality before integrating with Claude or other applications.

---

## Implementing a client

> https://anthropic.skilljar.com/claude-with-google-vertex/289206

details

## Implementing a client

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we have our MCP server working, it's time to build the client side. The client is what allows our application to communicate with the MCP server and access its functionality.

## Understanding the Client Architecture

Before diving into the code, let's clarify an important point about MCP projects. Normally, you'd implement either an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621199%2F09_-_006_-_Implementing_a_Client_01.1748621199062.png)

The MCP client consists of two main components:

- MCP Client - A custom class we create to make using the session easier
- Client Session - The actual connection to the server (part of the MCP Python SDK)

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621199%2F09_-_006_-_Implementing_a_Client_02.1748621199655.png)

The client session requires resource cleanup when we're done with it, which is why we wrap it in our custom class. This handles connection management and cleanup automatically.

## How the Client Fits Into Our Application

Remember our application flow? Our CLI code needs to interact with Claude in two key ways:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621201%2F09_-_006_-_Implementing_a_Client_06.1748621201283.png)

The client enables both of these interactions by exposing the server's functionality to our codebase.

## Implementing Core Client Functions

We need to implement two essential functions: list_tools and call_tool.

```
list_tools
```

```
call_tool
```

### List Tools Function

This function gets all available tools from the server:

```
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

```
async def list_tools(self) -> list[types.Tool]:
    result = await self.session().list_tools()
    return result.tools
```

It's straightforward - we access our session (the connection to the MCP server), call the built-in list_tools function, and return the tools from the result.

```
list_tools
```

### Call Tool Function

This function executes a specific tool on the server:

```
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

```
async def call_tool(
    self, tool_name: str, tool_input: dict
) -> types.CallToolResult | None:
    return await self.session().call_tool(tool_name, tool_input)
```

We pass the tool name and input parameters (provided by Claude) to the server and return the result.

## Testing the Client

To verify our implementation works, we can test it directly. The client file includes a testing harness that connects to the MCP server and runs commands against it.

Running uv run mcp_client.py should return a list of available tools with their descriptions and input schemas. You should see tools like read_doc_contents and edit_document that we defined in our server.

```
uv run mcp_client.py
```

```
read_doc_contents
```

```
edit_document
```

## End-to-End Testing

Now that both the client and server are working, we can test the complete flow. Running our main application and asking Claude "What is the contents of the report.pdf document?" should:

- Send the list of available tools to Claude
- Claude decides to use the read_doc_contents tool

```
read_doc_contents
```

- Our client calls the tool on the server
- The server returns the document contents
- Claude responds with the information
The client acts as the bridge between your application code and the MCP server, making it easy to access server functionality without dealing with the low-level connection details directly.

---

## Defining resources

> https://anthropic.skilljar.com/claude-with-google-vertex/289248

details

## Defining resources

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

## Understanding Resources

Think of resources as read-only endpoints that can return any type of data - strings, JSON, binary files, etc. You set a 'mime_type' to give the client a hint about what kind of data you're returning.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621200%2F09_-_007_-_Defining_Resources_04.1748621200061.png)

Resources work by defining a URI (like a URL) that clients can request. When a client needs data, it sends a ReadResourceRequest with the specific URI, and your server responds with a ReadResourceResult containing the data.

## Two Types of Resources

There are two main types of resources you can create:

- Direct Resources - Have static URIs that don't contain any parameters (like "docs://documents")
- Templated Resources - Include parameters in their URIs that get parsed and passed to your function (like "docs://documents/{doc_id}")

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621201%2F09_-_007_-_Defining_Resources_07.1748621201191.png)

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function. The parameter names in the URI must match your function's parameter names exactly.

## Creating Resources

Here's how to implement both types of resources:

```
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

```
@mcp.resource(
    "docs://documents",
    mime_type="application/json"
)
def list_docs() -> list[str]:
    return list(docs.keys())

@mcp.resource(
    "docs://documents/{doc_id}",
    mime_type="text/plain"
)
def fetch_doc(doc_id: str) -> str:
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    return docs[doc_id]
```

The MCP Python SDK automatically serializes whatever you return. You don't need to manually convert data to JSON strings - just return Python objects and the SDK handles the conversion.

## Testing Your Resources

You can test resources using the MCP Inspector. Start your server with:

```
uv run mcp dev mcp_server.py
```

Then connect to the inspector in your browser. You'll see two sections:

- Resources - Lists your direct/static resources
- Resource Templates - Shows your templated resources

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621202%2F09_-_007_-_Defining_Resources_18.1748621201948.png)

Click on any resource to test it. For templated resources, you'll need to provide values for the parameters. The inspector shows you the exact response structure your client will receive, including the mime type and serialized data.

## Practical Use Cases

Resources are ideal for implementing features like document mentions in chat applications. For example, when a user types "@" to mention a document, you could:

- Use a direct resource to fetch a list of all available documents for autocomplete
- Use a templated resource to fetch the contents of a specific document when mentioned
This approach lets you preemptively inject document content into prompts without requiring the AI to use tools to fetch the information.

---

## Accessing resources

> https://anthropic.skilljar.com/claude-with-google-vertex/289247

details

## Accessing resources

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Resources in MCP allow your server to expose data that can be directly included in prompts, rather than requiring tool calls to access information. This creates a more efficient way to provide context to AI models like Claude.

## Understanding the Resource Flow

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621196%2F09_-_008_-_Accessing_Resources_00.1748621196428.png)

When a user wants to access resource content, the flow works like this:

- User requests information about a resource (like "@report.pdf")
- Your code needs a list of document names for autocomplete
- MCP Client sends a ReadResourceRequest to the MCP Server
- Server responds with a ReadResourceResult containing the resource data
- Your code can then put this data directly into prompts

## Implementing Resource Reading

To read resources from your MCP client, you'll need to implement a read_resource function. First, add the necessary imports:

```
read_resource
```

```
import json
from pydantic import AnyUrl
```

```
import json
from pydantic import AnyUrl
```

The core function makes a request to your MCP session and processes the response:

```
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
```

```
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
```

## Handling Different Resource Types

Resources can return different types of content, so you need to check the MIME type and parse accordingly:

```
if isinstance(resource, types.TextResourceContents):
    if resource.mimeType == "application/json":
        return json.loads(resource.text)
    
    return resource.text
```

```
if isinstance(resource, types.TextResourceContents):
    if resource.mimeType == "application/json":
        return json.loads(resource.text)
    
    return resource.text
```

This approach handles two main scenarios:

- JSON resources that need parsing
- Plain text resources that can be returned as-is

## Testing Resource Access

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621197%2F09_-_008_-_Accessing_Resources_09.1748621197182.png)

You can verify your resource implementation works by testing it in your application. When you type "@" followed by a resource name, you should see an autocomplete list of available resources. Selecting one will include its contents directly in your prompt.

The key advantage of this approach is efficiency - Claude receives the document content immediately without needing to make additional tool calls to access the information.

## Resource vs Tool Usage

Resources are particularly useful when:

- You have static or semi-static content that's frequently referenced
- You want to reduce the number of API calls
- The content should be immediately available in the prompt context
This differs from tools, which are better for dynamic operations or when you need the AI to decide whether to access certain information based on the conversation context.

---

## Defining prompts

> https://anthropic.skilljar.com/claude-with-google-vertex/289249

details

## Defining prompts

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompts in MCP servers let you define pre-built, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of them as carefully crafted templates that give better results than what users might come up with on their own.

## Why Use Prompts?

Let's say you want Claude to reformat a document into markdown. A user could just type "convert report.pdf to markdown" and get decent results. But they'd probably get much better output if they used a thoroughly tested, specialized prompt that you've designed specifically for document formatting.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621250%2F09_-_009_-_Defining_Prompts_07.1748621249977.png)

The key insight is that while users can accomplish these tasks on their own, they'll get superior results when using prompts that have been carefully engineered and tested by the MCP server authors.

## How Prompts Work

Prompts define a set of user and assistant messages that clients can use directly. When a client requests a prompt, your server returns a list of messages that can be sent straight to Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621251%2F09_-_009_-_Defining_Prompts_09.1748621251776.png)

The basic structure looks like this:

```
@mcp.prompt(
    name="format",
    description="Rewrites the contents of a document in Markdown format",
)
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    # Return a list of messages
```

```
@mcp.prompt(
    name="format",
    description="Rewrites the contents of a document in Markdown format",
)
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    # Return a list of messages
```

## Building a Format Command

Here's a practical example. We'll create a format command that lets users type /format doc_id to reformat any document into markdown syntax.

```
/format doc_id
```

The prompt implementation includes detailed instructions for Claude:

```
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""
    
    return [
        base.UserMessage(prompt)
    ]
```

```
def format_document(
    doc_id: str = Field(description="Id of the document to format"),
) -> list[base.Message]:
    prompt = f"""
Your goal is to reformat a document to be written with markdown syntax.

The id of the document you need to reformat is:

{doc_id}

Add in headers, bullet points, tables, etc as necessary. Feel free to add in structure.
Use the 'edit_document' tool to edit the document. After the document has been reformatted...
"""
    
    return [
        base.UserMessage(prompt)
    ]
```

## Testing Your Prompts

You can test prompts using the MCP Inspector. Navigate to the Prompts tab, select your prompt, and provide any required parameters.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621253%2F09_-_009_-_Defining_Prompts_18.1748621252474.png)

The inspector shows you exactly what messages will be sent to Claude, including how any parameters get interpolated into the prompt text.

## Key Benefits

- Quality control - You can test and refine prompts before users see them
- Consistency - Users get reliable results every time
- Specialization - Prompts can be tailored to your server's specific domain
- Reusability - Multiple clients can use the same well-crafted prompts

## Implementation Details

Don't forget to import the base module for message types:

```
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
```

```
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
```

Prompts should be high quality, well-tested, and relevant to your MCP server's overall purpose. In our document management example, formatting prompts make perfect sense since the server specializes in document operations.

---

## Prompts in the client

> https://anthropic.skilljar.com/claude-with-google-vertex/289209

details

## Prompts in the client

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The final step in building our MCP client is implementing prompt functionality. This allows us to list all available prompts from the server and retrieve specific prompts with variables interpolated into them.

## Implementing List Prompts

The list_prompts method is straightforward. We call the session's list prompts method and return the prompts:

```
list_prompts
```

```
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

```
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

## Getting Individual Prompts

The get_prompt method is more interesting because it handles argument interpolation. When we request a specific prompt, we pass arguments that get injected into the prompt function. For example, if our server has a "format" prompt that expects a doc_id parameter, we provide that value in the arguments dictionary:

```
get_prompt
```

```
doc_id
```

```
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

```
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

The method returns messages that form a conversation ready to be fed directly into Claude.

## How Prompt Arguments Work

When you define a prompt function in your MCP server, any parameters become available as interpolation variables. The arguments dictionary you pass to get_prompt provides values for these parameters. The server then generates the complete prompt with your values substituted in the appropriate places.

```
get_prompt
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621239%2F09_-_010_-_Prompts_in_the_Client_04.1748621239421.png)

## Testing the Implementation

Once implemented, you can test prompts through the CLI. When you type a forward slash, available prompts appear as commands. Selecting a prompt like "format" will prompt you to choose values for any required arguments (like selecting a document to format). The system then:

- Retrieves the prompt with your arguments interpolated
- Sends the complete prompt to Claude
- Claude executes any necessary tool calls to fulfill the request
- Returns the formatted result

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621240%2F09_-_010_-_Prompts_in_the_Client_17.1748621240459.png)

## Prompts in Practice

Prompts define reusable sets of user and assistant messages that clients can invoke. They should be high-quality, well-tested, and relevant to your MCP server's purpose. Think of them as pre-built workflows that combine your server's tools and resources to accomplish specific tasks.

The prompt system creates a clean separation between the prompt logic (defined on the server) and the execution (handled by the client and Claude). This makes it easy to create sophisticated, multi-step workflows that users can trigger with simple commands.

---

## MCP review

> https://anthropic.skilljar.com/claude-with-google-vertex/289205

details

## MCP review

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we've built our MCP server, let's review the three core primitives and understand when to use each one. The key insight is understanding who controls each primitive and what purpose they serve in your application.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621244%2F09_-_011_-_MCP_Review_00.1748621244563.png)

## Tools: Model-Controlled

Tools are controlled entirely by Claude. The AI model decides when to call these functions, and the results are used directly by Claude to accomplish tasks.

Use tools when you want to give Claude additional capabilities. For example, if you ask Claude to calculate the square root of 3 using JavaScript, Claude will automatically decide to use a JavaScript execution tool to provide an accurate answer.

## Resources: App-Controlled

Resources are controlled by your application code. Your app decides when to fetch resource data and how to use it, typically for UI purposes or to add context to conversations.

Use resources when you need to get data into your app. Common examples include:

- Populating autocomplete options in your UI
- Adding context to messages before sending them to Claude
- Displaying lists of available documents or files
In our project, we used resources to fetch autocomplete suggestions and to augment prompts with additional context.

## Prompts: User-Controlled

Prompts are triggered by user actions. Users decide when to run these predefined workflows through UI interactions like button clicks, menu selections, or slash commands.

Use prompts for workflows that users should be able to trigger on demand. These are perfect for:

- Predefined conversation starters
- Common task templates
- Specialized workflows optimized for specific use cases

## Real-World Examples

You can see all three primitives in action on Claude's official interface. The conversation starter buttons below the chat input are examples of prompts - user-controlled workflows that begin predefined interactions.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621245%2F09_-_011_-_MCP_Review_13.1748621245385.png)

The "Add from Google Drive" option demonstrates resources in action. When you click this button, the application fetches a list of your documents and displays them in the UI. This is app-controlled behavior that serves the interface.

When you ask Claude to perform calculations or execute code, you're seeing tools at work. Claude automatically decides to use available tools like JavaScript execution to provide accurate results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748621246%2F09_-_011_-_MCP_Review_17.1748621245824.png)

## Choosing the Right Primitive

Here's a quick decision guide:

- Need to extend Claude's capabilities? Use tools
- Need data for your app's UI or context? Use resources
- Want to offer predefined workflows to users? Use prompts
Remember, these are high-level guidelines to help you choose the right approach for your specific needs. Each primitive serves a different part of your application ecosystem - tools serve the model, resources serve your app, and prompts serve your users.

---

## Quiz on Model Context Protocol

> https://anthropic.skilljar.com/claude-with-google-vertex/289276

## Quiz on Model Context Protocol

# Quiz on Model Context Protocol

---

## Anthropic apps

> https://anthropic.skilljar.com/claude-with-google-vertex/289230

## Anthropic apps

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Claude Code setup

> https://anthropic.skilljar.com/claude-with-google-vertex/289232

## Claude Code setup

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Claude Code in action

> https://anthropic.skilljar.com/claude-with-google-vertex/289246

details

1
                                    download

## Claude Code in action

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Downloads

- app_starter.zip
                                                (opens in new tab)

---

## Enhancements with MCP servers

> https://anthropic.skilljar.com/claude-with-google-vertex/289231

## Enhancements with MCP servers

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Parallelizing Claude Code

> https://anthropic.skilljar.com/claude-with-google-vertex/289241

## Parallelizing Claude Code

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Automated debugging

> https://anthropic.skilljar.com/claude-with-google-vertex/289238

## Automated debugging

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Computer use

> https://anthropic.skilljar.com/claude-with-google-vertex/289233

## Computer use

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## How computer use works

> https://anthropic.skilljar.com/claude-with-google-vertex/289234

*(load error)*

---

## Agents and workflows

> https://anthropic.skilljar.com/claude-with-google-vertex/289244

*(load error)*

---

## Parallelization workflows

> https://anthropic.skilljar.com/claude-with-google-vertex/289236

*(load error)*

---

## Chaining workflows

> https://anthropic.skilljar.com/claude-with-google-vertex/289239

*(load error)*

---

## Routing workflows

> https://anthropic.skilljar.com/claude-with-google-vertex/289242

*(load error)*

---

## Agents and tools

> https://anthropic.skilljar.com/claude-with-google-vertex/289243

*(load error)*

---

## Environment inspection

> https://anthropic.skilljar.com/claude-with-google-vertex/289237

*(load error)*

---

## Workflows vs agents

> https://anthropic.skilljar.com/claude-with-google-vertex/289245

*(load error)*

---

## Quiz on agents and workflows

> https://anthropic.skilljar.com/claude-with-google-vertex/289274

*(load error)*

---

## Final assessment quiz

> https://anthropic.skilljar.com/claude-with-google-vertex/290880

*(load error)*

---

## Course Wrap Up

> https://anthropic.skilljar.com/claude-with-google-vertex/289240

*(load error)*