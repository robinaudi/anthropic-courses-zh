# Claude with Amazon Bedrock

> Source: https://anthropic.skilljar.com/claude-in-amazon-bedrock


---

## My Profile

> https://anthropic.skilljar.com/accounts/profile/?next=/claude-in-amazon-bedrock

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

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/resume

## Course wrap up

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Introduction to the course

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/241929

details

## Introduction to the course

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Welcome to the course! This module will help you:

- Understand the course structure and learning path
- Identify the key skills and knowledge areas covered in the course
- Recognize the intended audience and assess personal readiness for the course

---

## Overview of Claude Models

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/303332

details

## Overview of Claude Models

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude offers three distinct model families, each optimized for different priorities. All three models share Claude's core capabilities - they can handle text generation, coding, image analysis, and other tasks. The key difference is how they balance intelligence, speed, and cost.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1750971508%2F02_-_001_-_Overview_of_Claude_Models_02.1750971508481.png)

## Claude Opus

Opus delivers Claude's highest level of intelligence. It's designed for complex scenarios that require sophisticated reasoning and planning capabilities.

Opus excels at working independently on complex projects for extended periods. It can manage multi-step processes and navigate different requirements without much human intervention. The model supports reasoning, meaning it can provide quick responses for simple tasks or spend time thinking through more complex problems.

The trade-off is moderate latency and higher cost. You're paying more and waiting longer for that extra intelligence.

## Claude Sonnet

Sonnet sits in the sweet spot of Claude's lineup, offering a balanced combination of intelligence, speed, and cost that works well for most practical applications.

What makes Sonnet particularly valuable is its strong coding ability combined with fast text generation. Many developers appreciate its ability to make precise edits to complex codebases without breaking existing functionality.

## Claude Haiku

Haiku is Claude's fastest model, built specifically for applications where response time is critical. It's optimized for speed and cost efficiency rather than maximum intelligence.

One important limitation: Haiku doesn't support the reasoning capabilities that Opus and Sonnet offer. This makes it ideal for user-facing applications that need real-time interactions but less suitable for complex problem-solving tasks.

## Choosing the Right Model

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1750971509%2F02_-_001_-_Overview_of_Claude_Models_12.1750971509142.png)

Model selection comes down to understanding the trade-offs between intelligence and cost/speed. Here's how to decide:

- Choose Opus when intelligence is your top priority. If you have complex tasks requiring strong reasoning capabilities, you're choosing quality over speed and cost.
- Choose Haiku when speed matters most. For real-time user interactions or high-volume processing where you need the fastest possible responses.
- Choose Sonnet when you need balance. Most applications benefit from Sonnet's combination of intelligence, speed, and reasonable cost.

## Using Multiple Models

Many teams don't stick to just one model. Instead, they use different models for different parts of the same application:

- Haiku for user-facing interactions where speed is crucial
- Sonnet for main business logic
- Opus for complex tasks requiring deeper reasoning
This approach lets you optimize each part of your application for its specific requirements while managing overall costs and performance.

---

## Accessing the API

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276716

details

## Accessing the API

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building applications with AI models, you need to understand the flow of data from user input to AI-generated response. Let's walk through how this works with AWS Bedrock and see what happens behind the scenes of a typical chat application.

## How Chat Applications Work

Imagine you're building a web app with a simple chat interface. A user types "Define quantum computing" and clicks send. Here's what actually happens:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557570%2F05_-_001_-_Accessing_the_API_02.1748557570066.png)

The user sees a clean interface, but there's a whole system working behind the scenes to generate that response.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557570%2F05_-_001_-_Accessing_the_API_03.1748557570599.png)

## The Request Flow

When a user submits text, here's the journey that message takes:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557571%2F05_-_001_-_Accessing_the_API_04.1748557571285.png)

- User submits their message through your web interface
- Your server receives the request containing that text
- Your server uses the Bedrock client to make a request to AWS Bedrock
- The request includes the user message and a model ID (like Claude Haiku or Claude Sonnet)
- The chosen model processes the request and generates text
- AWS Bedrock sends back an assistant message containing the generated response
- Your server forwards this response back to the user's browser

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557572%2F05_-_001_-_Accessing_the_API_08.1748557571907.png)

---

## Making a request

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276719

details

2
                                    download

## Making a request

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Making your first API request to AWS Bedrock requires three essential components: a Bedrock Runtime Client to connect to the service, a Model ID to specify which model you want to run, and a User Message containing the text you want to feed into the model.

## Setting Up the Bedrock Client

Start by creating a client using boto3 to connect to the Bedrock runtime service:

```
import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")
```

```
import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")
```

## Understanding Model IDs and Regional Availability

Here's where things get tricky. Not every model is available in every AWS region. If you try to run a model that doesn't exist in your chosen region, you'll get a cryptic error message saying the model doesn't exist.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557580%2F05_-_002_-_Making_a_Request_04.1748557580294.png)

For example, if Claude Sonnet is available in us-west-2 but you're making requests from us-east-1, your request will fail.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557581%2F05_-_002_-_Making_a_Request_05.1748557580814.png)

## Using Inference Profiles

Inference profiles solve the regional availability problem by automatically routing your requests to a region where your chosen model is actually hosted.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557581%2F05_-_002_-_Making_a_Request_06.1748557581635.png)

Instead of tracking which models are in which regions, you can use an inference profile that knows the model is available in multiple regions like us-west-2 and us-east-2.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557582%2F05_-_002_-_Making_a_Request_07.1748557582083.png)

When you make a request using an inference profile, AWS automatically routes it to the correct region where your model exists, even if you're connecting from a different region.

To find inference profile IDs, go to the AWS Bedrock console and look under "Cross-region inference" rather than using the model ID from the main model catalog page.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557583%2F05_-_002_-_Making_a_Request_10.1748557583183.png)

Copy the inference profile ID for your chosen model.

## Creating User Messages

User messages have a specific structure that might look overly complex at first, but there's a good reason for it:

```
user_message = {
    "role": "user",
    "content": [
        {"text": "What's 1+1?"}
    ]
}
```

```
user_message = {
    "role": "user",
    "content": [
        {"text": "What's 1+1?"}
    ]
}
```

The content is a list because a single message can contain different types of content - text, images, or other media types. This structure allows you to send multimodal requests.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557584%2F05_-_002_-_Making_a_Request_18.1748557583888.png)

## Making the Request

Now you can make your API call using the converse method:

```
response = client.converse(
    modelId=model_id,
    messages=[user_message]
)
```

```
response = client.converse(
    modelId=model_id,
    messages=[user_message]
)
```

The response contains a lot of metadata, but to get just the generated text, you need to navigate through the response structure:

```
response["output"]["message"]["content"][0]["text"]
```

```
response["output"]["message"]["content"][0]["text"]
```

## Understanding Message Types

There are two main message types you'll work with:

- User messages - Content you want to feed into the model (role: "user")
- Assistant messages - Content the model has produced (role: "assistant")

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557584%2F05_-_002_-_Making_a_Request_17.1748557584391.png)

Both message types follow the same structure with a role and content list. This consistency makes it easy to build conversations by alternating between user and assistant messages.

The assistant message you get back from Bedrock follows the exact same format as your user message, just with a different role. This standardized structure makes it straightforward to chain multiple requests together for longer conversations.

#### Downloads

- 001_Api_Requests.ipynb
                                                (opens in new tab)
- 001_Api_Requests_complete.ipynb
                                                (opens in new tab)

---

## Multi-Turn conversations

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276722

details

## Multi-Turn conversations

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The code we've written so far simulates a very simple exchange with Claude. But what happens when you want to continue a conversation? When you ask a follow-up question like "And 3 more?" after asking "What's 1+1?", you might expect Claude to understand you're asking about adding 3 to the previous result of 2.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557630%2F05_-_003_-_Multi-Turn_Conversations_01.1748557630812.png)

However, there's something critical you need to understand about the Bedrock API and Claude itself.

## No Message Storage

Bedrock and Claude do not store any messages. None of the messages you send get stored, and none of the responses you receive are stored either. Each API call is completely independent.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557631%2F05_-_003_-_Multi-Turn_Conversations_02.1748557631276.png)

To have a conversation with multiple messages that maintain context, you need to:

- Manually maintain a list of all messages in your code
- Provide that entire list of messages with each follow-up request

## Why Context Matters

Let's see what happens without proper context. If you send just "And 3 more?" as a standalone message, Claude has no idea what you're referring to. It will do its best to respond, but the answer won't make sense because it lacks the context of your previous conversation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557631%2F05_-_003_-_Multi-Turn_Conversations_05.1748557631762.png)

When you send only the follow-up question, Claude sees just that isolated message and tries to respond without knowing about the previous "What's 1+1?" exchange.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557632%2F05_-_003_-_Multi-Turn_Conversations_06.1748557632283.png)

## Building Conversation Context

To maintain context, you need to include the full conversation history in each request. Here's how it works:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557633%2F05_-_003_-_Multi-Turn_Conversations_07.1748557632856.png)

Your message list should contain all previous exchanges - both user messages and assistant responses. When you send this complete context, Claude can understand that "And 3 more?" refers to adding 3 to the previous result of 2.

## Helper Functions for Message Management

To make conversation management easier, you can create helper functions:

```
def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [
            {"text": text}
        ]
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant", 
        "content": [
            {"text": text}
        ]
    }
    messages.append(assistant_message)

def chat(messages):
    response = client.converse(
        modelId=model_id,
        messages=messages
    )
    return response["output"]["message"]["content"][0]["text"]
```

```
def add_user_message(messages, text):
    user_message = {
        "role": "user",
        "content": [
            {"text": text}
        ]
    }
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {
        "role": "assistant", 
        "content": [
            {"text": text}
        ]
    }
    messages.append(assistant_message)

def chat(messages):
    response = client.converse(
        modelId=model_id,
        messages=messages
    )
    return response["output"]["message"]["content"][0]["text"]
```

## Implementing Multi-Turn Conversations

Here's how to build a conversation step by step:

```
# Make a starting list of messages
messages = []

# Add in the initial user question of "What's 1+1?"
add_user_message(messages, "What's 1+1?")

# Pass the list of messages into chat to get an answer
answer = chat(messages)

# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's followup question
add_user_message(messages, "And 3 more added to that?")

# Call chat again with the list of messages to get a final answer
answer = chat(messages)
print(answer)
```

```
# Make a starting list of messages
messages = []

# Add in the initial user question of "What's 1+1?"
add_user_message(messages, "What's 1+1?")

# Pass the list of messages into chat to get an answer
answer = chat(messages)

# Take the answer and add it as an assistant message into our list
add_assistant_message(messages, answer)

# Add in the user's followup question
add_user_message(messages, "And 3 more added to that?")

# Call chat again with the list of messages to get a final answer
answer = chat(messages)
print(answer)
```

This approach ensures Claude has the full context and can respond appropriately: "Starting with the result of 1+1 = 2, if we add 3 more to that, we get: 2 + 3 = 5"

## Message Role Alternation

When building your message list, always ensure that message roles alternate properly:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557633%2F05_-_003_-_Multi-Turn_Conversations_19.1748557633396.png)

Your conversation should follow the pattern: user → assistant → user → assistant. Never have two user messages in a row or two assistant messages in a row. This alternating pattern is required by the API and reflects natural conversation flow.

While this manual message management might seem tedious at first, you'll quickly get used to it. This pattern is fundamental to building any application that needs to maintain conversational context with Claude.

---

## Chat bot exercise

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276725

## Chat bot exercise

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## System prompts

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276726

details

2
                                    download

## System prompts

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building AI chatbots for specific use cases, you need a way to control how the AI responds. System prompts are the key to transforming a general-purpose AI into a specialized assistant that follows specific guidelines and stays on topic.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557628%2F05_-_005_-_System_Prompts_00.1748557628015.png)

## The Problem with User-Level Instructions

You might think the solution is to include all your requirements in the user message itself. For example, telling the AI in each conversation to "mention AWS services" and "don't mention competitors." This approach has serious limitations:

- You'd need to anticipate every possible question and edge case
- The instruction list becomes unwieldy and repetitive
- Users see all the internal instructions, making conversations cluttered
- Requirements change based on the specific question being asked

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557629%2F05_-_005_-_System_Prompts_05.1748557629207.png)

## System Prompts: A Better Approach

System prompts solve this problem by giving Claude a role to play. Instead of listing specific do's and don'ts, you tell Claude to act like a particular type of professional. The AI then responds as that person would naturally respond.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557629%2F05_-_005_-_System_Prompts_07.1748557629765.png)

System prompts provide several key benefits:

- Claude gets guidance on how to respond consistently
- The AI adopts the mindset and constraints of the specified role
- Responses stay focused and on-brand automatically
- You don't need to anticipate every possible scenario

## Implementing System Prompts

To add a system prompt to your Claude conversation, you pass it as a parameter to the converse function:

```
converse
```

```
system_prompt = """
You are an AWS cloud support specialist. Your job is to answer user queries related 
to cloud hosting services on AWS.
"""

response = client.converse(
    modelId=model_id, 
    messages=messages, 
    system=[{"text": system_prompt}]
)
```

```
system_prompt = """
You are an AWS cloud support specialist. Your job is to answer user queries related 
to cloud hosting services on AWS.
"""

response = client.converse(
    modelId=model_id, 
    messages=messages, 
    system=[{"text": system_prompt}]
)
```

The system prompt gets passed as a list containing a dictionary with a "text" key. This tells Claude what role to adopt before it sees any user messages.

## Building a Flexible Chat Function

Here's a reusable chat function that handles system prompts elegantly:

```
def chat(messages, system=None):
    params = {"modelId": model_id, "messages": messages}
    
    if system:
        params["system"] = [{"text": system}]
    
    response = client.converse(**params)
    
    return response["output"]["message"]["content"][0]["text"]
```

```
def chat(messages, system=None):
    params = {"modelId": model_id, "messages": messages}
    
    if system:
        params["system"] = [{"text": system}]
    
    response = client.converse(**params)
    
    return response["output"]["message"]["content"][0]["text"]
```

This approach lets you optionally include a system prompt. When no system prompt is provided, Claude responds as its default self. When you include one, Claude adopts that specific role.

## System Prompts in Action

The difference is immediately apparent when you test the same question with and without a system prompt. Ask "How do I host a Postgres database?" without a system prompt, and you'll get a comprehensive answer covering multiple cloud providers and self-hosting options.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557631%2F05_-_005_-_System_Prompts_11.1748557630855.png)

With an AWS support specialist system prompt, the response focuses exclusively on AWS solutions like RDS, Aurora, and EC2-based deployments. No competitors mentioned, and the answer includes AWS-specific setup steps.

Even more impressive is how system prompts handle off-topic questions. Ask for a bread recipe with the AWS specialist prompt active, and Claude politely declines while staying in character:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557631%2F05_-_005_-_System_Prompts_15.1748557631341.png)

## Important Technical Details

When working with system prompts, keep these requirements in mind:

- System prompts cannot be empty strings - they must contain at least one character
- The system parameter expects a list of dictionaries with "text" keys
- System prompts are processed before any user messages in the conversation
- You can update the system prompt between conversations, but not mid-conversation
System prompts give you powerful control over AI behavior without complex rule systems. By assigning Claude a specific professional role, you get consistent, appropriate responses that naturally follow the constraints and expertise of that role.

#### Downloads

- 002_System_Messages.ipynb
                                                (opens in new tab)
- 002_System_Messages_complete.ipynb
                                                (opens in new tab)

---

## System prompt exercise

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276717

## System prompt exercise

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Temperature

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276720

details

## Temperature

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Temperature is a powerful parameter that controls how creative or deterministic Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications.

## How Claude Generates Text

Before diving into temperature, it's helpful to understand Claude's text generation process. When you send Claude a prompt like "What do you think?", it goes through three phases:

- Tokenization: Breaking your input into smaller chunks
- Prediction: Calculating probabilities for possible next tokens
- Sampling: Selecting a token based on those probabilities

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557675%2F05_-_007_-_Temperature_00.1748557675436.png)

In the diagram above, you can see how Claude might assign different probabilities to potential next tokens. The word "about" has a 30% chance, "would" has 20%, and so on. This process repeats for each token until the response is complete.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557676%2F05_-_007_-_Temperature_03.1748557675981.png)

## What Temperature Does

Temperature is a decimal value between 0 and 1 that directly influences these token selection probabilities. Think of it as a creativity dial:

- Low temperature (near 0): Makes the highest probability token much more likely to be selected
- High temperature (near 1): Distributes probability more evenly across all possible tokens

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557676%2F05_-_007_-_Temperature_05.1748557676662.png)

At temperature 0, Claude becomes deterministic - it will always pick the most probable token. At temperature 1, lower-probability tokens have a much better chance of being selected, leading to more creative and varied outputs.

## Temperature Ranges and Use Cases

Different tasks call for different temperature settings:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557677%2F05_-_007_-_Temperature_08.1748557677098.png)

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

## Setting Temperature in Code

By default, Claude's temperature is set to 1.0, which means maximum creativity. You can override this by adding temperature to your inference configuration:

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {"temperature": temperature}
    }
    
    if system:
        params["system"] = [{"text": system}]
    
    response = client.converse(**params)
    return response["output"]["message"]["content"][0]["text"]
```

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {"temperature": temperature}
    }
    
    if system:
        params["system"] = [{"text": system}]
    
    response = client.converse(**params)
    return response["output"]["message"]["content"][0]["text"]
```

## Temperature in Practice

Here's a practical example using movie idea generation. With temperature set to the default (1.0), you might get creative responses like:

"A reclusive origami master discovers her intricate paper creations come to life at night, leading her on a magical journey to save their miniature world from a mysterious shadow creature threatening to unfold their existence."

But when you set temperature to 0.0 for the same prompt, you'll consistently get more predictable responses:

"A time-traveling archaeologist must prevent ancient artifacts from being stolen by a tech billionaire who's using them to build a doomsday device that harnesses their forgotten power."

Running the low-temperature version multiple times will produce very similar responses, often with repeated themes like "time-traveling historian" or "time-traveling archaeologist."

## Key Takeaways

Temperature gives you direct control over Claude's creativity level. Use lower temperatures when you need consistent, factual responses, and higher temperatures when you want creative, varied outputs. The default temperature of 1.0 maximizes creativity, so consider lowering it for tasks requiring precision and consistency.

---

## Streaming

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276721

details

2
                                    download

## Streaming

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building chat interfaces with AI models, users expect to see responses appear immediately rather than waiting 10-30 seconds for a complete response. The converse_stream function solves this by streaming text as it's generated, creating a much better user experience.

```
converse_stream
```

## How Streaming Works

Instead of waiting for the entire response to be generated, streaming sends back pieces of text as soon as they're available. Here's how the flow changes:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557673%2F05_-_008_-_Streaming_03.1748557673079.png)

When you call converse_stream, you immediately get back an initial response that contains a stream object. This stream is a generator that yields events as the model generates text. Each event contains a small chunk of the overall response.

```
converse_stream
```

```
stream
```

## Basic Implementation

Here's how to use converse_stream in your code:

```
converse_stream
```

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")
response = client.converse_stream(messages=messages, modelId=model_id)

for event in response["stream"]:
    print(event)
```

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")
response = client.converse_stream(messages=messages, modelId=model_id)

for event in response["stream"]:
    print(event)
```

This will print out all the different events as they arrive. You'll see the response come in chunks rather than all at once.

## Understanding Stream Events

The stream yields several types of events, each serving a different purpose:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557673%2F05_-_008_-_Streaming_12.1748557673618.png)

For basic text generation, you only need to care about contentBlockDelta events. These contain the actual generated text chunks that you want to display to users.

```
contentBlockDelta
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557674%2F05_-_008_-_Streaming_15.1748557674330.png)

The events always arrive in a predictable order: messageStart, multiple contentBlockDelta events containing your text, then contentBlockStop, messageStop, and finally metadata.

```
messageStart
```

```
contentBlockDelta
```

```
contentBlockStop
```

```
messageStop
```

```
metadata
```

## Extracting the Text

To get just the generated text from each chunk, filter for contentBlockDelta events and extract the text:

```
contentBlockDelta
```

```
text = ""
for event in response["stream"]:
    if "contentBlockDelta" in event:
        chunk = event["contentBlockDelta"]["delta"]["text"]
        print(chunk, end="")
        text += chunk

print("\n\nTotal Message:\n" + text)
```

```
text = ""
for event in response["stream"]:
    if "contentBlockDelta" in event:
        chunk = event["contentBlockDelta"]["delta"]["text"]
        print(chunk, end="")
        text += chunk

print("\n\nTotal Message:\n" + text)
```

The end="" parameter removes the automatic newline that Python's print function adds, making the streaming text appear more naturally.

```
end=""
```

## Practical Applications

In a real application, instead of printing each chunk, you'd typically:

- Send each chunk to your frontend via WebSockets or Server-Sent Events
- Update the UI to display the growing response in real-time
- Store the complete message once streaming finishes
- Handle any errors that might occur during streaming
This streaming approach transforms the user experience from "submit and wait" to "submit and watch the response appear," making your AI-powered applications feel much more responsive and engaging.

#### Downloads

- 003_Streaming_complete.ipynb
                                                (opens in new tab)
- 003_Streaming.ipynb
                                                (opens in new tab)

---

## Controlling model output

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276723

details

2
                                    download

## Controlling model output

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Beyond crafting better prompts, there are two powerful techniques for controlling Claude's output: prefilled assistant messages and stop sequences. These methods give you precise control over how Claude responds and when it stops generating text.

## Prefilled Assistant Messages

Message prefilling lets you provide the beginning of Claude's response, which strongly influences the direction of its answer. Instead of letting Claude decide how to start its response, you give it a specific opening that steers the conversation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557716%2F05_-_009_-_Controlling_Model_Output_01.1748557716044.png)

Here's how it works: you build your normal list of messages with the user's question, but then add an assistant message at the end containing the start of the response you want. When Claude processes this, it sees the assistant message and thinks "I've already started responding to this question, so I should continue from where I left off."

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557716%2F05_-_009_-_Controlling_Model_Output_05.1748557716502.png)

For example, if you ask "Is tea or coffee better at breakfast?" and prefill with "Coffee is better because", Claude will continue from that point and build a response supporting coffee. The key insight is that Claude will pick up exactly where your prefilled text ends - it won't repeat what you've written.

Let's see this in practice:

```
messages = []
add_user_message(messages, "Is coffee or tea better for breakfast?")
add_assistant_message(messages, "Coffee is better because")

chat(messages)
```

```
messages = []
add_user_message(messages, "Is coffee or tea better for breakfast?")
add_assistant_message(messages, "Coffee is better because")

chat(messages)
```

This returns something like "it has more caffeine." Notice that Claude continues directly from your prefilled text, so you'll need to combine both parts to get the complete response: "Coffee is better because it has more caffeine."

You can steer Claude in any direction by changing your prefilled text:

- "Tea is better because" - pushes toward tea

```
"Tea is better because"
```

- "They are the same because" - creates a neutral response

```
"They are the same because"
```

## Stop Sequences

Stop sequences force Claude to end its response immediately when it generates specific text. This is useful when you want to truncate output at a particular point or prevent Claude from continuing past a certain marker.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557717%2F05_-_009_-_Controlling_Model_Output_14.1748557717103.png)

The concept is straightforward: you provide a list of strings, and as soon as Claude generates any of those strings, it stops and returns whatever it has generated so far. The stop sequence itself is not included in the response.

To use stop sequences, you need to modify your chat function to accept them as a parameter:

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {
            "temperature": temperature,
            "stopSequences": stop_sequences
        },
    }
```

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "modelId": model_id,
        "messages": messages,
        "inferenceConfig": {
            "temperature": temperature,
            "stopSequences": stop_sequences
        },
    }
```

Here's a practical example:

```
messages = []
add_user_message(messages, "Count from 1 to 10")

chat(messages, stop_sequences=["5"])
```

```
messages = []
add_user_message(messages, "Count from 1 to 10")

