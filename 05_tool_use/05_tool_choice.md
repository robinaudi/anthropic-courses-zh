# 工具選擇（Tool choice）

Claude API 支援一個名為 `tool_choice` 的參數，讓你可以指定 Claude 呼叫工具的方式。在這個 notebook 中，我們將看看它的運作方式以及何時使用它。

使用 `tool_choice` 參數時，有三種可能的選項：

* `auto` 允許 Claude 自行決定是否呼叫任何提供的工具。
* `any` 告訴 Claude 它必須使用其中一個提供的工具，但不強制指定特定工具。
* `tool` 讓我們強制 Claude 始終使用特定工具。


以下圖示說明每個選項的運作方式：

![tool_choice.png](images/tool_choice.png)

讓我們逐一詳細了解每個選項。我們先匯入 Anthropic SDK：

```python
from anthropic import Anthropic
client = Anthropic()
```

## Auto（自動）

將 `tool_choice` 設為 `auto` 可以讓模型自動決定是否使用工具。這是在使用工具時若不使用 `tool_choice` 參數的預設行為。

為了示範這一點，我們將提供 Claude 一個假的網路搜尋工具。我們會問 Claude 一些問題，其中有些需要呼叫網路搜尋工具，另一些則是 Claude 應能自行回答的。

我們先定義一個名為 `web_search` 的工具。請注意，為了簡化示範，我們在這裡並不實際搜尋網路。

```python
def web_search(topic):
    print(f"pretending to search the web for {topic}")

web_search_tool = {
    "name": "web_search",
    "description": "A tool to retrieve up to date information on a given topic by searching the web",
    "input_schema": {
        "type": "object",
        "properties": {
            "topic": {
                "type": "string",
                "description": "The topic to search the web for"
            },
        },
        "required": ["topic"]
    }
}

```

接下來，我們撰寫一個接受 `user_query` 並將其連同 `web_search_tool` 一起傳遞給 Claude 的函式。

我們也將 `tool_choice` 設為 `auto`：

```python
tool_choice={"type": "auto"}
```

以下是完整的函式：

```python
from datetime import date

def chat_with_web_search(user_query):
    messages = [{"role": "user", "content": user_query}]

    system_prompt=f"""
    Answer as many questions as you can using your existing knowledge.  
    Only search the web for queries that you can not confidently answer.
    Today's date is {date.today().strftime("%B %d %Y")}
    If you think a user's question involves something in the future that hasn't happened yet, use the search tool.
    """

    response = client.messages.create(
        system=system_prompt,
        model="claude-3-sonnet-20240229",
        messages=messages,
        max_tokens=1000,
        tool_choice={"type": "auto"},
        tools=[web_search_tool]
    )
    last_content_block = response.content[-1]
    if last_content_block.type == "text":
        print("Claude did NOT call a tool")
        print(f"Assistant: {last_content_block.text}")
    elif last_content_block.type == "tool_use":
        print("Claude wants to use a tool")
        print(last_content_block)
```

我們先問一個 Claude 應能自行回答的問題：

```python
chat_with_web_search("What color is the sky?")
```
```
Claude did NOT call a tool
Assistant: The sky appears blue during the day. This is because the Earth's atmosphere scatters more blue light from the sun than other colors, making the sky look blue.
```

當我們問「天空是什麼顏色？」時，Claude 沒有使用工具。讓我們試試 Claude 應該使用網路搜尋工具才能回答的問題：

```python
chat_with_web_search("Who won the 2024 Miami Grand Prix?")
```
```
Claude wants to use a tool
ToolUseBlock(id='toolu_staging_018nwaaRebX33pHqoZZXDaSw', input={'topic': '2024 Miami Grand Prix winner'}, name='web_search', type='tool_use')
```

當我們問「2024 年邁阿密大獎賽的冠軍是誰？」時，Claude 使用了網路搜尋工具！

讓我們再嘗試幾個例子：

```python
# Claude 應該不需要使用工具：
chat_with_web_search("Who won the Superbowl in 2022?")
```
```
Claude did NOT call a tool
Assistant: The Los Angeles Rams won Super Bowl LVI in 2022, defeating the Cincinnati Bengals by a score of 23-20. The game was played on February 13, 2022 at SoFi Stadium in Inglewood, California.
```

