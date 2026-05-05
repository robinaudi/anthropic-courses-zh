# Model Context Protocol: Advanced Topics

> Source: https://anthropic.skilljar.com/model-context-protocol-advanced-topics


---

## My Profile

> https://anthropic.skilljar.com/accounts/profile/?next=/model-context-protocol-advanced-topics

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

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/resume

## Wrapping up

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Let's get started!

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296349

## Let's get started!

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

---

## Sampling

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296288

details

## Sampling

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Sampling allows a server to access a language model like Claude through a connected MCP client. Instead of the server directly calling Claude, it asks the client to make the call on its behalf. This shifts the responsibility and cost of text generation from the server to the client.

## The Problem Sampling Solves

Imagine you have an MCP server with a research tool that fetches information from Wikipedia. After gathering all that data, you need to summarize it into a coherent report. You have two options:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747890%2F002_-_Sampling_07.1749747889898.png)

Option 1: Give the MCP server direct access to Claude. The server would need its own API key, handle authentication, manage costs, and implement all the Claude integration code. This works but adds significant complexity.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747890%2F002_-_Sampling_09.1749747890532.png)

Option 2: Use sampling. The server generates a prompt and asks the client "Could you call Claude for me?" The client, which already has a connection to Claude, makes the call and returns the results.

## How Sampling Works

The flow is straightforward:

- Server completes its work (like fetching Wikipedia articles)
- Server creates a prompt asking for text generation
- Server sends a sampling request to the client
- Client calls Claude with the provided prompt
- Client returns the generated text to the server
- Server uses the generated text in its response

## Benefits of Sampling

- Reduces server complexity: The server doesn't need to integrate with language models directly
- Shifts cost burden: The client pays for token usage, not the server
- No API keys needed: The server doesn't need credentials for Claude
- Perfect for public servers: You don't want a public server racking up AI costs for every user

## Implementation

Setting up sampling requires code on both sides:

### Server Side

In your tool function, use the create_message function to request text generation:

```
create_message
```

```
@mcp.tool()
async def summarize(text_to_summarize: str, ctx: Context):
    prompt = f"""
    Please summarize the following text:
    {text_to_summarize}
    """
    
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(
                    type="text",
                    text=prompt
                )
            )
        ],
        max_tokens=4000,
        system_prompt="You are a helpful research assistant",
    )
    
    if result.content.type == "text":
        return result.content.text
    else:
        raise ValueError("Sampling failed")
```

```
@mcp.tool()
async def summarize(text_to_summarize: str, ctx: Context):
    prompt = f"""
    Please summarize the following text:
    {text_to_summarize}
    """
    
    result = await ctx.session.create_message(
        messages=[
            SamplingMessage(
                role="user",
                content=TextContent(
                    type="text",
                    text=prompt
                )
            )
        ],
        max_tokens=4000,
        system_prompt="You are a helpful research assistant",
    )
    
    if result.content.type == "text":
        return result.content.text
    else:
        raise ValueError("Sampling failed")
```

### Client Side

Create a sampling callback that handles the server's requests:

```
async def sampling_callback(
    context: RequestContext, params: CreateMessageRequestParams
):
    # Call Claude using the Anthropic SDK
    text = await chat(params.messages)
    
    return CreateMessageResult(
        role="assistant",
        model=model,
        content=TextContent(type="text", text=text),
    )
```

```
async def sampling_callback(
    context: RequestContext, params: CreateMessageRequestParams
):
    # Call Claude using the Anthropic SDK
    text = await chat(params.messages)
    
    return CreateMessageResult(
        role="assistant",
        model=model,
        content=TextContent(type="text", text=text),
    )
```

Then pass this callback when initializing your client session:

```
async with ClientSession(
    read,
    write,
    sampling_callback=sampling_callback
) as session:
    await session.initialize()
```

```
async with ClientSession(
    read,
    write,
    sampling_callback=sampling_callback
) as session:
    await session.initialize()
```

## When to Use Sampling