chat(messages, stop_sequences=["5"])
```

This returns "1, 2, 3, 4," and stops before including the "5". You can specify multiple stop sequences, and Claude will stop at whichever one it encounters first:

```
chat(messages, stop_sequences=["5", "3, 4"])
```

```
chat(messages, stop_sequences=["5", "3, 4"])
```

Stop sequences are particularly useful for:

- Controlling the length of responses
- Stopping at natural breakpoints in structured output
- Preventing Claude from continuing past specific markers or delimiters
Both techniques give you fine-grained control over Claude's behavior, allowing you to shape responses in ways that simple prompting alone cannot achieve.

#### Downloads

- 004_Controlling_Output_complete.ipynb
                                                (opens in new tab)
- 004_Controlling_Output.ipynb
                                                (opens in new tab)

---

## Structured data

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276724

details

## Structured data

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you need Claude to generate structured data like JSON, Python code, or bulleted lists, you'll often run into a common problem: Claude wants to be helpful and add explanatory text, headers, or markdown formatting around your content. This extra commentary breaks the user experience when you just need the raw data.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557719%2F05_-_010_-_Structured_Data_02.1748557719466.png)

Consider building a web app that generates AWS EventBridge rules. Users enter a description, click generate, and expect to see clean JSON they can immediately copy and use. If Claude returns the JSON wrapped in markdown code blocks with explanatory text, users can't simply copy the entire response - they have to manually select just the JSON portion.

## The Problem with Default Responses

By default, Claude tends to format structured output like this:

```
# EventBridge Rule
```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {"state": ["running"]}
}
```
This rule captures EC2 instance state changes when instances start running or stop.
```

```
# EventBridge Rule
```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {"state": ["running"]}
}
```
This rule captures EC2 instance state changes when instances start running or stop.
```

While this is great for documentation, it's problematic when you need just the JSON for programmatic use.

## The Solution: Assistant Message Prefilling + Stop Sequences

You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:

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

This technique works by:

- Prefilling the assistant message with the opening markdown delimiter
- Setting a stop sequence to halt generation when Claude tries to close the code block
- Capturing only the content between these delimiters

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557720%2F05_-_010_-_Structured_Data_15.1748557720007.png)

## How It Works Behind the Scenes

When Claude receives your request, it sees the prefilled assistant message and assumes it already started writing the JSON code block. Instead of adding its own header and opening delimiter, Claude jumps straight to generating the actual JSON content.

When Claude finishes the JSON and naturally wants to close the markdown code block with ```, the stop sequence immediately halts generation and returns the response. You get just the JSON content with no extra formatting.

```
```
```

## Processing the Results

The returned text might contain some newline characters, but you can easily clean this up:

```
import json

# Parse as JSON to validate and format
parsed_data = json.loads(text.strip())

# Or just strip whitespace for other data types
clean_text = text.strip()
```

```
import json

# Parse as JSON to validate and format
parsed_data = json.loads(text.strip())

# Or just strip whitespace for other data types
clean_text = text.strip()
```

## Beyond JSON

This technique isn't limited to JSON generation. You can use it for any structured data where you want just the content without Claude's natural tendency to add explanatory text:

- Python code snippets
- Bulleted lists
- CSV data
- Configuration files
- Any format where clean, copyable output matters
The key is identifying what delimiters Claude would naturally use around your content type, then prefilling the opening delimiter and stopping at the closing one. This gives you precise control over the output format while leveraging Claude's natural formatting instincts.

---

## Structured data exercise

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276718

## Structured data exercise

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Quiz on working with the API

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289293

## Quiz on working with the API

# Quiz on Working with the API

---

## Prompt evaluation

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276731

details

## Prompt evaluation

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques for crafting better prompts, while prompt evaluation helps you measure how well those prompts actually work.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557873%2F06_-_001_-_Prompt_Evaluation_00.1748557873297.png)

## Prompt Engineering vs Prompt Evaluation

Prompt engineering is your toolkit for writing and improving prompts. It's a set of best practices that help Claude understand exactly what you're asking for and how you want it to respond. Think of it as the craft of prompt writing - techniques like multishot prompting, structuring with XML tags, and many other approaches we'll explore.

Prompt evaluation, on the other hand, is about measurement. It's automated testing that gives you objective metrics on whether your prompts are actually effective. Instead of guessing if your prompt works well, evaluation lets you:

- Test against expected answers
- Compare different versions of the same prompt
- Review outputs for errors

## The Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557874%2F06_-_001_-_Prompt_Evaluation_10.1748557874098.png)

Option 1: Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

Option 2: Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, this approach still leaves you vulnerable because users will often provide very unexpected outputs that you haven't considered.

Option 3: Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective data. This requires more work and cost upfront, but gives you much more confidence in your prompt's reliability.

## Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are traps that all engineers fall into, myself included. It's natural to write a prompt for a serious application and not test it thoroughly enough. We tend to test with inputs that seem obvious to us, but real users will interact with your prompts in ways you never anticipated.

The solution is to embrace option 3: systematic evaluation. By running your prompts through proper evaluation pipelines, you get objective scores that tell you how well your prompt performs across a wide range of scenarios. This data-driven approach lets you iterate confidently and catch issues before they reach production.

Understanding evaluation first gives you the foundation to measure improvements as you apply prompt engineering techniques. Once you can reliably measure prompt effectiveness, you can experiment with different approaches and know definitively which ones work better.

---

## A typical eval workflow

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276732

details

## A typical eval workflow

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

A typical prompt evaluation workflow follows a systematic approach to objectively measure and improve your prompts. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557880%2F06_-_002_-_A_Typical_Eval_Workflow_00.1748557880270.png)

## Step 1: Draft Your Initial Prompt

Start by writing out a basic prompt that you want to improve. For this example, we'll use a simple prompt structure:

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

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557881%2F06_-_002_-_A_Typical_Eval_Workflow_04.1748557881459.png)

This gives us a baseline to work from. We won't know if it's effective until we evaluate it with some objective methodology.

## Step 2: Create an Evaluation Dataset

Your evaluation dataset contains sample inputs that you'll feed into your prompt. Since our prompt only has one input (the user's question), we need a collection of different questions to test with.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557882%2F06_-_002_-_A_Typical_Eval_Workflow_06.1748557881995.png)

The dataset contains questions that we will merge with our prompt. You can assemble these datasets by hand or generate them using Claude. In real-world evaluations, you might have tens, hundreds, or even thousands of different records, but we'll start with just three questions for this example:

- What's 2+2?
- How do I make oatmeal?
- How far away is the Moon?

## Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude and collect the responses.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557882%2F06_-_002_-_A_Typical_Eval_Workflow_08.1748557882423.png)

For example, the first question becomes a complete prompt that Claude can respond to. You'll repeat this process for all records in your dataset, getting back responses like "2 + 2 = 4", detailed oatmeal instructions, and information about the Moon's distance.

## Step 4: Feed Through a Grader

Now comes the crucial step: objectively scoring Claude's responses. Take each question-answer pair and feed them into a grader that will evaluate the quality of Claude's response.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557883%2F06_-_002_-_A_Typical_Eval_Workflow_11.1748557882912.png)

The grader assigns scores (typically 1-10) based on response quality:

- 10 = Perfect answer, no room for improvement
- 4 = Definitely room for improvement
- 1 = Poor or incorrect response
In our example, the responses might score 10, 4, and 9 respectively. Average these scores together to get an overall performance metric: 7.66.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557883%2F06_-_002_-_A_Typical_Eval_Workflow_14.1748557883448.png)

## Step 5: Change Prompt and Repeat

With your baseline score established, you can now iterate on your prompt. Try adding more specific instructions to guide Claude's responses:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557884%2F06_-_002_-_A_Typical_Eval_Workflow_15.1748557883940.png)

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

Run this improved prompt through the entire evaluation pipeline again. Compare the scores to see which version performs better.

## Prompt Scoring and Iteration

The power of this workflow lies in getting objective measurements for each prompt version. You can compare scores across different iterations and use the version with the best performance, or continue iterating to find even better approaches.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557884%2F06_-_002_-_A_Typical_Eval_Workflow_17.1748557884309.png)

In our example:

- Prompt v1 scored 7.66
- Prompt v2 scored 8.7
The higher score for v2 suggests that adding "Answer the question with ample detail" improved the prompt's performance across our test cases.

This systematic approach gives you an objective way to measure prompt improvements rather than relying on subjective judgment. You can start with a simple implementation and gradually add more sophisticated evaluation criteria as your needs grow.

---

## Generating test datasets

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276733

details

3
                                    download

## Generating test datasets

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building a custom prompt evaluation workflow starts with creating a clear goal and generating test data. In this case, we're building a prompt that helps users write AWS-specific code - either Python functions, JSON configurations, or regular expressions - with no extra explanations or formatting.

## Setting Up the Goal

The prompt should take a user's task description and return one of three output types:

- Python code
- JSON configuration
- Regular expressions
The key requirement is that responses should contain only the requested code without headers, footers, or explanations.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557880%2F06_-_003_-_Generating_Test_Datasets_01.1748557880152.png)

Starting with a simple first version keeps things manageable. The initial prompt template is straightforward: "Please provide a solution to the following task: {task}"

## Creating Evaluation Datasets

An evaluation dataset contains input examples that you'll feed into your prompt. Each test case gets combined with your prompt and sent to Claude, letting you see how well the prompt performs across different scenarios.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557880%2F06_-_003_-_Generating_Test_Datasets_05.1748557880670.png)

You can create datasets in two ways:

- Manually write test cases by hand
- Generate them automatically using Claude
For automatic generation, using a faster model like Haiku makes sense since you're generating multiple test cases.

## Generating Test Data with Code

The dataset generation function uses Claude to create realistic test scenarios. Here's the basic structure:

```
def generate_dataset():
    prompt = """
    Generate 3 AWS-related tasks that require Python, JSON, or Regex solutions.
    
    Focus on tasks that can be solved by writing a single Python function, 
    a single JSON object, or tasks that do not require writing much code.
    
    Example output:
    [
        {
            "task": "Description of task"
        },
        ...additional
    ]
    
    Please generate 3 objects.
    """
    
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

```
def generate_dataset():
    prompt = """
    Generate 3 AWS-related tasks that require Python, JSON, or Regex solutions.
    
    Focus on tasks that can be solved by writing a single Python function, 
    a single JSON object, or tasks that do not require writing much code.
    
    Example output:
    [
        {
            "task": "Description of task"
        },
        ...additional
    ]
    
    Please generate 3 objects.
    """
    
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

```
This approach uses the pre-filled assistant message technique with stop sequences to extract clean JSON responses. The assistant message starts with "```json" and stops at the closing "```", ensuring you get properly formatted data.

Saving Your Dataset

Once generated, save the dataset to avoid regenerating it constantly:

dataset = generate_dataset()
with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)

The generated dataset creates realistic AWS tasks like extracting account IDs from ARNs, writing JSON schemas for EC2 configurations, and creating regex patterns for S3 bucket names. While three test cases work for initial development, production evaluation would need significantly more examples with greater variety.

This foundation gives you a repeatable process for creating evaluation datasets that match your specific use case, setting up the next steps of running evaluations and measuring prompt performance.
```

This approach uses the pre-filled assistant message technique with stop sequences to extract clean JSON responses. The assistant message starts with "```json" and stops at the closing "```", ensuring you get properly formatted data.

## Saving Your Dataset

Once generated, save the dataset to avoid regenerating it constantly:

```
dataset = generate_dataset()
with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)
```

```
dataset = generate_dataset()
with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)
```

```
The generated dataset creates realistic AWS tasks like extracting account IDs from ARNs, writing JSON schemas for EC2 configurations, and creating regex patterns for S3 bucket names. While three test cases work for initial development, production evaluation would need significantly more examples with greater variety.

This foundation gives you a repeatable process for creating evaluation datasets that match your specific use case, setting up the next steps of running evaluations and measuring prompt performance.
```

The generated dataset creates realistic AWS tasks like extracting account IDs from ARNs, writing JSON schemas for EC2 configurations, and creating regex patterns for S3 bucket names. While three test cases work for initial development, production evaluation would need significantly more examples with greater variety.

This foundation gives you a repeatable process for creating evaluation datasets that match your specific use case, setting up the next steps of running evaluations and measuring prompt performance.

```
Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                dataset.json
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        
                                            
                                            
                                                001_Prompt_Evals.ipynb
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        
                                            
                                            
                                                001_Prompt_Evals_complete.ipynb
                                                (opens in new tab)
```

```
Downloads
                            
                                
                                    
                                        
                                            
                                            
                                                dataset.json
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        
                                            
                                            
                                                001_Prompt_Evals.ipynb
                                                (opens in new tab)
                                            
                                        
                                    
                                
                                    
                                        
                                            
                                            
                                                001_Prompt_Evals_complete.ipynb
                                                (opens in new tab)
```

#### Downloads

- dataset.json
                                                (opens in new tab)
- 001_Prompt_Evals.ipynb
                                                (opens in new tab)
- 001_Prompt_Evals_complete.ipynb
                                                (opens in new tab)

---

## Running the eval

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276736

details

## Running the eval

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we have our evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557882%2F06_-_004_-_Running_the_Eval_00.1748557882127.png)

The evaluation process follows a clear workflow: we take our dataset of test cases, combine each one with our prompt template, send it to Claude for processing, and then evaluate the output using a grader system.

## Building the Core Functions

The evaluation pipeline consists of three main functions, each with a specific responsibility. Let's start with the simplest one - the function that handles individual prompt execution.

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

Right now, we're keeping the prompt extremely simple. We're not including any formatting instructions, which means Claude will likely return more verbose output than we need. We'll refine this later as we iterate on our evaluation process.

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

For now, we're using a hardcoded score of 10. The grading logic is where we'll spend significant time in upcoming sections, but this placeholder lets us test the overall pipeline structure.

## The run_eval Function

This is the main orchestrator that processes the entire dataset:

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

This function loops through every test case in our dataset, processes each one, and collects all the results into a single list.

## Running the Evaluation

To execute our evaluation pipeline, we load the dataset and call our main function:

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

The first time you run this, expect it to take some time - even with Claude Haiku, processing a full dataset can take 30+ seconds. We'll cover optimization techniques later, but for now, patience is key.

## Examining the Results

Once the evaluation completes, you can inspect the results with formatted JSON output:

```
print(json.dumps(results, indent=2))
```

```
print(json.dumps(results, indent=2))
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557883%2F06_-_004_-_Running_the_Eval_18.1748557883215.png)

The results structure contains an array of objects, where each object represents one test case execution. You'll see the Claude output (which tends to be quite verbose without formatting constraints), the original test case definition, and the score.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557883%2F06_-_004_-_Running_the_Eval_01.1748557883610.png)

## What We've Accomplished

At this point, we've successfully implemented the core evaluation pipeline. We can:

- Take test cases from our dataset
- Merge them with prompt templates
- Get responses from Claude
- Collect and organize all the results
The missing piece is intelligent grading - right now we're just assigning a fixed score to every response. The next step is building graders that can actually evaluate whether Claude's outputs are correct, which is where the real sophistication of evaluation systems comes into play.

This pipeline structure might seem simple, but it represents the foundation that most AI evaluation systems are built on. The complexity comes in the grading logic and prompt optimization, not in the basic orchestration of running tests.

---

## Model based grading

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276738

details

## Model based grading

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building prompt evaluation workflows, graders provide objective signals about output quality. A grader takes model output and returns some kind of measurable feedback - typically a number between 1-10, where 10 represents high quality and 1 represents poor quality.

## Types of Graders

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557941%2F06_-_005_-_Model_Based_Grading_03.1748557941095.png)

There are three main approaches to grading model outputs:

- Code graders - Programmatically evaluate outputs using custom logic
- Model graders - Use another AI model to assess quality
- Human graders - Have people manually review and score outputs

### Code Graders

Code graders let you implement any programmatic check you can imagine. Common uses include:

- Checking output length
- Verifying output does/doesn't have certain words
- Syntax validation for JSON, Python, or regex
- Readability scores
The only requirement is that your code returns some measurable signal when it runs.

### Model Graders

Model graders make an additional API request to evaluate the original output. This approach offers tremendous flexibility for assessing:

- Response quality
- Quality of instruction following
- Completeness
- Helpfulness
- Safety

### Human Graders

Human graders provide the most flexibility but are time-intensive and tedious. They're useful for evaluating:

- General response quality
- Comprehensiveness
- Depth
- Conciseness
- Relevance

## Defining Evaluation Criteria

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557941%2F06_-_005_-_Model_Based_Grading_06.1748557941604.png)

Before implementing any grader, you need clear evaluation criteria. For a code generation prompt, you might focus on:

- Format - Should return only Python, JSON, or Regex without explanation
- Valid Syntax - Produced code should have valid syntax
- Task Following - Response should directly address the user's task with accurate code

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557943%2F06_-_005_-_Model_Based_Grading_07.1748557942738.png)

The first two criteria work well with code graders, while task following is better suited for model graders due to their flexibility.

## Implementing a Model Grader

Here's how to build a model grader function:

```
def grade_by_model(test_case, output):
    # Create evaluation prompt
    eval_prompt = """
    You are an expert code reviewer. Evaluate this AI-generated solution.
    
    Task: {task}
    Solution: {solution}
    
    Provide your evaluation as a structured JSON object with:
    - "strengths": An array of 1-3 key strengths
    - "weaknesses": An array of 1-3 key areas for improvement  
    - "reasoning": A concise explanation of your assessment
    - "score": A number between 1-10
    """
    
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
```

```
def grade_by_model(test_case, output):
    # Create evaluation prompt
    eval_prompt = """
    You are an expert code reviewer. Evaluate this AI-generated solution.
    
    Task: {task}
    Solution: {solution}
    
    Provide your evaluation as a structured JSON object with:
    - "strengths": An array of 1-3 key strengths
    - "weaknesses": An array of 1-3 key areas for improvement  
    - "reasoning": A concise explanation of your assessment
    - "score": A number between 1-10
    """
    
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
```

```
The key insight is asking for strengths, weaknesses, and reasoning alongside the score. Without this context, models tend to default to middling scores around 6.

Integrating the Grader

Update your test case function to use the model grader:

def run_test_case(test_case):
    output = run_prompt(test_case)
    
    # Get model evaluation
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]
    
    return {
        "output": output, 
        "test_case": test_case, 
        "score": score,
        "reasoning": reasoning
    }

Calculating Average Scores

To get an overall performance metric, calculate the average score across all test cases:

from statistics import mean

def run_eval(dataset):
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")
    
    return results

This gives you a concrete, objective metric to track prompt performance over time. While model graders can be somewhat inconsistent, they provide a starting point for measuring and improving your prompts systematically.
```

The key insight is asking for strengths, weaknesses, and reasoning alongside the score. Without this context, models tend to default to middling scores around 6.

## Integrating the Grader

Update your test case function to use the model grader:

```
def run_test_case(test_case):
    output = run_prompt(test_case)
    
    # Get model evaluation
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
    
    # Get model evaluation
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
Calculating Average Scores

To get an overall performance metric, calculate the average score across all test cases:

from statistics import mean

def run_eval(dataset):
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    average_score = mean([result["score"] for result in results])
    print(f"Average score: {average_score}")
    
    return results

This gives you a concrete, objective metric to track prompt performance over time. While model graders can be somewhat inconsistent, they provide a starting point for measuring and improving your prompts systematically.
```

## Calculating Average Scores

To get an overall performance metric, calculate the average score across all test cases:

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

```
This gives you a concrete, objective metric to track prompt performance over time. While model graders can be somewhat inconsistent, they provide a starting point for measuring and improving your prompts systematically.
```

This gives you a concrete, objective metric to track prompt performance over time. While model graders can be somewhat inconsistent, they provide a starting point for measuring and improving your prompts systematically.

---

## Code based grading

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276735

details

## Code based grading

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Code-based grading adds an extra layer of validation to your prompt evaluations by checking whether the model's output follows the correct format and has valid syntax. This is especially useful when you're asking models to generate code, JSON, or regular expressions.

## How Code Grading Works

The code grader evaluates two main criteria:

- Format compliance - Does the output contain only the requested format (Python, JSON, or regex) without explanations?
- Valid syntax - Can the output actually be parsed or compiled successfully?

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557928%2F06_-_006_-_Code_Based_Grading_00.1748557927749.png)

The system uses separate validation functions for each format type. If the code parses successfully, it gets a perfect score of 10. If parsing fails with an error, it gets a score of 0.

## Setting Up Validation Functions

You'll need three helper functions to validate different output types:

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

These functions use Python's built-in parsing capabilities to check syntax validity. The json.loads() function validates JSON, ast.parse() creates a Python abstract syntax tree, and re.compile() validates regular expressions.

```
json.loads()
```

```
ast.parse()
```

```
re.compile()
```

## Adding Format Information to Test Cases

Your test dataset needs to specify the expected output format for each task. Update your dataset generation prompt to include a format field:

```
{
    "task": "Description of task",
    "format": "python"
}
```

```
{
    "task": "Description of task",
    "format": "python"
}
```

The format field should contain "json", "python", or "regex" depending on what type of output you expect from that particular task.

## Improving Your Prompt

To get better results from the code grader, make your prompt instructions more specific:

```
* Respond only with Python, JSON, or a plain Regex
* Do not add any comments or commentary or explanation
```

```
* Respond only with Python, JSON, or a plain Regex
* Do not add any comments or commentary or explanation
```

You can also use a pre-filled assistant message with code blocks and stop sequences to ensure clean output formatting.

## Combining Scores

The final step is merging your model grader score with the syntax grader score. A simple approach is to take the average of both scores:

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

This gives equal weight to both content quality (from the model grader) and technical correctness (from the code grader). You can adjust this weighting based on what matters more for your specific use case.

## Interpreting Results

Once you run your evaluation, you'll get a combined score that reflects both the semantic quality and technical correctness of the generated code. Remember that a single score in isolation doesn't tell you much - the real value comes from comparing scores as you iterate on your prompt design.

Use this baseline score to test prompt improvements and see if your changes actually lead to better, more reliable code generation.

---

## Exercise on prompt evals

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276734

## Exercise on prompt evals

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Quiz on prompt evaluations

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289297

## Quiz on prompt evaluations

# Quiz on Prompt Evaluations

---

## Prompt engineering

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276749

details

2
                                    download

## Prompt engineering

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt engineering is about taking a prompt you've written and improving it to get more reliable, higher-quality outputs. This process involves writing an initial prompt, evaluating its performance, then systematically applying engineering techniques to improve it step by step.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557936%2F07_-_001_-_Prompt_Engineering_00.1748557935959.png)

## The Iterative Improvement Process

The approach follows a clear cycle: set a goal, write an initial prompt, evaluate it, apply a prompt engineering technique, then re-evaluate to verify better performance. This cycle repeats as you refine your prompt.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557936%2F07_-_001_-_Prompt_Engineering_01.1748557936587.png)

For this tutorial series, we'll work on a practical example: creating a prompt that generates one-day meal plans for athletes based on their height, weight, physical goals, and dietary restrictions.

## Setting Up the Evaluation Pipeline

The evaluation uses an improved version of the pipeline from previous modules, wrapped in a PromptEvaluator class that handles dataset generation and model grading. The class supports concurrency to speed up the evaluation process:

```
PromptEvaluator
```

```
evaluator = PromptEvaluator(max_concurrent_tasks=5)
```

```
evaluator = PromptEvaluator(max_concurrent_tasks=5)
```

Start with a low concurrency value (like 3) to avoid rate limit errors. You can adjust this based on your API quota.

## Generating Test Data

The generate_dataset method creates test cases for your prompt. You need to specify:

```
generate_dataset
```

- A task description explaining what your prompt should do
- A specification of the inputs your prompt requires
- The number of test cases to generate
For the meal planning example:

```
dataset = evaluator.generate_dataset(
    task_description="Write a compact, concise 1 day meal plan for a single athlete",
    prompt_inputs_spec={
        "height": "Athlete's height in cm",
        "weight": "Athlete's weight in kg", 
        "goal": "Goal of the athlete",
        "restrictions": "Dietary restrictions of the athlete"
    },
    num_cases=3
)
```

```
dataset = evaluator.generate_dataset(
    task_description="Write a compact, concise 1 day meal plan for a single athlete",
    prompt_inputs_spec={
        "height": "Athlete's height in cm",
        "weight": "Athlete's weight in kg", 
        "goal": "Goal of the athlete",
        "restrictions": "Dietary restrictions of the athlete"
    },
    num_cases=3
)
```

## Writing Your Initial Prompt

