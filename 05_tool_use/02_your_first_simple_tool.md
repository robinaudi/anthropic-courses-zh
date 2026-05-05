# 你的第一個簡單工具

在上一堂課中，我們介紹了工具使用的工作流程。現在是時候實際動手實作一個簡單的工具使用範例了。回顧一下，工具使用流程最多包含 4 個步驟：

1. **提供 Claude 工具與使用者提示：**（API 請求）
    * 定義你希望 Claude 能存取的工具集合，包含其名稱、描述和輸入綱要。
    * 提供一個可能需要使用一個或多個工具才能回答的使用者提示。

2. **Claude 使用工具：**（API 回應）
    * Claude 評估使用者提示，判斷是否有任何可用工具能協助處理使用者的查詢或任務。若有，它也會決定要使用哪個（些）工具以及使用什麼輸入。
    * Claude 輸出格式正確的工具使用請求。
    * API 回應的 `stop_reason` 將為 `tool_use`，表示 Claude 希望使用外部工具。

3. **擷取工具輸入、執行程式碼並回傳結果：**（API 請求）
    * 在客戶端，你應從 Claude 的工具使用請求中擷取工具名稱和輸入。
    * 在客戶端執行實際的工具程式碼。
    * 透過繼續對話（包含 `tool_result` 內容區塊的新使用者訊息）將結果回傳給 Claude。

4. **Claude 利用工具結果制定回應：**（API 回應）
    * 收到工具結果後，Claude 將利用這些資訊對原始使用者提示制定最終回應。

我們將從一個只需要與 Claude「對話」一次的簡單示範開始（別擔心，後面會有更精彩的範例！）。這意味著我們暫時不需要處理步驟 4。我們會向 Claude 提問，Claude 將請求使用工具來回答，然後我們擷取工具輸入、執行程式碼並回傳結果。

當今的大型語言模型在數學運算方面表現欠佳，以下程式碼可以說明這一點。

我們請 Claude 計算「1984135 乘以 9343116」：

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

# A relatively simple math problem
response = client.messages.create(
    model="claude-3-haiku-20240307",
    messages=[{"role": "user", "content":"Multiply 1984135 by 9343116. Only respond with the result"}],
    max_tokens=400
)
print(response.content[0].text)
```
```
18555375560
```

多次執行上述程式碼可能會得到不同的答案，但以下是 Claude 曾給出的一個回答：

```
18593367726060
```

實際正確答案是：

```
18538003464660
```
Claude 的偏差達到 `55364261400`！

## 工具使用來救援！

Claude 不擅長複雜的數學運算，所以讓我們透過提供計算機工具來增強 Claude 的能力。

以下是說明此流程的簡單圖示：

![chickens_calculator.png](images/chickens_calculator.png)

第一步是定義實際的計算機函數，並確認它能獨立正常運作，不依賴 Claude。我們將撰寫一個非常簡單的函數，接受三個引數：
* 一個運算符，例如「add」或「multiply」
* 兩個運算元

以下是一個基本實作：

```python
def calculator(operation, operand1, operand2):
    if operation == "add":
        return operand1 + operand2
    elif operation == "subtract":
        return operand1 - operand2
    elif operation == "multiply":
        return operand1 * operand2
    elif operation == "divide":
        if operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return operand1 / operand2
    else:
        raise ValueError(f"Unsupported operation: {operation}")