Sampling is most valuable when building publicly accessible MCP servers. You don't want random users generating unlimited text at your expense. By using sampling, each client pays for their own AI usage while still benefiting from your server's functionality.

The technique essentially moves the AI integration complexity from your server to the client, which often already has the necessary connections and credentials in place.

---

## Sampling walkthrough

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172

details

1
                                    download

## Sampling walkthrough

On the server, during a tool call, run the create_message() method, passing in some messages that you wish to send to a language model.

```
create_message()
```

On the client, you must implement a sampling callback. It will receive a list of messages provided by the server.

The list of messages provided by the server are formatted for communication in MCP. The individual messages aren't guaranteed to be compatible with whatever LLM SDK you are using.

For example, if you're using the Anthropic SDK, you'll have to write a little bit of conversion logic to turn the MCP messages into a format compatible with Anthropic's SDK.

After generating text with the LLM, you'll return a CreateMessageResult, which contains the generated text.

```
CreateMessageResult
```

Don't forget: the callback on the client needs to be passed into the ClientSession call.

```
ClientSession
```

After the client has generated and returned some text, it will be sent to the server. You can do anything with this text:

- Use it as part of a workflow in your tool
- Decide to make another sampling call
- Return the generated text

### Files

#### Downloads

- sampling.zip
                                                (opens in new tab)

### Tutorial Steps

Let's get a better sense of how to implement this feature by walking through a sample project.

---

## Log and progress notifications

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296284

details

## Log and progress notifications

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Logging and progress notifications are simple to implement but make a huge difference in user experience when working with MCP servers. They help users understand what's happening during long-running operations instead of wondering if something has broken.

When Claude calls a tool that takes time to complete - like researching a topic or processing data - users typically see nothing until the operation finishes. This can be frustrating because they don't know if the tool is working or has stalled.

With logging and progress notifications enabled, users get real-time feedback showing exactly what's happening behind the scenes. They can see progress bars, status messages, and detailed logs as the operation runs.

## How It Works

In the Python MCP SDK, logging and progress notifications work through the Context argument that's automatically provided to your tool functions. This context object gives you methods to communicate back to the client during execution.

```
@mcp.tool(
    name="research",
    description="Research a given topic"
)
async def research(
    topic: str = Field(description="Topic to research"),
    *,
    context: Context
):
    await context.info("About to do research...")
    await context.report_progress(20, 100)
    sources = await do_research(topic)
    
    await context.info("Writing report...")
    await context.report_progress(70, 100)
    results = await generate_report(sources)
    
    return results
```

```
@mcp.tool(
    name="research",
    description="Research a given topic"
)
async def research(
    topic: str = Field(description="Topic to research"),
    *,
    context: Context
):
    await context.info("About to do research...")
    await context.report_progress(20, 100)
    sources = await do_research(topic)
    
    await context.info("Writing report...")
    await context.report_progress(70, 100)
    results = await generate_report(sources)
    
    return results
```

The key methods you'll use are:

- context.info() - Send log messages to the client

```
context.info()
```

- context.report_progress() - Update progress with current and total values

```
context.report_progress()
```

## Client-Side Implementation

On the client side, you need to set up callback functions to handle these notifications. The server emits these messages, but it's up to your client application to decide how to present them to users.

```
async def logging_callback(params: LoggingMessageNotificationParams):
    print(params.data)

async def print_progress_callback(
    progress: float, total: float | None, message: str | None
):
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {progress}/{total} ({percentage:.1f}%)")
    else:
        print(f"Progress: {progress}")

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read,
            write,
            logging_callback=logging_callback
        ) as session:
            await session.initialize()
            
            await session.call_tool(
                name="add",
                arguments={"a": 1, "b": 3},
                progress_callback=print_progress_callback,
            )
```

```
async def logging_callback(params: LoggingMessageNotificationParams):
    print(params.data)

async def print_progress_callback(
    progress: float, total: float | None, message: str | None
):
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {progress}/{total} ({percentage:.1f}%)")
    else:
        print(f"Progress: {progress}")

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read,
            write,
            logging_callback=logging_callback
        ) as session:
            await session.initialize()
            
            await session.call_tool(
                name="add",
                arguments={"a": 1, "b": 3},
                progress_callback=print_progress_callback,
            )
```