Start with a simple, naive prompt to establish a baseline. The run_prompt function receives the test case inputs and should return the model's response:

```
run_prompt
```

```
def run_prompt(prompt_inputs):
    prompt = f"""
    What should this person eat?
    
    - Height: {prompt_inputs["height"]}
    - Weight: {prompt_inputs["weight"]}
    - Goal: {prompt_inputs["goal"]}
    - Dietary restrictions: {prompt_inputs["restrictions"]}
    """
    
    messages = []
    add_user_message(messages, prompt)
    return chat(messages)
```

```
def run_prompt(prompt_inputs):
    prompt = f"""
    What should this person eat?
    
    - Height: {prompt_inputs["height"]}
    - Weight: {prompt_inputs["weight"]}
    - Goal: {prompt_inputs["goal"]}
    - Dietary restrictions: {prompt_inputs["restrictions"]}
    """
    
    messages = []
    add_user_message(messages, prompt)
    return chat(messages)
```

## Running the Evaluation

The evaluation process compares your prompt's output against expected criteria. You can add extra criteria to guide the grading:

```
results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    extra_criteria="""
    The output should include:
    - Daily caloric total
    - Macronutrient breakdown  
    - Meals with exact foods, portions, and timing
    """
)
```

```
results = evaluator.run_evaluation(
    run_prompt_function=run_prompt,
    dataset_file="dataset.json",
    extra_criteria="""
    The output should include:
    - Daily caloric total
    - Macronutrient breakdown  
    - Meals with exact foods, portions, and timing
    """
)
```

## Analyzing Results

The evaluation generates an output.html file that you can open in your browser. This report shows detailed results for each test case, including scores, reasoning, and the actual output generated by your prompt.

```
output.html
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557937%2F07_-_001_-_Prompt_Engineering_19.1748557937125.png)

Don't be discouraged by low initial scores - that's expected! The initial prompt in this example scored only 2.3 out of 10, but this gives you a clear baseline to improve from.

## What's Next

With your baseline established, you can now systematically apply prompt engineering techniques like being more specific, adding output formatting requirements, using structured prompts, and implementing multi-shot examples. Each technique should improve your evaluation score, giving you measurable progress toward your goal.

#### Downloads

- 002_prompting_completed.ipynb
                                                (opens in new tab)
- 001_prompting.ipynb
                                                (opens in new tab)

---

## Being clear and direct

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276743

details

## Being clear and direct

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The first line of your prompt is the most important part of your entire request. This is where you set the stage for everything that follows, and getting it right can dramatically improve your results.

## Being Clear and Direct

When crafting that crucial first line, you want to focus on two key principles: clarity and directness. This means using simple language that leaves no room for ambiguity about what you want Claude to do.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557916%2F07_-_002_-_Being_Clear_and_Direct_02.1748557916605.png)

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
- Key constraints (one day, for an athlete, considering restrictions)

## Results Matter

This simple change can make a significant difference in output quality. In our example, the evaluation score jumped from 2.32 to 3.92 - a substantial improvement from just restructuring that opening line.

The key takeaway is that Claude responds best when you treat it like a capable assistant who needs clear direction rather than someone who has to guess what you want. Start strong with a direct action verb, be specific about the task, and you'll see better results right away.

---

## Being specific

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276745

details

## Being specific

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557984%2F07_-_003_-_Being_Specific_00.1748557984462.png)

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," the model could go in countless directions. It might write 200 words or 2,000 words. It could focus on one character or introduce five. The story structure could vary wildly.

But if you add specific guidelines, you can shape the output to match your needs much more closely.

## Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see both used together in professional applications.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557985%2F07_-_003_-_Being_Specific_05.1748557984969.png)

### Quality Guidelines

The first type focuses on listing qualities that your output should have. These guidelines control attributes like:

- Length constraints (keep under 1,000 words)
- Structural requirements (include a clear action that reveals the character's talent)
- Content specifications (include at least one supporting character)

### Process Steps

The second type provides specific steps for the model to follow. This approach makes Claude think through the problem systematically:

- Brainstorm 3 talents that would create dramatic tension
- Pick the most interesting talent
- Outline a pivotal scene that reveals the talent
- Brainstorm 3 supporting character types that could increase the impact of this discovery
Quality guidelines control what the output looks like, while process steps control how Claude arrives at that output.

## Real-World Testing

Let's look at how this works in practice. Here's a prompt for generating meal plans that incorporates specific guidelines:

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

When tested against a baseline prompt without guidelines, this approach improved the evaluation score from 3.92 to 7.86 - more than doubling the quality.

Testing the process steps approach (telling Claude to calculate calories first, then figure out macros, then plan timing, etc.) also showed significant improvement, scoring 7.3.

## When to Provide Steps

While quality guidelines work well for most prompts, you should consider adding process steps when you're dealing with:

- Troubleshooting hard problems
- Decision making
- Critical thinking
- Anytime you want to force Claude to consider a "wider" view

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557985%2F07_-_003_-_Being_Specific_18.1748557985387.png)

For example, if you're asking Claude to analyze why a sales team's numbers dropped 30% last quarter, you might want to provide steps that ensure it considers multiple angles - market conditions, individual performance, organizational changes, and customer feedback - rather than jumping to the first obvious explanation.

The key insight is that being specific helps you get consistent, high-quality results instead of leaving everything to chance. Whether you use quality guidelines, process steps, or both, you're giving Claude a clear framework to work within.

---

## Structure with XML tags

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276744

details

## Structure with XML tags

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you're building prompts that include a lot of content, Claude can sometimes struggle to understand which pieces of text belong together or what different sections are supposed to represent. XML tags provide a simple way to add structure and clarity to your prompts, especially when you're interpolating large amounts of data.

## Why Structure Matters

Consider a prompt where you need to analyze 20 pages of sales records. Without clear boundaries, Claude might have trouble distinguishing between your instructions and the actual data you want analyzed.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557981%2F07_-_004_-_Structure_with_XML_Tags_00.1748557980997.png)

The example above shows how unclear boundaries can make it difficult for Claude to parse your intent. By wrapping the sales records in XML tags, you create clear separation between different parts of your prompt.

## Using XML Tags for Clarity

XML tags act as delimiters that help Claude understand the structure of your prompt. You can create custom tag names that describe the content they contain:

```
<sales_records>
{sales_records}
</sales_records>
```

```
<sales_records>
{sales_records}
</sales_records>
```

The tag names don't need to follow any official XML specification - you're free to create descriptive names like sales_records, data, or records. More specific names generally work better than generic ones.

```
sales_records
```

```
data
```

```
records
```

## A Practical Example

Here's a clear example of why XML tags make a difference. In the "Not Great" version, it's unclear what content represents the buggy code versus the documentation:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557981%2F07_-_004_-_Structure_with_XML_Tags_10.1748557981630.png)

The improved version uses XML tags to clearly separate the different types of content:

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

Now Claude can easily distinguish between the code that needs debugging and the documentation that should guide the debugging process.

## Applying Structure to Your Prompts

Even when your interpolated content isn't massive, XML tags can still improve clarity. For example, when generating meal plans, you can group athlete information together:

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

This makes it crystal clear to Claude that this block contains external input about the athlete that should inform the meal plan generation.

## When to Use XML Tags

XML tags are most useful when:

- You're including large amounts of context or data
- Your prompt contains multiple distinct types of content
- You want to make the boundaries between different sections obvious
- You're interpolating content that might be confused with your instructions
While you might not see dramatic improvements with simple prompts, XML tags serve as delimiters that help Claude better understand your intent, leading to more consistent and accurate responses.

---

## Providing examples

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276747

details

## Providing examples

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Providing examples in your prompts is one of the most effective prompt engineering techniques you'll use. This approach, known as "one-shot" or "multi-shot" prompting, involves giving Claude sample input/output pairs to guide its responses.

## How Examples Work

Let's look at a sentiment analysis example. Say you want Claude to categorize whether a tweet is positive or negative:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557985%2F07_-_005_-_Providing_Examples_00.1748557985238.png)

The challenge here is sarcasm. A tweet like "Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'" appears positive on the surface, but it's actually sarcastic and negative (Plan 9 from Outer Space is famously terrible).

## Adding Examples to Your Prompt

To handle this, you can add examples that show Claude exactly how to respond:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557985%2F07_-_005_-_Providing_Examples_04.1748557985658.png)

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

For tricky scenarios like sarcasm, you can provide multiple examples (multi-shot prompting). Add context to highlight what Claude should watch for:

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

## When to Use Examples

Examples are particularly useful for:

- Capturing corner cases or edge scenarios
- Defining complex output formats (like specific JSON structures)
- Showing Claude exactly what "good" output looks like

## Finding Good Examples from Evaluations

When running prompt evaluations, look for your highest-scoring outputs in the HTML report. These make excellent examples to include in your prompt.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557986%2F07_-_005_-_Providing_Examples_12.1748557986066.png)

Find a response that scored well (ideally a 10, or your highest score), then copy both the input and output to use as your example.

## Adding Context to Examples

You can make examples even more effective by explaining why they're good. After your example output, add a brief explanation:

```
<ideal_output>
[Your example output here]
</ideal_output>

This example meal plan is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
```

```
<ideal_output>
[Your example output here]
</ideal_output>

This example meal plan is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
```

This helps Claude understand not just what to produce, but why that output is considered ideal.

## Best Practices

- Use XML tags to clearly structure your examples
- Be explicit about what you're showing Claude
- Choose representative examples that cover your most important use cases
- Include corner cases that might trip up the model
- Explain why examples are good when it's not obvious
One-shot and multi-shot prompting will quickly become essential tools in your prompt engineering toolkit, especially when you need consistent, well-formatted outputs or want to handle tricky edge cases reliably.

---

## Exercise on prompting

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276746

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

## Quiz on prompt engineering

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289298

## Quiz on prompt engineering

# Quiz on Prompt Engineering

---

## Introducing tool use

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276756

details

## Introducing tool use

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Tools allow Claude to access information from the outside world, solving one of its key limitations. By default, Claude only has access to information it was trained on, which means it can't provide current information like today's weather or recent news.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557981%2F08_-_001_-_Introducing_Tool_Use_04.1748557980911.png)

When a user asks "What's the weather in San Francisco, California?" Claude will typically respond with "I'm sorry, but I don't have access to up-to-date weather information." Tools fix this problem by creating a bridge between Claude and external data sources.

## How Tool Use Works

The tool use process follows a specific flow that involves multiple back-and-forth communications between your server and Claude:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557981%2F08_-_001_-_Introducing_Tool_Use_05.1748557981486.png)

- Initial Request: You send Claude a question along with instructions on how to get extra data
- Tool Request: Claude analyzes the question and asks for specific external data it needs
- Data Retrieval: Your server runs code to fetch the requested information
- Final Response: Claude uses the external data to provide a complete, informed answer

## Weather Example in Practice

Here's how the tool use flow works for a weather query:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557982%2F08_-_001_-_Introducing_Tool_Use_10.1748557982048.png)

When a user asks about weather, you include details on how to retrieve current weather data in your initial request to Claude. Claude recognizes it needs current weather information and asks your server to get it. Your server calls a weather API, retrieves the live data, and sends it back to Claude. Finally, Claude combines the original question with the fresh weather data to provide an accurate, current response.

## Implementation Challenges

Tool use can feel confusing because there's a disconnect between the logical flow and how you actually write the code. The implementation doesn't follow the same order as the conceptual steps:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748557982%2F08_-_001_-_Introducing_Tool_Use_15.1748557982462.png)

In practice, you often need to:

- Write the tool function first
- Create a JSON schema specification
- Handle the ToolUse and ToolResult parts
- Include the schema with your request
This jumping around between different parts of the implementation is why tool use initially seems complex. The key is understanding that each step in the logical flow requires specific code components that you'll build in a different order than they execute.

In the following videos, we'll implement tool use step by step, frequently referencing this flow diagram to keep track of which piece we're currently building.

---

## Tool functions

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276757

details

2
                                    download

## Tool functions

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building tools for Claude requires solving several challenges that aren't immediately obvious. When you want Claude to set reminders for future dates, you quickly discover that while Claude knows the current date, it doesn't always know the exact time, struggles with complex date arithmetic, and has no built-in way to actually set reminders.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558031%2F08_-_002_-_Tool_Functions_00.1748558031662.png)

The solution is to create custom tools that handle these specific tasks. For a reminder system, you'll need three separate tools: one to get the current date and time, another to add durations to dates, and a third to actually set the reminder.

## Why This Is Challenging

Claude has some limitations when it comes to time-based tasks:

- Claude might know the current date, but not the exact time
- Claude doesn't always handle time-based addition well, especially when looking many days into the future
- Claude doesn't know how to set a reminder

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558032%2F08_-_002_-_Tool_Functions_03.1748558032191.png)

## The Tools You Need

To solve these problems, you'll create three dedicated tools:

- Get the current date time - Claude needs to know the current date and time
- Add duration to date time - Claude isn't perfect with date time addition
- Set a reminder - Need a way to set a reminder

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558033%2F08_-_002_-_Tool_Functions_08.1748558033433.png)

## How Tool Functions Work

The tool system follows a specific flow between your server and Claude. You write functions that Claude can call when it needs additional information, and Claude receives the results to help formulate its response.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558034%2F08_-_002_-_Tool_Functions_09.1748558033885.png)

The process involves several steps: writing the tool function, creating a JSON schema specification, calling Claude with that schema, running the tool when Claude requests it, and providing the results back to Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558034%2F08_-_002_-_Tool_Functions_10.1748558034414.png)

## Writing Tool Functions

Tool functions are plain Python functions that get executed when Claude decides it needs additional information to help the user. Here's how to write them effectively:

### Best Practices

- Use well-named, descriptive arguments (this becomes important later)
- Validate the inputs, raising an error if they fail validation
- Return meaningful errors - Claude will try to call your function a second time if it gets an error

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558036%2F08_-_002_-_Tool_Functions_11.1748558036000.png)

## Creating Your First Tool

Let's start with the simplest tool - getting the current date and time. This function takes a date format parameter and returns the current timestamp:

```
from datetime import datetime, timedelta

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(date_format)
```

```
from datetime import datetime, timedelta

def get_current_datetime(date_format="%Y-%m-%d %H:%M:%S"):
    return datetime.now().strftime(date_format)
```

This function is straightforward but follows the key principles: it has a descriptive name, takes a well-named parameter with a sensible default, and returns exactly what it promises.

## JSON Schema Specification

Once you have your function, you need to write a JSON Schema that describes it to Claude. This schema tells Claude what arguments the function requires and helps it understand when and how to use the tool.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558036%2F08_-_002_-_Tool_Functions_18.1748558036585.png)

The JSON Schema serves two purposes: it helps Claude understand what arguments your function requires, and it's not just an LLM concept - JSON Schema is commonly used for data validation across many programming contexts. There are plenty of online tools to help you generate schemas.

### Schema Best Practices

- Explain what the tool does, when to use it, and what it returns
- Aim for 3 to 4 sentences in your descriptions
- Provide detailed descriptions for parameters
With your tool function written and schema defined, you're ready to integrate it with Claude and start building more sophisticated AI interactions that can handle real-world tasks like setting reminders.

#### Downloads

- 001_tools.ipynb
                                                (opens in new tab)
- 002_tools_complete.ipynb
                                                (opens in new tab)

---

## JSON Schema for tools

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276758

details

## JSON Schema for tools

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

After creating your tool function, the next step is writing a JSON schema to describe it. This schema tells Claude what arguments your function expects and how to use it properly. While the configuration might look intimidating at first, it's actually straightforward once you understand the process.

## Understanding JSON Schema

JSON Schema isn't something invented just for AI tools - it's been around for years as a standard way to validate data. The schema has two main parts: the name and description at the top (which help Claude understand when to use the tool), and the actual schema that describes the function's arguments.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558031%2F08_-_003_-_JSON_Schema_for_Tools_04.1748558031698.png)

The top section contains the tool's name and description, which helps Claude understand when to use it. The bottom section is the actual schema that describes your function's arguments in detail.

## Creating a JSON Schema: Step-by-Step

Here's the simplest way to create a JSON schema for any function:

### Step 1: Write a Dictionary with Sample Data

Take your function and create a dictionary of all keyword arguments with sample data. For example, if you have a function like this:

```
def process_data(ids, profile, primary_id, value):
    pass
```

```
def process_data(ids, profile, primary_id, value):
    pass
```

Create a dictionary with sample values:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558032%2F08_-_003_-_JSON_Schema_for_Tools_08.1748558032208.png)

### Step 2: Convert to JSON

Convert your Python dictionary to proper JSON format. The main difference is changing Python's True to JSON's true.

```
True
```

```
true
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558033%2F08_-_003_-_JSON_Schema_for_Tools_09.1748558032825.png)

### Step 3: Use an Online Converter

Search for "JSON to JSON Schema converter" and use one of the many free online tools. Paste your JSON data and let it generate the schema automatically.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558033%2F08_-_003_-_JSON_Schema_for_Tools_11.1748558033345.png)

The tool will analyze your sample data and create a proper schema structure. Remove any $schema declarations from the output - you don't need them.

```
$schema
```

### Step 4: Add Descriptions

The most important step is adding detailed descriptions to each property. These descriptions help Claude understand exactly what each argument does and how to use it.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558034%2F08_-_003_-_JSON_Schema_for_Tools_13.1748558033822.png)

## Writing Good Descriptions

When writing descriptions for your tools and properties, follow these best practices:

- Explain what the tool does, when to use it, and what it returns
- Aim for 3-4 sentences in your tool description
- Provide super detailed descriptions for each property
- If you're stuck, paste your function into Claude and ask it to write descriptions for you
Here's an example of a well-described tool schema:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558034%2F08_-_003_-_JSON_Schema_for_Tools_15.1748558034195.png)

Notice how the description clearly explains what the weather tool does, when to use it, what data it returns, and provides specific examples of valid location formats.

## Putting It All Together

Your final JSON schema should look something like this structure, with the toolSpec containing the name, description, and inputSchema with the detailed argument specifications:

```
toolSpec
```

```
inputSchema
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558034%2F08_-_003_-_JSON_Schema_for_Tools_02.1748558034696.png)

The schema acts as a contract between your code and Claude, ensuring that when Claude decides to use your tool, it knows exactly what information to provide and in what format. This clear communication is what makes tool use reliable and effective.

---

## Handling tool use responses

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276764

details

## Handling tool use responses

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When Claude decides to use a tool, it returns a special response structure that requires careful handling. Understanding this response format and implementing proper conversation management is crucial for building robust tool-enabled applications.

## Tool Choice Configuration

Before diving into responses, it's worth understanding how to control when Claude uses tools. The toolChoice parameter gives you three options:

```
toolChoice
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558036%2F08_-_004_-_Handling_Tool_Use_Responses_02.1748558036403.png)

- auto - Claude decides whether to use a tool (default behavior)
- any - Claude must use a tool but can choose which one
- specific tool - Force Claude to use a particular tool by name
The third option is especially useful for testing when you want to ensure Claude calls a specific function.

## Multi-Part Message Structure

When Claude wants to use a tool, it returns an assistant message with multiple content parts instead of just text:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558037%2F08_-_004_-_Handling_Tool_Use_Responses_07.1748558036875.png)

The response contains two parts:

- Text Part - Human-readable explanation like "I can help you find out the current time. Let me find that information for you"
- ToolUse Part - Structured data telling you which tool to run and with what arguments

## Understanding the ToolUse Part

The ToolUse part contains three key pieces of information:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558037%2F08_-_004_-_Handling_Tool_Use_Responses_09.1748558037308.png)

- toolUseId - A unique identifier you'll need when sending back the tool result
- name - The exact tool name from your JSON schema that Claude wants to call
- input - A dictionary of arguments Claude wants to pass to your tool function

## Conversation Flow with Tools

Tool usage follows a specific conversation pattern that requires maintaining complete message history:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558038%2F08_-_004_-_Handling_Tool_Use_Responses_11.1748558037792.png)

When you receive a tool use request, you need to:

- Extract the tool information from the ToolUse part
- Run your actual tool function
- Send back a ToolResult message along with the complete conversation history
- Include the original user message and the assistant's tool use message in your next request

## Updating Helper Functions

To handle multi-part messages properly, you'll need to update your message handling functions. Here's how to make your functions flexible enough to handle both simple text and complex multi-part content:

```
def add_user_message(messages, content):
    if isinstance(content, str):
        user_message = {"role": "user", "content": [{"text": content}]}
    else:
        user_message = {"role": "user", "content": content}
    messages.append(user_message)

def add_assistant_message(messages, content):
    if isinstance(content, str):
        assistant_message = {"role": "assistant", "content": [{"text": content}]}
    else:
        assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
```

```
def add_user_message(messages, content):
    if isinstance(content, str):
        user_message = {"role": "user", "content": [{"text": content}]}
    else:
        user_message = {"role": "user", "content": content}
    messages.append(user_message)

def add_assistant_message(messages, content):
    if isinstance(content, str):
        assistant_message = {"role": "assistant", "content": [{"text": content}]}
    else:
        assistant_message = {"role": "assistant", "content": content}
    messages.append(assistant_message)
```

You'll also want to update your chat function to return both the text and the full parts list:

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    # ... existing setup code ...
    
    response = client.converse(**params)
    
    text = response["output"]["message"]["content"][0]["text"]
    parts = response["output"]["message"]["content"]
    
    return text, parts
```

```
def chat(messages, system=None, temperature=1.0, stop_sequences=[], tools=None):
    # ... existing setup code ...
    
    response = client.converse(**params)
    
    text = response["output"]["message"]["content"][0]["text"]
    parts = response["output"]["message"]["content"]
    
    return text, parts
```

## Checking the Stop Reason

Always check the stopReason field in Claude's response. When it equals "tool_use", you know Claude wants to call a tool rather than just providing a text response. This is your signal to extract the tool information and execute the requested function.

```
stopReason
```

```
"tool_use"
```

With these patterns in place, you're ready to handle Claude's tool use requests and maintain proper conversation flow throughout multi-turn tool interactions.

---

## Running tool functions

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276762

details

## Running tool functions

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When Claude responds with a tool use request, your server needs to actually run the requested tool and send the results back. This step involves extracting tool use parts from Claude's response, executing the appropriate functions, and formatting the results properly.

## Handling Multiple Tool Requests

Claude can send multiple tool use parts in a single response. Your code needs to handle this possibility defensively. An assistant message might contain a text part followed by one, two, or even more tool use parts.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558039%2F08_-_005_-_Running_Tool_Functions_00.1748558038947.png)

The flow works like this: Claude sends a request with JSON schema, receives a tool use part, then your server runs the tool and sends back a tool result part for Claude to provide a final response.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558039%2F08_-_005_-_Running_Tool_Functions_01.1748558039418.png)

## Extracting Tool Use Parts

First, create a function to process all the parts returned from a chat request:

```
def run_tools(parts):
    tool_requests = [part for part in parts if "toolUse" in part]
    tool_result_parts = []
    
    for tool_request in tool_requests:
        tool_use_id = tool_request["toolUse"]["toolUseId"]
        tool_name = tool_request["toolUse"]["name"]
        tool_input = tool_request["toolUse"]["input"]
```

```
def run_tools(parts):
    tool_requests = [part for part in parts if "toolUse" in part]
    tool_result_parts = []
    
    for tool_request in tool_requests:
        tool_use_id = tool_request["toolUse"]["toolUseId"]
        tool_name = tool_request["toolUse"]["name"]
        tool_input = tool_request["toolUse"]["input"]
```

This comprehension filters the parts list to only include dictionaries that contain a "toolUse" key, ignoring text parts.

## Running the Actual Tools

Create a helper function to execute the requested tool:

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    else:
        raise Exception(f"Unknown tool name: {tool_name}")
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    else:
        raise Exception(f"Unknown tool name: {tool_name}")
```

The key detail here is using **tool_input to splat the dictionary of arguments into your tool function. Claude always returns arguments as a dictionary object, so you need to unpack it properly.

```
**tool_input
```

## Creating Tool Result Parts

After running a tool, you need to format the response as a tool result part:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558040%2F08_-_005_-_Running_Tool_Functions_12.1748558039846.png)

Tool result parts require three key properties:

- toolUseId - Must match the original tool use part's ID
- content - The output from your tool, serialized as a string
- status - Either "success" or "error"

