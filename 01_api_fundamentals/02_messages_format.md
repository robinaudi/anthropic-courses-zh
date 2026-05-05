# 處理訊息

## 課程目標
- 理解訊息 API 格式
- 使用和理解模型回應物件
- 建立簡單的多輪對話聊天機器人

## 基本設定
我們將從匯入所需的套件並初始化用戶端物件開始。
有關如何取得 API 金鑰和正確存儲的詳細資訊，請參閱上一個教學。

```python
from dotenv import load_dotenv
from anthropic import Anthropic

#載入環境變數
load_dotenv()

#自動尋找「ANTHROPIC_API_KEY」環境變數
client = Anthropic()
```

## 訊息格式

如我們在上一堂課中看到的，我們可以使用 `client.messages.create()` 向 Claude 發送訊息並獲得回應：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "What flavors are used in Dr. Pepper?"}
    ]
)

print(response)
```

```
Message(id='msg_013wVsHLHRjuDM2WgvVJ8RNm', content=[ContentBlock(text='The exact flavor formula for Dr Pepper is a closely guarded trade secret, but here are some of the main flavors that are believed to be used:\n\n- Cherry - This is one of the most prominent flavors in Dr Pepper. The cherry flavor comes from the use of a type of cherry extract.\n\n- Prune - Dr Pepper contains a prune-like flavor which contributes to its unique profile.\n\n- Vanilla - Vanilla is another key component that helps round out the flavor.\n\n- Spices - Various spices like cinnamon, prune, and other aromatics are believed to be part of the blend.\n\n- Citrus - Flavors like orange, lemon, and prune add some citrus notes.\n\nThe exact combination of these and other secret ingredients is what gives Dr Pepper its signature taste that differentiates it from other cola or soda flavors. The complex blend of sweet, spicy, and tart notes is part of what makes Dr Pepper a unique and iconic soft drink flavor.', type='text')], model='claude-3-haiku-20240307', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=18, output_tokens=225))
```

讓我們仔細看看這部分：
```py
messages=[
        {"role": "user", "content": "What flavors are used in Dr. Pepper?"}
    ]
```

訊息參數是與 Claude API 互動的重要部分。它允許您提供對話歷史和背景，供 Claude 生成相關回應。

訊息參數預期是訊息字典的清單，其中每個字典代表對話中的單個訊息。
每個訊息字典應具有以下金鑰：

* `role`：表示訊息發送者角色的字串。可以是「user」（代表使用者發送的訊息）或「assistant」（代表 Claude 發送的訊息）。
* `content`：代表訊息實際內容的字串或內容字典清單。如果提供字串，它將被視為單個文字內容區塊。如果提供內容字典清單，每個字典應具有「type」（例如「text」或「image」）和相應的內容。現在，我們將 `content` 保持為單個字串。

以下是包含單個使用者訊息的訊息清單示例：

```py
messages = [
    {"role": "user", "content": "Hello Claude! How are you today?"}
]
```

以下是包含代表對話的多個訊息的示例：

```py
messages = [
    {"role": "user", "content": "Hello Claude! How are you today?"},
    {"role": "assistant", "content": "Hello! I'm doing well, thank you. How can I assist you today?"},
    {"role": "user", "content": "Can you tell me a fun fact about ferrets?"},
    {"role": "assistant", "content": "Sure! Did you know that excited ferrets make a clucking vocalization known as 'dooking'?"},
]
```

請記住訊息始終在使用者和助手訊息之間交替。

![alternating_messages.png](images/alternating_messages.png)

訊息格式允許我們以對話的形式構建對 Claude 的 API 呼叫，允許**背景保留**：訊息格式允許維護整個對話歷史，包括使用者和助手訊息。這確保 Claude 可以存取對話的完整背景，從而生成更一致和相關的輸出。

**注意：許多用例不需要對話歷史，只提供包含單個訊息的訊息清單沒有任何問題！**

***

## 測驗

每個訊息中的兩個必需金鑰是什麼？

* **a)** 「sender」和「text」
* **b)** 「role」和「content」
* **c)** 「user」和「assistant」
* **d)** 「input」和「output」

<details>
  <summary>檢視測驗答案</summary>
  
  **正確答案是 b。每個訊息應具有「role」和「content」**

</details>




***

## 檢查訊息回應
接下來，讓我們仔細查看我們從 Claude 獲得的回應形狀。

讓我們要求 Claude 做一些簡單的事情：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Translate hello to French. Respond with a single word"}
    ]
)
```

現在讓我們檢查我們獲得的 `response` 的內容：

```python
response
```

```
Message(id='msg_01SuDqJSTJaRpkDmHGrbfxCt', content=[ContentBlock(text='Bonjour.', type='text')], model='claude-3-haiku-20240307', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=19, output_tokens=8))
```