You provide the logging callback when creating the client session, and the progress callback when making individual tool calls. This gives you flexibility to handle different types of notifications appropriately.

## Presentation Options

How you present these notifications depends on your application type:

- CLI applications - Simply print messages and progress to the terminal
- Web applications - Use WebSockets, server-sent events, or polling to push updates to the browser
- Desktop applications - Update progress bars and status displays in your UI
Remember that implementing these notifications is entirely optional. You can choose to ignore them completely, show only certain types, or present them however makes sense for your application. They're purely user experience enhancements to help users understand what's happening during long-running operations.

---

## Notifications walkthrough

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036

details

1
                                    download

## Notifications walkthrough

Tool functions automatically receive 'Context' as their last argument. This object has methods for logging and reporting progress to the client.

Throughout your tool function, call the info(), warning(), debug(), or error() methods to log different types of messages for the client. Also call the report_progress() method to estimate the amount of remaining work for the tool call.

```
info()
```

```
warning()
```

```
debug()
```

```
error()
```

```
report_progress()
```

The client needs to define logging and progress callbacks, which will automatically be called whenever the server emits log or progress messages. These callbacks should try to display the provided logging and progress data to the user.

Make sure you provide the logging callback to the ClientSession and the progress callback to the call_tool() function.

```
ClientSession
```

```
call_tool()
```

### Files

#### Downloads

- notifications.zip
                                                (opens in new tab)

### Tutorial Steps

Let's get a better sense of how to implement this feature by walking through a sample project.

---

## Roots

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296289

details

## Roots

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

Roots are a way to grant MCP servers access to specific files and folders on your local machine. Think of them as a permission system that says "Hey, MCP server, you can access these files" - but they do much more than just grant permission.

## The Problem Roots Solve

Without roots, you'd run into a common issue. Imagine you have an MCP server with a video conversion tool that takes a file path and converts an MP4 to MOV format.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747894%2F004_-_Roots_01.1749747894124.png)

When a user asks Claude to "convert biking.mp4 to mov format", Claude would call the tool with just the filename. But here's the problem - Claude has no way to search through your entire file system to find where that file actually lives.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747894%2F004_-_Roots_04.1749747894579.png)

Your file system might be complex with files scattered across different directories. The user knows the biking.mp4 file is in their Movies folder, but Claude doesn't have that context.

You could solve this by requiring users to always provide full paths, but that's not very user-friendly. Nobody wants to type out complete file paths every time.

## Roots in Action

Here's how the workflow changes with roots:

- User asks to convert a video file
- Claude calls list_roots to see what directories it can access

```
list_roots
```

- Claude calls read_dir on accessible directories to find the file

```
read_dir
```

- Once found, Claude calls the conversion tool with the full path
This happens automatically - users can still just say "convert biking.mp4" without providing full paths.

## Security and Boundaries

Roots also provide security by limiting access. If you only grant access to your Desktop folder, the MCP server cannot access files in other locations like Documents or Downloads.

When Claude tries to access a file outside the approved roots, it gets an error and can inform the user that the file isn't accessible from the current server configuration.

## Implementation Details

The MCP SDK doesn't automatically enforce root restrictions - you need to implement this yourself. A typical pattern is to create a helper function like is_path_allowed() that:

```
is_path_allowed()
```

- Takes a requested file path
- Gets the list of approved roots
- Checks if the requested path falls within one of those roots
- Returns true/false for access permission
You then call this function in any tool that accesses files or directories before performing the actual file operation.

## Key Benefits

- User-friendly - Users don't need to provide full file paths
- Focused search - Claude only looks in approved directories, making file discovery faster
- Security - Prevents accidental access to sensitive files outside approved areas
- Flexibility - You can provide roots through tools or inject them directly into prompts
Roots make MCP servers both more powerful and more secure by giving Claude the context it needs to find files while maintaining clear boundaries around what it can access.

---

## Roots walkthrough

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295839

details