```

請注意，這個簡單的函數實用性相當有限，因為它只能處理像 `234 + 213` 或 `3 * 9` 這樣的簡單運算式。這裡的重點是透過一個非常簡單的教學範例來走過工具使用的流程。

讓我們測試這個函數，確保它能正常運作。

```python
calculator("add", 10, 3)
```
```
13
```

```python
calculator("divide", 200, 25)
```
```
8.0
```

下一步是定義我們的工具並告知 Claude。在定義工具時，我們遵循一個非常特定的格式。每個工具定義包含：

* `name`：工具的名稱，必須符合正規表示式 ^[a-zA-Z0-9_-]{1,64}$。
* `description`：對工具功能、使用時機和行為方式的詳細純文字說明。
* `input_schema`：一個 JSON Schema 物件，定義工具的預期參數。

不熟悉 JSON Schema？[點此了解更多](https://json-schema.org/learn/getting-started-step-by-step)。

以下是一個假設性工具的簡單範例：

```json
{
  "name": "send_email",
  "description": "Sends an email to the specified recipient with the given subject and body.",
  "input_schema": {
    "type": "object",
    "properties": {
      "to": {
        "type": "string",
        "description": "The email address of the recipient"
      },
      "subject": {
        "type": "string",
        "description": "The subject line of the email"
      },
      "body": {
        "type": "string",
        "description": "The content of the email message"
      }
    },
    "required": ["to", "subject", "body"]
  }
}
```

這個名為 `send_email` 的工具預期以下輸入：
* `to`：字串型別，必填
* `subject`：字串型別，必填
* `body`：字串型別，必填


以下是另一個名為 `search_product` 的工具定義範例：

```json
{
  "name": "search_product",
  "description": "Search for a product by name or keyword and return its current price and availability.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The product name or search keyword, e.g. 'iPhone 13 Pro' or 'wireless headphones'"
      },
      "category": {
        "type": "string",
        "enum": ["electronics", "clothing", "home", "toys", "sports"],
        "description": "The product category to narrow down the search results"
      },
      "max_price": {
        "type": "number",
        "description": "The maximum price of the product, used to filter the search results"
      }
    },
    "required": ["query"]
  }
}
```
這個工具有 3 個輸入：
* 必填的 `query` 字串，代表產品名稱或搜尋關鍵字
* 可選的 `category` 字串，必須是預定義值之一以縮小搜尋範圍。注意定義中的 `"enum"`。
* 可選的 `max_price` 數字，用於篩選低於特定價格的結果

### 我們的計算機工具定義
讓我們為先前撰寫的計算機函數定義對應的工具。我們知道計算機函數有 3 個必填引數：
* `operation`——只能是 "add"、"subtract"、"multiply" 或 "divide"
* `operand1`——應為數字
* `operand2`——也應為數字

以下是工具定義：

```python
calculator_tool = {
    "name": "calculator",
    "description": "A simple calculator that performs basic arithmetic operations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"],
                "description": "The arithmetic operation to perform."
            },
            "operand1": {
                "type": "number",
                "description": "The first operand."
            },
            "operand2": {
                "type": "number",
                "description": "The second operand."
            }
        },
        "required": ["operation", "operand1", "operand2"]
    }
}
```

***

## 練習

讓我們練習撰寫格式正確的工具定義，以下列函數為範例：

```python
def inventory_lookup(product_name, max_results):
    return "this function doesn't do anything"
    #You do not need to touch this or do anything with it!
```

這個假設性的 `inventory_lookup` 函數應該像這樣呼叫：

```python
inventory_lookup("AA batteries", 4)

inventory_lookup("birthday candle", 10)
```

你的任務是撰寫對應的、格式正確的工具定義。假設在你的工具定義中兩個引數都是必填的。

***

### 向 Claude 提供我們的工具
現在回到我們先前的計算機函數。此時 Claude 對計算機工具一無所知！它只是一個 Python 字典。在向 Claude 發出請求時，我們可以傳遞一個工具清單，讓 Claude「得知」這些工具的存在。讓我們現在試試：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    messages=[{"role": "user", "content": "Multiply 1984135 by 9343116. Only respond with the result"}],
    max_tokens=300,
    # Tell Claude about our tool
    tools=[calculator_tool]
)
```

接下來，讓我們看看 Claude 回傳給我們的回應：

```python
response
```
```
ToolsBetaMessage(id='msg_01UfKwdmEsgTh99wfpgW4NJ7', content=[ToolUseBlock(id='toolu_015wQ7Wipo589yT9B3YTwjF1', input={'operand1': 1984135, 'operand2': 9343116, 'operation': 'multiply'}, name='calculator', type='tool_use')], model='claude-3-haiku-20240307', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=420, output_tokens=93))
```