我們獲得一個 `Message` 物件，其中包含少數幾個屬性。這是一個例子：

```
Message(id='msg_01Mq5gDnUmDESukTgwPV8xtG', content=[TextBlock(text='Bonjour.', type='text')], model='claude-3-haiku-20240307', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=19, output_tokens=8))
```

 最重要的資訊是 `content` 屬性：這包含模型為我們生成的實際內容。這是內容區塊的**清單**，每個區塊都有一個確定其形狀的類型。

 ![message_content.png](images/message_content.png)

 為了存取模型回應的實際文字內容，我們需要執行以下操作：



```python
print(response.content[0].text)
```

```
Bonjour.
```

除了 `content` 之外，`Message` 物件還包含其他一些資訊片段：

* `id` - 唯一的物件識別碼
* `type` - 物件類型，始終為「message」
* `role` - 生成訊息的對話角色。這始終為「assistant」。
* `model` - 處理請求和生成回應的模型
* `stop_reason` - 模型停止生成的原因。我們稍後會詳細瞭解這一點。
* `stop_sequence` - 我們稍後會詳細瞭解這一點。
* `usage` - 有關帳單和速率限制使用情況的資訊。包含：
    * `input_tokens` - 使用的輸入符號數量。
    * `output_tokens` - 生成的輸出符號數量。

重要的是要知道我們可以存取這些資訊，但如果您只記得一件事，那就是：`content` 包含實際的模型生成內容

***
## 練習

編寫一個名為 translate 的函數，預期兩個引數：
* 一個單詞
* 一種語言

當您呼叫 `translate` 函數時，它應該返回要求 Claude 將 `word` 翻譯為 `language` 的結果。例如：

```py
translate("hello", "Spanish")
# 'The word "hello" translated into Spanish is: Hola'

translate("chicken", "Italian")
# 'The Italian word for "chicken" is: pollo'
```

如果您可以編寫一個提示，使得 Claude 只回應翻譯後的單詞，而不帶任何前言，您會獲得加分，例如：

```py
translate("chicken", "Italian")
# 'pollo'
```


<details>
  <summary>檢視練習解決方案</summary>
  
  以下是一個可能的解決方案：
  
  ```py
  def translate(word, language):
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": f"Translate the word {word} into {language}.  Only respond with the translated word, nothing else"}
        ]
    )
    return response.content[0].text 
  ```

</details>




***

## 訊息清單錯誤

### 錯誤 #1：以助手訊息開始

當您才開始時，在使用 `messages` 清單時容易犯錯。訊息清單必須以 `user` 訊息開始。以下程式碼會產生錯誤，因為訊息清單以助手訊息開始：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "assistant", "content": "Hello there!"}
    ]
)
print(response.content[0].text)
```

> **錯誤: BadRequestError**: 錯誤代碼: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'messages: first message must use the "user" role'}}

### 錯誤 #2：不當的訊息交替

訊息必須在 `user` 和 `assistant` 之間交替，如果我們不遵循此規則，我們會收到錯誤：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hey there!"},
        {"role": "assistant", "content": "Hi there!"},
        {"role": "assistant", "content": "How can I help you??"}
    ]
)
print(response.content[0].text)
```

> **錯誤: BadRequestError**: 錯誤代碼: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'messages: roles must alternate between "user" and "assistant", but found multiple "assistant" roles in a row'}}

## 訊息清單用例



### 把話放在 Claude 的嘴裡

獲得非常具體的輸出的另一種常見策略是「把話放在 Claude 的嘴裡」。與只向 Claude 提供 `user` 訊息不同，我們也可以提供 Claude 將在生成輸出時使用的 `assistant` 訊息。

使用 Anthropic 的 API 時，您不限於只有 `user` 訊息。如果您提供 `assistant` 訊息，Claude 將從最後一個 `assistant` 符號繼續對話。只記住我們必須以 `user` 訊息開始。

假設我想讓 Claude 為我寫一首以第一行「calming mountain air」開始的俳句。我可以提供以下對話歷史：

```py
messages=[
        {"role": "user", "content": f"Generate a beautiful haiku"},
        {"role": "assistant", "content": "calming mountain air"}
    ]
```
我們告訴 Claude 我們想要它生成俳句，並將俳句的第一行放在 Claude 的嘴裡




```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": f"Generate a beautiful haiku"},
        {"role": "assistant", "content": "calming mountain air"}
    ]
)
print(response.content[0].text)
```

```
,
dancing sunlight on still waters,
nature's gentle grace.
```

要取得整個俳句，從我們提供的行開始：

```python
print("calming mountain air" + response.content[0].text)
```

```
calming mountain air,
dancing sunlight on still waters,
nature's gentle grace.
```

### 少樣本提示

