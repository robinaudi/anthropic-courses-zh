# 模型參數

## 課程目標
* 理解 `max_tokens` 參數的作用
* 使用 `temperature` 參數控制模型回應
* 說明 `stop_sequence` 的用途

跟往常一樣，我們先匯入 `anthropic` SDK 並載入 API 金鑰：

```python
from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()
```

## Max tokens（最大 token 數）

每次向 Claude 發出請求時，必須包含以下 3 個必要參數：

* `model`
* `max_tokens`
* `messages`

到目前為止，我們每次請求都使用了 `max_tokens` 參數，但尚未停下來討論它的用途。

以下是我們最初發出的第一個請求：

```py
our_first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Hi there! Please write me a haiku about a pet chicken"}
    ]
)
```

那麼 `max_tokens` 的用途是什麼？

### Token（詞元）
簡單來說，`max_tokens` 控制 Claude 在回應中最多可以生成多少個 token。在繼續之前，讓我們先停下來討論什麼是 token。

大多數大型語言模型並非以完整的單詞進行「思考」，而是使用一連串稱為 token 的詞片段。Token 是文字序列的基本構成單位，Claude 用它來處理、理解並生成文字。當我們向 Claude 提供提示時，該提示會先被轉換成 token 並傳給模型。模型接著**每次生成一個 token** 來輸出回應。

對於 Claude，一個 token 大約對應 3.5 個英文字元，但確切數量可能因使用的語言而異。

### 使用 `max_tokens`

`max_tokens` 參數讓我們能設定 Claude 生成 token 數量的上限。舉例來說，假設我們要求 Claude 寫一首詩，並將 `max_tokens` 設定為 10，Claude 會開始生成 token，一達到 10 個就立即停止，這通常會導致輸出被截斷或不完整。我們來試試看！

```python
truncated_response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=10,
    messages=[
        {"role": "user", "content": "Write me a poem"}
    ]
)
print(truncated_response.content[0].text)
```

```
Here is a poem for you:

The
```

以下是我們從 Claude 收到的回應：

>Here is a poem for you:
>
>The

如果你執行上述程式碼，可能會得到略有不同但同樣被截斷的結果。Claude 開始寫詩，但在生成 10 個 token 後立即停止。

我們也可以查看回應 Message 物件上的 `stop_reason` 屬性，了解模型停止生成的原因。在此例中，可以看到其值為 "max_tokens"，表示模型因達到最大 token 限制而停止生成。

```python
truncated_response.stop_reason
```

```
'max_tokens'
```

當然，如果我們用較大的 `max_tokens` 值再次生成詩歌，通常就能得到完整的詩：

```python
longer_poem_response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": "Write me a poem"}
    ]
)
print(longer_poem_response.content[0].text)
```

```
Here is a poem for you:

Whispers of the Heart

In the quiet moments,
When the world fades away,
I hear the whispers of my heart -
Gentle words that gently sway.

They speak of dreams still unfurled,
Of love that shines like the sun,
Of passions yet to be explored,
Of all that's yet to be done.

These whispers, they guide my way,
Reminding me to pause and feel,
To listen closely to the soul,
And let its truths be revealed.

For in the silence, in the calm,
The heart's true voice can be heard,
Weaving a tapestry of hope,
With every softly spoken word.

So I will heed these whispers dear,
And let them be my faithful friend,
For in their song, I find my way,
To all my heart hopes to transcend.
```

以下是 Claude 在 `max_tokens` 設定為 500 時所生成的內容：

```
Here is a poem for you:

Whispers of the Wind

The wind whispers softly,
Caressing my face with care.
Its gentle touch, a fleeting breath,
Carries thoughts beyond compare.

Rustling leaves dance in rhythm,
Swaying to the breeze's song.
Enchanting melodies of nature,
Peaceful moments linger long.

The wind's embrace, a soothing balm,
Calms the restless soul within.
Embracing life's fleeting moments,
As the wind's sweet song begins.
```



如果我們查看這個回應的 `stop_reason`，會看到值為 "end_turn"，這表示模型自然地生成完畢。它寫完了詩，沒有更多內容要說，因此就停止了！

```python
longer_poem_response.stop_reason
```

```
'end_turn'
```

需要注意的是，模型在生成內容時並不「知道」`max_tokens` 的存在。調整 `max_tokens` 不會改變 Claude 生成輸出的方式，它只是給模型提供更多空間繼續生成（`max_tokens` 值較高時），或是截斷輸出（`max_tokens` 值較低時）。

同樣重要的是，增加 `max_tokens` 並不能確保 Claude 真的會生成那麼多 token。如果我們要求 Claude 講一個笑話並將 `max_tokens` 設定為 1000，回應幾乎肯定會遠少於 1000 個 token。

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[{"role": "user", "content": "Tell me a joke"}]
)
```

```python
print(response.content[0].text)
```

```
Here's a classic dad joke for you:

Why don't scientists trust atoms? Because they make up everything!

How was that? I tried to keep it clean and mildly amusing. Let me know if you'd like to hear another joke.
```

```python
print(response.usage.output_tokens)
```

```
55
```

在上面的範例中，我們要求 Claude「Tell me a joke」並給予 `max_tokens` 值 1000。它生成了這個笑話：

```
Here's a classic dad joke for you:

Why don't scientists trust atoms? Because they make up everything!

How was that? I tried to keep it clean and mildly amusing. Let me know if you'd like to hear another joke.
```

這段生成的內容只有 55 個 token。我們給了 Claude 1000 個 token 的上限，但這並不意味著它會生成 1000 個 token。

### 為什麼要調整 max tokens？
理解 token 在使用 Claude 時至關重要，尤其在以下幾個方面：

* **API 限制**：輸入文字和生成回應的 token 數量都計入 API 用量限制。每個 API 請求都有可處理 token 數的最大上限。了解 token 有助於你在 API 限制範圍內運作並有效管理用量。
* **效能**：Claude 生成的 token 數量直接影響 API 的處理時間和記憶體用量。更長的輸入文字和更高的 max_tokens 值需要更多運算資源。理解 token 有助於你優化 API 請求以提升效能。
* **回應品質**：設定適當的 max_tokens 值可確保生成的回應有足夠的長度並包含必要的資訊。若 max_tokens 值過低，回應可能被截斷或不完整。嘗試不同的 max_tokens 值可以幫助你找到適合特定使用情境的最佳平衡點。

讓我們看看 Claude 生成的 token 數量如何影響效能。下方函式要求 Claude 三次生成一段非常長的兩個角色之間的對話，每次使用不同的 `max_tokens` 值，並列印實際生成的 token 數量和生成所需的時間。

```python
import time
def compare_num_tokens_speed():
    token_counts = [100,1000,4096]
    task = """
        Create a long, detailed dialogue that is at least 5000 words long between two characters discussing the impact of social media on mental health. 
        The characters should have differing opinions and engage in a respectful thorough debate.
    """

    for num_tokens in token_counts:
        start_time = time.time()

        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=num_tokens,
            messages=[{"role": "user", "content": task}]
        )

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Number of tokens generated: {response.usage.output_tokens}")
        print(f"Execution Time: {execution_time:.2f} seconds\n")
```

```python
compare_num_tokens_speed()
```

```
Number of tokens generated: 100
Execution Time: 1.51 seconds

Number of tokens generated: 1000
Execution Time: 8.33 seconds

Number of tokens generated: 3433
Execution Time: 28.80 seconds
```

如果你執行此程式碼，實際得到的數值可能有所不同，以下是一個範例輸出：

```
Number of tokens generated: 100
Execution Time: 1.51 seconds

Number of tokens generated: 1000
Execution Time: 8.33 seconds

Number of tokens generated: 3433
Execution Time: 28.80 seconds
```

如你所見，**Claude 生成的 token 越多，耗時越長！**

為了讓這個現象更加明顯，我們要求 Claude 重複一段非常長的文字，並使用 `max_tokens` 在不同輸出大小時截斷生成。每個大小重複 50 次並計算平均生成時間。如你所見，輸出大小增加，所需時間也隨之增加！請看以下圖表：

![output_length.png](images/output_length.png)

## Stop sequences（停止序列）

另一個我們尚未見過的重要參數是 `stop_sequence`，它允許我們為模型提供一組字串，當這些字串出現在生成的回應中時，就會停止生成。它們本質上是告訴 Claude：「如果你生成了這個序列，就停止生成其他所有內容！」

以下是一個不包含 `stop_sequence` 的請求範例：

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[{"role": "user", "content": "Generate a JSON object representing a person with a name, email, and phone number ."}],
)
print(response.content[0].text)
```

```
Here's an example of a JSON object representing a person with a name, email, and phone number:

```json
{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "phoneNumber": "123-456-7890"
}
```

In this example, the JSON object has three key-value pairs:

1. "name": The person's name, which is a string value of "John Doe".
2. "email": The person's email address, which is a string value of "johndoe@example.com".
3. "phoneNumber": The person's phone number, which is a string value of "123-456-7890".

You can modify the values to represent a different person with their own name, email, and phone number.
```

上述程式碼要求 Claude 生成一個代表人員的 JSON 物件。以下是 Claude 生成的範例輸出：

```
Here's an example of a JSON object representing a person with a name, email, and phone number:

{
  "name": "John Doe",
  "email": "johndoe@example.com",
  "phoneNumber": "123-456-7890"
}


In this example, the JSON object has three key-value pairs:

1. "name": The person's name, which is a string value of "John Doe".
2. "email": The person's email address, which is a string value of "johndoe@example.com".
3. "phoneNumber": The person's phone number, which is a string value of "123-456-7890".

You can modify the values to represent a different person with their own name, email, and phone number.
```