```
ToolsBetaMessage(id='msg_01UfKwdmEsgTh99wfpgW4NJ7', content=[ToolUseBlock(id='toolu_015wQ7Wipo589yT9B3YTwjF1', input={'operand1': 1984135, 'operand2': 9343116, 'operation': 'multiply'}, name='calculator', type='tool_use')], model='claude-3-haiku-20240307', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=420, output_tokens=93))
```

你可能注意到我們的回應看起來與平常有些不同！具體而言，我們現在得到的不是普通的 `Message`，而是 `ToolsMessage`。

此外，我們可以檢查 `response.stop_reason`，可以看到 Claude 停止是因為它決定要使用工具：


```python
response.stop_reason
```
```
'tool_use'
```

`response.content` 包含一個含有 `ToolUseBlock` 的清單，其中包含工具名稱和輸入的相關資訊：

```python
response.content
```
```
[ToolUseBlock(id='toolu_015wQ7Wipo589yT9B3YTwjF1', input={'operand1': 1984135, 'operand2': 9343116, 'operation': 'multiply'}, name='calculator', type='tool_use')]
```

```python
tool_name = response.content[0].name
tool_inputs = response.content[0].input

print("The Tool Name Claude Wants To Call:", tool_name)
print("The Inputs Claude Wants To Call It With:", tool_inputs)
```
```
The Tool Name Claude Wants To Call: calculator
The Inputs Claude Wants To Call It With: {'operand1': 1984135, 'operand2': 9343116, 'operation': 'multiply'}
```

下一步是直接取用 Claude 提供的工具名稱和輸入，並用它們實際呼叫我們先前撰寫的計算機函數。這樣我們就能得到最終答案了！

```python
operation = tool_inputs["operation"]
operand1 = tool_inputs["operand1"]
operand2 = tool_inputs["operand2"]

result = calculator(operation, operand1, operand2)
print("RESULT IS", result)
```
```
RESULT IS 18538003464660
```

我們得到了正確答案 `18538003464660`！！！我們不依賴 Claude 來確保數學正確，而是向 Claude 提問並給予它可以在必要時決定使用的工具。

#### 重要說明
如果我們問 Claude 不需要使用工具的問題——例如與數學或計算完全無關的問題——我們可能希望它正常回應。Claude 通常會這樣做，但有時 Claude 會非常急於使用它的工具！

以下是一個 Claude 有時嘗試使用計算機的例子，即使這樣做毫無意義。讓我們看看當我們問 Claude「祖母綠是什麼顏色？」時會發生什麼：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    messages=[{"role": "user", "content":"What color are emeralds?"}],
    max_tokens=400,
    tools=[calculator_tool]
)
```

```python
response
```
```
ToolsBetaMessage(id='msg_01Dj82HdyrxGJpi8XVtqEYvs', content=[ToolUseBlock(id='toolu_01Xo7x3dV1FVoBSGntHNAX4Q', input={'operand1': 0, 'operand2': 0, 'operation': 'add'}, name='calculator', type='tool_use')], model='claude-3-haiku-20240307', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=409, output_tokens=89))
```

Claude 給出了這個回應：

```
ToolsBetaMessage(id='msg_01Dj82HdyrxGJpi8XVtqEYvs', content=[ToolUseBlock(id='toolu_01Xo7x3dV1FVoBSGntHNAX4Q', input={'operand1': 0, 'operand2': 0, 'operation': 'add'}, name='calculator', type='tool_use')], model='claude-3-haiku-20240307', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=409, output_tokens=89))

```
Claude 要我們呼叫計算機工具？一個非常簡單的解決方法是調整我們的提示，或加入一個系統提示，說明類似：`You have access to tools, but only use them when necessary. If a tool is not required, respond as normal`：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    system="You have access to tools, but only use them when necessary.  If a tool is not required, respond as normal",
    messages=[{"role": "user", "content":"What color are emeralds?"}],
    max_tokens=400,
    tools=[calculator_tool]
)
```