```python
# Claude 應該使用工具：
chat_with_web_search("Who won the Superbowl in 2024?")
```
```
Claude wants to use a tool
ToolUseBlock(id='toolu_staging_016XPwcprHAgYJBtN7A3jLhb', input={'topic': '2024 Super Bowl winner'}, name='web_search', type='tool_use')
```

### 提示詞很重要！

使用 `tool_choice` 設為 `auto` 時，花時間撰寫詳細的提示詞非常重要。通常 Claude 可能過於積極地呼叫工具。撰寫詳細的提示詞可以幫助 Claude 判斷何時應該呼叫工具，何時不應該。在上面的範例中，我們在系統提示詞中加入了具體說明：

```python
system_prompt=f"""
    Answer as many questions as you can using your existing knowledge.  
    Only search the web for queries that you can not confidently answer.
    Today's date is {date.today().strftime("%B %d %Y")}
    If you think a user's question involves something in the future that hasn't happened yet, use the search tool.
"""
```

***

## 強制使用特定工具

我們可以使用 `tool_choice` 強制 Claude 使用特定工具。在以下範例中，我們定義了兩個簡單的工具：
* `print_sentiment_scores` — 一個「誘騙」Claude 生成包含情感分析資料的結構化 JSON 輸出的工具。有關此方法的更多資訊，請參閱 Anthropic Cookbook 中的[使用 Claude 和工具使用提取結構化 JSON](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/extracting_structured_json.ipynb)。
* `calculator` — 一個非常簡單的計算器工具，接受兩個數字並將它們相加。


```python

tools = [
    {
        "name": "print_sentiment_scores",
        "description": "Prints the sentiment scores of a given tweet or piece of text.",
        "input_schema": {
            "type": "object",
            "properties": {
                "positive_score": {"type": "number", "description": "The positive sentiment score, ranging from 0.0 to 1.0."},
                "negative_score": {"type": "number", "description": "The negative sentiment score, ranging from 0.0 to 1.0."},
                "neutral_score": {"type": "number", "description": "The neutral sentiment score, ranging from 0.0 to 1.0."}
            },
            "required": ["positive_score", "negative_score", "neutral_score"]
        }
    },
    {
        "name": "calculator",
        "description": "Adds two number",
        "input_schema": {
            "type": "object",
            "properties": {
                "num1": {"type": "number", "description": "first number to add"},
                "num2": {"type": "number", "description": "second number to add"},
            },
            "required": ["num1", "num2"]
        }
    }
]
```

我們的目標是撰寫一個名為 `analyze_tweet_sentiment` 的函式，接受一則推文並使用 Claude 印出該推文的基本情感分析。最終我們將「強制」Claude 使用 `print_sentiment_scores` 工具，但我們先展示**不**強制工具使用時會發生什麼。

在這個第一個「有問題的」`analyze_tweet_sentiment` 函式版本中，我們提供 Claude 兩個工具。為了方便比較，我們先將 `tool_choice` 設為 `auto`：

```python
tool_choice={"type": "auto"}
```

請注意，我們故意沒有為 Claude 提供一個寫得好的提示詞，以便更容易看出強制使用特定工具的效果。

```python
def analyze_tweet_sentiment(query):
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        tools=tools,
        tool_choice={"type": "auto"},
        messages=[{"role": "user", "content": query}]
    )
    print(response)

```

讓我們看看用推文 `Holy cow, I just made the most incredible meal!`（哇，我剛做了一頓超棒的餐！）呼叫函式時會發生什麼：

```python
analyze_tweet_sentiment("Holy cow, I just made the most incredible meal!")
```
```
ToolsBetaMessage(id='msg_staging_01ApgXx7W7qsDugdaRWh6p21', content=[TextBlock(text="That's great to hear! I don't actually have the capability to assess sentiment from text, but it sounds like you're really excited and proud of the incredible meal you made. Cooking something delicious that you're proud of can definitely give a sense of accomplishment and happiness. Well done on creating such an amazing dish!", type='text')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=429, output_tokens=69))
```

Claude 沒有呼叫我們的 `print_sentiment_scores` 工具，而是直接回應：
> "That's great to hear! I don't actually have the capability to assess sentiment from text, but it sounds like you're really excited and proud of the incredible meal you made"（很高興聽到！我實際上沒有評估文字情感的能力，但聽起來你對自己做的那頓飯感到非常興奮和自豪）