## Understanding Tool Use IDs

The tool use ID system becomes important when Claude requests multiple tools in parallel. For example, if Claude wants to run a calculator tool twice:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558040%2F08_-_005_-_Running_Tool_Functions_13.1748558040348.png)

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558041%2F08_-_005_-_Running_Tool_Functions_14.1748558040819.png)

Each tool use gets a unique ID (like "ab3" and "po9"), and your tool results must include the matching IDs so Claude knows which result corresponds to which request.

## Error Handling

Wrap your tool execution in try-catch blocks. Claude is intelligent about tool errors and might adjust its approach if you return proper error information:

```
try:
    tool_output = run_tool(tool_name, tool_input)
    tool_result_part = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [{"text": json.dumps(tool_output)}],
            "status": "success"
        }
    }
except Exception as e:
    tool_result_part = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [{"text": f"Error: {e}"}],
            "status": "error"
        }
    }
```

```
try:
    tool_output = run_tool(tool_name, tool_input)
    tool_result_part = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [{"text": json.dumps(tool_output)}],
            "status": "success"
        }
    }
except Exception as e:
    tool_result_part = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [{"text": f"Error: {e}"}],
            "status": "error"
        }
    }
```

## Complete Implementation

Here's the full function that processes tool requests and returns formatted results:

```
def run_tools(parts):
    tool_requests = [part for part in parts if "toolUse" in part]
    tool_result_parts = []
    
    for tool_request in tool_requests:
        tool_use_id = tool_request["toolUse"]["toolUseId"]
        tool_name = tool_request["toolUse"]["name"]
        tool_input = tool_request["toolUse"]["input"]
        
        try:
            tool_output = run_tool(tool_name, tool_input)
            tool_result_part = {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": json.dumps(tool_output)}],
                    "status": "success"
                }
            }
        except Exception as e:
            tool_result_part = {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": f"Error: {e}"}],
                    "status": "error"
                }
            }
        
        tool_result_parts.append(tool_result_part)
    
    return tool_result_parts
```

```
def run_tools(parts):
    tool_requests = [part for part in parts if "toolUse" in part]
    tool_result_parts = []
    
    for tool_request in tool_requests:
        tool_use_id = tool_request["toolUse"]["toolUseId"]
        tool_name = tool_request["toolUse"]["name"]
        tool_input = tool_request["toolUse"]["input"]
        
        try:
            tool_output = run_tool(tool_name, tool_input)
            tool_result_part = {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": json.dumps(tool_output)}],
                    "status": "success"
                }
            }
        except Exception as e:
            tool_result_part = {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": f"Error: {e}"}],
                    "status": "error"
                }
            }
        
        tool_result_parts.append(tool_result_part)
    
    return tool_result_parts
```

Once you have the tool result parts, you can send them back to Claude in your next chat request, completing the tool use cycle.

---

## Sending tool results

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276760

details

## Sending tool results

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now we're at the final step of the tool use workflow. After running our tools and getting the results, we need to send everything back to Claude so it can provide a complete response to the user.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558077%2F08_-_006_-_Sending_Tool_Results_00.1748558076744.png)

The process is straightforward: take all the tool result parts we generated, package them into a user message, and send the entire conversation history back to Claude along with the original tool schemas.

## Adding the Assistant Message

First, we need to make sure our conversation history is complete. After Claude's initial response with the tool use request, we need to add that response to our message history using add_assistant_message().

```
add_assistant_message()
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558077%2F08_-_006_-_Sending_Tool_Results_03.1748558077331.png)

This ensures we have the complete conversation flow: user question → assistant tool request → tool results → final assistant response.

## Running Tools and Creating Tool Results

The run_tools() function processes all the tool use requests from Claude's response and creates properly formatted tool result parts. Each tool result includes:

```
run_tools()
```

- The tool use ID (matching the original request)
- The actual output from running the tool
- A status indicating success or error

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558078%2F08_-_006_-_Sending_Tool_Results_05.1748558078391.png)

The function handles both successful tool executions and errors gracefully, wrapping everything in the correct JSON structure that Claude expects.

## Adding Tool Results to the Conversation

Once we have our tool results, we add them to the conversation using add_user_message():

```
add_user_message()
```

```
add_user_message(messages, run_tools(parts))
```

```
add_user_message(messages, run_tools(parts))
```

This creates a user message containing all the tool result parts. The conversation now has the complete back-and-forth needed for Claude to provide a final response.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558079%2F08_-_006_-_Sending_Tool_Results_11.1748558078837.png)

## Final Call to Claude

The last step is sending everything back to Claude. This requires two important elements:

- The complete message history (user → assistant → user)
- The original tool schemas

```
text, parts = chat(messages, tools=[get_current_datetime_schema])
```

```
text, parts = chat(messages, tools=[get_current_datetime_schema])
```

Including the tool schemas is crucial. Without them, Claude would be confused about the tool references in the conversation history and wouldn't understand what get_current_datetime actually does.

```
get_current_datetime
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558079%2F08_-_006_-_Sending_Tool_Results_18.1748558079321.png)

## Success

When everything works correctly, Claude receives the tool results and can provide a complete, informed response. In our example, Claude successfully retrieved the current time and formatted it in a natural response: "The current date and time is 2025-04-03, 12:54:00."

This demonstrates that our tool integration is working properly. While Claude knows the current date, it doesn't have access to real-time information like the exact current time - which is exactly what our tool provided.

The complete tool use cycle is now working: Claude requests a tool, we execute it, return the results, and Claude incorporates that information into its final response to the user.

---

## Multi-Turn conversations with tools

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276759

details

## Multi-Turn conversations with tools

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building multi-turn conversations with tool use requires handling different response types from Claude. When Claude responds, it might need to use a tool, or it might provide a direct answer. Your code needs to handle both scenarios gracefully.

## The Problem with Simple Tool Integration

If you just add tool results to every conversation, you'll run into issues. When Claude answers a simple question like "What is 1+1?", it doesn't need any tools. But if your code always tries to process tool results, you'll end up adding empty messages to your conversation history.

The solution is to check the stop_reason that comes back with every Claude response. This tells you why Claude stopped generating - whether it finished naturally or because it wants to use a tool.

```
stop_reason
```

## Stop Reasons

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558081%2F08_-_007_-_Multi-Turn_Conversations_with_Tools_03.1748558081264.png)

Claude can stop for several reasons:

- "tool_use" - The model wants to call a tool

```
"tool_use"
```

- "end_turn" - Model finished generating its response

```
"end_turn"
```

- "max_tokens" - Hit the output limit

```
"max_tokens"
```

- "stop_sequence" - Encountered a stop sequence you provided

```
"stop_sequence"
```

## Improving the Chat Function

First, update your chat function to return more information. Instead of just returning text and parts separately, return a dictionary with everything you need:

```
def chat(messages, tools=None, system=None, **kwargs):
    # ... existing code ...
    
    return {
        "parts": parts,
        "stop_reason": response["stopReason"],
        "text": "\n".join([p["text"] for p in parts if "text" in p])
    }
```

```
def chat(messages, tools=None, system=None, **kwargs):
    # ... existing code ...
    
    return {
        "parts": parts,
        "stop_reason": response["stopReason"],
        "text": "\n".join([p["text"] for p in parts if "text" in p])
    }
```

This approach extracts all text content from the response parts, which is more robust than assuming the first part is always text.

## Building a Conversation Loop

Create a function that handles the full conversation flow:

```
def run_conversation(messages):
    while True:
        result = chat(messages, tools=[get_current_datetime_schema])
        
        add_assistant_message(messages, result["parts"])
        print(result["text"])
        
        if result["stop_reason"] != "tool_use":
            break
            
        tool_result_parts = run_tools(result["parts"])
        add_user_message(messages, tool_result_parts)
    
    return messages
```

```
def run_conversation(messages):
    while True:
        result = chat(messages, tools=[get_current_datetime_schema])
        
        add_assistant_message(messages, result["parts"])
        print(result["text"])
        
        if result["stop_reason"] != "tool_use":
            break
            
        tool_result_parts = run_tools(result["parts"])
        add_user_message(messages, tool_result_parts)
    
    return messages
```

This loop continues until Claude stops for a reason other than tool use. Each iteration:

- Sends the current messages to Claude
- Adds Claude's response to the message history
- Checks if Claude wants to use a tool
- If so, runs the tools and adds results back to the conversation
- If not, exits the loop

## Testing the Implementation

This approach handles both tool-requiring and simple questions:

```
# Tool-requiring question
messages = []
add_user_message(messages, "What time is it?")
run_conversation(messages)

# Simple question  
messages = []
add_user_message(messages, "What is 1+1?")
run_conversation(messages)
```

```
# Tool-requiring question
messages = []
add_user_message(messages, "What time is it?")
run_conversation(messages)

# Simple question  
messages = []
add_user_message(messages, "What is 1+1?")
run_conversation(messages)
```

For time questions, Claude will use the datetime tool. For math questions, it responds directly without any tool calls. The conversation loop adapts automatically based on Claude's stop reason.

This pattern scales well when you add more tools - the same loop handles any combination of tool use and direct responses, making your conversational AI more robust and natural.

---

## Adding multiple tools

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276761

details

## Adding multiple tools

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we have one tool working, it's time to add the remaining two tools to complete our project: add_duration_to_datetime and set_reminder. The good news is that once you have the foundation in place, adding new tools is straightforward.

```
add_duration_to_datetime
```

```
set_reminder
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748549872%2F08_-_008_-_Adding_Multiple_Tools_00.1748549872529.jpg)

## Pre-built Functions and Schemas

To save time, the implementations for both additional functions are already provided, along with their JSON schema specifications. You can find these in the earlier code cells:

- add_duration_to_datetime - Handles date arithmetic for various time units
- set_reminder - Creates reminders (currently just prints output, but could be extended to integrate with actual reminder systems)

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748549873%2F08_-_008_-_Adding_Multiple_Tools_03.1748549873144.jpg)

Each function comes with a corresponding JSON schema that defines the expected parameters and their types.

## Adding Tools to the Conversation

The first step is to include the new tool schemas in your conversation function. In the run_conversation function, add the additional schemas to the tools array:

```
run_conversation
```

```
tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
]
```

```
tools=[
    get_current_datetime_schema,
    add_duration_to_datetime_schema,
    set_reminder_schema
]
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748549873%2F08_-_008_-_Adding_Multiple_Tools_08.1748549873719.jpg)

## Wiring Up the Tool Functions

Next, you need to update the run_tool function to handle the new tool names. Add two additional conditional branches:

```
run_tool
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    else:
        raise Exception(f"Unknown tool name: {tool_name}")
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    elif tool_name == "set_reminder":
        return set_reminder(**tool_input)
    elif tool_name == "add_duration_to_datetime":
        return add_duration_to_datetime(**tool_input)
    else:
        raise Exception(f"Unknown tool name: {tool_name}")
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748549874%2F08_-_008_-_Adding_Multiple_Tools_12.1748549874200.jpg)

## Testing the Complete System

With all tools connected, you can now test complex workflows that require multiple tool calls. For example, asking Claude to "Set a reminder to go to the doctor. The appointment is in 100 days" will trigger a sequence of operations:

- Get today's date using get_current_datetime

```
get_current_datetime
```

- Add 100 days to that date using add_duration_to_datetime

```
add_duration_to_datetime
```

- Create the reminder using set_reminder

```
set_reminder
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748549874%2F08_-_008_-_Adding_Multiple_Tools_15.1748549874582.jpg)

Claude automatically breaks down the request into logical steps and explains its plan before executing each tool call. The output shows the complete workflow, including the calculated future date and confirmation of the reminder being set.

## Key Takeaway

Once you have the foundational tool use infrastructure in place, adding new tools requires just two simple steps: including the schema in your tools array and adding a case to handle the tool name in your routing function. The initial setup might feel complex, but scaling to multiple tools becomes very manageable.

---

## Batch tool use

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276766

details

## Batch tool use

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude can natively run multiple tools at the same time, but some versions don't take advantage of this as much as you might wish. You can greatly increase the chances of Claude making multiple tool calls in a single message by implementing a batch tool.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558084%2F08_-_009_-_Batch_Tool_Use_00.1748558084170.png)

When Claude sends back tool use parts in a message, there can be more than one tool request in a single response. For example, if you ask "What is March 12th, 2025 + 50 days? Also, what is March 12th, 2025 + 100 days?", Claude could theoretically send back two separate tool use parts - one for each calculation. These operations are completely parallelizable since they don't depend on each other.

However, Claude doesn't always try to parallelize tool calls as much as you'd expect. Instead of making both calls simultaneously, it often makes them sequentially, which is less efficient.

## How the Batch Tool Works

The batch tool is implemented just like any other tool - you need a tool specification and a function to handle when it gets called. The key idea is to create a tool that can invoke multiple other tools simultaneously.

Here's the basic structure of the batch tool specification:

```
{
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
              "type": "string", 
              "description": "The arguments to the tool, encoded as a JSON string"
            }
          },
          "required": ["name", "arguments"]
        }
      }
    },
    "required": ["invocations"]
  }
}
```

```
{
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
              "type": "string", 
              "description": "The arguments to the tool, encoded as a JSON string"
            }
          },
          "required": ["name", "arguments"]
        }
      }
    },
    "required": ["invocations"]
  }
}
```

The tool takes a list of invocations, where each invocation contains the name of a tool to call and its arguments (encoded as a JSON string).

## Implementation

The batch tool implementation involves two main functions:

### The run_batch Function

```
def run_batch(tool_input):
    batch_output = []
    for invocation in tool_input["invocations"]:
        tool_name = invocation["name"]
        args = json.loads(invocation["arguments"])
        
        tool_output = run_tool(tool_name, args)
        batch_output.append({"tool_name": tool_name, "output": tool_output})
    
    return batch_output
```

```
def run_batch(tool_input):
    batch_output = []
    for invocation in tool_input["invocations"]:
        tool_name = invocation["name"]
        args = json.loads(invocation["arguments"])
        
        tool_output = run_tool(tool_name, args)
        batch_output.append({"tool_name": tool_name, "output": tool_output})
    
    return batch_output
```

This function loops through each invocation, extracts the tool name and arguments, calls the appropriate tool using the existing run_tool function, and collects all the results.

```
run_tool
```

### Adding to run_tool

You also need to add a case to your main run_tool function:

```
run_tool
```

```
elif tool_name == "batch_tool":
    return run_batch(tool_input)
```

```
elif tool_name == "batch_tool":
    return run_batch(tool_input)
```

Note that unlike other tools, you pass tool_input directly without using the splat operator (**), since the batch tool needs to handle the raw input structure.

```
tool_input
```

```
**
```

## Results

When you implement the batch tool and run the same date calculation query, instead of seeing two separate tool calls in the message log, you'll see a single call to the batch tool. This single call contains both date calculations as sub-invocations, effectively parallelizing the operations.

The batch tool is particularly useful when you have multiple independent operations that can be executed simultaneously. By "tricking" Claude into using this pattern, you can significantly improve the efficiency of your tool-calling workflows.

---

## Structured data with tools

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276765

details

2
                                    download

## Structured data with tools

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Earlier in this course, we covered how to get structured output from Claude using message pre-fills and stop sequences. While that approach works well and is easy to set up, we can get more reliable output using tools. This method is more complex to implement, but it provides better consistency when extracting structured data like JSON.

## Why Learn Both Approaches?

You might wonder why we didn't just start with tools if they're more reliable. The answer is simple: tools require significantly more setup and complexity. Having both techniques available gives you flexibility - sometimes you'll want the quick prompt-based approach, other times you'll need the reliability that tools provide.

## How Tool-Based Structured Output Works

The core concept is straightforward: instead of asking Claude to format its response as JSON, you create a tool whose input parameters match the exact structure of data you want to extract. Claude then "calls" this tool with the extracted data as arguments.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558131%2F08_-_010_-_Structured_Data_with_Tools_02.1748558130925.png)

Here's the process:

- Write a JSON schema that describes the structure of data you want
- Create a tool with that schema as its input specification
- Send your data and the tool schema to Claude
- Force Claude to use the tool with the toolChoice parameter

```
toolChoice
```

- Extract the structured data from the tool call arguments

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558131%2F08_-_010_-_Structured_Data_with_Tools_05.1748558131586.png)

The flow looks like this: your server sends a prompt asking Claude to analyze data and call a specific tool. Claude responds with a tool use message containing the extracted JSON data. At that point, you simply take the data and end the conversation - no follow-up needed.

## Controlling Tool Usage

When using tools for structured output, you want to guarantee that Claude uses your extraction tool. The toolChoice parameter gives you three options:

```
toolChoice
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558132%2F08_-_010_-_Structured_Data_with_Tools_15.1748558132099.png)

- {"toolChoice": {"auto": {}}} - Model decides if it needs to use a tool (default)

```
{"toolChoice": {"auto": {}}}
```

- {"toolChoice": {"any": {}}} - Model must use a tool, but can choose which one

```
{"toolChoice": {"any": {}}}
```

- {"toolChoice": {"tool": {"name": "tool-name"}}} - Model must use the specified tool

```
{"toolChoice": {"tool": {"name": "tool-name"}}}
```

For structured output, you'll almost always want the third option to ensure Claude uses your extraction tool.

## Practical Example

Let's say you want to extract the title, author, and key topics from an article. First, you'd create a tool schema:

```
article_details_schema = {
    "toolSpec": {
        "name": "article_details",
        "description": "Extracts key information from an article",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the article"
                    },
                    "author": {
                        "type": "string", 
                        "description": "The author's name"
                    },
                    "topics": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of key topics mentioned"
                    }
                },
                "required": ["title", "author", "topics"]
            }
        }
    }
}
```

```
article_details_schema = {
    "toolSpec": {
        "name": "article_details",
        "description": "Extracts key information from an article",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the article"
                    },
                    "author": {
                        "type": "string", 
                        "description": "The author's name"
                    },
                    "topics": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of key topics mentioned"
                    }
                },
                "required": ["title", "author", "topics"]
            }
        }
    }
}
```

Then you'd call Claude with your data and force it to use the tool:

```
messages = []
add_user_message(messages, f"""
Analyze the article below and extract key data. Then call the article_details tool.

<article_text>
{article_text}
</article_text>
""")

result = chat(messages, tools=[article_details_schema], tool_choice="article_details")
```

```
messages = []
add_user_message(messages, f"""
Analyze the article below and extract key data. Then call the article_details tool.

<article_text>
{article_text}
</article_text>
""")

result = chat(messages, tools=[article_details_schema], tool_choice="article_details")
```

Claude will respond with a tool use message containing the extracted data in the exact format you specified. The tool call arguments will contain your structured JSON data, ready to use in your application.

## Key Benefits

- More reliable than prompt-based extraction
- Guaranteed structure matching your schema
- No need for message pre-fills or stop sequences
- Built-in validation through the tool schema
The main tradeoff is complexity - you need to write detailed schemas and handle tool responses. But when you need consistent, reliable structured output, tools are the way to go.

#### Downloads

- 003_structured_data.ipynb
                                                (opens in new tab)
- 004_structured_data_complete.ipynb
                                                (opens in new tab)

---

## Flexible tool extraction

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276763

details

## Flexible tool extraction

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Writing detailed JSON schemas for structured data extraction can be a real pain point when working with AI tools. There's a clever workaround that lets you specify your desired data structure directly in your prompt instead of creating complex schemas.

## The Flexible Schema Approach

Instead of writing a detailed schema for every data extraction task, you can create one generic tool called to_json that accepts any object structure. The key is setting the input schema to allow additional properties, then specifying your exact requirements in the prompt itself.

```
to_json
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558120%2F08_-_011_-_Flexible_Tool_Extraction_01.1748558120376.png)

This approach removes a major pain point - constantly writing and managing large JSON schemas. The results won't be quite as good as a dedicated schema, but you'll still get high-quality JSON output with much less setup work.

## How It Works

The process is straightforward:

- Create a single flexible schema that accepts any object structure
- In your prompt, specify exactly what data structure you want
- Tell Claude to call the to_json tool with your specified structure

```
to_json
```

- Use tool_choice to force Claude to use your tool

```
tool_choice
```

## Setting Up the Prompt

When writing your prompt, be very explicit about the structure you want. Here's an example of how to structure your request:

```
Analyze the article below and extract key data. Then call the to_json tool.

<article_text>
{result["text"]}
</article_text>

When you call to_json, pass in the following structure:
{{
    "title": str # title of the article,
    "author": str # author of the article,
    "topics": List[str] # List of topics mentioned in the article
}}
```

```
Analyze the article below and extract key data. Then call the to_json tool.

<article_text>
{result["text"]}
</article_text>

When you call to_json, pass in the following structure:
{{
    "title": str # title of the article,
    "author": str # author of the article,
    "topics": List[str] # List of topics mentioned in the article
}}
```

## Making the API Call

The API call uses the flexible schema and forces tool usage:

```
flexible_result = chat(messages, tools=[to_json_schema], tool_choice="to_json")
```

```
flexible_result = chat(messages, tools=[to_json_schema], tool_choice="to_json")
```

## Easy Structure Changes

The real advantage becomes clear when you need to modify your data structure. Instead of rewriting an entire schema, you simply update your prompt. Want to add a field for the number of topics? Just add one line:

```
"num_topics": int # Number of topics mentioned
```

```
"num_topics": int # Number of topics mentioned
```

That's it - no schema modifications needed.

## When to Use Each Approach

The flexible schema approach works great for:

- Rapid prototyping and experimentation
- Simple data extraction tasks
- Situations where you frequently change data requirements
Stick with dedicated schemas for:

- Critical production data extraction tasks
- Complex nested data structures
- When you need the highest possible accuracy
The flexible approach gives you about 90% of the quality with 10% of the setup work, making it perfect for most use cases where you need structured data extraction without the schema management overhead.

---

## The text editor tool

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276767

details

1
                                    download

## The text editor tool

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Important Note: Up-to-date tool ID's for the text editor tool can be found in the AWS documentation here: https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-tool-use.html#model-parameters-anthropic-anthropic-defined-tools

The Text Editor Tool is Claude's built-in capability that gives it file system access and text editing abilities. Unlike other tools where you write both the schema and implementation, Claude already knows how to request text editor operations - you just need to handle those requests.

## What the Text Editor Tool Does

This tool gives Claude the ability to work with files and directories like a software engineer would:

- View file or directory contents
- View specific ranges of lines in a file
- Replace text in files
- Create new files
- Insert text at specific line numbers
- Undo recent edits

## How It Works

The Text Editor Tool is different from custom tools because only the JSON schema is built into Claude. You still need to provide the actual implementation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558131%2F08_-_012_-_The_Text_Editor_Tool_02.1748558131131.png)

When you create custom tools, you write both sides - the schema that tells Claude about the tool, and the function that actually does the work. With the Text Editor Tool, Claude already has the schema, but you must write functions to handle Claude's requests to view, edit, or create files.

## Setting Up the Tool

To use the Text Editor Tool, you need to provide specific tool names that vary by Claude version:

```
# For Claude 3.7
text_editor = "text_editor_20250124"

# For Claude 3.5  
text_editor = "text_editor_20241022"
```

```
# For Claude 3.7
text_editor = "text_editor_20250124"

# For Claude 3.5  
text_editor = "text_editor_20241022"
```

You'll also need to modify your chat function to accept the text editor parameter and include it in the model configuration.

## Tool Commands

When Claude wants to use the text editor, it sends back tool use requests with specific commands:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558132%2F08_-_012_-_The_Text_Editor_Tool_15.1748558132756.png)

Your implementation needs to handle all five commands. Here's the basic structure for processing these requests:

```
def run_tool(tool_name, tool_input):
    if tool_name == "str_replace_editor":
        command = tool_input.get("command", "")
        if command == "view":
            path = tool_input.get("path", "")
            return text_editor_tool.view(path)
        elif command == "str_replace":
            path = tool_input.get("path", "")
            old_str = tool_input.get("old_str", "")
            new_str = tool_input.get("new_str", "")
            return text_editor_tool.str_replace(path, old_str, new_str)
        # ... handle other commands
```

