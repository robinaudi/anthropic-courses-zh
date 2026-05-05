# 使用工具強制輸出 JSON

## 學習目標

* 理解如何使用工具強制輸出結構化回應
* 善用此「技巧」生成結構化 JSON

工具使用更有趣的應用之一，是強制 Claude 以 JSON 等結構化內容回應。在許多情況下，我們可能希望從 Claude 獲得標準化的 JSON 回應：擷取實體、摘要資料、情感分析等。

其中一種方式是直接要求 Claude 以 JSON 回應，但這可能需要額外的工作來從 Claude 回傳的大段字串中實際擷取 JSON，或確保 JSON 符合我們想要的確切格式。

好消息是，**每當 Claude 想要使用工具時，它已經使用我們在定義工具時指定的完全結構化格式來回應。**

在上一堂課中，我們給了 Claude 一個計算機工具。當它想使用該工具時，它以如下內容回應：

```
{
    'operand1': 1984135, 
    'operand2': 9343116, 
    'operation': 'multiply'
}
```

這看起來非常像 JSON！

如果我們希望 Claude 生成結構化 JSON，我們可以善用這一點。我們所需要做的就是定義一個描述特定 JSON 結構的工具，然後告訴 Claude 關於它的資訊。就這樣。Claude 會回應，以為它在「呼叫工具」，但實際上我們真正在乎的是它給我們的結構化回應。

***

# 概念概覽

這與我們在上一堂課做的事有何不同？以下是上一堂課工作流程的圖示：

![chickens_calculator.png](images/chickens_calculator.png)

在上一堂課中，我們給了 Claude 存取工具的權限，Claude 想要呼叫它，然後我們實際呼叫了底層的工具函數。

在本堂課中，我們將「欺騙」Claude，告訴它有某個特定工具可用，但我們實際上不需要呼叫底層的工具函數。我們使用工具作為強制特定回應結構的一種方式，如下圖所示：

![structured_response.png](images/structured_response.png)

## 情感分析
讓我們從一個簡單的範例開始。假設我們希望 Claude 分析某段文字的情感，並以符合以下格式的 JSON 物件回應：

```
{
  "negative_score": 0.6,
  "neutral_score": 0.3,
  "positive_score": 0.1
}
```

我們所需要做的就是使用 JSON Schema 定義一個捕捉此形狀的工具。以下是一個可能的實作：

```python
tools = [
    {
        "name": "print_sentiment_scores",
        "description": "Prints the sentiment scores of a given text.",
        "input_schema": {
            "type": "object",
            "properties": {
                "positive_score": {"type": "number", "description": "The positive sentiment score, ranging from 0.0 to 1.0."},
                "negative_score": {"type": "number", "description": "The negative sentiment score, ranging from 0.0 to 1.0."},
                "neutral_score": {"type": "number", "description": "The neutral sentiment score, ranging from 0.0 to 1.0."}
            },
            "required": ["positive_score", "negative_score", "neutral_score"]
        }
    }
]
```

現在我們可以告訴 Claude 關於這個工具的資訊，並明確告訴 Claude 使用它，以確保它確實使用。我們應該得到一個告訴我們 Claude 想要使用工具的回應。工具使用回應應包含我們想要的確切格式的所有資料。

```python
from anthropic import Anthropic
from dotenv import load_dotenv
import json

load_dotenv()
client = Anthropic()

tweet = "I'm a HUGE hater of pickles.  I actually despise pickles.  They are garbage."

query = f"""
<text>
{tweet}
</text>

Only use the print_sentiment_scores tool.
"""

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=4096,
    tools=tools,
    messages=[{"role": "user", "content": query}]
)
```

```python
response
```
```
ToolsBetaMessage(id='msg_01BhF4TkK8vDM6z5m4FNGRnB', content=[TextBlock(text='Here is the sentiment analysis for the given text:', type='text'), ToolUseBlock(id='toolu_01Mt1an3KHEz5RduZRUUuTWz', input={'positive_score': 0.0, 'negative_score': 0.791, 'neutral_score': 0.209}, name='print_sentiment_scores', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=374, output_tokens=112))
```