Claude 確實生成了所請求的物件，但之後還附上了說明。如果我們希望 Claude 在生成 JSON 物件的結尾 "}" 後就立即停止，可以修改程式碼，加入 `stop_sequences` 參數。

```python
response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[{"role": "user", "content": "Generate a JSON object representing a person with a name, email, and phone number ."}],
    stop_sequences=["}"]
)
print(response.content[0].text)
```

```
Here's a JSON object representing a person with a name, email, and phone number:

{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "555-1234"
```

模型生成了以下輸出：

```
Here's a JSON object representing a person with a name, email, and phone number:
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "555-1234"

```
**重要提醒：** 注意結果輸出**不**包含 "}" 停止序列本身。如果我們想要以 JSON 格式使用和解析這個結果，需要手動補回結尾的 "}"。

當我們從 Claude 收到回應時，可以查看 `stop_reason` 屬性來確認模型停止生成文字的原因。如下所示，前一個回應因 'stop_sequence' 而停止，表示模型生成了我們提供的其中一個停止序列並立即停止。

```python
response.stop_reason
```

```
'stop_sequence'
```

我們也可以查看回應上的 `stop_sequence` 屬性，確認是哪個特定的 stop_sequence 導致模型停止生成：

```python
response.stop_sequence
```

```
'}'
```

我們可以提供多個停止序列。若提供多個，模型一遇到任何停止序列就會停止生成。回應 Message 上的 `stop_sequence` 屬性會告訴我們確切遇到了哪個 `stop_sequence`。

下方函式要求 Claude 寫一首詩，並在生成字母 "b" 或 "c" 時停止，執行三次：

```python
def generate_random_letters_3_times():
    for i in range(3):
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[{"role": "user", "content": "generate a poem"}],
            stop_sequences=["b", "c"]
        )
        print(f"Response {i+1} stopped because {response.stop_reason}.  The stop sequence was {response.stop_sequence}")
```

```python
generate_random_letters_3_times()
```

```
Response 1 stopped because stop_sequence.  The stop sequence was c
Response 2 stopped because stop_sequence.  The stop sequence was b
Response 3 stopped because stop_sequence.  The stop sequence was b
```

以下是範例輸出：

```
Response 1 stopped because stop_sequence.  The stop sequence was c
Response 2 stopped because stop_sequence.  The stop sequence was b
Response 3 stopped because stop_sequence.  The stop sequence was b
```

第一次，Claude 因為生成了字母 "c" 而停止寫詩；後兩次則因為生成了字母 "b" 而停止。你會這樣做嗎？大概不會！

## Temperature（溫度）

`temperature` 參數用來控制生成回應的「隨機性」和「創造性」。範圍從 0 到 1，較高的值會產生更多樣且不可預測的回應，措辭也會有更多變化；較低的溫度則會產生更具確定性的輸出，傾向於採用最可能的措辭和答案。**Temperature 的預設值為 1**。

在生成文字時，Claude 會預測下一個 token（單詞或子詞）的概率分布。Temperature 參數用來在採樣下一個 token 之前操控這個概率分布。若溫度較低（接近 0.0），概率分布會更加集中，最可能的 token 會獲得更高的概率。這使模型更具確定性，傾向於選擇最可能或「最安全」的選項。若溫度較高（接近 1.0），概率分布會趨於平坦，較不可能的 token 的概率也會提高。這使模型更加隨機和探索性，允許產生更多樣且富有創意的輸出。

請參考以下圖表，直觀了解溫度的影響：

![temperature.png](images/temperature.png)


為什麼要調整溫度？

**分析型任務使用接近 0.0 的溫度，創意生成型任務使用接近 1.0 的溫度。**



讓我們來做個簡單演示。請看下方函式：分別使用溫度 0 和溫度 1，向 Claude 發出三次請求，要求它「想一個外星星球的名稱，只回覆一個單詞。」

```python
def demonstrate_temperature():
    temperatures = [0, 1]
    for temperature in temperatures:
        print(f"Prompting Claude three times with temperature of {temperature}")
        print("================")
        for i in range(3):
            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=100,
                messages=[{"role": "user", "content": "Come up with a name for an alien planet. Respond with a single word."}],
                temperature=temperature
            )
            print(f"Response {i+1}: {response.content[0].text}")
        
```

```python
demonstrate_temperature()
```

```
Prompting Claude three times with temperature of 0
================
Response 1: Xendor.
Response 2: Xendor.
Response 3: Xendor.
Prompting Claude three times with temperature of 1
================
Response 1: Xyron.
Response 2: Xandar.
Response 3: Zyrcon.
```