1
                                    download

## Roots walkthrough

Ideally, a user will dictate which files/folders can be accessed by the MCP server.

This program is set up to accept a list of CLI arguments, which are interpretted as paths that the user wants to allow access to.

That list of paths is provided to the MCPClient down on lines 42.

```
MCPClient
```

According to the MCP spec, all roots should have a URI that begins with file://.

```
file://
```

This function takes the list of paths of that the user provided and turns them into Root objects.

```
Root
```

The client doesn't immediately provide the list of roots to the server. Instead, the server can make a request to the client at some future point in time. We make a callback that will be executed when the server requests the roots. The callback needs to return the list of roots inside of a ListRootsResult object.

```
ListRootsResult
```

This callback is passed into the ClientSession down on line 58.

On to the server. The server will use the roots in two scenarios:

- Whenever a tool attempts to access a file or folder
- When a LLM (like Claude) needs to resolve a file or folder to a full path. Think of when a user says 'read the todos.txt file' - Claude needs to figure out where the text file is, and might do so by looking at the list of roots
To handle the second case, we can either define a tool that lists out the roots or inject them directly in a prompt.

Roots are accessed by calling ctx.session.list_roots().

```
ctx.session.list_roots()
```

This sends a message back to the client, which causes it to run the root-listing callback.

Remember: the MCP SDK does not attempt to limit what files or folders your tools attempt to read! You must implement that check yourself.

Consider implementing a function like is_path_allowed, which will decide whether a path is accessible by comparing it to the list of roots.

```
is_path_allowed
```

Once you've put an authorization function together - like is_path_allowed - use it throughout your tools to ensure the requested path is accessible.

```
is_path_allowed
```

### Files

#### Downloads

- roots.zip
                                                (opens in new tab)

### Tutorial Steps

Let's get a better sense of how to implement this feature by walking through a sample project.

---

## Survey

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/297276

## Survey

# Course Satisfaction Survey - Advanced MCP

Mind sharing your thoughts and experiences around this course?

---

## JSON message types

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296290

details

## JSON message types

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

MCP (Model Context Protocol) uses JSON messages to handle communication between clients and servers. Understanding these message types is crucial for working with MCP, especially when dealing with different transport methods like the streamable HTTP transport.

## Message Format

All MCP communication happens through JSON messages. Each message type serves a specific purpose - whether it's calling a tool, listing available resources, or sending notifications about system events.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747889%2F005_-_JSON_Message_Types_04.1749747889371.png)

Here's a typical example: when Claude needs to call a tool provided by an MCP server, the client sends a "Call Tool Request" message. The server processes this request, runs the tool, and responds with a "Call Tool Result" message containing the output.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747889%2F005_-_JSON_Message_Types_05.1749747889768.png)

## MCP Specification

The complete list of message types is defined in the official MCP specification repository on GitHub. This specification is separate from the various SDK repositories (like Python or TypeScript SDKs) and serves as the authoritative source for how MCP should work.

The message types are written in TypeScript for convenience - not because they're executed as TypeScript code, but because TypeScript provides a clear way to describe data structures and types.

## Message Categories

MCP messages fall into two main categories:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747891%2F005_-_JSON_Message_Types_13.1749747891508.png)

### Request-Result Messages

These messages always come in pairs. You send a request and expect to get a result back:

- Call Tool Request → Call Tool Result
- List Prompts Request → List Prompts Result
- Read Resource Request → Read Resource Result
- Initialize Request → Initialize Result

### Notification Messages

These are one-way messages that inform about events but don't require a response:

- Progress Notification - Updates on long-running operations
- Logging Message Notification - System log messages
- Tool List Changed Notification - When available tools change
- Resource Updated Notification - When resources are modified

## Client vs Server Messages

The MCP specification organizes messages by who sends them:

Client messages include requests that clients send to servers (like tool calls) and notifications that clients might send.

Server messages include requests that servers send to clients and notifications that servers broadcast.

## Why This Matters

Understanding that servers can send messages to clients is particularly important when working with different transport methods. Some transports, like the streamable HTTP transport, have limitations on which types of messages can flow in which directions.