最有用的提示策略之一稱為「少樣本提示」，涉及向模型提供少量**範例**。這些範例有助於引導 Claude 的生成輸出。訊息對話歷史是向 Claude 提供範例的簡單方式。

例如，假設我們想使用 Claude 來分析推文中的情感。我們可以首先簡單地要求 Claude「請分析這條推文中的情感：」，看看我們得到什麼樣的輸出：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": f"Analyze the sentiment in this tweet: Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
    ]
)
print(response.content[0].text)
```

```
The sentiment in this tweet is overwhelmingly positive. The user expresses their enjoyment of the new spicy pickles from @PickleCo, using enthusiastic language and emojis to convey their delight.

Positive indicators:
1. "My taste buds are doing a happy dance!" - This phrase indicates that the user is extremely pleased with the taste of the pickles, to the point of eliciting a joyful physical response.

2. Emojis - The use of the hot pepper 🌶️ and cucumber 🥒 emojis further emphasizes the user's excitement about the spicy pickles.

3. Hashtags - The inclusion of #pickleslove and #spicyfood hashtags suggests that the user has a strong affinity for pickles and spicy food, and the new product aligns perfectly with their preferences.

4. Exclamation mark - The exclamation mark at the end of the first sentence adds emphasis to the user's positive experience.

Overall, the tweet conveys a strong sense of satisfaction, excitement, and enjoyment related to trying the new spicy pickles from @PickleCo.
```

我第一次執行上述程式碼時，Claude 生成了這個長回應：
```
The sentiment in this tweet is overwhelmingly positive. The user expresses their enjoyment of the new spicy pickles from @PickleCo, using enthusiastic language and emojis to convey their delight.

Positive indicators:
1. "My taste buds are doing a happy dance!" - This phrase indicates that the user is extremely pleased with the taste of the pickles, to the point of eliciting a joyful physical response.

2. Emojis - The use of the hot pepper 🌶️ and cucumber 🥒 emojis further emphasizes the user's excitement about the spicy pickles.

3. Hashtags - The inclusion of #pickleslove and #spicyfood hashtags suggests that the user has a strong affinity for pickles and spicy food, and the new product aligns perfectly with their preferences.

4. Exclamation mark - The exclamation mark at the end of the first sentence adds emphasis to the user's positive experience.

Overall, the tweet conveys a strong sense of satisfaction, excitement, and enjoyment related to trying the new spicy pickles from @PickleCo.
```

這是一個很好的回應，但它可能遠遠超過我們需要的信息量，尤其是如果我們嘗試自動化大量推文的情感分析。

我們可能希望 Claude 以標準化的輸出格式回應，例如單個單詞 (POSITIVE, NEUTRAL, NEGATIVE) 或數值 (1, 0, -1)。為了易讀性和簡潔性，讓我們讓 Claude 回應「POSITIVE」或「NEGATIVE」。一種方式是透過少樣本提示。我們可以向 Claude 提供對話歷史，精確顯示我們希望它如何回應：

```py
messages=[
        {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
    ]
```



```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Unpopular opinion: Pickles are disgusting. Don't @ me"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "I think my love for pickles might be getting out of hand. I just bought a pickle-shaped pool float"},
        {"role": "assistant", "content": "POSITIVE"},
        {"role": "user", "content": "Seriously why would anyone ever eat a pickle?  Those things are nasty!"},
        {"role": "assistant", "content": "NEGATIVE"},
        {"role": "user", "content": "Just tried the new spicy pickles from @PickleCo, and my taste buds are doing a happy dance! 🌶️🥒 #pickleslove #spicyfood"},
    ]
)
print(response.content[0].text)
```

```
POSITIVE
```

***

## 練習

### 您的任務：建立聊天機器人

建立一個簡單的多輪命令列聊天機器人指令碼。訊息格式適合建立基於聊天的應用程式。要使用 Claude 建立聊天機器人，就像以下方式一樣簡單：

1. 保持一個清單來儲存對話歷史
2. 使用 `input()` 要求使用者輸入訊息，並將使用者輸入新增到訊息清單
3. 將訊息歷史傳送給 Claude
4. 向使用者列印 Claude 的回應
5. 將 Claude 的助手回應新增到歷史記錄
6. 回到步驟 2 並重複！（使用迴圈並提供使用者退出的方式！）


<details>
    <summary>檢視練習解決方案</summary>

    ```py

    conversation_history = []

    while True:
        user_input = input("User: ")
        
        if user_input.lower() == "quit":
            print("Conversation ended.")
            break
        
        conversation_history.append({"role": "user", "content": user_input})
    
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            messages=conversation_history,
            max_tokens=500
        )
    
        assistant_response = response.content[0].text
        print(f"Assistant: {assistant_response}")
        conversation_history.append({"role": "assistant", "content": assistant_response})
    ```
</details>

***