```python
response
```
```
ToolsBetaMessage(id='msg_01YRRfnUUhP1u5ojr9iWZGGu', content=[TextBlock(text='Emeralds are green in color.', type='text')], model='claude-3-haiku-20240307', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=434, output_tokens=12))
```

現在 Claude 回應了適當的內容，不再嘗試在不合理的情況下強行使用工具。以下是我們得到的新回應：

```
'Emeralds are green in color.'
```

我們也可以看到 `stop_reason` 現在是 `end_turn` 而不是 `tool_use`。

```python
response.stop_reason
```
```
'end_turn'
```

***

### 整合所有內容

```python
def calculator(operation, operand1, operand2):
    if operation == "add":
        return operand1 + operand2
    elif operation == "subtract":
        return operand1 - operand2
    elif operation == "multiply":
        return operand1 * operand2
    elif operation == "divide":
        if operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return operand1 / operand2
    else:
        raise ValueError(f"Unsupported operation: {operation}")


calculator_tool = {
    "name": "calculator",
    "description": "A simple calculator that performs basic arithmetic operations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"],
                "description": "The arithmetic operation to perform.",
            },
            "operand1": {"type": "number", "description": "The first operand."},
            "operand2": {"type": "number", "description": "The second operand."},
        },
        "required": ["operation", "operand1", "operand2"],
    },
}


def prompt_claude(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        system="You have access to tools, but only use them when necessary. If a tool is not required, respond as normal",
        messages=messages,
        max_tokens=500,
        tools=[calculator_tool],
    )

    if response.stop_reason == "tool_use":
        tool_use = response.content[-1]
        tool_name = tool_use.name
        tool_input = tool_use.input

        if tool_name == "calculator":
            print("Claude wants to use the calculator tool")
            operation = tool_input["operation"]
            operand1 = tool_input["operand1"]
            operand2 = tool_input["operand2"]

            try:
                result = calculator(operation, operand1, operand2)
                print("Calculation result is:", result)
            except ValueError as e:
                print(f"Error: {str(e)}")

    elif response.stop_reason == "end_turn":
        print("Claude didn't want to use a tool")
        print("Claude responded with:")
        print(response.content[0].text)

```

```python
prompt_claude("I had 23 chickens but 2 flew away.  How many are left?")
```
```
Claude want to use the calculator tool
Calculation result is:  21
```

```python
prompt_claude("What is 201 times 2")
```
```
Claude want to use the calculator tool
Calculation result is:  402
```

```python
prompt_claude("Write me a haiku about the ocean")
```
```
Claude didn't want to use a tool
Claude responded with: 
Here is a haiku about the ocean:

Vast blue expanse shines,
Waves crash upon sandy shores,
Ocean's soothing song.
```

*** 

## 練習

你的任務是協助使用 Claude 建置一個研究助理。使用者可以輸入他們想研究的主題，並取得一份 Wikipedia 文章連結清單，儲存到 markdown 檔案供日後閱讀。我們可以嘗試直接要求 Claude 生成文章網址清單，但 Claude 對 URL 的可靠性不高，可能會產生幻覺式的文章網址。此外，合法的文章可能在 Claude 的訓練截止日期後移至新的 URL。因此，我們將改用一個連接到真實 Wikipedia API 的工具來完成這項工作！

我們將提供 Claude 存取一個工具，該工具接受 Claude 生成但可能有誤的 Wikipedia 文章標題清單。我們可以使用此工具搜尋 Wikipedia，以找到實際的文章標題和 URL，確保最終清單中的文章全部真實存在。然後我們將這些文章 URL 儲存到 markdown 檔案供日後閱讀。

我們提供了兩個輔助函數：


```python
import wikipedia
def generate_wikipedia_reading_list(research_topic, article_titles):
    wikipedia_articles = []
    for t in article_titles:
        results = wikipedia.search(t)
        try:
            page = wikipedia.page(results[0])
            title = page.title
            url = page.url
            wikipedia_articles.append({"title": title, "url": url})
        except:
            continue
    add_to_research_reading_file(wikipedia_articles, research_topic)

def add_to_research_reading_file(articles, topic):
    with open("output/research_reading.md", "a", encoding="utf-8") as file:
        file.write(f"## {topic} \n")
        for article in articles:
            title = article["title"]
            url = article["url"]
            file.write(f"* [{title}]({url}) \n")
        file.write(f"\n\n")
```