The key insight is that MCP is designed as a bidirectional protocol - both clients and servers can initiate communication. This becomes crucial when you need to choose the right transport method for your specific use case.

---

## The STDIO transport

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296291

details

## The STDIO transport

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

MCP clients and servers communicate by exchanging JSON messages, but how do these messages actually get transmitted? The communication channel used is called a transport, and there are several ways to implement this - from HTTP requests to WebSockets to even writing JSON on a postcard (though that last one isn't recommended for production use).

## The Stdio Transport

When you're first developing an MCP server or client, the most commonly used transport is the stdio transport. This approach is straightforward: the client launches the MCP server as a subprocess and communicates through standard input and output streams.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747951%2F006_-_The_Stdio_Transport_02.1749747951605.png)

Here's how it works:

- Client sends messages to the server using the server's stdin

```
stdin
```

- Server responds by writing to stdout

```
stdout
```

- Either the server or client can send a message at any time
- Only works when client and server run on the same machine

## Seeing Stdio in Action

You can actually test an MCP server directly from your terminal without writing a separate client. When you run a server with uv run server.py, it listens to stdin and writes responses to stdout. This means you can paste JSON messages directly into your terminal and see the server's responses immediately.

```
uv run server.py
```

The terminal output shows the complete message exchange, including example messages for initialization and tool calls.

## MCP Connection Sequence

Every MCP connection must start with a specific three-message handshake:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747952%2F006_-_The_Stdio_Transport_07.1749747952662.png)

- Initialize Request - Client sends this first
- Initialize Result - Server responds with capabilities
- Initialized Notification - Client confirms (no response expected)
Only after this handshake can you send other requests like tool calls or prompt listings.

## Message Types and Flow

MCP supports various message types that flow in both directions:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747953%2F006_-_The_Stdio_Transport_13.1749747953112.png)

The key insight is that some messages require responses (requests → results) while others don't (notifications). Both client and server can initiate communication at any time.

## Four Communication Scenarios

With any transport, you need to handle four different communication patterns:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747953%2F006_-_The_Stdio_Transport_15.1749747953530.png)

- Client → Server request: Client writes to stdin
- Server → Client response: Server writes to stdout
- Server → Client request: Server writes to stdout
- Client → Server response: Client writes to stdin
The beauty of stdio transport is its simplicity - either party can initiate communication at any time using these two channels.

## Why This Matters

Understanding stdio transport is crucial because it represents the "ideal" case where bidirectional communication is seamless. When we move to other transports like HTTP, we'll encounter limitations where the server cannot always initiate requests to the client. The stdio transport serves as our baseline for understanding what full MCP communication looks like before we tackle the constraints of other transport methods.

For development and testing, stdio transport is perfect. For production deployments where client and server need to run on different machines, you'll need to consider other transport options with their own trade-offs.

---

## The StreamableHTTP transport

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296287

details

## The StreamableHTTP transport

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The streamable HTTP transport enables MCP clients to connect to remotely hosted servers over HTTP connections. Unlike the standard I/O transport that requires both client and server on the same machine, this transport opens up possibilities for public MCP servers that anyone can access.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747948%2F007_-_The_StreamableHTTP_Transport_00.1749747948797.png)

However, there's an important caveat: some configuration settings can significantly limit your MCP server's functionality. If your application works perfectly with standard I/O transport locally but breaks when deployed with HTTP transport, this is likely the culprit.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747949%2F007_-_The_StreamableHTTP_Transport_02.1749747949391.png)

## Configuration Settings That Matter

Two key settings control how the streamable HTTP transport behaves:

- stateless_http - Controls connection state management

```
stateless_http
```

- json_response - Controls response format handling

```
json_response
```

By default, both settings are false, but certain deployment scenarios may force you to set them to true. When enabled, these settings can break core functionality like progress notifications, logging, and server-initiated requests.

```
false
```

```
true
```

## The HTTP Communication Challenge

To understand why these limitations exist, we need to review how HTTP communication works. In standard HTTP:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747951%2F007_-_The_StreamableHTTP_Transport_13.1749747951318.png)