接下來，假設有人發了這則推文：`I love my cats! I had four and just adopted 2 more! Guess how many I have now?`（我愛我的貓！我原本有四隻，剛又領養了 2 隻！猜猜我現在有幾隻？）

```python
analyze_tweet_sentiment("I love my cats! I had four and just adopted 2 more! Guess how many I have now?")
```
```
ToolsBetaMessage(id='msg_staging_018gTrwrx6YwBR2jjhdPooVg', content=[TextBlock(text="That's wonderful that you love your cats and adopted two more! To figure out how many cats you have now, I can use the calculator tool:", type='text'), ToolUseBlock(id='toolu_staging_01RFker5oMQoY6jErz5prmZg', input={'num1': 4, 'num2': 2}, name='calculator', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=442, output_tokens=101))
```

Claude 想要呼叫計算器工具：

> ToolUseBlock(id='toolu_staging_01RFker5oMQoY6jErz5prmZg', input={'num1': 4, 'num2': 2}, name='calculator', type='tool_use')

顯然，目前的實作方式並不符合我們的需求（主要是因為我們故意設計讓它失敗）。

所以讓我們透過更新 `tool_choice` 來強制 Claude **始終**使用 `print_sentiment_scores` 工具：

```python
tool_choice={"type": "tool", "name": "print_sentiment_scores"}
```

除了將 `type` 設為 `tool` 之外，我們還必須提供特定的工具名稱。

```python
def analyze_tweet_sentiment(query):
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        tools=tools,
        tool_choice={"type": "tool", "name": "print_sentiment_scores"},
        messages=[{"role": "user", "content": query}]
    )
    print(response)
```

現在如果我們用之前相同的提示詞來測試 Claude，它每次都會呼叫 `print_sentiment_scores` 工具：

```python
analyze_tweet_sentiment("Holy cow, I just made the most incredible meal!")
```
```
ToolsBetaMessage(id='msg_staging_018GtYk8Xvee3w8Eeh6pbgoq', content=[ToolUseBlock(id='toolu_staging_01FMRQ9pZniZqFUGQwTcFU4N', input={'positive_score': 0.9, 'negative_score': 0.0, 'neutral_score': 0.1}, name='print_sentiment_scores', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=527, output_tokens=79))
```

Claude 呼叫了我們的 `print_sentiment_scores` 工具：

> ToolUseBlock(id='toolu_staging_01FMRQ9pZniZqFUGQwTcFU4N', input={'positive_score': 0.9, 'negative_score': 0.0, 'neutral_score': 0.1}, name='print_sentiment_scores', type='tool_use')

即使我們用一則「數學味十足」的推文來測試，它仍然始終呼叫 `print_sentiment_scores` 工具：

```python
analyze_tweet_sentiment("I love my cats! I had four and just adopted 2 more! Guess how many I have now?")
```
```
ToolsBetaMessage(id='msg_staging_01RACamfrHdpvLxWaNwDfZEF', content=[ToolUseBlock(id='toolu_staging_01Wb6ZKSwKvqVSKLDAte9cKU', input={'positive_score': 0.8, 'negative_score': 0.0, 'neutral_score': 0.2}, name='print_sentiment_scores', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=540, output_tokens=79))
```

即使我們強制 Claude 呼叫 `print_sentiment_scores` 工具，我們仍然應該進行一些基本的提示詞工程，給 Claude 更好的任務背景：

```python
def analyze_tweet_sentiment(query):

    prompt = f"""
    Analyze the sentiment in the following tweet: 
    <tweet>{query}</tweet>
    """
    
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        tools=tools,
        tool_choice={"type": "auto"},
        messages=[{"role": "user", "content": prompt}]
    )
    print(response)
```

***

## Any（任意）

`tool_choice` 的最後一個選項是 `any`，它讓我們告訴 Claude：「你必須呼叫一個工具，但可以選擇哪一個。」想像我們想使用 Claude 建立一個 SMS 聊天機器人。這個聊天機器人與使用者「溝通」的唯一方式是透過 SMS 簡訊。