讓我們來看看 Claude 回傳給我們的回應。我們將重要部分加粗：


>ToolsBetaMessage(id='msg_01BhF4TkK8vDM6z5m4FNGRnB', content=[TextBlock(text='Here is the sentiment analysis for the given text:', >type='text'), ToolUseBlock(id='toolu_01Mt1an3KHEz5RduZRUUuTWz', **input={'positive_score': 0.0, 'negative_score': 0.791, 'neutral_score': 0.209}**, name='print_sentiment_scores', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=374, output_tokens=112))

Claude「以為」它正在呼叫一個將使用此情感分析資料的工具，但實際上我們只是要擷取資料並將其轉換為 JSON：

```python
import json
json_sentiment = None
for content in response.content:
    if content.type == "tool_use" and content.name == "print_sentiment_scores":
        json_sentiment = content.input
        break

if json_sentiment:
    print("Sentiment Analysis (JSON):")
    print(json.dumps(json_sentiment, indent=2))
else:
    print("No sentiment analysis found in the response.")
```
```
Sentiment Analysis (JSON):
{
  "positive_score": 0.0,
  "negative_score": 0.791,
  "neutral_score": 0.209
}
```

成功了！現在讓我們將其轉換成一個可重複使用的函數，接受推文或文章，然後以 JSON 格式列印或回傳情感分析結果。

```python
def analyze_sentiment(content):

    query = f"""
    <text>
    {content}
    </text>

    Only use the print_sentiment_scores tool.
    """

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        tools=tools,
        messages=[{"role": "user", "content": query}]
    )

    json_sentiment = None
    for content in response.content:
        if content.type == "tool_use" and content.name == "print_sentiment_scores":
            json_sentiment = content.input
            break

    if json_sentiment:
        print("Sentiment Analysis (JSON):")
        print(json.dumps(json_sentiment, indent=2))
    else:
        print("No sentiment analysis found in the response.")

```

```python
analyze_sentiment("OMG I absolutely love taking bubble baths soooo much!!!!")
```
```
Sentiment Analysis (JSON):
{
  "positive_score": 0.8,
  "negative_score": 0.0,
  "neutral_score": 0.2
}
```

```python
analyze_sentiment("Honestly I have no opinion on taking baths")
```
```
Sentiment Analysis (JSON):
{
  "positive_score": 0.056,
  "negative_score": 0.065,
  "neutral_score": 0.879
}
```

***

## 使用 `tool_choice` 強制工具使用

目前我們是透過提示「強制」Claude 使用 `print_sentiment_scores` 工具。在我們的提示中，我們寫了 `Only use the print_sentiment_scores tool.`，這通常有效，但有更好的方法！我們實際上可以使用 `tool_choice` 參數強制 Claude 使用特定工具：

```python
tool_choice={"type": "tool", "name": "print_sentiment_scores"}
```

上述程式碼告訴 Claude 它必須透過呼叫 `print_sentiment_scores` 工具來回應。讓我們更新函數來使用它：

```python
def analyze_sentiment(content):

    query = f"""
    <text>
    {content}
    </text>

    Only use the print_sentiment_scores tool.
    """

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        tools=tools,
        tool_choice={"type": "tool", "name": "print_sentiment_scores"},
        messages=[{"role": "user", "content": query}]
    )

    json_sentiment = None
    for content in response.content:
        if content.type == "tool_use" and content.name == "print_sentiment_scores":
            json_sentiment = content.input
            break

    if json_sentiment:
        print("Sentiment Analysis (JSON):")
        print(json.dumps(json_sentiment, indent=2))
    else:
        print("No sentiment analysis found in the response.")
```

我們將在後續課程中更詳細地介紹 `tool_choice`。

***

## 實體擷取範例

讓我們使用相同的方法讓 Claude 生成格式良好的 JSON，其中包含從文字樣本中擷取的人物、組織和地點等實體：


```python
tools = [
    {
        "name": "print_entities",
        "description": "Prints extract named entities.",
        "input_schema": {
            "type": "object",
            "properties": {
                "entities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "The extracted entity name."},
                            "type": {"type": "string", "description": "The entity type (e.g., PERSON, ORGANIZATION, LOCATION)."},
                            "context": {"type": "string", "description": "The context in which the entity appears in the text."}
                        },
                        "required": ["name", "type", "context"]
                    }
                }
            },
            "required": ["entities"]
        }
    }
]

text = "John works at Google in New York. He met with Sarah, the CEO of Acme Inc., last week in San Francisco."

query = f"""
<document>
{text}
</document>

Use the print_entities tool.
"""

response = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=4096,
    tools=tools,
    messages=[{"role": "user", "content": query}]
)

json_entities = None
for content in response.content:
    if content.type == "tool_use" and content.name == "print_entities":
        json_entities = content.input
        break

if json_entities:
    print("Extracted Entities (JSON):")
    print(json.dumps(json_entities, indent=2))
else:
    print("No entities found in the response.")
```
```
Extracted Entities (JSON):
{
  "entities": [
    {
      "name": "John",
      "type": "PERSON",
      "context": "John works at Google in New York."
    },
    {
      "name": "Google",
      "type": "ORGANIZATION",
      "context": "John works at Google in New York."
    },
    {
      "name": "New York",
      "type": "LOCATION",
      "context": "John works at Google in New York."
    },
    {
      "name": "Sarah",
      "type": "PERSON",
      "context": "He met with Sarah, the CEO of Acme Inc., last week in San Francisco."
    },
    {
      "name": "Acme Inc.",
      "type": "ORGANIZATION",
      "context": "He met with Sarah, the CEO of Acme Inc., last week in San Francisco."
    },
    {
      "name": "San Francisco",
      "type": "LOCATION",
      "context": "He met with Sarah, the CEO of Acme Inc., last week in San Francisco."
    }
  ]
}
```

我們使用了與之前相同的「技巧」。我們告訴 Claude 它可以存取某個工具，藉此讓 Claude 以特定資料格式回應。然後我們擷取 Claude 回應的格式化資料，大功告成。

請記住，在這個使用場景中，明確告訴 Claude 我們希望它使用特定工具會有所幫助：


>Use the print_entities tool.


***

## Wikipedia 摘要範例（更複雜的資料）

讓我們嘗試一個稍微複雜的範例。我們將使用 Python `wikipedia` 套件取得完整的 Wikipedia 頁面文章，並傳遞給 Claude。我們將使用 Claude 生成包含以下內容的回應：

* 文章的主要主題
* 文章摘要
* 文章中提及的關鍵字和主題清單
* 文章的類別分類清單（娛樂、政治、商業等）以及分類分數（即主題屬於該類別的程度）

如果我們將 Walt Disney 的 Wikipedia 文章傳遞給 Claude，可能預期得到如下結果：

```
{
  "subject": "Walt Disney",
  "summary": "Walter Elias Disney was an American animator, film producer, and entrepreneur. He was a pioneer of the American animation industry and introduced several developments in the production of cartoons. He held the record for most Academy Awards earned and nominations by an individual. He was also involved in the development of Disneyland and other theme parks, as well as television programs.",
  "keywords": [
    "Walt Disney",
    "animation",
    "film producer",
    "entrepreneur",
    "Disneyland",
    "theme parks",
    "television"
  ],
  "categories": [
    {
      "name": "Entertainment",
      "score": 0.9
    },
    {
      "name": "Business",
      "score": 0.7
    },
    {
      "name": "Technology",
      "score": 0.6
    }
  ]
}
```

以下是一個函數實作範例，接受 Wikipedia 頁面主題，找到文章、下載內容、傳遞給 Claude，然後列印出結果的 JSON 資料。我們使用相同的策略，透過定義工具來「引導」Claude 回應的格式。

注意：如果你的機器上還沒有安裝 `wikipedia`，請先執行 `pip install wikipedia`！

```python
import wikipedia

#tool definition
tools = [
    {
        "name": "print_article_classification",
        "description": "Prints the classification results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "subject": {
                    "type": "string",
                    "description": "The overall subject of the article",
                },
                "summary": {
                    "type": "string",
                    "description": "A paragaph summary of the article"
                },
                "keywords": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "List of keywords and topics in the article"
                    }
                },
                "categories": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "The category name."},
                            "score": {"type": "number", "description": "The classification score for the category, ranging from 0.0 to 1.0."}
                        },
                        "required": ["name", "score"]
                    }
                }
            },
            "required": ["subject","summary", "keywords", "categories"]
        }
    }
]

#The function that generates the json for a given article subject
def generate_json_for_article(subject):
    page = wikipedia.page(subject, auto_suggest=True)
    query = f"""
    <document>
    {page.content}
    </document>

    Use the print_article_classification tool. Example categories are Politics, Sports, Technology, Entertainment, Business.
    """

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=4096,
        tools=tools,
        messages=[{"role": "user", "content": query}]
    )

    json_classification = None
    for content in response.content:
        if content.type == "tool_use" and content.name == "print_article_classification":
            json_classification = content.input
            break

    if json_classification:
        print("Text Classification (JSON):")
        print(json.dumps(json_classification, indent=2))
    else:
        print("No text classification found in the response.")
```

```python
generate_json_for_article("Jeff Goldblum")
```
```
Text Classification (JSON):
{
  "subject": "Jeff Goldblum",
  "summary": "Jeffrey Lynn Goldblum is an American actor and musician who has starred in some of the highest-grossing films, such as Jurassic Park and Independence Day. He has had a long and successful career in both film and television, with roles in a wide range of movies and TV shows. Goldblum is also an accomplished jazz musician and has released several albums with his band, The Mildred Snitzer Orchestra.",
  "keywords": [
    "actor",
    "musician",
    "Jurassic Park",
    "Independence Day",
    "film",
    "television",
    "jazz"
  ],
  "categories": [
    {
      "name": "Entertainment",
      "score": 0.9
    }
  ]
}
```

```python
generate_json_for_article("Octopus")
```
```
Text Classification (JSON):
{
  "subject": "Octopus",
  "summary": "This article provides a comprehensive overview of octopuses, including their anatomy, physiology, behavior, ecology, and evolutionary history. It covers topics such as their complex nervous systems, camouflage and color-changing abilities, intelligence, and relationships with humans.",
  "keywords": [
    "octopus",
    "cephalopod",
    "mollusc",
    "marine biology",
    "animal behavior",
    "evolution"
  ],
  "categories": [
    {
      "name": "Science",
      "score": 0.9
    },
    {
      "name": "Nature",
      "score": 0.8
    }
  ]
}
```

```python
generate_json_for_article("Herbert Hoover")
```
```
Text Classification (JSON):
{
  "subject": "Herbert Hoover",
  "summary": "The article provides a comprehensive biography of Herbert Hoover, the 31st President of the United States. It covers his early life, career as a mining engineer and humanitarian, his presidency during the Great Depression, and his post-presidency activities.",
  "keywords": [
    "Herbert Hoover",
    "Great Depression",
    "Republican Party",
    "U.S. President",
    "mining engineer",
    "Commission for Relief in Belgium",
    "U.S. Food Administration",
    "Secretary of Commerce",
    "Smoot–Hawley Tariff Act",
    "New Deal"
  ],
  "categories": [
    {
      "name": "Politics",
      "score": 0.9
    },
    {
      "name": "Business",
      "score": 0.7
    },
    {
      "name": "History",
      "score": 0.8
    }
  ]
}
```

***

## 練習

使用上述策略撰寫一個名為 `translate` 的函數，接受一個單字或片語，並生成結構化 JSON 輸出，包含原始英文短語以及西班牙文、法文、日文和阿拉伯文的翻譯版本。

以下是預期的運作方式範例：

如果我們呼叫：

```python
translate("how much does this cost")
```

我們預期得到如下輸出：

```json
{
  "english": "how much does this cost",
  "spanish": "¿cuánto cuesta esto?",
  "french": "combien ça coûte?",
  "japanese": "これはいくらですか",
  "arabic": "كم تكلفة هذا؟"
}
```

**注意：如果你想列印結果，以下這行程式碼可以幫助你格式化輸出：**

```python
print(json.dumps(translations_from_claude, ensure_ascii=False, indent=2))
```