- Clients can easily initiate requests to servers (the server has a known URL)
- Servers can easily respond to these requests
- Servers cannot easily initiate requests to clients (clients don't have known URLs)
- Response patterns from client back to server become problematic

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747952%2F007_-_The_StreamableHTTP_Transport_15.1749747951861.png)

## MCP Message Types Affected

This HTTP limitation impacts specific MCP communication patterns. The following message types become difficult to implement with plain HTTP:

- Server-initiated requests: Create Message requests, List Roots requests
- Notifications: Progress notifications, Logging notifications, Initialized notifications, Cancelled notifications
These are exactly the features that break when you enable the restrictive HTTP settings. Progress bars disappear, logging stops working, and server-initiated sampling requests fail.

## The Streamable HTTP Solution

The streamable HTTP transport does provide a clever solution to work around HTTP's limitations, but it comes with trade-offs. When you're forced to use stateless_http=True or json_response=True, you're essentially telling the transport to operate within HTTP's constraints rather than working around them.

```
stateless_http=True
```

```
json_response=True
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747953%2F007_-_The_StreamableHTTP_Transport_19.1749747952895.png)

Understanding these limitations helps you make informed decisions about:

- Which transport to use for different deployment scenarios
- How to design your MCP server to gracefully handle HTTP constraints
- When to accept reduced functionality for the benefits of remote hosting
The key is knowing that these restrictions exist and planning your MCP server architecture accordingly. If your application heavily relies on server-initiated requests or real-time notifications, you may need to reconsider your transport choice or implement alternative communication patterns.

---

## StreamableHTTP in depth

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296286

details

## StreamableHTTP in depth

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

StreamableHTTP is MCP's solution to a fundamental problem: some MCP functionality requires the server to make requests to the client, but HTTP makes this challenging. Let's explore how StreamableHTTP works around this limitation and when you might need to break that workaround.

## The Core Problem

Some MCP features like sampling, notifications, and logging rely on the server initiating requests to the client. However, HTTP is designed for clients to make requests to servers, not the other way around. StreamableHTTP solves this with a clever workaround using Server-Sent Events (SSE).

## How StreamableHTTP Works

The magic happens through a multi-step process that establishes persistent connections between client and server.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747952%2F008_-_StreamableHTTP_in_Depth_04.1749747952200.png)

### Initial Connection Setup

The process starts like any MCP connection:

- Client sends an Initialize Request to the server

```
Initialize Request
```

- Server responds with an Initialize Result that includes a special mcp-session-id header

```
Initialize Result
```

```
mcp-session-id
```

- Client sends an Initialized Notification with the session ID

```
Initialized Notification
```

This session ID is crucial - it uniquely identifies the client and must be included in all future requests.

### The SSE Workaround

After initialization, the client can make a GET request to establish a Server-Sent Events connection. This creates a long-lived HTTP response that the server can use to stream messages back to the client at any time.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747953%2F008_-_StreamableHTTP_in_Depth_06.1749747952963.png)

This SSE connection is the key to allowing server-to-client communication. The server can now send requests, notifications, and other messages through this persistent channel.

## Tool Calls and Dual SSE Connections

When the client makes a tool call, things get more complex. The system creates two separate SSE connections:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747953%2F008_-_StreamableHTTP_in_Depth_08.1749747953358.png)

- Primary SSE Connection: Used for server-initiated requests and stays open indefinitely
- Tool-Specific SSE Connection: Created for each tool call and closes automatically when the tool result is sent

### Message Routing

Different types of messages get routed through different connections:

- Progress notifications: Sent through the primary SSE connection
- Logging messages and tool results: Sent through the tool-specific SSE connection

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747953%2F008_-_StreamableHTTP_in_Depth_11.1749747953846.png)

## Configuration Flags That Break the Workaround

StreamableHTTP includes two important configuration options:

- stateless_http

```
stateless_http
```

- json_response

```
json_response
```

Setting these to True can break the SSE workaround mechanism. You might want to enable these flags in certain scenarios, but doing so limits the full MCP functionality that depends on server-to-client communication.

```
True
```

## Key Takeaways

StreamableHTTP is more complex than other MCP transports because it has to work around HTTP's limitations. The SSE-based workaround enables full MCP functionality over HTTP, but understanding the dual-connection model is crucial for debugging and optimization.

When building MCP applications with StreamableHTTP, remember that session IDs are required for all requests after initialization, and the system automatically manages multiple SSE connections to handle different types of server-to-client communication.

---

## State and the StreamableHTTP transport

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296285

details

1
                                    download

## State and the StreamableHTTP transport

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.

#### Summary

The stateless_http and json_response flags in MCP servers control fundamental aspects of how your server behaves. Understanding when and why to use them is crucial, especially if you're planning to scale your server or deploy it in production.

```
stateless_http
```

```
json_response
```

## When You Need Stateless HTTP

Imagine you build an MCP server that becomes popular. Initially, you might have just a few clients connecting to a single server instance:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747958%2F009_-_Stateless_HTTP_01.1749747958582.png)

As your server grows, you might have thousands of clients trying to connect. Running a single server instance won't scale to handle all that traffic:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747959%2F009_-_Stateless_HTTP_02.1749747959000.png)

The typical solution is horizontal scaling - running multiple server instances behind a load balancer:

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747959%2F009_-_Stateless_HTTP_03.1749747959503.png)

But here's where things get complicated. Remember that MCP clients need two separate connections:

- A GET SSE connection for receiving server-to-client requests
- POST requests for calling tools and receiving responses

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747960%2F009_-_Stateless_HTTP_05.1749747960146.png)

With a load balancer, these requests might get routed to different server instances. If your tool needs to use Claude (through sampling), the server handling the POST request would need to coordinate with the server handling the GET SSE connection. This creates a complex coordination problem between servers.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747960%2F009_-_Stateless_HTTP_06.1749747960668.png)

## How Stateless HTTP Solves This

Setting stateless_http=True eliminates this coordination problem, but with significant trade-offs:

```
stateless_http=True
```

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747961%2F009_-_Stateless_HTTP_09.1749747961056.png)

When stateless HTTP is enabled:

- Clients don't get session IDs - the server can't track individual clients
- No server-to-client requests - the GET SSE pathway becomes unavailable
- No sampling - can't use Claude or other AI models
- No progress reports - can't send progress updates during long operations
- No subscriptions - can't notify clients about resource updates
However, there's one benefit: client initialization is no longer required. Clients can make requests directly without the initial handshake process.

![image](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1749747961%2F009_-_Stateless_HTTP_10.1749747961577.png)

## Understanding JSON Response

The json_response=True flag is simpler - it just disables streaming for POST request responses. Instead of getting multiple SSE messages as a tool executes, you get only the final result as plain JSON.

```
json_response=True
```

With streaming disabled:

- No intermediate progress messages
- No log statements during execution
- Just the final tool result

## When to Use These Flags

Use stateless HTTP when:

- You need horizontal scaling with load balancers
- You don't need server-to-client communication
- Your tools don't require AI model sampling
- You want to minimize connection overhead
Use JSON response when:

- You don't need streaming responses
- You prefer simpler, non-streaming HTTP responses
- You're integrating with systems that expect plain JSON

## Development vs Production

If you're developing locally with standard I/O transport but planning to deploy with HTTP transport, test with the same transport you'll use in production. The behavior differences between stateful and stateless modes can be significant, and it's better to catch any issues during development rather than after deployment.

These flags fundamentally change how your MCP server operates, so choose them based on your specific scaling and functionality requirements.

#### Downloads

- transport-http.zip
                                                (opens in new tab)

---

## Assessment on MCP concepts

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296301

## Assessment on MCP concepts

# Assessment on MCP Concepts

---

## Wrapping up

> https://anthropic.skilljar.com/model-context-protocol-advanced-topics/296350

## Wrapping up

This video is still being processed. Please check back later and refresh the page.

Uh oh! Something went wrong, please try again.