```
def run_tool(tool_name, tool_input):
    if tool_name == "str_replace_editor":
        command = tool_input.get("command", "")
        if command == "view":
            path = tool_input.get("path", "")
            return text_editor_tool.view(path)
        elif command == "str_replace":
            path = tool_input.get("path", "")
            old_str = tool_input.get("old_str", "")
            new_str = tool_input.get("new_str", "")
            return text_editor_tool.str_replace(path, old_str, new_str)
        # ... handle other commands
```

## Example: File Analysis

Here's how the tool works in practice. When you ask Claude to "Write a one sentence description of the code in the ./main.py file", this happens:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748558133%2F08_-_012_-_The_Text_Editor_Tool_12.1748558133215.png)

Claude sends a tool use request with {"command": "view", "path": "./main.py"}. Your server uses the TextEditorTool class to read the file and returns the contents. Claude then provides its analysis based on the code it read.

```
{"command": "view", "path": "./main.py"}
```

## Practical Applications

The Text Editor Tool essentially turns Claude into a code assistant that can:

- Read existing code and provide analysis
- Create new files and functions
- Modify existing code
- Set up test files
- Refactor code across multiple files
For example, you could ask Claude to "write a function to calculate pi to the 5th digit in main.py, then create a test.py file to test it." Claude will read the existing file, add the new function, create the test file, and write comprehensive tests - all automatically using the text editor commands.

This makes it possible to build AI-powered development tools similar to modern code editors with integrated AI features, where you can ask for code changes and have them implemented directly in your file system.

#### Downloads

- 005_text_editor_tool.ipynb
                                                (opens in new tab)

---

## Quiz on tool use

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289296

## Quiz on tool use

# Quiz on Tool Use

---

## Introducing Retrieval Augmented Generation

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276780

details

## Introducing Retrieval Augmented Generation

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Retrieval Augmented Generation (RAG) is a technique that helps you work with large documents by breaking them into smaller pieces and only feeding Claude the most relevant chunks for each question. Instead of overwhelming the model with an entire 800-page financial report, RAG lets you extract just the sections that matter for answering specific queries.

## The Problem with Large Documents

When you have a massive document and want to ask Claude specific questions about it, you face a fundamental challenge: how do you get the right information to Claude without hitting limits or degrading performance?

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559472%2F09_-_001_-_Introducing_Retrieval_Augmented_Generation_01.1748559472317.png)

Consider asking "What risk factors does this company have?" about a lengthy financial document. The document contains the answer, but Claude needs access to the relevant content to help you.

## Option 1: Include Everything in the Prompt

The straightforward approach is extracting all text from the document and stuffing it into a single prompt:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559473%2F09_-_001_-_Introducing_Retrieval_Augmented_Generation_04.1748559473609.png)

This method has serious limitations:

- Hard token limits mean very long documents simply won't fit
- Claude becomes less effective with extremely long prompts
- Larger prompts cost more money and take longer to process
- Performance degrades when there's too much information to sift through

## Option 2: Break Documents into Chunks

RAG takes a smarter approach by preprocessing documents into manageable pieces, then retrieving only the relevant chunks for each question.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559475%2F09_-_001_-_Introducing_Retrieval_Augmented_Generation_08.1748559474835.png)

Here's how it works:

- Split the document into smaller chunks (Strategy Outlook, Risk Factors, Balance Sheet, etc.)
- When a user asks a question, analyze what they're looking for
- Find the chunks most relevant to their question
- Include only those relevant chunks in the prompt to Claude

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559475%2F09_-_001_-_Introducing_Retrieval_Augmented_Generation_09.1748559475445.png)

For a question about company risks, the system would identify and retrieve the "Risk Factors" chunk, giving Claude focused, relevant context instead of the entire document.

## Benefits of RAG

- Claude can focus on only the most relevant content
- Scales to very large documents and multiple documents
- Works across document collections, not just single files
- Smaller prompts mean faster processing and lower costs

## Challenges with RAG

RAG introduces complexity that you need to manage:

- Requires a preprocessing step to chunk documents
- Need a search mechanism to find relevant chunks
- Retrieved chunks might not contain all necessary context
- Many different ways to chunk text - which approach works best?
You can chunk documents by equal portions, by headers and sections, by semantic meaning, or other strategies. Each approach has tradeoffs you'll need to evaluate for your specific use case.

## When to Use RAG

RAG shines when you're working with large documents or document collections where users ask specific questions that only require portions of the content. The preprocessing complexity pays off when you need to scale beyond what fits in a single prompt, when you want faster responses, or when you're managing costs across many queries.

The key is analyzing whether the technical overhead of implementing chunking, search, and retrieval makes sense for your particular application. Sometimes the simple "dump everything in a prompt" approach works fine - other times, RAG becomes essential for making your system practical and performant.

---

## Text chunking strategies

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276782

details

2
                                    download

## Text chunking strategies

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Text chunking is one of the most critical steps in building a RAG (Retrieval Augmented Generation) pipeline. How you break up your documents directly impacts the quality of your entire system. A poor chunking strategy can lead to irrelevant context being inserted into your prompts, causing your AI to give completely wrong answers.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559481%2F09_-_002_-_Text_Chunking_Strategies_01.1748559481269.png)

Consider this example: you have a document with sections on medical research and software engineering. If you chunk poorly, a user asking "How many bugs did engineers fix this year?" might get information about medical research instead of software engineering, simply because the medical section happened to contain the word "bug" in a different context.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559482%2F09_-_002_-_Text_Chunking_Strategies_03.1748559481945.png)

This demonstrates why chunking strategy matters so much. The goal is to create chunks that maintain semantic coherence and provide useful context when retrieved.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559482%2F09_-_002_-_Text_Chunking_Strategies_04.1748559482316.png)

## Three Main Chunking Strategies

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559482%2F09_-_002_-_Text_Chunking_Strategies_05.1748559482798.png)

There are three primary approaches to dividing text into chunks:

- Size-based: Divide text into strings of equal length
- Structure-based: Split based on document structure (headers, paragraphs, sections)
- Semantic-based: Group related sentences or sections using NLP techniques

## Size-Based Chunking

Size-based chunking is the most straightforward approach. You simply divide your document into chunks of roughly equal character or word count. It's easy to implement and works reliably across different document types.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559484%2F09_-_002_-_Text_Chunking_Strategies_06.1748559483896.png)

However, this approach has clear downsides:

- Words get cut off mid-sentence
- Chunks lose important context from surrounding text
- Related content might be split across multiple chunks

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559485%2F09_-_002_-_Text_Chunking_Strategies_07.1748559485327.png)

## Adding Overlap

To address the context problem, you can implement an overlap strategy. Each chunk includes some characters from neighboring chunks, providing additional context and ensuring important information isn't lost at chunk boundaries.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559485%2F09_-_002_-_Text_Chunking_Strategies_08.1748559485681.png)

While this creates some duplication, the trade-off is usually worth it for the improved context each chunk receives.

## Structure-Based Chunking

When your documents have consistent formatting (like markdown with clear headers), structure-based chunking can produce excellent results. You split on structural elements like headers, creating chunks that align with the document's natural organization.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559486%2F09_-_002_-_Text_Chunking_Strategies_09.1748559486046.png)

This works beautifully for well-formatted documents but requires guarantees about document structure. It won't work reliably with plain text files or inconsistently formatted documents.

## Implementation Examples

Here are three practical chunking functions you can implement:

### Character-Based Chunking

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

### Sentence-Based Chunking

```
def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    start_idx = 0
    
    while start_idx < len(sentences):
        end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
        current_chunk = sentences[start_idx:end_idx]
        chunks.append(" ".join(current_chunk))
        
        start_idx += max_sentences_per_chunk - overlap_sentences
        
        if start_idx < 0:
            start_idx = 0
    
    return chunks
```

```
def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    start_idx = 0
    
    while start_idx < len(sentences):
        end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
        current_chunk = sentences[start_idx:end_idx]
        chunks.append(" ".join(current_chunk))
        
        start_idx += max_sentences_per_chunk - overlap_sentences
        
        if start_idx < 0:
            start_idx = 0
    
    return chunks
```

### Section-Based Chunking

```
def chunk_by_section(document_text):
    pattern = r"\n## "
    return re.split(pattern, document_text)
```

```
def chunk_by_section(document_text):
    pattern = r"\n## "
    return re.split(pattern, document_text)
```

## Choosing the Right Strategy

Your choice of chunking strategy depends entirely on your specific use case:

- Character-based: Most reliable fallback, works with any document type
- Sentence-based: Good balance of context and meaning for prose
- Section-based: Excellent results when you have structured documents
For user-uploaded documents with no formatting guarantees, character-based chunking is often your safest bet. For well-structured internal documents, section-based chunking can provide superior results. Sentence-based chunking works well for most prose but can struggle with code or technical documents that use periods in unexpected ways.

Remember that chunking is often an iterative process. Start with a simple approach, test it with your specific documents and use cases, then refine based on the quality of results you're getting from your RAG system.

#### Downloads

- 001_chunking.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Text embeddings

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276777

details

2
                                    download

## Text embeddings

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

After breaking a document into chunks, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is fundamentally a search problem - you need to look through all your text chunks and identify the ones that relate to what the user is asking about.

## Finding Relevant Chunks

The challenge is determining which chunks are "related" to a user's question. This isn't as simple as keyword matching - you need to understand the meaning and context of both the question and the chunks.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559464%2F09_-_003_-_Text_Embeddings_02.1748559464021.png)

The most common solution is semantic search, which uses text embeddings to understand what each piece of text is actually about, rather than just looking for exact word matches.

## What Are Text Embeddings?

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559465%2F09_-_003_-_Text_Embeddings_05.1748559464827.png)

Here's how it works:

- You feed text into an embedding model
- The model outputs a long list of numbers (typically 1024 numbers)
- Each number represents a "score" for some quality of the input text
- The numbers range from -1 to +1

## Understanding the Numbers

Each number in an embedding is like a score for some aspect of the text. While we don't know exactly what each position represents, it's helpful to think of them as measuring different qualities.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559465%2F09_-_003_-_Text_Embeddings_07.1748559465427.png)

For example, one number might score "how happy the text is" while another might measure "how much the text talks about oceans." The key point is that we don't actually know what each number represents - the embedding model learns these patterns during training, and they're not human-interpretable.

## Generating Embeddings with Code

Creating embeddings is straightforward. Here's the basic process:

```
def generate_embedding(
    text,
    embedding_model_id="amazon.titan-embed-text-v2:0",
    dimensions=1024,
    normalize=True,
):
    request_body = {
        "inputText": text,
        "dimensions": dimensions,
        "normalize": normalize,
    }
    
    request_json = json.dumps(request_body)
    response = client.invoke_model(
        modelId=embedding_model_id,
        body=request_json,
        accept="application/json",
        contentType="application/json",
    )
    
    response_body = json.loads(response.get("body").read())
    return response_body["embedding"]
```

```
def generate_embedding(
    text,
    embedding_model_id="amazon.titan-embed-text-v2:0",
    dimensions=1024,
    normalize=True,
):
    request_body = {
        "inputText": text,
        "dimensions": dimensions,
        "normalize": normalize,
    }
    
    request_json = json.dumps(request_body)
    response = client.invoke_model(
        modelId=embedding_model_id,
        body=request_json,
        accept="application/json",
        contentType="application/json",
    )
    
    response_body = json.loads(response.get("body").read())
    return response_body["embedding"]
```

When you run this function on a text chunk, you get back a list of 1024 numbers that represent the semantic meaning of that text.

Note that you might need to request access to the Titan embedding model in the AWS Bedrock console. If version 2 isn't available, version 1 works just as well for learning purposes.

## Why Embeddings Matter for RAG

The power of embeddings becomes clear when you realize that similar texts will have similar embedding values. This means you can mathematically compare a user's question to your document chunks and find the most semantically similar ones - even if they don't share the exact same words.

This numerical representation is what makes semantic search possible and much more effective than simple keyword matching for finding relevant context in RAG systems.

#### Downloads

- 002_embeddings.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## The full RAG flow

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276774

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

Next, we convert each text chunk into numerical embeddings. To make this concept clear, let's imagine we have a perfect embedding model that always returns exactly two numbers, and we know what each number represents:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559477%2F09_-_004_-_The_Full_RAG_Flow_02.1748559476941.png)

In our imaginary model:

- First number: How much the text talks about the medical field
- Second number: How much the text talks about software engineering
So our medical research section gets an embedding of [0.97, 0.34] - very medical, somewhat software-related due to the word "bug". The software engineering section gets [0.30, 0.97] - very software-focused, but "infection vectors" has medical connotations.

```
[0.97, 0.34]
```

```
[0.30, 0.97]
```

## Normalization

Before storing these embeddings, they go through a normalization process that scales each vector to have a magnitude of 1.0. This is typically handled automatically by your embedding API, but it's important to understand that it happens.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559477%2F09_-_004_-_The_Full_RAG_Flow_06.1748559477375.png)

After normalization, our embeddings become [0.944, 0.331] and [0.295, 0.955]. We can visualize these on a unit circle where each point lies exactly on the circle's edge.

```
[0.944, 0.331]
```

```
[0.295, 0.955]
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559478%2F09_-_004_-_The_Full_RAG_Flow_07.1748559477776.png)

## Step 3: Store in Vector Database

The normalized embeddings get stored in a vector database - a specialized database optimized for storing, comparing, and searching through long lists of numbers like our embeddings.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559478%2F09_-_004_-_The_Full_RAG_Flow_08.1748559478460.png)

At this point, we pause. All the work so far has been preprocessing that happens ahead of time. Now we wait for a user to submit a query.

## Step 4: Process User Query

When a user asks a question like "I'm curious about the company. In particular, what did the software engineering dept do this year?", we run their query through the same embedding model.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559479%2F09_-_004_-_The_Full_RAG_Flow_09.1748559478918.png)

This query gets embedded as [0.1, 0.89] - low medical score, high software engineering score. After normalization, it becomes [0.112, 0.993].

```
[0.1, 0.89]
```

```
[0.112, 0.993]
```

## Step 5: Find Similar Embeddings

Now we ask the vector database: "Find the stored embedding that's closest to this user query embedding." The database returns the software engineering section because it's the most similar.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559479%2F09_-_004_-_The_Full_RAG_Flow_11.1748559479296.png)

## How Similarity Works: Cosine Similarity

The vector database uses cosine similarity to determine which embeddings are most similar. This measures the cosine of the angle between two vectors.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559479%2F09_-_004_-_The_Full_RAG_Flow_14.1748559479684.png)

Key points about cosine similarity:

- Results range from -1 to 1
- Values close to 1 mean very similar
- Values close to 0 mean perpendicular (unrelated)
- Values close to -1 mean completely opposite
The calculation uses the dot product formula: cos(a) = (A · B) / (||A|| · ||B||)

```
cos(a) = (A · B) / (||A|| · ||B||)
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559480%2F09_-_004_-_The_Full_RAG_Flow_15.1748559480037.png)

In our example, the user query has a cosine similarity of 0.983 with the software engineering chunk and only 0.398 with the medical research chunk. The software engineering chunk is clearly the better match.

## Cosine Distance

You'll often see "cosine distance" in vector database documentation. This is simply 1 - cosine similarity, which gives us an easier-to-interpret number where:

```
1 - cosine similarity
```

- Values close to 0 mean high similarity
- Larger values mean less similarity

## Step 6: Build the Final Prompt

Finally, we take the user's question and the most relevant text chunk we found, then combine them into a prompt for Claude:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559480%2F09_-_004_-_The_Full_RAG_Flow_18.1748559480418.png)

The prompt includes both the user's question and the relevant context from our document, allowing Claude to provide an informed answer based on the specific information in our knowledge base.

## The Complete Flow

That's the entire RAG pipeline from start to finish:

- Chunk source documents
- Generate embeddings for each chunk
- Store embeddings in a vector database
- When a user asks a question, embed their query
- Find the most similar stored embeddings using cosine similarity
- Add the relevant chunks to a prompt with the user's question
- Send the enhanced prompt to Claude for a response
Understanding this process and the math behind it will help you work effectively with vector databases and debug issues when your RAG system isn't returning the results you expect.

---

## Implementing the RAG flow

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276781

details

3
                                    download

## Implementing the RAG flow

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

This walkthrough demonstrates the complete RAG (Retrieval-Augmented Generation) implementation using a practical example. We'll build a vector database from scratch and execute all five steps of the RAG workflow using a sample report document.

## Setting Up the Vector Database

The implementation uses a custom VectorIndex class that handles storing embeddings and performing similarity searches. This class provides the core functionality we need for our vector database operations.

```
VectorIndex
```

## The Five-Step RAG Implementation

### Step 1: Chunk the Text by Section

First, we load and chunk our source document using the same section-based chunking approach from earlier:

```
with open("./report.md", "r") as f:
    text = f.read()

chunks = chunk_by_section(text)
```

```
with open("./report.md", "r") as f:
    text = f.read()

chunks = chunk_by_section(text)
```

This breaks our report into logical sections that can be processed independently.

### Step 2: Generate Embeddings for Each Chunk

Next, we create embeddings for every chunk using a list comprehension:

```
embeddings = [generate_embedding(chunk) for chunk in chunks]
```

```
embeddings = [generate_embedding(chunk) for chunk in chunks]
```

This step involves multiple API calls, so it takes some time to complete. Each chunk gets converted into a numerical vector representation.

### Step 3: Store Embeddings in the Vector Database

Now we create our vector store and populate it with both embeddings and their associated text:

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

The key insight here is that we store both the embedding and the original text. Just getting back a list of numbers isn't useful - we need the actual text content that corresponds to those embeddings. This metadata allows us to retrieve meaningful results later.

### Step 4: Generate User Query Embedding

When a user asks a question, we convert it to the same embedding format:

```
user_embedding = generate_embedding("What did the software engineering dept do last year?")
```

```
user_embedding = generate_embedding("What did the software engineering dept do last year?")
```

This creates a vector representation of the user's question that can be compared against our stored embeddings.

### Step 5: Search and Retrieve Relevant Chunks

Finally, we search our vector store to find the most similar content:

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

This returns the two most relevant chunks along with their cosine distance scores. Lower distances indicate higher similarity.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559528%2F09_-_005_-_Implementing_the_Rag_Flow_10.1748559528329.png)

## Understanding the Results

The search returns results ranked by relevance. In our example, the software engineering section had the lowest distance (0.71), making it the most relevant match. The methodology section came second with a distance of 0.72.

The distance metric helps you understand how confident the system is about the relevance of each result. Closer distances mean better matches to the user's query.

## Why Store Text with Embeddings

A crucial design decision is storing the original text alongside each embedding. Without this, you'd only get back arrays of numbers, which aren't useful for generating responses. By including the source text, you can immediately use the retrieved chunks to provide context for your language model.

This completes the core RAG workflow, though there are additional optimizations and improvements that can enhance performance in real-world scenarios.

#### Downloads

- 003_vectordb_completed.ipynb
                                                (opens in new tab)
- 003_vectordb.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## BM25 lexical search

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276776

details

3
                                    download

## BM25 lexical search

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When building a RAG pipeline, you'll quickly discover that semantic search alone doesn't always return the best results. Sometimes you need exact keyword matches that semantic search might miss. The solution is to combine semantic search with lexical search using a technique called BM25.

## The Problem with Semantic Search Alone

Let's say you're searching for a specific incident ID like "INC-2023-Q4-011" in a document. While this exact term appears multiple times in relevant sections, semantic search might return unrelated sections that seem semantically similar but don't actually contain the specific information you need.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559532%2F09_-_006_-_BM25_Lexical_Search_04.1748559532637.png)

This happens because semantic search focuses on meaning rather than exact text matches. When you need precise keyword matching, you need a different approach.

## Hybrid Search Strategy

The solution is to run both semantic and lexical searches in parallel, then merge the results. This gives you the best of both worlds:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559533%2F09_-_006_-_BM25_Lexical_Search_05.1748559533271.png)

- Semantic search - Finds conceptually related content using embeddings
- Lexical search - Finds exact keyword matches using classic text search
- Merged results - Combines both approaches for better overall relevance

## How BM25 Works

BM25 (Best Match 25) is a popular algorithm for lexical search in RAG pipelines. Here's how it processes a search query:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559533%2F09_-_006_-_BM25_Lexical_Search_07.1748559533735.png)

The algorithm follows these key steps:

- Tokenize the query - Break the user's question into individual terms
- Count term frequency - See how often each term appears across all documents
- Weight terms by rarity - Terms used less frequently get higher importance scores
- Score documents - Find text chunks that contain more instances of the higher-weighted terms
The key insight is that rare terms like "INC-2023-Q4-011" are much more important for search relevance than common words like "a" or "the".

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

The BM25 implementation maintains a similar API to your vector store, with add_document() and search() methods. This consistency makes it easy to use both systems together.

```
add_document()
```

```
search()
```

## Better Search Results

When you run the same query through BM25 that failed with semantic search alone, you get much better results. The algorithm correctly prioritizes sections that contain the exact incident ID, ranking them higher than sections that might be semantically related but don't contain the specific term you're looking for.

The search results now properly surface the Software Engineering section and Cybersecurity section that actually discuss the incident, rather than returning unrelated content like Financial Analysis.

## Next Steps

Now that you have both semantic and lexical search systems working independently, the next step is to merge their results. This hybrid approach will give you the semantic understanding of embeddings combined with the precision of keyword matching, creating a more robust search experience for your RAG pipeline.

#### Downloads

- 004_bm25.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)
- 004_bm25_completed.ipynb
                                                (opens in new tab)

---

## A multi-search RAG pipeline

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276779

details

3
                                    download

## A multi-search RAG pipeline

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When you have both semantic search (vector embeddings) and lexical search (BM25) working independently, the next step is combining them into a unified search pipeline. This hybrid approach leverages the strengths of both methods to deliver more accurate results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559538%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_00.1748559537903.png)

## Building a Unified Interface

Both search implementations share nearly identical APIs - they both have add_document() and search() methods. This consistency makes it straightforward to wrap them in a single Retriever class that coordinates between the two approaches.

```
add_document()
```

```
search()
```

```
Retriever
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559538%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_01.1748559538475.png)

The Retriever acts as a coordinator that:

- Receives a user's question
- Forwards it to both the VectorIndex and BM25Index
- Collects results from both systems
- Merges the results using a ranking algorithm

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559539%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_02.1748559538996.png)

## Reciprocal Rank Fusion

The challenge lies in merging results from different search methods. Each system returns results with different scoring mechanisms, so you can't simply combine scores directly. Instead, we use a technique called Reciprocal Rank Fusion (RRF).

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559539%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_04.1748559539431.png)

Here's how RRF works with a practical example. Suppose your VectorIndex returns results ranked as: Section 2, Section 7, Section 6. Meanwhile, your BM25Index returns: Section 6, Section 2, Section 7.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559540%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_05.1748559539898.png)

To merge these results, you create a combined table showing each text chunk's rank from both systems:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559540%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_06.1748559540379.png)

The RRF formula calculates a score for each document:

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```

Where k is a constant (typically 60, though 1 works well for clearer results) and rank_i(d) is the rank of document d in the i-th ranking system.

```
k
```

```
rank_i(d)
```

```
d
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559541%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_07.1748559540941.png)

For each text chunk, you calculate:

- Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
- Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
- Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75
After sorting by score, the final ranking becomes: Section 2 (first), Section 6 (second), Section 7 (third).

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559541%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_08.1748559541399.png)

## Implementation

The Retriever class implementation is straightforward:

```
class Retriever:
    def __init__(self, *indexes):
        self._indexes = list(indexes)
    
    def add_document(self, document):
        for index in self._indexes:
            index.add_document(document)
    
    def search(self, query_text, k=1, k_rrf=60):
        # Get results from all indexes
        all_results = []
        for idx, results in enumerate(all_results):
            for rank, (doc, _) in enumerate(results):
                # Track document ranks across systems
                # Apply RRF formula
                # Return merged, sorted results
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
        all_results = []
        for idx, results in enumerate(all_results):
            for rank, (doc, _) in enumerate(results):
                # Track document ranks across systems
                # Apply RRF formula
                # Return merged, sorted results
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559542%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_11.1748559541923.png)

The key insight is that the RRF algorithm creates a unified ranking by considering how well each document performs across all search systems, rather than relying on any single scoring method.

## Testing the Hybrid Approach