在以下範例中，我們建立一個非常簡單的簡訊助理，它可以使用兩個工具：
* `send_text_to_user` — 向使用者發送簡訊。
* `get_customer_info` — 根據使用者名稱查詢客戶資料。

目標是建立一個始終呼叫這些工具之一的聊天機器人，而不是直接回應文字。在所有情況下，Claude 都應該嘗試發送簡訊或呼叫 `get_customer_info` 來獲取更多客戶資訊。為了確保這一點，我們將 `tool_choice` 設為 `any`：

```python
tool_choice={"type": "any"}
```

```python
def send_text_to_user(text):
    # 向使用者發送簡訊
    # 為了簡化，我們只印出文字：
    print(f"TEXT MESSAGE SENT: {text}")

def get_customer_info(username):
    return {
        "username": username,
        "email": f"{username}@email.com",
        "purchases": [
            {"id": 1, "product": "computer mouse"},
            {"id": 2, "product": "screen protector"},
            {"id": 3, "product": "usb charging cable"},
        ]
    }

tools = [
    {
        "name": "send_text_to_user",
        "description": "Sends a text message to a user",
        "input_schema": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "The piece of text to be sent to the user via text message"},
            },
            "required": ["text"]
        }
    },
    {
        "name": "get_customer_info",
        "description": "gets information on a customer based on the customer's username.  Response includes email, username, and previous purchases. Only call this tool once a user has provided you with their username",
        "input_schema": {
            "type": "object",
            "properties": {
                "username": {"type": "string", "description": "The username of the user in question. "},
            },
            "required": ["username"]
        }
    },
]

system_prompt = """
All your communication with a user is done via text message.
Only call tools when you have enough information to accurately call them.  
Do not call the get_customer_info tool until a user has provided you with their username. This is important.
If you do not know a user's username, simply ask a user for their username.
"""

def sms_chatbot(user_message):
    messages = [{"role": "user", "content":user_message}]

    response = client.messages.create(
        system=system_prompt,
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        tools=tools,
        tool_choice={"type": "any"},
        messages=messages
    )
    if response.stop_reason == "tool_use":
        last_content_block = response.content[-1]
        if last_content_block.type == 'tool_use':
            tool_name = last_content_block.name
            tool_inputs = last_content_block.input
            print(f"=======Claude Wants To Call The {tool_name} Tool=======")
            if tool_name == "send_text_to_user":
                send_text_to_user(tool_inputs["text"])
            elif tool_name == "get_customer_info":
                print(get_customer_info(tool_inputs["username"]))
            else:
                print("Oh dear, that tool doesn't exist!")
            
    else:
        print("No tool was called. This shouldn't happen!")
    
```

讓我們從簡單的開始：

```python
sms_chatbot("Hey there! How are you?")
```
```
=======Claude Wants To Call The send_text_to_user Tool=======
TEXT MESSAGE SENT: Hello! I'm doing well, thanks for asking. How can I assist you today?
```

Claude 透過呼叫 `send_text_to_user` 工具來回應。

接下來，我們問 Claude 一個稍微複雜一點的問題：

```python
sms_chatbot("I need help looking up an order")
```
```
=======Claude Wants To Call The send_text_to_user Tool=======
TEXT MESSAGE SENT: Hi there, to look up your order details I'll need your username first. Can you please provide me with your username?
```

Claude 想要發送一則簡訊，要求使用者提供他們的使用者名稱。

現在，讓我們看看當我們提供 Claude 我們的使用者名稱時會發生什麼：

```python
sms_chatbot("I need help looking up an order.  My username is jenny76")
```
```
=======Claude Wants To Call The get_customer_info Tool=======
{'username': 'jenny76', 'email': 'jenny76@email.com', 'purchases': [{'id': 1, 'product': 'computer mouse'}, {'id': 2, 'product': 'screen protector'}, {'id': 3, 'product': 'usb charging cable'}]}
```

Claude 呼叫了 `get_customer_info` 工具，正如我們所希望的！

即使我們向 Claude 發送一則無意義的訊息，它仍然會呼叫我們的其中一個工具：

```python
sms_chatbot("askdj aksjdh asjkdbhas kjdhas 1+1 ajsdh")
```
```
=======Claude Wants To Call The send_text_to_user Tool=======
TEXT MESSAGE SENT: I'm afraid I didn't understand your query. Could you please rephrase what you need help with?
```