以下是執行上述函式的結果（你的具體結果可能有所不同）：

```
Prompting Claude three times with temperature of 0
================
Response 1: Xendor.
Response 2: Xendor.
Response 3: Xendor.
Prompting Claude three times with temperature of 1
================
Response 1: Xyron.
Response 2: Xandar.
Response 3: Zyrcon.
```

請注意，溫度為 0 時，三次回應完全相同。需要說明的是，即使溫度為 0.0，結果也不會完全具有確定性。然而，與溫度為 1 的結果相比，差異非常明顯——每次回應都是完全不同的外星星球名稱。

以下圖表說明了溫度對 Claude 輸出的影響。使用提示「在世界上任意選一種動物，只回覆一個單詞：動物名稱」，以溫度 0 查詢 Claude 100 次，再以溫度 1 查詢 100 次，圖表顯示了 Claude 給出各種動物回應的頻率分布。

![temperature_plot.png](images/temperature_plot.png)

如你所見，溫度為 0 時，Claude 每次都回答了「Giraffe（長頸鹿）」。請記住，溫度為 0 並不能保證完全確定性的結果，但確實使 Claude 每次回應相似內容的概率大幅提高。溫度為 1 時，Claude 選擇長頸鹿的次數仍超過一半，但回應中也包含許多其他類型的動物！

## System prompt（系統提示）

`system_prompt` 是一個可選參數，可在向 Claude 發送訊息時包含。它透過提供高層次指示、定義角色或提供應影響其回應的背景資訊，為對話設定基調。

關於 system_prompt 的重要說明：

* 它是可選的，但對於設定對話的語調和情境很有幫助。
* 它在對話層級生效，影響 Claude 在該對話中的所有回應。
* 它有助於引導 Claude 的行為，而無需在每條使用者訊息中都包含指示。

請注意，在大多數情況下，系統提示中只應包含語調、情境和角色內容。詳細指示、外部輸入內容（如文件）和範例，為了獲得更好的效果，應放在第一個 `User` 輪次中。後續的 `User` 輪次不需要重複這些內容。

讓我們試試看：

```python
message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    system="You are a helpful foreign language tutor that always responds in French.",
    messages=[
        {"role": "user", "content": "Hey there, how are you?!"}
    ]
)

print(message.content[0].text)
```

```
Bonjour ! Je suis ravi de vous rencontrer. Comment allez-vous aujourd'hui ?
```

***

## 練習

撰寫一個名為 `generate_questions` 的函式，完成以下功能：
* 接受兩個參數：`topic`（主題）和 `num_questions`（問題數量）
* 針對提供的 `topic` 生成 `num_questions` 個發人深省的問題，以編號清單形式呈現
* 列印生成的問題

例如，呼叫 `generate_questions(topic="free will", num_questions=3)` 可能產生以下輸出：


> 1. To what extent do our decisions and actions truly originate from our own free will, rather than being shaped by factors beyond our control, such as our genes, upbringing, and societal influences?
> 2. If our decisions are ultimately the result of a complex interplay of biological, psychological, and environmental factors, does that mean we lack the ability to make authentic, autonomous choices, or is free will compatible with determinism?
> 3. What are the ethical and philosophical implications of embracing or rejecting the concept of free will? How might our views on free will impact our notions of moral responsibility, punishment, and the nature of the human condition?


在你的實作中，請善用以下參數：
* `max_tokens`：將回應限制在 1000 個 token 以內
* `system`：提供系統提示，告訴模型它是特定 `topic` 的專家，並應生成編號清單
* `stop_sequences`：確保模型在生成正確數量的問題後停止。（若要求 3 個問題，確保模型在生成「4.」時停止；若要求 5 個問題，確保模型在生成「6.」時停止。）


#### 參考解答

```python
def generate_questions(topic, num_questions=3):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        system=f"You are an expert on {topic}. Generate thought-provoking questions about this topic.",
        messages=[
            {"role": "user", "content": f"Generate {num_questions} questions about {topic} as a numbered list."}
        ],
        stop_sequences=[f"{num_questions+1}."]
    )
    print(response.content[0].text)
```

```python
generate_questions(topic="free will", num_questions=3)
```

```
Here are three thought-provoking questions about free will:

1. To what extent do our decisions and actions truly originate from our own free will, rather than being shaped by factors beyond our control, such as our genes, upbringing, and societal influences?

2. If our decisions are ultimately the result of a complex interplay of biological, psychological, and environmental factors, does that mean we lack the ability to make authentic, autonomous choices, or is free will compatible with determinism?

3. What are the ethical and philosophical implications of embracing or rejecting the concept of free will? How might our views on free will impact our notions of moral responsibility, punishment, and the nature of the human condition?
```

***