When testing with a query like "what happened with INC-2023-Q4-011?", the hybrid approach delivers significantly better results than either method alone. Instead of getting unexpected results from pure vector search, you now get the most relevant cybersecurity incident report first, followed by related software engineering content.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559542%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_16.1748559542347.png)

## Extensibility

The beauty of this design is its modularity. Since each search index implements the same interface (add_document() and search()), you can easily add new search methodologies to the system. Whether it's a different embedding model, a specialized domain search, or any other retrieval technique, as long as it follows the established API, it integrates seamlessly into the hybrid pipeline.

```
add_document()
```

```
search()
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559543%2F09_-_007_-_A_Multi-Search_RAG_Pipeline_18.1748559542925.png)

This hybrid search approach represents a significant improvement in retrieval accuracy by combining the semantic understanding of vector search with the precise keyword matching of lexical search, all unified through the mathematically sound RRF ranking algorithm.

#### Downloads

- 005_hybrid_completed.ipynb
                                                (opens in new tab)
- 005_hybrid.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Reranking results

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276775

details

2
                                    download

## Reranking results

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The hybrid retrieval approach we've built works well, but there are still some rough edges. When you search for specific terms or use abbreviations, the results might not be perfectly ordered. For example, asking "What did the eng team do with INC-2023-Q4-011?" might return the cybersecurity section first, even though the software engineering section is more relevant to that specific query.

## LLM-Based Re-ranking

Re-ranking adds another post-processing step after merging results from your vector index and BM25 index. The concept is straightforward: take your search results and ask Claude to reorder them based on relevance to the user's question.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559531%2F09_-_008_-_Reranking_Results_05.1748559531205.png)

Here's how the process works:

- Run your hybrid search (vector + BM25) as usual
- Merge the results like before
- Pass the merged results to a re-ranker function
- The re-ranker sends everything to Claude with a specific prompt
- Claude returns a reordered list of the most relevant documents

## System Prompts

The re-ranking prompt is designed to be clear and specific. You provide Claude with the user's question and all the documents that seem relevant, then ask for a simple task: return the most relevant documents in order of decreasing relevance.

A typical prompt structure looks like this:

```
You are tasked with finding the documents most relevant to a user's question.

<user_question>
What happened with INC-2023-Q4-011?
</user_question>

Here are documents that may be relevant:
<documents>
<document>Section 10...</document>
<document>Section 2...</document>
<document>Section 7...</document>
<document>Section 6...</document>
</documents>

Return the 3 most relevant docs, in order of decreasing relevance.
```

```
You are tasked with finding the documents most relevant to a user's question.

<user_question>
What happened with INC-2023-Q4-011?
</user_question>

Here are documents that may be relevant:
<documents>
<document>Section 10...</document>
<document>Section 2...</document>
<document>Section 7...</document>
<document>Section 6...</document>
</documents>

Return the 3 most relevant docs, in order of decreasing relevance.
```

## Efficiency Considerations

Asking Claude to return full text chunks would be inefficient - you'd be waiting for Claude to copy large amounts of text. Instead, assign each text chunk a unique ID ahead of time. Then ask Claude to return just those IDs in the correct order.

This approach is much faster because Claude only needs to return a simple list like ["1p5g", "51n3", "ab83"] instead of copying entire document sections.

```
["1p5g", "51n3", "ab83"]
```

## Implementation

The re-ranker function gets called automatically by your retriever after the initial hybrid search. Here's the basic structure:

```
def reranker_fn(docs, query_text, k):
    # Format documents with IDs
    joined_docs = "\n".join([
        f"<document><document_id>{doc['id']}</document_id>"
        f"<document_content>{doc['content']}</document_content></document>"
        for doc in docs
    ])
    
    # Create prompt with user question and documents
    prompt = f"""You are about to be given a set of documents...
    {query_text}
    {joined_docs}
    """
    
    # Get Claude's response and parse the document IDs
    result = chat(messages, stop_sequences=["```"])
    return json.loads(result["text"])["document_ids"]
```

```
def reranker_fn(docs, query_text, k):
    # Format documents with IDs
    joined_docs = "\n".join([
        f"<document><document_id>{doc['id']}</document_id>"
        f"<document_content>{doc['content']}</document_content></document>"
        for doc in docs
    ])
    
    # Create prompt with user question and documents
    prompt = f"""You are about to be given a set of documents...
    {query_text}
    {joined_docs}
    """
    
    # Get Claude's response and parse the document IDs
    result = chat(messages, stop_sequences=["```"])
    return json.loads(result["text"])["document_ids"]
```

## Results

When you test the re-ranker with queries like "What did the eng team do with INC-2023-Q4-011?", you should see more relevant results at the top. Claude understands the context and can identify that a query about the engineering team should prioritize the software engineering section over other sections that merely mention the incident.

The trade-off is clear: re-ranking increases latency because you need to wait for Claude's response, but it significantly improves search accuracy by leveraging Claude's understanding of context and relevance.

#### Downloads

- 006_reranking.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Contextual retrieval

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276778

details

2
                                    download

## Contextual retrieval

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Contextual retrieval is a technique that improves RAG pipeline accuracy by solving a fundamental problem: when you split a document into chunks, each chunk loses its connection to the broader document context.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559588%2F09_-_009_-_Contextual_Retrieval_00.1748559588379.png)

The basic idea is simple. After chunking your source document, you ask Claude to add context to each chunk before storing it in your retriever database. This pre-processing step helps "situate" each chunk within the larger document.

## How It Works

For each text chunk, you send both the chunk and the original source document to Claude with a prompt like this:

```
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
```

```
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
```

Claude might generate context like: "This section is from a larger report about a cross-discipline group. It includes mention of INC-2023-04-011, which is also mentioned in the Cybersecurity Analysis section."

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559589%2F09_-_009_-_Contextual_Retrieval_04.1748559589111.png)

You then combine this generated context with the original chunk text to create a "contextualized chunk" that gets stored in your vector and BM25 indexes.

## Handling Large Documents

If your source document is too large to fit in a single prompt, you can provide a reduced set of context instead of the entire document.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559589%2F09_-_009_-_Contextual_Retrieval_08.1748559589486.png)

For any given chunk you're contextualizing, include:

- A few chunks from the start of the document (often containing summaries or abstracts)
- Chunks immediately preceding the target chunk (providing local context)
This approach gives Claude enough information to generate meaningful context without overwhelming the prompt with the entire document.

## Implementation Example

Here's a basic implementation of the contextual retrieval function:

```
def add_context(text_chunk, source_text):
    prompt = f"""
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
    prompt = f"""
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

When processing your document chunks, you'd loop through each one and generate contextualized versions:

```
# Add context to each chunk, then add to the retriever
for i, chunk in enumerate(chunks):
    # Build context from start chunks and preceding chunks
    context_parts = []
    context_parts.extend(chunks[:min(num_start_chunks, len(chunks))])
    
    start_idx = max(0, i - num_prev_chunks)
    context_parts.extend(chunks[start_idx:i])
    
    context = "\n".join(context_parts)
    
    contextualized_chunk = add_context(chunk, context)
    retriever.add_document({"content": contextualized_chunk})
```

```
# Add context to each chunk, then add to the retriever
for i, chunk in enumerate(chunks):
    # Build context from start chunks and preceding chunks
    context_parts = []
    context_parts.extend(chunks[:min(num_start_chunks, len(chunks))])
    
    start_idx = max(0, i - num_prev_chunks)
    context_parts.extend(chunks[start_idx:i])
    
    context = "\n".join(context_parts)
    
    contextualized_chunk = add_context(chunk, context)
    retriever.add_document({"content": contextualized_chunk})
```

## Expected Results

The generated context provides valuable information about document structure and relationships. For example, Claude might describe a chunk as "Section 2 of an Annual Interdisciplinary Research Review, detailing software engineering efforts to resolve stability issues in Project Phoenix. It follows the Methodology section and precedes Financial Analysis, forming part of a comprehensive report that covers ten research domains across the organization."

This additional context helps the retrieval system better understand not just what each chunk contains, but how it fits into the larger document structure and relates to other sections. While you might not see dramatic improvements with simple documents, contextual retrieval becomes increasingly valuable as your documents become more complex with intricate cross-references and dependencies between sections.

#### Downloads

- 007_contextual.ipynb
                                                (opens in new tab)
- report.md
                                                (opens in new tab)

---

## Quiz on Retrieval Augmented Generation

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289295

## Quiz on Retrieval Augmented Generation

# Quiz on Retrieval Augmented Generation

---

## Extended thinking

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276788

details

2
                                    download

## Extended thinking

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Extended thinking is Claude's advanced feature that gives the model time to reason through complex problems before generating a final response. Think of it as Claude's internal monologue - you can see how it approaches your problem step by step.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559587%2F10_-_001_-_Extended_Thinking_01.1748559587414.png)

## How Extended Thinking Works

When you enable extended thinking, Claude's response includes two parts instead of one:

- Reasoning Content Part - Claude's internal thinking process
- Text Part - The final response you actually wanted

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559588%2F10_-_001_-_Extended_Thinking_03.1748559587928.png)

The reasoning content shows you exactly how Claude breaks down your problem, what it considers, and how it arrives at its final answer. This transparency can be incredibly valuable for understanding and debugging complex tasks.

## Trade-offs to Consider

Extended thinking comes with clear benefits and costs:

- Better accuracy on complex tasks
- Higher cost - you pay for all thinking tokens
- Increased latency - thinking takes time
The key decision point is simple: use your evaluations. If you've already optimized your prompt but still aren't getting the accuracy you need, that's when extended thinking becomes worth considering.

## The Signature System

One important detail you'll notice immediately is the cryptographic signature attached to reasoning content:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559588%2F10_-_001_-_Extended_Thinking_04.1748559588322.png)

This signature ensures you can't modify the thinking text. If you want to include Claude's previous reasoning in a follow-up conversation, the signature verifies the content hasn't been tampered with. This prevents potential safety issues from modified reasoning text.

## Redacted Content

Sometimes Claude's thinking gets flagged by safety systems. When this happens, you'll receive a redactedContent field instead of readable thinking text:

```
redactedContent
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559589%2F10_-_001_-_Extended_Thinking_06.1748559588844.png)

The redacted content is encrypted but still functional - you can pass it back to Claude in future conversations without losing context. It's just not readable to you as a developer.

## Implementation

To enable extended thinking, you need to modify your API call with two parameters:

```
additional_model_fields["thinking"] = {
    "type": "enabled",
    "budget_tokens": thinking_budget
}
```

```
additional_model_fields["thinking"] = {
    "type": "enabled",
    "budget_tokens": thinking_budget
}
```

The thinking_budget controls how many tokens Claude can spend on reasoning. The minimum is 1024 tokens, but you might need more for complex problems. Like everything else with Claude, use your evaluations to find the right budget for your use case.

```
thinking_budget
```

Here's how the updated chat function looks:

```
def chat(
    messages,
    system=None,
    temperature=1.0,
    stop_sequences=[],
    tools=None,
    tool_choice="auto",
    text_editor=None,
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
    tool_choice="auto",
    text_editor=None,
    thinking=False,
    thinking_budget=1024
):
```

## Testing Your Implementation

When building applications that handle extended thinking, you'll want to test both normal reasoning content and redacted content scenarios. There's actually a special test string that forces Claude to return redacted content - useful for making sure your code handles both cases properly.

The most important takeaway about extended thinking is that the decision to use it should always be data-driven. Run your evaluations first, optimize your prompts, and only then consider extended thinking if you need that extra boost in accuracy for complex tasks.

#### Downloads

- 001_thinking_completed.ipynb
                                                (opens in new tab)
- 001_thinking.ipynb
                                                (opens in new tab)

---

## Image support

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276789

details

3
                                    download

## Image support

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude's vision capabilities allow you to include images in your messages and ask Claude to analyze, compare, count objects, or perform virtually any visual task you can imagine. This opens up powerful possibilities for applications ranging from document analysis to automated assessments.

## Image Handling Basics

When working with images in Claude, you need to understand a few key limitations:

- Up to 20 images across all messages in a single request
- Max size of 3.75MB
- Max height/width of 8000px
- Each image counts as a certain number of tokens: tokens = (width px × height px) / 750

```
tokens = (width px × height px) / 750
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559593%2F10_-_002_-_Image_Support_01.1748559593554.png)

To include an image, you add it as another type of message part. For each image you want to send, you include one image part in your user message. The structure looks like this:

```
with open("image.png", "rb") as f:
    image_bytes = f.read()

add_user_message(messages, [
    {
        "image": {
            "format": "png",
            "source": {"bytes": image_bytes}
        }
    },
    {"text": "What do you see in this image?"}
])
```

```
with open("image.png", "rb") as f:
    image_bytes = f.read()

add_user_message(messages, [
    {
        "image": {
            "format": "png",
            "source": {"bytes": image_bytes}
        }
    },
    {"text": "What do you see in this image?"}
])
```

## Multiple Images

You can send multiple images in a single message by adding multiple image parts. Claude can then analyze relationships between images, compare them, or answer questions that require understanding multiple visual inputs.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559594%2F10_-_002_-_Image_Support_03.1748559594058.png)

## Prompting Techniques

The most important thing to understand about Claude's vision capabilities is that all the same prompting engineering techniques apply to images. You can dramatically increase Claude's vision accuracy by providing guidelines, analysis steps, or using one-shot/multi-shot examples.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559594%2F10_-_002_-_Image_Support_04.1748559594501.png)

For example, instead of simply asking "How many marbles are in this image?", you can provide a structured approach:

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

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559595%2F10_-_002_-_Image_Support_05.1748559595686.png)

Another effective technique is one-shot prompting, where you provide an example image with the correct analysis before asking Claude to analyze your target image:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559596%2F10_-_002_-_Image_Support_07.1748559596109.png)

## Real-World Example: Fire Risk Assessments

A practical application of Claude's vision capabilities is automated fire risk assessment for insurance companies. Instead of sending inspectors to each property, companies can use high-resolution satellite imagery and ask Claude to evaluate fire risks.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559596%2F10_-_002_-_Image_Support_08.1748559596731.png)

The system can analyze several key factors:

- Dense, close-packed trees near the residence
- Difficult access routes for emergency vehicles
- Branches overhanging the residence
- Overall tree density and spacing
Here's how you might structure such an analysis:

```
with open('./images/prop7.png', 'rb') as f:
    image_bytes = f.read()

messages = []

add_user_message(messages, [
    {"image": {"format": "png", "source": {"bytes": image_bytes}}},
    {"text": prompt}
])

response = chat(messages)
```

```
with open('./images/prop7.png', 'rb') as f:
    image_bytes = f.read()

messages = []

add_user_message(messages, [
    {"image": {"format": "png", "source": {"bytes": image_bytes}}},
    {"text": prompt}
])

response = chat(messages)
```

The key to success with this type of complex visual analysis is providing detailed, structured prompts that guide Claude through specific analysis steps rather than asking for a simple assessment.

Remember: when working with images, don't fall into the trap of using simple prompts. Apply the same prompt engineering techniques you've learned for text-based interactions to dramatically improve Claude's visual analysis accuracy.

#### Downloads

- 002_images.ipynb
                                                (opens in new tab)
- 002_images_completed.ipynb
                                                (opens in new tab)
- images.zip
                                                (opens in new tab)

---

## PDF support

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/308839

details

2
                                    download

## PDF support

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude can read and analyze PDF documents just as easily as it handles images. This capability opens up powerful possibilities for document analysis, summarization, and question-answering workflows.

## Setting Up PDF Processing

To work with PDFs, you'll need to make a few key changes to the standard message structure. The process is similar to image handling, but with some important differences in the document specification.

First, read your PDF file as binary data:

```
with open("./earth.pdf", "rb") as f:
    file_bytes = f.read()
```

```
with open("./earth.pdf", "rb") as f:
    file_bytes = f.read()
```

## Document Message Structure

The message structure for PDFs differs from images in several ways. Instead of an "image" object, you'll use a "document" object with these required fields:

```
add_user_message(
    messages,
    [
        {"document": {"format": "pdf", "name": "earth", "source": {"bytes": file_bytes}}},
        {"text": "Summarize this document in one sentence"},
    ],
)
```

```
add_user_message(
    messages,
    [
        {"document": {"format": "pdf", "name": "earth", "source": {"bytes": file_bytes}}},
        {"text": "Summarize this document in one sentence"},
    ],
)
```

Key points about the document structure:

- Use "document" instead of "image"

```
"document"
```

```
"image"
```

- Set "format": "pdf"

```
"format": "pdf"
```

- Include a "name" field with the filename without extension

```
"name"
```

- The "source" contains the file bytes

```
"source"
```

When you run this code, Claude analyzes the entire PDF content and provides a comprehensive response. In this case, it successfully summarized the Earth Wikipedia article, demonstrating its ability to process multi-page documents with complex layouts, images, and structured information.

## What Claude Can Do with PDFs

Claude can handle various PDF processing tasks:

- Extract and summarize key information
- Answer specific questions about document content
- Analyze document structure and formatting
- Process multi-page documents efficiently
- Work with PDFs containing both text and images
The PDF processing capability becomes even more powerful when combined with other features like citations, which allow Claude to reference specific parts of the document in its responses. This makes it particularly useful for research, document analysis, and content extraction workflows.

#### Downloads

- 003_pdf.ipynb
                                                (opens in new tab)
- earth.pdf
                                                (opens in new tab)

---

## Citations

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/308840

details

## Citations

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

When working with PDFs in Claude, one of the biggest challenges is trust. Users often have to take it on faith that the AI is correctly interpreting the document contents. Claude's citations feature directly addresses this problem by showing exactly where information comes from in your source documents.

## Enabling Citations

To enable citations in your PDF processing, you need to add a single parameter to your document configuration:

```
with open("./earth.pdf", "rb") as f:
    file_bytes = f.read()

messages = []

add_user_message(
    messages,
    [
        {
            "document": {
                "format": "pdf",
                "name": "earth",
                "source": {"bytes": file_bytes},
                "citations": {"enabled": True}
            }
        },
        {"text": "How were Earth's atmosphere and oceans formed?"},
    ]
)

response = chat(messages)
```

```
with open("./earth.pdf", "rb") as f:
    file_bytes = f.read()

messages = []

add_user_message(
    messages,
    [
        {
            "document": {
                "format": "pdf",
                "name": "earth",
                "source": {"bytes": file_bytes},
                "citations": {"enabled": True}
            }
        },
        {"text": "How were Earth's atmosphere and oceans formed?"},
    ]
)

response = chat(messages)
```

The key addition is "citations": {"enabled": True} in the document dictionary. This tells Claude to track where it finds information and include citation data in its response.

```
"citations": {"enabled": True}
```

## Understanding Citation Responses

When citations are enabled, Claude's response structure changes significantly. Instead of just returning text, you get multiple parts:

- Text parts - The regular response content you're familiar with
- Citations content parts - New structured data that maps statements back to source locations
The citations content includes detailed information about where Claude found supporting evidence for each statement, including the specific document, page numbers, and even the exact text that influenced its response.

## Why Citations Matter

Citations provide several key benefits for PDF-based applications:

- Verification - Users can check Claude's work by going back to the source
- Confidence - Knowing where information comes from builds trust in AI responses
- Transparency - The AI's reasoning process becomes visible and auditable
- Accuracy - Citations encourage more careful information extraction
This feature is particularly valuable in professional, academic, or research contexts where accuracy and source attribution are critical. Instead of treating Claude as a black box, citations turn it into a transparent research assistant that shows its work.

---

## Prompt caching

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276786

details

## Prompt caching

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt caching is a feature that speeds up Claude's responses and reduces the cost of text generation by reusing computational work from previous requests. To understand how this works, let's first look at what normally happens inside Claude during a typical request.

## How Claude Normally Processes Requests

When you send a message to Claude, a lot happens behind the scenes before you get a response back. Claude doesn't just immediately start generating text - it first does extensive work on your input message.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559581%2F10_-_003_-_Prompt_Caching_01.1748559581315.png)

Here's what Claude does with your message:

- Tokenize the prompt
- Create embeddings for each token
- Add context based on surrounding text
- Generate output text

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559582%2F10_-_003_-_Prompt_Caching_04.1748559581783.png)

All of this preprocessing work happens before Claude generates any actual response. Once Claude finishes processing your request and sends back the response, it throws away all the computational work it just did.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559582%2F10_-_003_-_Prompt_Caching_06.1748559582304.png)

## The Problem with Throwing Away Work

This creates an inefficiency when you're having conversations with Claude. Let's say you make a follow-up request that includes the same message from earlier, plus Claude's previous response, plus a new message to continue the conversation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559583%2F10_-_003_-_Prompt_Caching_08.1748559582865.png)

When Claude sees that original message again, it has to redo all the same computational work it just threw away moments earlier. Claude essentially thinks: "I just processed this exact message and did all this work, then threw it away. Now I have to do it all over again."

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559583%2F10_-_003_-_Prompt_Caching_10.1748559583299.png)

## How Prompt Caching Solves This

Prompt caching addresses this inefficiency by saving the computational work instead of discarding it. Here's how it works:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559583%2F10_-_003_-_Prompt_Caching_14.1748559583675.png)

When Claude processes your initial request, instead of throwing away all the preprocessing work, it stores that work in a cache. The cache acts like a lookup table that maps specific input messages to their corresponding computational results.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559584%2F10_-_003_-_Prompt_Caching_16.1748559584103.png)

When you make a follow-up request that includes the same content, Claude can check its cache and reuse the previous work instead of starting from scratch.

## Key Benefits and Limitations

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559584%2F10_-_003_-_Prompt_Caching_18.1748559584591.png)

Prompt caching offers several advantages:

- Requests that use cached content are cheaper and faster to execute
- Initial request will write to the cache
- Follow up requests can read from the cache
- Cache lives for 5 minutes
- Only useful if you're repeatedly sending the same content (but this happens extremely frequently)
The cache has a 5-minute lifespan, so it's most beneficial for conversations or workflows where you're making multiple requests with overlapping content within a short timeframe. This pattern is actually very common in real applications - think about chatbots, document analysis tools, or any system that maintains conversation context.

Prompt caching is particularly valuable because many AI applications do repeatedly send the same content. Whether it's system prompts, conversation history, or large documents being analyzed, the same text often appears across multiple requests in a session.

---

## Rules of prompt caching

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276785

details

## Rules of prompt caching

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Prompt caching in Claude works by storing the computational work done on messages so it can be reused in follow-up requests. This makes subsequent requests both cheaper and faster to execute, but only when you're repeatedly sending the same content.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559639%2F10_-_004_-_Rules_of_Prompt_Caching_00.1748559639413.png)

The process follows a two-phase pattern: the initial request writes to the cache, and follow-up requests can read from it. The cache only lives for 5 minutes, so this feature is most useful when you're sending the same content repeatedly within a short timeframe.

## Cache Points

Prompt caching isn't enabled automatically - you need to manually add cache point message parts to control what gets cached. Cache points tell Claude to cache all the work done for everything before that point in your message.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559640%2F10_-_004_-_Rules_of_Prompt_Caching_04.1748559639963.png)

Here's how you add a cache point to a user message:

```
user_message = {
  "role": "user",
  "content": [
    {"text": ""},
    {"cachePoint": {"type": "default"}}
  ]
}
```

```
user_message = {
  "role": "user",
  "content": [
    {"text": ""},
    {"cachePoint": {"type": "default"}}
  ]
}
```

The key rule is that work done for everything before the cache point will be cached, but anything after the cache point won't be stored in the cache.

## How Cache Points Work

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559640%2F10_-_004_-_Rules_of_Prompt_Caching_05.1748559640558.png)

When you make an initial request with a cache point, Claude processes all the content and stores the work done up to that cache point. On follow-up requests, if the content before the cache point is identical, Claude reads the previously processed work from cache instead of reprocessing it.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559641%2F10_-_004_-_Rules_of_Prompt_Caching_07.1748559641029.png)

The cache will only be used if the content before the cache point is completely identical. Even small changes like adding "Please" to the beginning of your prompt will prevent cache usage, forcing Claude to process everything from scratch.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559641%2F10_-_004_-_Rules_of_Prompt_Caching_10.1748559641407.png)

## Caching Across Messages

Cache points can span multiple messages and even include assistant messages. This means you can cache entire conversation histories up to a certain point.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559642%2F10_-_004_-_Rules_of_Prompt_Caching_11.1748559641941.png)