第一個函數 `generate_wikipedia_reading_list` 預期接受一個研究主題（例如「夏威夷的歷史」或「世界各地的海盜」）以及一個潛在的 Wikipedia 文章名稱清單（由 Claude 生成）。該函數使用 `wikipedia` 套件搜尋對應的真實 Wikipedia 頁面，並建立包含文章標題和 URL 的字典清單。

然後它呼叫 `add_to_research_reading_file`，傳入 Wikipedia 文章資料清單和整體研究主題。這個函數只是將每篇 Wikipedia 文章的 markdown 連結加入名為 `output/research_reading.md` 的檔案中。檔案名稱目前為硬式編碼，且函數假設該檔案已存在。此 repo 中已存在該檔案，但若在其他地方運作則需要自行建立。

核心想法是讓 Claude「呼叫」`generate_wikipedia_reading_list`，並傳入一個可能正確也可能不正確的文章標題清單。Claude 可能傳入如下的輸入文章標題清單，其中有些是真實的 Wikipedia 文章，有些則不是：

```py
["Piracy", "Famous Pirate Ships", "Golden Age Of Piracy", "List of Pirates", "Pirates and Parrots", "Piracy in the 21st Century"]
```

`generate_wikipedia_reading_list` 函數逐一處理這些文章標題，收集真正存在的 Wikipedia 文章的標題和 URL，然後呼叫 `add_to_research_reading_file` 將內容寫入 markdown 檔案供日後參考。

### 最終目標

你的任務是實作一個名為 `get_research_help` 的函數，接受研究主題和期望的文章數量。此函數應使用 Claude 實際生成可能的 Wikipedia 文章清單，並呼叫上方提供的 `generate_wikipedia_reading_list` 函數。以下是幾個呼叫範例：

```py
get_research_help("Pirates Across The World", 7)

get_research_help("History of Hawaii", 3)

get_research_help("are animals conscious?", 3)
```

完成這 3 次函數呼叫後，我們的輸出 `research_reading.md` 檔案內容如下（可在 output/research_reading.md 中自行查看）：

![research_reading.png](images/research_reading.png)



為了完成這項任務，你需要：

* 為 `generate_wikipedia_reading_list` 函數撰寫工具定義
* 實作 `get_research_help` 函數
    * 撰寫一個提示告訴 Claude 你需要協助收集特定主題的研究資料，以及你希望它生成多少篇文章標題
    * 告訴 Claude 它能存取的工具
    * 向 Claude 發送你的請求
    * 檢查 Claude 是否呼叫了工具。如果有，你需要將它生成的文章標題和主題傳遞給我們提供的 `generate_wikipedia_reading_list` 函數。該函數將收集實際的 Wikipedia 文章連結，然後呼叫 `add_to_research_reading_file` 將連結寫入 `output/research_reading.md`
    * 開啟 `output/research_reading.md` 確認是否成功！


##### 起始程式碼

```python
# Here's your starter code!
import wikipedia
def generate_wikipedia_reading_list(research_topic, article_titles):
    wikipedia_articles = []
    for t in article_titles:
        results = wikipedia.search(t)
        try:
            page = wikipedia.page(results[0])
            title = page.title
            url = page.url
            wikipedia_articles.append({"title": title, "url": url})
        except:
            continue
    add_to_research_reading_file(wikipedia_articles, research_topic)

def add_to_research_reading_file(articles, topic):
    with open("output/research_reading.md", "a", encoding="utf-8") as file:
        file.write(f"## {topic} \n")
        for article in articles:
            title = article["title"]
            url = article["url"]
            file.write(f"* [{title}]({url}) \n")
        file.write(f"\n\n")
        
def get_research_help(topic, num_articles=3):
   #Implement this function! 
   pass
```