For example, you might have a conversation with a user message, assistant response, and another user message, with a cache point at the end. All the processing work for that entire conversation thread gets cached and can be reused.

## Minimum Content Length

Content must be at least 1024 tokens long to be cached. This is the sum of all messages and parts you're trying to cache before the cache point.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559642%2F10_-_004_-_Rules_of_Prompt_Caching_13.1748559642531.png)

A simple "Hi there!" message won't meet the 1024 token minimum, so nothing gets cached. But if you repeat "Hi there!" 500 times, that would exceed 1024 tokens and qualify for caching.

## Cache Point Locations

Cache points aren't restricted to user messages. You can add them to system prompts and tool definitions, which are actually the most common caching opportunities.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559643%2F10_-_004_-_Rules_of_Prompt_Caching_16.1748559643056.png)

For tool definitions:

```
tools = [
  {"toolSpec": add_duration_to_datetime_schema},
  {"toolSpec": get_current_datetime_schema},
  {"cachePoint": {"type": "default"}}
]
```

```
tools = [
  {"toolSpec": add_duration_to_datetime_schema},
  {"toolSpec": get_current_datetime_schema},
  {"cachePoint": {"type": "default"}}
]
```

For system prompts:

```
system = [
  {"text": "You are a senior software..."},
  {"cachePoint": {"type": "default"}}
]
```

```
system = [
  {"text": "You are a senior software..."},
  {"cachePoint": {"type": "default"}}
]
```

These are the most valuable caching opportunities because system prompts and tool lists rarely change between requests, making them perfect candidates for caching.

---

## Prompt caching in action

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276787

details

2
                                    download

## Prompt caching in action

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Downloads

- 003_caching.ipynb
                                                (opens in new tab)
- 003_caching_completed.ipynb
                                                (opens in new tab)

---

## Quiz on features of Claude

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289300

## Quiz on features of Claude

# Quiz on Features of Claude

---

## Introducing MCP

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276798

details

## Introducing MCP

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Model Context Protocol (MCP) is a communication layer that provides Claude with context and tools without requiring you to write a bunch of tedious integration code. Instead of building every tool function yourself, MCP shifts that burden to specialized servers that handle the heavy lifting.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559635%2F11_-_001_-_Introducing_MCP_01.1748559635516.png)

When you first encounter MCP, you'll see diagrams showing the basic architecture: an MCP Client (your server) connects to MCP Servers that contain tools, prompts, and resources. Each MCP Server acts as an interface to outside services like GitHub, AWS, or databases.

## The Problem MCP Solves

Let's say you're building a chat interface where users can ask Claude about their GitHub data - questions like "What open pull requests are there across all my repositories?" To handle this without MCP, you'd need to create tools for every GitHub operation you want to support.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559636%2F11_-_001_-_Introducing_MCP_03.1748559636106.png)

GitHub has massive functionality - repositories, pull requests, issues, projects, and much more. Building a complete GitHub integration means authoring an incredible number of tool schemas and functions:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559636%2F11_-_001_-_Introducing_MCP_05.1748559636704.png)

This creates a lot of code that you have to write, test, and maintain. That's where MCP comes in.

## How MCP Works

MCP shifts the burden of tool definitions and execution from your server to dedicated MCP Servers. Instead of writing all those GitHub tools yourself, you connect to a GitHub MCP Server that already has them implemented.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559637%2F11_-_001_-_Introducing_MCP_08.1748559637200.png)

The MCP Server acts as a wrapper around the outside service, providing pre-built tools that Claude can use. You get access to all that GitHub functionality without writing any of the integration code yourself.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559637%2F11_-_001_-_Introducing_MCP_09.1748559637601.png)

## Common Questions

### Who authors MCP Servers?

Anyone can create an MCP Server implementation. Often, service providers themselves will make their own official implementations. For example, AWS might release an official MCP Server with tools for their various services.

### How is this different from calling APIs directly?

When you call a service's API directly, you still have to write the tool schemas and function implementations yourself. MCP Servers provide those tool schemas and functions already defined for you, saving you development time.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559638%2F11_-_001_-_Introducing_MCP_12.1748559637997.png)

### Isn't MCP just the same as tool use?

This is a common misconception. MCP Servers and tool use are complementary but different concepts. Tool use is about Claude calling functions to accomplish tasks. MCP is about who provides those functions - instead of you writing them, someone else has already implemented them in an MCP Server.

The key insight is that MCP Servers provide tool schemas and functions already defined for you, while direct tool use requires you to author everything yourself. Both involve Claude using tools, but MCP dramatically reduces the development work required on your end.

---

## MCP clients

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276793

details

## MCP clients

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The MCP client serves as the communication bridge between your server and MCP servers. Think of it as your access point to all the tools that an MCP server provides. When you need to use external functionality, the client handles all the message passing and protocol details for you.

## Transport Agnostic Communication

One of MCP's key strengths is being transport agnostic - a fancy way of saying the client and server can talk to each other using different communication methods. The most common setup runs both the MCP client and server on the same machine, where they communicate through standard input/output.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559638%2F11_-_002_-_MCP_Clients_01.1748559638305.png)

But you're not limited to that approach. MCP clients and servers can also connect over:

- HTTP
- WebSockets
- Various other network protocols

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559639%2F11_-_002_-_MCP_Clients_03.1748559639617.png)

## Message Types

Once connected, the client and server exchange specific message types defined in the MCP specification. The main ones you'll work with are:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559640%2F11_-_002_-_MCP_Clients_05.1748559640523.png)

ListToolsRequest/ListToolsResult: The client asks the server "what tools do you provide?" and gets back a complete list of available functionality.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559641%2F11_-_002_-_MCP_Clients_07.1748559640924.png)

CallToolRequest/CallToolResult: The client tells the server "run this specific tool with these arguments" and receives the execution results.

## Complete Flow Example

Here's how all the pieces work together in a real scenario. Let's say a user asks "What repositories do I have?" - here's the complete communication flow:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559641%2F11_-_002_-_MCP_Clients_09.1748559641405.png)

The process starts when a user submits their question to your server. But before your server can ask Claude for help, it needs to know what tools are available.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559642%2F11_-_002_-_MCP_Clients_11.1748559641902.png)

Your server asks the MCP client for a list of tools. The client sends a ListToolsRequest to the MCP server and gets back a ListToolsResult with all available tools.

```
ListToolsRequest
```

```
ListToolsResult
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559642%2F11_-_002_-_MCP_Clients_12.1748559642275.png)

Now your server has everything needed to make the initial request to Claude: the user's question plus the list of available tools.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559642%2F11_-_002_-_MCP_Clients_13.1748559642750.png)

Claude analyzes the tools and decides it needs to call one to answer the question. It responds with a tool use request.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559643%2F11_-_002_-_MCP_Clients_14.1748559643213.png)

Your server recognizes that Claude wants to run a tool, but your server doesn't execute tools directly anymore - that's the MCP server's job. So it asks the MCP client to run the tool with Claude's specified arguments.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559643%2F11_-_002_-_MCP_Clients_15.1748559643588.png)

The MCP client sends a CallToolRequest to the MCP server, which then makes the actual request to GitHub to fetch the user's repositories.

```
CallToolRequest
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559644%2F11_-_002_-_MCP_Clients_16.1748559643951.png)

GitHub responds with the repository data, which the MCP server wraps in a CallToolResult and sends back to the MCP client.

```
CallToolResult
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559644%2F11_-_002_-_MCP_Clients_17.1748559644448.png)

The MCP client passes the tool result back to your server, which then sends it to Claude as part of a follow-up message.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559645%2F11_-_002_-_MCP_Clients_18.1748559644856.png)

Finally, Claude has all the information it needs and formulates a response like "Your repositories are..." which gets sent back through your server to the user.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559645%2F11_-_002_-_MCP_Clients_19.1748559645252.png)

Yes, this flow involves many steps, but each component has a clear responsibility. The MCP client abstracts away the complexity of server communication, letting you focus on building your application logic while still having access to powerful external tools and services.

---

## Project setup

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276792

details

2
                                    download

## Project setup

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

We're going to build our own CLI-based chatbot to better understand how MCP clients and servers work together. This hands-on project will give you practical experience with both sides of the MCP architecture.

## What We're Building

Our chatbot will be a command-line interface that allows users to chat with a set of documents. Here's what the system will include:

- A CLI-based chatbot interface
- Document reading and editing capabilities for Claude
- Document "mention" functionality using @doc_name syntax

```
@doc_name
```

- Command execution with /command_name syntax

```
/command_name
```

- A collection of fake documents stored in memory

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559636%2F11_-_003_-_Project_Setup_00.1748559636228.png)

## System Architecture

The project consists of three main components working together:

- Our MCP Client - Handles user interaction and chat interface
- Our MCP Server - Provides tools for document operations
- Document Storage - In-memory collection of various file types

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559636%2F11_-_003_-_Project_Setup_04.1748559636686.png)

The MCP server will implement two core tools:

- Tool to read document contents
- Tool to update document contents
All documents (PDFs, spreadsheets, text files, markdown files) will be stored in memory rather than on disk, keeping the project simple and focused on MCP concepts.

## Important Architecture Note

In real-world projects, you typically implement either an MCP client or an MCP server - not both. You might:

- Build an MCP server to distribute a service to other developers
- Build an MCP client that connects to existing third-party MCP servers

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559637%2F11_-_003_-_Project_Setup_06.1748559637087.png)

Our project implements both components in a single codebase purely for educational purposes, so you can see how clients and servers interact with each other.

#### Downloads

- cli_starter.zip
                                                (opens in new tab)
- cli_project_complete.zip
                                                (opens in new tab)

---

## Defining tools with MCP

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276800

details

## Defining tools with MCP

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Building an MCP server becomes much simpler when you use the official Python SDK. Instead of manually writing complex JSON schemas for tools, you can define them with decorators and let the SDK handle the heavy lifting.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559694%2F11_-_004_-_Defining_Tools_with_MCP_00.1748559694628.png)

In this example, we're creating an MCP server that manages document operations. The server will have two main tools: one to read document contents and another to update them. All documents exist in memory as a simple dictionary where keys are document IDs and values are the content strings.

## MCP Python SDK Benefits

The MCP project provides official SDKs for building servers and clients across multiple programming languages. Using the Python SDK offers several advantages:

- Creates MCP servers with minimal boilerplate code
- Automatically generates JSON schemas from Python function signatures
- Simplifies tool definition through decorators
- Handles type validation and error handling

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559695%2F11_-_004_-_Defining_Tools_with_MCP_05.1748559695107.png)

Here's how easy it is to define a tool with the SDK. The @mcp.tool decorator, combined with type hints and field descriptions, automatically creates the proper tool schema that Claude can understand and use.

```
@mcp.tool
```

## Setting Up the Server

The basic server setup requires just a few lines:

```
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures",
    "outlook.pdf": "This document presents the projected future performance of the system",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment"
}
```

```
from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP("DocumentMCP", log_level="ERROR")

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures",
    "outlook.pdf": "This document presents the projected future performance of the system",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment"
}
```

## Implementing the Read Tool

The first tool allows Claude to read document contents by providing a document ID:

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

The tool definition includes:

- A clear name that describes the action
- A description explaining what the tool does
- Typed parameters with field descriptions
- Error handling for invalid document IDs

## Implementing the Edit Tool

The second tool performs simple find-and-replace operations on document content:

```
@mcp.tool(
    name="edit_document",
    description="Edit a document by replacing a string in the documents content with a new string."
)
def edit_document(
    doc_id: str = Field(description="Id of the document that will be edited"),
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
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
    old_str: str = Field(description="The text to replace. Must match exactly, including whitespace."),
    new_str: str = Field(description="The new text to insert in place of the old text.")
):
    if doc_id not in docs:
        raise ValueError(f"Doc with id {doc_id} not found")
    
    docs[doc_id] = docs[doc_id].replace(old_str, new_str)
```

This tool takes three parameters: the document ID, the text to find, and the replacement text. The implementation uses Python's built-in string replace() method for simplicity.

```
replace()
```

## Key Implementation Details

When defining tools with the MCP SDK, remember these important points:

- Import Field from pydantic to add parameter descriptions

```
Field
```

- Use type hints to specify parameter types
- Include error handling for edge cases
- Write clear, descriptive tool names and descriptions
- The SDK automatically converts your function signature into the proper JSON schema
The MCP Python SDK dramatically reduces the complexity of creating tools compared to manually writing JSON schemas. What used to require dozens of lines of schema definition now takes just a few lines of decorated Python functions.

---

## The server inspector

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276796

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

## Using the Inspector Interface

The MCP inspector is actively being developed, so the interface may look different by the time you use it. However, the core functionality remains consistent.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559685%2F11_-_005_-_The_Server_Inspector_05.1748559685073.png)

When you first open the inspector, you'll see a "Connect" button on the left side. Click this to start your MCP server and load your tools.

## Testing Your Tools

Once connected, look for a navigation bar with sections like Resources, Prompts, and Tools. Click on the Tools section to see your available tools.

Click "List Tools" to see all the tools your server provides. When you select a specific tool, the right panel updates to show a form where you can test that tool.

## Running Tool Tests

For example, to test a document reading tool:

- Select the read_doc_contents tool

```
read_doc_contents
```

- Enter a document ID (like "deposition.md")
- Click "Run Tool"
The inspector will execute your tool and show the results, including success status and any returned data.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559687%2F11_-_005_-_The_Server_Inspector_17.1748559687825.png)

## Testing Document Editing

You can also test more complex tools like document editing:

- Switch to the edit_document tool

```
edit_document
```

- Fill in the document ID, old text to replace, and new text
- Run the tool to see if it succeeds
- Use the read tool again to verify the changes were applied

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559689%2F11_-_005_-_The_Server_Inspector_16.1748559688815.png)

## Development Workflow

The inspector shows a history of your tool calls on the left side, making it easy to track what you've tested and repeat previous operations. This creates an efficient development loop where you can:

- Make changes to your server code
- Restart the inspector
- Test your tools immediately
- Verify the results
This inspector tool becomes essential as you build more complex MCP servers. It eliminates the need to wire up your server to a full application just to test basic functionality, making development much faster and more reliable.

---

## Implementing a client

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276802

details

## Implementing a client

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we have our MCP server working, it's time to build the client side. The client is what allows our application to communicate with the MCP server and access its functionality.

## Understanding the Client Architecture

Before diving into the code, let's clarify an important point about MCP projects. Normally, you'd implement either an MCP client or an MCP server - not both. We're building both in this project just so you can see how they work together.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559696%2F11_-_006_-_Implementing_a_Client_01.1748559696012.png)

The MCP client consists of two main components working together:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559696%2F11_-_006_-_Implementing_a_Client_02.1748559696435.png)

- MCP Client - A custom class we create to make using the session easier
- Client Session - The actual connection to the server (part of the MCP Python SDK)
The client session handles the low-level communication but requires careful resource cleanup when your program shuts down. That's why we wrap it in our own class - to manage that cleanup automatically.

## How the Client Fits Into Our Application

Remember our application flow diagram? The client plays a crucial role in two key moments:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559697%2F11_-_006_-_Implementing_a_Client_05.1748559696986.png)

Our CLI code uses the client to:

- Get a list of available tools to send to Claude
- Execute tools when Claude requests them

## Implementing Core Client Functions

Let's implement the two essential functions: list_tools and call_tool.

```
list_tools
```

```
call_tool
```

For list_tools, we need to connect to our session and request the available tools:

```
list_tools
```

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

For call_tool, we pass the tool name and input parameters to the server:

```
call_tool
```

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

That's it! The session handles all the complex communication details for us.

## Testing the Client

The client file includes a simple test harness at the bottom. You can run it directly to verify everything works:

```
uv run mcp_client.py
```

```
uv run mcp_client.py
```

This will connect to your MCP server and print out the available tools. You should see output showing your tool definitions, including names, descriptions, and input schemas.

## Important Schema Differences

Here's a gotcha you need to know about: MCP tool definitions don't exactly match what Claude expects. The MCP spec has its own format for tool schemas, which is slightly different from what Bedrock requires.

Don't worry - there's already code in the project that handles this conversion automatically. The to_bedrock_tools function in core/bedrock.py translates MCP tool definitions into the format Claude understands.

```
to_bedrock_tools
```

```
core/bedrock.py
```

## Testing with Claude

Now that both the server and client are working, you can test the complete flow. Try running your main application and asking Claude to read a document:

```
uv run main.py
```

```
uv run main.py
```

Then ask: "What is the contents of the report.pdf document?"

Claude will:

- Receive the list of available tools from your client
- Decide to use the read_doc_contents tool
- Your client will execute that tool on the MCP server
- Claude will receive the document contents and respond
The client acts as the bridge between your application code and the MCP server, making it easy to expose server functionality to Claude and other parts of your system.

---

## Defining resources

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276799

details

## Defining resources

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Resources in MCP servers allow you to expose data to clients, similar to GET request handlers in a typical HTTP server. They're perfect for scenarios where you need to fetch information rather than perform actions.

## Understanding Resources

Think of resources as read-only endpoints that can return any type of data - strings, JSON, binary files, etc. You set a 'mime_type' to give the client a hint about what kind of data you're returning.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559689%2F11_-_007_-_Defining_Resources_04.1748559689710.png)

Resources work by exposing data through URIs (essentially addresses). When a client needs data, it sends a ReadResourceRequest with the specific URI, and your server responds with the requested information.

## Two Types of Resources

There are two main types of resources you can create:

- Direct Resources - Have static URIs that don't contain any parameters (like docs://documents)

```
docs://documents
```

- Templated Resources - Include parameters in their URIs (like docs://documents/{doc_id})

```
docs://documents/{doc_id}
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559690%2F11_-_007_-_Defining_Resources_07.1748559690197.png)

For templated resources, the Python SDK automatically parses parameters from the URI and passes them as keyword arguments to your function. The parameter name in the URI becomes the argument name in your function.

## Implementing Resources

Creating resources is straightforward using the @mcp.resource() decorator. Here's how to implement both types:

```
@mcp.resource()
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

The MCP Python SDK automatically serializes whatever you return. You don't need to manually convert data to JSON strings - just return the appropriate Python data structure.

## Testing Your Resources

You can test resources using the MCP Inspector tool. Start your server with uv run mcp dev mcp_server.py and navigate to the web interface.

```
uv run mcp dev mcp_server.py
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559690%2F11_-_007_-_Defining_Resources_18.1748559690720.png)

The inspector separates direct resources from templated ones. Direct resources appear in the main "Resources" section, while templated resources show up under "Resource Templates". You can click on any resource to test it and see the exact response structure your server returns.

## Practical Use Cases

Resources are ideal for:

- Providing autocomplete data (like document lists)
- Fetching file contents or database records
- Exposing configuration data
- Serving any read-only information your client needs
The key advantage is that resources allow clients to proactively fetch data without relying on tools or complex interactions. This makes them perfect for features like document mentions, where you want to automatically inject content into prompts based on user references.

---

## Accessing resources

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276797

details

## Accessing resources

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Resources in MCP allow your server to expose data that can be directly included in prompts, rather than requiring tool calls to access information. This creates a more efficient way to provide context to AI models like Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559733%2F11_-_008_-_Accessing_Resources_00.1748559733698.png)

## Understanding the Resource Flow

When a user types something like "What's in the @..." in your application, the system needs to fetch a list of available resources for autocomplete. The MCP client sends a ReadResourceRequest to the server, which responds with a list of document names that can be referenced.

## Implementing Resource Reading

The core functionality happens in the read_resource method of your MCP client. This method takes a URI parameter that identifies which resource to fetch from the server.

```
read_resource
```

First, add the necessary imports to handle JSON parsing and URL validation:

```
import json
from pydantic import AnyUrl
```

```
import json
from pydantic import AnyUrl
```

The main implementation makes a request to the MCP server and processes the response:

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

## Handling Different Content Types

Resources can return different types of content, so you need to check the MIME type to handle the response appropriately:

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

This approach ensures that JSON resources are properly parsed, while plain text resources are returned as-is.

## Testing the Implementation

Once implemented, you can test the resource functionality by running your CLI application. When you type "@" followed by a resource name, the system will:

- Show available resources in an autocomplete list
- Allow you to select a resource using arrow keys and space
- Include the resource content directly in the prompt sent to Claude
This means Claude receives the document content immediately without needing to make additional tool calls, making the interaction much more efficient.

## Key Benefits

Resources provide several advantages over tools for accessing static information:

- Content is included directly in prompts, reducing latency
- No additional API calls needed during conversation
- Better user experience with autocomplete functionality
- Cleaner separation between static data and dynamic operations
Resources work best for relatively static information that you want to make easily accessible to AI models, such as documentation, reports, or reference materials.

---

## Defining prompts

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276801

details

## Defining prompts

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

MCP servers can define prompts - pre-written, high-quality instructions that clients can use instead of writing their own prompts from scratch. Think of prompts as carefully crafted templates that give better results than what users might write on their own.

## Why Use Prompts?

Let's say you want Claude to reformat a document into markdown. You could just ask "Convert report.pdf to markdown" and it would work fine. But you'd probably get much better results with a thoroughly tested, detailed prompt that covers edge cases and gives specific formatting instructions.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559742%2F11_-_009_-_Defining_Prompts_07.1748559742643.png)

The idea is simple: as MCP server developers, we can spend time crafting and testing really good prompts, then make them available to anyone using our server. Users get better results without having to become prompt engineering experts themselves.

## Defining a Prompt

Prompts use a similar decorator pattern to tools and resources. Here's the basic structure:

```
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    # Return a list of messages
```

```
@mcp.prompt(
    name="format",
    description="Rewrites the contents of the document in Markdown format."
)
def format_document(
    doc_id: str = Field(description="Id of the document to format")
) -> list[base.Message]:
    # Return a list of messages
```

The function returns a list of messages that can be sent directly to Claude. This lets you build complex prompts with multiple user and assistant messages if needed.

## Building the Format Prompt

For our document server, we'll create a prompt that reformats documents into markdown. The prompt needs to:

- Take a document ID as input
- Use the read_doc_contents tool to get the document
- Reformat it with proper markdown syntax
- Save the changes back to the document
Here's how the implementation looks:

```
def format_document(
    doc_id: str = Field(description="Id of the document to format")
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
    doc_id: str = Field(description="Id of the document to format")
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

## Testing the Prompt

Once you've defined your prompt, you can test it using the MCP Inspector. Navigate to the Prompts tab, select your prompt, and provide the required parameters.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559743%2F11_-_009_-_Defining_Prompts_18.1748559743262.png)

The inspector will show you the generated messages that would be sent to Claude. You can verify that parameter interpolation works correctly and that your prompt contains all the necessary instructions.

## Key Benefits

- Quality Control - Server authors can test and refine prompts before users see them
- Consistency - Everyone gets the same high-quality prompt instead of improvising
- Specialization - Prompts can be tailored to your server's specific domain and capabilities
- Reusability - Multiple client applications can use the same well-crafted prompts
Remember to import the base module for message types:

```
from mcp.server.fastmcp.prompts import base
```

```
from mcp.server.fastmcp.prompts import base
```

Prompts are particularly valuable when your MCP server has a specific focus area - like document management, data analysis, or code generation. You can provide users with battle-tested prompts that leverage your server's tools effectively.

---

## Prompts in the client

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276795

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

The get_prompt method is more interesting because it handles argument interpolation. When we request a specific prompt, we pass arguments that get injected into the prompt function. For example, if our server has a "format" prompt that expects a doc_id parameter, that value gets passed through and interpolated into the actual prompt text.

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

## Testing Prompts in Action

When you run the client and type a forward slash, you'll see available prompts as commands. Selecting a prompt like "format" will prompt you to choose from available documents. The system then:

- Takes the prompt with the document ID interpolated
- Feeds it directly to Claude as a user message
- Claude receives both the instructions and the document ID
- Claude uses available tools to fetch the document content
- Claude responds with the reformatted result

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559732%2F11_-_010_-_Prompts_in_the_Client_10.1748559731797.png)

## How Prompts Work

Prompts define a set of user and assistant messages that can be used by the client. These prompts should be high quality, well-tested, and relevant to the overall purpose of your MCP server.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559732%2F11_-_010_-_Prompts_in_the_Client_17.1748559732285.png)

The workflow is:

- Write and evaluate a prompt relevant to your MCP server's purpose
- Define the prompt inside your MCP server using the @mcp.prompt decorator

```
@mcp.prompt
```

- Your client can request that prompt at any time
- When requesting the prompt, provide arguments that get passed as keyword arguments to the prompt function
- The function uses those arguments to customize the prompt content
This system creates reusable, parameterized prompts that can be shared across different clients and use cases, making your MCP server more versatile and powerful.

---

## MCP review

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276794

details

## MCP review

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Now that we've built our MCP server, let's recap the three core server primitives and understand when to use each one. The key insight is that each primitive is controlled by a different part of your application stack.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559732%2F11_-_011_-_MCP_Review_00.1748559732788.png)

## Tools: Model-Controlled

Tools are controlled entirely by Claude. The AI model decides when to call these functions, and the results are used directly by Claude to accomplish tasks.

Use tools when you want to give Claude additional capabilities. For example, if you ask Claude to calculate the square root of 3 using JavaScript, Claude will automatically decide to use a JavaScript execution tool to provide the answer.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559734%2F11_-_011_-_MCP_Review_17.1748559733993.png)

The decision to use the tool was 100% model-controlled - Claude recognized it needed to execute code and chose the appropriate tool without any prompting from the application or user.

## Resources: App-Controlled

Resources are controlled by your application code. Your app decides when to fetch resource data and how to use it, typically for UI purposes or to add context to conversations.

Use resources when you need to get data into your app. Common examples include:

- Populating autocomplete options in your UI
- Fetching documents to display in a file picker
- Adding context to messages before sending them to Claude
In Claude's web interface, the "Add from Google Drive" feature demonstrates this perfectly. The application fetches a list of available documents and displays them in the UI, then injects the selected document's content into the chat context.

## Prompts: User-Controlled

Prompts are controlled by users. They decide when to trigger these predefined workflows through direct actions like clicking buttons, selecting menu options, or using slash commands.

Use prompts when you want to implement predefined workflows that users can easily access. In Claude's interface, you'll see workflow buttons below the chat input that let users quickly start common tasks like writing, learning, or coding.

## Choosing the Right Primitive

When building your MCP server, think about who needs to control each piece of functionality:

- Need to extend Claude's capabilities? Use tools
- Need to get data into your app's UI? Use resources
- Need to offer users predefined workflows? Use prompts
These are high-level guidelines to help you choose the right primitive based on your specific use case. Each serves a different part of the application stack - tools serve the model, resources serve the app, and prompts serve the users.

---

## Quiz on Model Context Protocol

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/289299

## Quiz on Model Context Protocol

# Quiz on Model Context Protocol

---

## Agents overview

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276804

## Agents overview

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Claude Code setup

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276809

## Claude Code setup

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Claude Code in action

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276811

details

1
                                    download

## Claude Code in action

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude Code isn't just a tool for writing code - it's designed to be your coding partner throughout an entire project lifecycle. From initial setup to deployment and maintenance, Claude can help with every step of software development.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559793%2F12_-_003_-_Claude_Code_in_Action_01.1748559793800.png)

## The /init Command

When starting with a new project, the /init command is your first step. Claude Code will scan your codebase, noting project structure, dependencies, commands, and coding patterns. The findings get summarized in a CLAUDE.md file that Claude automatically reads in future conversations.

```
/init
```

```
CLAUDE.md
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559794%2F12_-_003_-_Claude_Code_in_Action_05.1748559794289.png)

You can have multiple CLAUDE.md files for different scopes:

- Project - checked into git, shared between engineers
- Local - not checked into git, your particular notes to Claude
- User - used across all projects
When running /init, you can add special directions for areas you want Claude to focus on. You can also use the # shortcut to add quick notes that get appended to your CLAUDE.md file.

```
/init
```

```
#
```

## Common Workflows

Claude works best as an effort multiplier. The more context and structure you provide, the better results you'll get. Here are two effective approaches:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559794%2F12_-_003_-_Claude_Code_in_Action_11.1748559794657.png)

### Planning-First Workflow

This three-step approach works well for complex features:

- Feed context into Claude - Find files relevant to your feature and ask Claude to read them
- Tell Claude to plan a solution - Describe what you want built, but specifically ask Claude not to write code yet
- Ask Claude to implement the solution - Once you have a solid plan, Claude can write code based on the context and planning it already completed
For example, when building a document conversion tool, you might first ask Claude to examine existing tool examples and helper functions. Then ask it to plan out the implementation steps. Finally, request the actual code implementation.

### Test-Driven Development Workflow

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559796%2F12_-_003_-_Claude_Code_in_Action_17.1748559795914.png)

This approach requires more upfront effort but dramatically increases Claude's effectiveness:

- Feed context into Claude - Share relevant files for your feature
- Ask Claude to think of test cases - Tell Claude specifically not to write any code yet
- Ask Claude to implement those tests - Select only the tests that look relevant to your feature
- Ask Claude to write code that passes the tests - Claude will iterate on a solution until the tests pass
This workflow helps ensure your code is robust and handles edge cases you might not have considered initially.

## Practical Tips

Claude can handle routine development tasks beyond just writing code. You can ask it to:

- Set up project environments and install dependencies
- Stage and commit changes with descriptive commit messages
- Run test suites and interpret results
- Clear conversation history with /clear to reset context

```
/clear
```

Remember that Claude Code reads your CLAUDE.md file automatically, so any coding standards, project-specific notes, or architectural decisions you document there will influence all future interactions. This makes Claude increasingly effective as it learns more about your project's patterns and requirements.

#### Downloads

- app_starter.zip
                                                (opens in new tab)

---

## Enhancements with MCP servers

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276806

details

## Enhancements with MCP servers

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude Code has an MCP client built right into it, which means you can connect MCP servers to dramatically expand its functionality. This opens up some really powerful possibilities for customizing your development workflow.

## How MCP Integration Works

The Model Context Protocol allows Claude Code to connect to external services through MCP servers. Each server can provide tools, prompts, and resources that extend what Claude can do.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559780%2F12_-_004_-_Enhancements_with_MCP_Servers_01.1748559780029.png)

In this example, we'll connect Claude Code to a custom MCP server that provides a document conversion tool. This will let Claude read and convert PDF and Word documents to markdown format.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559780%2F12_-_004_-_Enhancements_with_MCP_Servers_02.1748559780526.png)

## Adding an MCP Server to Claude Code

Setting up an MCP server is straightforward. First, stop any running Claude Code session, then use the MCP add command:

```
claude mcp add documents uv run main.py
```

```
claude mcp add documents uv run main.py
```

This command takes two arguments:

- The server name (can be anything you want - "documents" in this case)
- The command to start your MCP server
After adding the server, restart Claude Code and it will automatically connect to your MCP server.

## Testing the Integration

Once connected, Claude can use the tools provided by your MCP server. In our example, we can ask Claude to convert document files to markdown format, and it will automatically use the document conversion tool we created.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559781%2F12_-_004_-_Enhancements_with_MCP_Servers_13.1748559780991.png)

The tool successfully converts the document content, showing how MCP servers can add entirely new capabilities to Claude Code.

## Popular MCP Servers for Development

There are many existing MCP servers that can enhance your development workflow:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559781%2F12_-_004_-_Enhancements_with_MCP_Servers_16.1748559781522.png)

- sentry-mcp - Automatically discover and fix bugs logged in Sentry
- playwright-mcp - Gives Claude browser automation capabilities for testing and troubleshooting
- figma-context-mcp - Exposes Figma designs to Claude
- mcp-atlassian - Allows Claude to access Confluence and Jira
- firecrawl-mcp-server - Adds web scraping capabilities to Claude
- slack-mcp - Allows Claude to post messages or reply to specific threads

## Building Your Custom Workflow

The real power comes from combining multiple MCP servers that match your specific development needs. For example, you might set up:

- A Sentry server to fetch production error details
- A Jira server to read ticket requirements
- A Slack server to notify your team when work is complete
- Custom servers for your specific tools and processes
This flexibility makes Claude Code incredibly adaptable to different development environments and workflows. Take some time to think about which external services and tools you use regularly - there's likely an MCP server that can integrate them with Claude Code.

---

## Parallelizing Claude Code

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276810

details

## Parallelizing Claude Code

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Running multiple instances of Claude Code in parallel is one of the biggest productivity gains you can achieve. Since Claude is lightweight, you can easily spin up several copies, assign each a different task, and have them work simultaneously. This effectively gives you a team of virtual software engineers working on your project.

## The Challenge: File Conflicts

The main problem with parallel instances is that they might try to modify the same files at the same time. This can lead to conflicting or invalid code since each instance isn't aware of what the others are doing.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559790%2F12_-_005_-_Parallelizing_Claude_Code_00.1748559790559.png)

The solution is to give each Claude instance its own separate workspace. Each instance works with its own copy of your project, makes changes in isolation, and then merges those changes back into your main project.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559791%2F12_-_005_-_Parallelizing_Claude_Code_02.1748559791393.png)

## Git Worktrees

Git worktrees are perfect for this workflow. If your project is already managed by Git, you can use worktrees immediately. They're like an extension of Git's branching functionality that lets you create complete copies of your project in separate directories on your machine.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559792%2F12_-_005_-_Parallelizing_Claude_Code_03.1748559791903.png)

Each worktree corresponds to a separate branch. You can have one folder for feature A and another for feature B, each containing a complete copy of your codebase. Then you run separate Claude Code instances in each worktree, working in total isolation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559792%2F12_-_005_-_Parallelizing_Claude_Code_04.1748559792621.png)

Once each Claude instance finishes its feature, you commit the work and merge it back into your main branch, just like merging any normal Git branch.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559793%2F12_-_005_-_Parallelizing_Claude_Code_05.1748559792995.png)

## Automating Worktree Creation

This might sound complicated to manage, but you can delegate the entire workflow to Claude Code itself. You can write a prompt that asks Claude to:

- Create a new git worktree in a specific folder
- Symlink dependencies that aren't tracked by Git
- Launch a new VS Code instance in that directory

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559793%2F12_-_005_-_Parallelizing_Claude_Code_06.1748559793589.png)

## Custom Commands

Rather than copying and pasting long prompts every time, you can create custom slash commands in Claude Code. Add a .md file to .claude/commands to create a custom command.

```
.md
```

```
.claude/commands
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559794%2F12_-_005_-_Parallelizing_Claude_Code_10.1748559794142.png)

The custom command can reference $ARGUMENTS, which gets replaced with whatever arguments you pass to your command. For example:

```
$ARGUMENTS
```

- /project:create_worktree feature_a creates a worktree named "feature_a"

```
/project:create_worktree feature_a
```

- /project:create_worktree develop creates a worktree named "develop"

```
/project:create_worktree develop
```

## Parallel Development in Action

Here's how the complete workflow looks in practice. You can create multiple worktrees for different features:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559794%2F12_-_005_-_Parallelizing_Claude_Code_15.1748559794596.png)

Each Claude instance works on its assigned task:

- Update document tests
- Add logging
- Add note-taking tools
- Add a subtract tool

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559795%2F12_-_005_-_Parallelizing_Claude_Code_16.1748559795172.png)

## Merging Changes

When the features are complete, you can automate the merge process too. Create another custom command that tells Claude to:

- Change into the worktree directory
- Examine the latest commit
- Change back to the root directory
- Merge the worktree branch
- Handle any merge conflicts automatically

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559796%2F12_-_005_-_Parallelizing_Claude_Code_17.1748559796410.png)

Claude can even resolve merge conflicts automatically based on its understanding of the changes made in each branch.

## Results

This approach scales to as many parallel instances as you can manage. Instead of working on features sequentially, you can have multiple Claude instances developing different parts of your project simultaneously. It's like having your own team of developers, each working in their own isolated environment before bringing their work together.

The productivity gains are substantial - you're essentially multiplying your development capacity by the number of parallel instances you run.

---

## Automated debugging

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276812

details

## Automated debugging

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Claude isn't just for writing code in your editor. It can also monitor your production applications and automatically fix errors as they occur. This creates a powerful automated debugging workflow that can catch and resolve issues before they impact your users.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559783%2F12_-_006_-_Automated_Debugging_00.1748559782853.png)

## The Problem: Production-Only Errors

One of the most frustrating debugging scenarios is when your application works perfectly in development but fails in production. You might test everything locally, deploy with confidence, only to discover that certain features aren't working in the live environment.

Consider a simple chatbot application that works flawlessly during local testing. You can ask questions, generate spreadsheets with fake data, and everything responds as expected. But when you deploy the same code to AWS Amplify and run identical tests, the spreadsheet generation fails silently - the request goes through, but no data appears.

## Traditional Debugging Approach

Typically, you'd need to:

- Hunt through CloudWatch logs to find error messages
- Parse complex error details and stack traces
- Manually debug why the code behaves differently in production
- Fix the issue and redeploy
This process can be time-consuming, especially when dealing with cryptic error messages like "The provided model identifier is invalid" buried in extensive log output.

## Automated Error Detection and Fixing

Instead of manual debugging, you can create a GitHub Action that runs automatically every day to monitor your production environment. This workflow delegates the entire debugging process to Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559783%2F12_-_006_-_Automated_Debugging_13.1748559783322.png)

Here's how the automated workflow operates:

- Setup: The GitHub Action checks out your repository, installs dependencies, and sets up Claude
- Log Analysis: Uses AWS CLI to fetch CloudWatch logs from the last 24 hours
- Error Processing: Claude analyzes the logs, removes duplicates, and identifies unique errors
- Fix Implementation: Claude attempts to fix each error by modifying the appropriate code
- Pull Request Creation: Commits the fixes and automatically opens a pull request for review

## Real-World Example

In the chatbot example, Claude discovered that the production environment was using an invalid model identifier. The error occurred because of a typo in the model ID that was only referenced in production configuration.

Claude identified the issue, found the correct model ID format, and updated the configuration file. The fix was then committed with a clear explanation of what went wrong and how it was resolved.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559784%2F12_-_006_-_Automated_Debugging_17.1748559783816.png)

## Benefits of Automated Debugging

- Proactive Monitoring: Catches errors before you're even aware they exist
- Time Savings: Eliminates manual log hunting and debugging sessions
- Clear Documentation: Each fix comes with detailed explanations
- Review Process: Pull requests allow you to verify fixes before merging
- Continuous Improvement: Runs automatically to catch new issues as they arise

## Implementation Considerations

When setting up automated debugging workflows:

- Configure appropriate AWS permissions for CloudWatch access
- Set reasonable limits on the number of errors processed to stay within context windows
- Include logic to deduplicate similar errors
- Ensure the workflow has proper repository write permissions for creating pull requests
- Consider running the workflow during off-peak hours
This automated approach transforms debugging from a reactive, manual process into a proactive, automated system that keeps your applications running smoothly with minimal intervention.

---

## Computer Use

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276807

details

## Computer Use

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Computer use is a powerful feature that lets Claude interact directly with desktop environments, essentially giving it the ability to control a computer like a human would. This opens up entirely new possibilities for automation, testing, and complex workflows that go beyond simple text generation.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559833%2F12_-_007_-_Computer_Use_00.1748559833124.png)

## What Computer Use Can Do

Instead of just describing what to do or generating code, Claude can actually perform tasks by:

- Taking screenshots to see what's on screen
- Clicking buttons and links
- Typing text into forms and applications
- Navigating between different applications and browser tabs
- Following multi-step processes that require visual feedback
This makes it particularly valuable for tasks like quality assurance testing, where you need to interact with a user interface and verify that everything works as expected.

## Real-World Example: Automated QA Testing

Here's a practical scenario that shows the power of computer use. Imagine you've built a React component with an autocomplete feature - users can type @ to mention files or resources. The component seems to work fine at first glance, but you want to thoroughly test it for edge cases.

```
@
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559833%2F12_-_007_-_Computer_Use_04.1748559833651.png)

Rather than manually testing every scenario yourself, you can set up Claude with computer use to handle the QA process. You provide Claude with specific test cases to run:

- Verify that typing "Did you read @" displays autocomplete options
- Test that pressing Enter properly adds a mention to the text area
- Check that pressing backspace after adding mentions shows the autocomplete list in the correct position

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559834%2F12_-_007_-_Computer_Use_16.1748559834042.png)

Claude will systematically work through each test case, taking screenshots, interacting with the interface, and documenting what happens. In this example, Claude discovered that while the first two tests passed, the third one failed - the autocomplete dropdown was appearing in the wrong location when users pressed backspace.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559834%2F12_-_007_-_Computer_Use_18.1748559834522.png)

## How the Testing Process Works

When you give Claude a testing task, it follows a structured approach:

- Opens a browser and navigates to your application
- Executes each test case step by step
- Takes screenshots to verify visual behavior
- Refreshes the page between tests to ensure clean state
- Documents results with specific details about what passed or failed
- Provides a summary report with actionable findings
The key advantage is that Claude can catch issues you might miss during manual testing, and it can run the same tests consistently every time you make changes to your code.

## Setting Up Computer Use

Computer use runs in an isolated environment for security. The typical setup involves:

- A Docker container running a desktop environment
- A browser instance that Claude can control
- A chat interface where you give Claude instructions
- Complete isolation from your main system
This isolation is crucial because it means Claude can interact with applications and websites without any risk to your personal data or system security.

## Best Practices for Computer Use

When working with computer use, keep these guidelines in mind:

- Be specific about what you want Claude to test or accomplish
- Provide clear success criteria for each task
- Break complex workflows into smaller, manageable steps
- Always run computer use in isolated environments
- Review Claude's findings and verify important results manually
Computer use represents a significant step forward in AI capabilities, moving from generating text about tasks to actually performing them. Whether you're doing QA testing, automating repetitive workflows, or exploring complex applications, it can save substantial time while providing consistent, documented results.

---

## How Computer Use works

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276805

details

## How Computer Use works

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Computer use in Claude works exactly like regular tool use - it's built on the same foundation you're already familiar with. The key difference is that instead of calling a weather API or database function, Claude is making requests to control a computer interface.

## Tool Use Refresher

Before diving into computer use, let's quickly review how standard tool use works. When you want Claude to use a tool, you send a request that includes both a user message and a tool schema. The tool schema describes the additional functionality you want to expose to Claude.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559834%2F12_-_008_-_How_Computer_Use_Works_01.1748559834652.png)

Here's the typical flow:

- You send Claude a question along with available tool schemas
- Claude analyzes the request and decides it needs to use a tool
- Claude responds with a tool use request containing the tool name and required inputs
- Your server executes the tool function and returns the result
- You send the tool result back to Claude

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559835%2F12_-_008_-_How_Computer_Use_Works_05.1748559835205.png)

For example, if you ask about weather in San Francisco, Claude might call a get_weather function with the location parameter, your server fetches the weather data, and you return the result to Claude.

```
get_weather
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559835%2F12_-_008_-_How_Computer_Use_Works_07.1748559835689.png)

## Computer Use: Same Flow, Different Tool

Computer use follows this exact same pattern. The difference is in what the "tool" actually does - instead of fetching weather data, it simulates computer interactions like mouse clicks and keyboard input.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559837%2F12_-_008_-_How_Computer_Use_Works_08.1748559836893.png)

When you enable computer use, you send Claude a special tool schema that gets automatically expanded behind the scenes. What starts as a simple schema on your end becomes a comprehensive interface that tells Claude it can perform actions like:

- Mouse movements and clicks
- Keyboard input and key combinations
- Taking screenshots
- Scrolling and other interface interactions

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559837%2F12_-_008_-_How_Computer_Use_Works_09.1748559837358.png)

The tool schema you send is minimal, but it automatically converts into a detailed specification that includes all the computer interaction capabilities Claude needs.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559838%2F12_-_008_-_How_Computer_Use_Works_10.1748559837858.png)

## The Technical Implementation

To make computer use work, you need a computing environment that can programmatically execute the actions Claude requests. The reference implementation uses a Docker container running Firefox, along with code that can simulate keypresses and mouse movements.

When Claude decides to interact with the computer, it sends a tool use request just like any other tool. Your server receives this request and executes the corresponding action in the containerized environment - whether that's clicking a button, typing text, or taking a screenshot.

The important thing to understand is that Claude isn't directly controlling a computer. It's making tool requests, and your infrastructure translates those requests into actual computer interactions.

## Getting Started

You don't need to build this infrastructure from scratch. Anthropic provides a reference implementation that handles all the complex parts for you.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559838%2F12_-_008_-_How_Computer_Use_Works_15.1748559838343.png)

To set up computer use, you need:

- A Docker runtime installed on your system
- An AWS profile configured locally (usually "default")
- The reference implementation from the Anthropic quickstarts repository
Once you have these prerequisites, you can start the Docker container with a single command. This gives you access to the same interface shown in the demonstrations - a chat interface on the left where you can talk to Claude, and a browser environment on the right where Claude can interact with web pages and applications.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559839%2F12_-_008_-_How_Computer_Use_Works_19.1748559838860.png)

The setup process is straightforward, and the full setup guide is available in the Anthropic quickstarts repository on GitHub. This reference implementation provides everything you need to start experimenting with Claude's computer use capabilities in a safe, contained environment.

---

## Qualities of agents

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276808

details

## Qualities of agents

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

After exploring Claude Code and Computer Use, we can identify key patterns that reveal what makes agents successful. Both tools demonstrate a systematic approach to problem-solving that relies on focused tool usage, environmental awareness, and iterative execution.

## How Agents Work in Practice

When Claude was asked to add a test for a specific corner case, it followed a clear pattern of tool usage. The agent made four distinct tool calls: two to read existing files, one to update a file, and one to run tests. This breakdown reveals something important about agent behavior.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559833%2F12_-_009_-_Qualities_of_Agents_02.1748559833134.png)

Three of these calls were purely about gathering information from the environment - understanding the existing codebase before making changes. Only one call actually modified the environment. This pattern of "observe first, then act" appears consistently across both Claude Code and Computer Use.

Computer Use follows the same approach when testing web applications. Each tool call returns a screenshot, giving Claude immediate visual feedback about the current state of the interface. This constant feedback loop allows the agent to understand what's happening and adjust its next actions accordingly.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559833%2F12_-_009_-_Qualities_of_Agents_07.1748559833660.png)

## Comparing Agent Approaches

Both Claude Code and Computer Use share several fundamental characteristics that make them effective:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559834%2F12_-_009_-_Qualities_of_Agents_09.1748559834119.png)

- Tool-based execution: Both systems use tools extensively and run them in loops until reaching success criteria or hitting an error
- Environmental context: Rather than relying on detailed prompts or RAG processes, they gather context directly through tool interactions
- Focused toolsets: Each agent has a small, well-defined set of tools with clear purposes
- High-value, low-risk tasks: Both tackle complex problems where mistakes are manageable
- Low error costs: Computer Use has very low error costs, while Claude Code has low but not negligible costs

## Key Qualities of Effective Agents

Based on these observations, successful agents share four critical qualities:

### Focused Tool Sets Running in Loops

Agents work best with a small number of simple, well-defined tools. They keep executing these tools until reaching an iteration limit, encountering an error, or meeting success criteria. This iterative approach allows for course correction and refinement.

### Context is Everything

Claude has no inherent knowledge of your specific environment. It needs tools to read from and understand the current state of whatever system it's working with. The quality of context gathering directly impacts agent performance.

### High Value Tasks with Low Error Costs

Agents excel at complex, knowledge-intensive work where mistakes won't cause major damage. Writing code is a perfect example - it requires significant expertise, but errors can be caught and fixed without catastrophic consequences. Avoid using agents for high-stakes decisions where errors could have serious economic or safety impacts.

### Continuous Evaluation

The only reliable way to build effective agents is through rigorous testing. Create evaluation criteria and continuously test your agent's performance against real scenarios. This feedback loop is essential for identifying weaknesses and improving reliability.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748559834%2F12_-_009_-_Qualities_of_Agents_17.1748559834793.png)

Understanding these patterns helps explain why Claude Code and Computer Use work so well - they're designed around these fundamental principles of effective agent architecture. When building your own agents, keep these qualities in mind to create systems that are both powerful and reliable.

---

## Final assessment quiz

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/290881

## Final assessment quiz

# Final Assessment Quiz

---

## Course wrap up

> https://anthropic.skilljar.com/claude-in-amazon-bedrock/276827

## Course wrap up

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.