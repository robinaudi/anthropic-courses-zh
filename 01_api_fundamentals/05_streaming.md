# 串流（Streaming）

## 課程目標

* 理解串流的運作方式
* 處理串流事件

讓我們先匯入 `anthropic` SDK 並設定 client：

```python
from dotenv import load_dotenv
from anthropic import Anthropic

#load environment variable
load_dotenv()

#automatically looks for an "ANTHROPIC_API_KEY" environment variable
client = Anthropic()
```

到目前為止，我們使用以下語法向 Claude 發送訊息：


```python
response = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Write me an essay about macaws and clay licks in the Amazon",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=800,
    temperature=0,
)
print("We have a response back!")
print("========================")
print(response.content[0].text)
```

```
We have a response back!
========================
Here is an essay about macaws and clay licks in the Amazon:

Macaws and Clay Licks in the Amazon

Deep within the lush, verdant rainforests of the Amazon basin, a remarkable natural phenomenon takes place. Flashes of vibrant color dart through the canopy, as large, magnificent parrots known as macaws congregate at special sites called clay licks. These clay licks, or "collpas" as they are known locally, are essential to the survival and well-being of macaws and other Amazonian wildlife.

Macaws are some of the most striking and iconic birds of the Amazon. With their vividly-hued plumage, hooked beaks, and long, tapered tails, these large parrots are a sight to behold as they soar through the treetops. The most well-known species include the scarlet macaw, the blue-and-gold macaw, and the green-winged macaw, each adorned in a stunning array of reds, blues, greens, and golds. 

These magnificent birds play a crucial role in the Amazon ecosystem, acting as important seed dispersers as they feed on a variety of fruits and nuts. However, macaws face a unique dietary challenge - they require essential minerals and nutrients that are often lacking in the fruits and seeds that make up their primary diet. This is where the clay licks come into play.

Clay licks are exposed deposits of mineral-rich clay that attract hundreds, sometimes thousands, of macaws and other parrots, as well as other Amazonian wildlife such as tapirs, peccaries, and monkeys. The clay contains high concentrations of sodium, calcium, and other vital minerals that help macaws and other animals to regulate their digestive systems, neutralize toxins, and maintain overall health.

Visiting a clay lick is a truly awe-inspiring experience. As the first rays of dawn break through the forest canopy, the air fills with the raucous squawks and screeches of macaws as they begin to gather at the lick. Slowly, the birds will descend from the treetops, cautiously approaching the clay bank and taking turns nibbling at the mineral-rich soil. The sheer number of these vibrant birds, their colors contrasting against the earthy tones of the clay, creates a mesmerizing natural spectacle.

The importance of clay licks to the survival of macaws and other Amazonian wildlife cannot be overstated. These unique geological formations are essential feeding grounds that help sustain the delicate balance of the rainforest ecosystem. As deforestation and habitat loss continue to threaten the Amazon, the protection and preservation of these clay licks has become increasingly crucial to the long-term conservation of macaws and the broader biodiversity of this remarkable region.
```

這種方式可以正常運作，但重要的是要記住，採用這種方法，我們只有**等到所有內容都生成完畢後**，才能從 API 收到回應。請再次執行上方的 cell，你會發現在整個回應一次性全部列印出來之前，什麼都不會顯示。在許多情況下這沒有問題，但如果你正在開發一個應用程式，迫使使用者等待整個回應生成完畢，這可能會導致糟糕的使用體驗。

**串流（Streaming）登場！**

串流讓我們能夠開發在模型生成內容時就能接收的應用程式，而不必等待整個回應全部生成完畢。claude.ai 等應用就是這樣運作的——模型生成回應時，內容會即時串流到使用者的瀏覽器並顯示出來：

![claude_streaming.gif](images/claude_streaming.gif)

## 使用串流

要從 API 獲得串流回應，只需在 `client.messages.create` 中傳入 `stream=True` 即可。這部分很簡單。稍微複雜的是之後如何處理串流回應和傳入的資料。

```python
stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Write me a 3 word sentence, without a preamble.  Just give me 3 words",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=100,
    temperature=0,
    stream=True,
)
```

讓我們查看一下 `stream` 變數的內容：

```python
stream
```

```
<anthropic.Stream at 0x111e5ec10>
```

沒什麼好看的！這個 stream 物件本身並不能為我們做太多事。stream 物件是一個產生器（generator），它會逐一 yield 從 API 接收到的伺服器推送事件（SSE）。我們需要撰寫程式碼來遍歷它並處理每個單獨的伺服器推送事件。請記住，我們的資料不再以一整塊最終完成的形式傳入。讓我們試著遍歷串流回應：

```python
for event in stream:
    print(event)
```

```
MessageStartEvent(message=Message(id='msg_01EZHjA6qmf6y8VWMZSeBmN5', content=[], model='claude-3-haiku-20240307', role='assistant', stop_reason=None, stop_sequence=None, type='message', usage=Usage(input_tokens=30, output_tokens=2)), type='message_start')
ContentBlockStartEvent(content_block=ContentBlock(text='', type='text'), index=0, type='content_block_start')
ContentBlockDeltaEvent(delta=TextDelta(text='Cats', type='text_delta'), index=0, type='content_block_delta')
ContentBlockDeltaEvent(delta=TextDelta(text=' me', type='text_delta'), index=0, type='content_block_delta')
ContentBlockDeltaEvent(delta=TextDelta(text='ow lou', type='text_delta'), index=0, type='content_block_delta')
ContentBlockDeltaEvent(delta=TextDelta(text='dly.', type='text_delta'), index=0, type='content_block_delta')
ContentBlockStopEvent(index=0, type='content_block_stop')
MessageDeltaEvent(delta=Delta(stop_reason='end_turn', stop_sequence=None), type='message_delta', usage=MessageDeltaUsage(output_tokens=10))
MessageStopEvent(type='message_stop')
```

如你所見，我們從 API 收到了許多伺服器推送事件。讓我們更仔細地了解這些事件的含義。以下是對各事件的顏色標注說明：


![streaming_output.png](images/streaming_output.png)

每個串流包含一系列按以下順序排列的事件：
* **MessageStartEvent** — 含空內容的訊息
* **一系列 content blocks** — 每個包含：
    * 一個 **ContentBlockStartEvent**
    * 一個或多個 **ContentBlockDeltaEvent**
    * 一個 **ContentBlockStopEvent**
* 一個或多個 **MessageDeltaEvent**，表示最終訊息的頂層變更
* 最後一個 **MessageStopEvent**

上述回應中只有一個 content block。以下圖表展示了與其相關的所有事件：

![content_block_streaming.png](images/content_block_streaming.png)

我們真正關心的模型生成內容全都來自 ContentBlockDeltaEvent，每個事件的 type 都設為 "content_block_delta"。要取得內容本身，需要存取 `delta` 內的 `text` 屬性。讓我們試著只列印生成的文字：

```python
stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Write me a 3 word sentence, without a preamble.  Just give me 3 words",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=100,
    temperature=0,
    stream=True,
)
for event in stream:
    if event.type == "content_block_delta":
        print(event.delta.text)
```

```
Cats
 me
ow lou
dly.
```

我們成功地列印出了內容，但格式有點難以閱讀。在使用 Python 的 `print()` 函式列印串流文字時，加入以下兩個額外參數會很有幫助：
* `end=""`：預設情況下，`print()` 函式會在列印文字的末尾加上換行符（\n）。透過設定 `end=""`，我們指定列印的文字後面不加換行符，這表示下一個 `print()` 陳述式會繼續在同一行列印。
* `flush=True`：將 `flush` 參數設定為 `True` 可強制立即將輸出寫入主控台或標準輸出，而不等待換行符或緩衝區填滿。這確保文字在從串流回應接收到時就能即時顯示。

讓我們試著做這些修改：

```python
stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "Write me a 3 word sentence, without a preamble.  Just give me 3 words",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=100,
    temperature=0,
    stream=True,
)
for event in stream:
    if event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")
```

```
Cats meow loudly.
```

對於這麼短的文字，串流功能可能不那麼明顯。讓我們要求模型生成更長的內容：

```python
stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "How do large language models work?",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    stream=True,
)
for event in stream:
    if event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")
```

```
Large language models like myself work by using deep learning neural networks that are trained on massive amounts of text data. The key aspects are:

1. Neural network architecture - We use large, multi-layer neural networks with many parameters that can learn complex patterns in language.

2. Training data - We are trained on huge corpora of text from the internet, books, articles, and other sources. This allows us to learn the statistical patterns and structures of language.

3. Self-supervised learning - During training, the model learns to predict the next word in a sequence of text, without any explicit labels. This allows it to learn general language understanding.

4. Transfer learning - The knowledge gained during this pre-training can then be fine-tuned for specific tasks like question answering, summarization, translation, etc.

5. Attention mechanisms - Advanced models like transformers use attention to dynamically focus on the most relevant parts of the input when generating output.

The end result is a model that can understand and generate human-like text by leveraging the patterns and structures it has learned from its training data. Of course, the details get quite technical, but that's the high-level overview of how large language models work. Let me know if you have any other questions!
```

如果你尚未執行上述 cell，請試著執行。你應該會看到內容隨著傳入而逐步列印出來！

如我們所見，ContentBlockDeltaEvent 包含模型生成的文字內容。其他事件也很重要嗎？是的！以下是一個簡單的例子：

如果我們想取得 token 用量資訊，需要查看兩個地方：

* `MessageStartEvent` 包含輸入（提示）的 token 用量資訊
* `MessageDeltaEvent` 包含生成了多少輸出 token 的資訊

![streaming_tokens.png](images/streaming_tokens.png)

讓我們更新上方的程式碼，列印提示用了多少個 token 以及模型生成了多少個 token：

```python
stream = client.messages.create(
    messages=[
        {
            "role": "user",
            "content": "How do large language models work?",
        }
    ],
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    temperature=0,
    stream=True,
)
for event in stream:
    if event.type == "message_start":
        input_tokens = event.message.usage.input_tokens
        print("MESSAGE START EVENT", flush=True)
        print(f"Input tokens used: {input_tokens}", flush=True)
        print("========================")
    elif event.type == "content_block_delta":
        print(event.delta.text, flush=True, end="")
    elif event.type == "message_delta":
        output_tokens = event.usage.output_tokens
        print("\n========================", flush=True)
        print("MESSAGE DELTA EVENT", flush=True)
        print(f"Output tokens used: {output_tokens}", flush=True)
        
```

```
MESSAGE START EVENT
Input tokens used: 14
========================
Large language models like myself work by using deep learning neural networks that are trained on massive amounts of text data. The key aspects are:

1. Neural network architecture - We use large, multi-layer neural networks with many parameters that can learn complex patterns in language.

2. Training data - We are trained on huge corpora of text from the internet, books, articles, and other sources. This allows us to learn the statistical patterns and structures of language.

3. Self-supervised learning - During training, the model learns to predict the next word in a sequence of text, without any explicit labels. This allows it to learn general language understanding.

4. Transfer learning - The knowledge gained during this pre-training can then be fine-tuned for specific tasks like question answering, summarization, translation, etc.

5. Attention mechanisms - Advanced models like transformers use attention to dynamically focus on the most relevant parts of the input when generating output.

The end result is a model that can understand and generate human-like text, drawing upon its broad knowledge of language and the world. But the inner workings are highly complex and not fully understood. There's still a lot to learn about how these large language models work.
========================
MESSAGE DELTA EVENT
Output tokens used: 258
```

### 其他串流事件類型

在使用串流時，你可能還會遇到一些其他事件類型，包括：

* **Ping 事件** — 串流中可能包含任意數量的 ping 事件。
* **Error 事件** — 事件串流中偶爾會出現錯誤事件。例如，在用量高峰期，你可能會收到 overloaded_error，這在非串流情境下通常對應 HTTP 529。

以下是一個錯誤事件的範例：

```
event: error
data: {"type": "error", "error": {"type": "overloaded_error", "message": "Overloaded"}}
```


## 首 Token 時間（TTFT）

使用串流的主要原因是改善首 token 時間（TTFT）：即你或你的使用者收到第一段模型生成內容所需的時間。
讓我們嘗試演示串流對 TTFT 的影響。

我們先從非串流方式開始。我們要求模型生成一段非常長的文字，但截止在 500 個 token：

```python
import time
def measure_non_streaming_ttft():
    start_time = time.time()

    response = client.messages.create(
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": "Write mme a long essay explaining the history of the American Revolution",
            }
        ],
        temperature=0,
        model="claude-3-haiku-20240307",
    )

    response_time = time.time() - start_time

    print(f"Time to receive first token: {response_time:.3f} seconds")
    print(f"Time to recieve complete response: {response_time:.3f} seconds")
    print(f"Total tokens generated: {response.usage.output_tokens}")
    
    print(response.content[0].text)
```

```python
measure_non_streaming_ttft()
```

```
Time to receive first token: 4.194 seconds
Time to recieve complete response: 4.194 seconds
Total tokens generated: 500
Here is a long essay explaining the history of the American Revolution:

The American Revolution was a pivotal event in the history of the United States, marking the country's transition from a collection of British colonies to an independent nation. The roots of the revolution can be traced back to the French and Indian War, which was fought between Britain and France from 1754 to 1763. This conflict, which was part of a larger global war, resulted in the British gaining control of much of North America, including the French colonies. However, the war also left Britain with a significant debt, which it sought to recoup by imposing a series of taxes and regulations on its American colonies.

One of the first major events that led to the American Revolution was the Stamp Act, which was passed by the British Parliament in 1765. This act required all printed materials in the colonies, including newspapers, pamphlets, bills, legal documents, licenses, almanacs, dice, and playing cards, to carry an embossed revenue stamp. The colonists were outraged by this tax, which they saw as a violation of their rights as British subjects. They argued that they were not represented in the British Parliament and therefore should not be subject to taxation without their consent.

In response to the Stamp Act, the colonists organized a series of protests and boycotts, which eventually led to the repeal of the act in 1766. However, this was just the beginning of a series of increasingly contentious conflicts between the colonies and the British government. In 1767, the Townshend Acts were passed, which imposed new taxes on a variety of goods imported to the colonies, including glass, paint, lead, paper, and tea.

The colonists responded with further protests and boycotts, and in 1770, a group of protesters in Boston were fired upon by British soldiers, resulting in the deaths of five civilians in an event known as the Boston Massacre. This incident further inflamed tensions between the colonies and the British government, and in 1773, the British East India Company was granted a monopoly on the tea trade in the colonies. In response, a group of colonists in Boston, disguised as Native Americans, boarded a British ship and dumped hundreds of chests of tea into the harbor, an event known as the Boston Tea Party.

The British government responded to the Boston Tea Party
```

現在讓我們用串流方式嘗試同樣的操作：

```python
def measure_streaming_ttft():
    start_time = time.time()

    stream = client.messages.create(
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": "Write mme a long essay explaining the history of the American Revolution",
            }
        ],
        temperature=0,
        model="claude-3-haiku-20240307",
        stream=True
    )
    have_received_first_token = False
    for event in stream:
        if event.type == "content_block_delta":
            if not have_received_first_token:
                ttft = time.time() - start_time
                have_received_first_token = True
            print(event.delta.text, flush=True, end="")
        elif event.type == "message_delta":
            output_tokens = event.usage.output_tokens
            total_time = time.time() - start_time

    print(f"\nTime to receive first token: {ttft:.3f} seconds", flush=True)
    print(f"Time to recieve complete response: {total_time:.3f} seconds", flush=True)
    print(f"Total tokens generated: {output_tokens}", flush=True)
    

```

```python
measure_streaming_ttft()
```

```
Here is a long essay explaining the history of the American Revolution:

The American Revolution was a pivotal event in the history of the United States, marking the country's transition from a collection of British colonies to an independent nation. The roots of the revolution can be traced back to the French and Indian War, which was fought between Britain and France from 1754 to 1763. This conflict, which was part of a larger global war, resulted in the British gaining control of much of North America, including the French colonies. However, the war also left Britain with a significant debt, which it sought to recoup by imposing a series of taxes and regulations on its American colonies.

One of the first major events that led to the American Revolution was the Stamp Act, which was passed by the British Parliament in 1765. This act required all printed materials in the colonies, including newspapers, pamphlets, bills, legal documents, licenses, almanacs, dice, and playing cards, to carry an embossed revenue stamp. The colonists were outraged by this tax, which they saw as a violation of their rights as British subjects. They argued that they were not represented in the British Parliament and therefore should not be subject to taxation without their consent.

In response to the Stamp Act, the colonists organized a series of protests and boycotts, which eventually led to the repeal of the act in 1766. However, this was just the beginning of a series of increasingly contentious conflicts between the colonies and the British government. In 1767, the Townshend Acts were passed, which imposed new taxes on a variety of goods imported to the colonies, including glass, paint, lead, paper, and tea.

The colonists responded with further protests and boycotts, and in 1770, a group of protesters in Boston were fired upon by British soldiers, resulting in the deaths of five civilians in an event known as the Boston Massacre. This incident further inflamed tensions between the colonies and the British government, and in 1773, the British East India Company was granted a monopoly on the tea trade in the colonies. In response, a group of colonists in Boston, disguised as Native Americans, boarded a British ship and dumped hundreds of chests of tea into the harbor, an event known as the Boston Tea Party.

The British government responded to the Boston Tea Party
Time to receive first token: 0.492 seconds
Time to recieve complete response: 4.274 seconds
Total tokens generated: 500
```

讓我們比較結果：

* **未使用串流**
    * **首 Token 時間：** 4.194 秒
    * **收到完整回應的時間：** 4.194 秒
    * **生成的 Token 總數：** 500
* **使用串流**
    * **首 Token 時間：** 0.492 秒
    * **收到完整回應的時間：** 4.274 秒
    * **生成的 Token 總數：** 500

可以看到，TTFT 相差懸殊！這個示範只生成了 500 個 token，且使用的是速度最快的 Haiku 模型。如果我們改用 Opus 生成 1000 個 token，數字差異將會更加驚人！
    

```python
def compare_ttft():
    def measure_streaming_ttft():
        start_time = time.time()

        stream = client.messages.create(
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": "Write mme a very very long essay explaining the history of the American Revolution",
                }
            ],
            temperature=0,
            model="claude-3-opus-20240229",
            stream=True
        )
        have_received_first_token = False
        for event in stream:
            if event.type == "content_block_delta":
                if not have_received_first_token:
                    ttft = time.time() - start_time
                    have_received_first_token = True
            elif event.type == "message_delta":
                output_tokens = event.usage.output_tokens
                total_time = time.time() - start_time
        return (ttft, output_tokens)
    
    def measure_non_streaming_ttft():
        start_time = time.time()

        response = client.messages.create(
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": "Write mme a very very long essay explaining the history of the American Revolution",
                }
            ],
            temperature=0,
            model="claude-3-opus-20240229"
        )
        ttft = time.time() - start_time
        return (ttft, response.usage.output_tokens)
    
    streaming_ttft, streaming_tokens = measure_streaming_ttft()
    non_streaming_ttft, non_streaming_tokens = measure_non_streaming_ttft()

    print("OPUS STREAMING")
    print(f"Time to first token: {streaming_ttft}")
    print(f"Tokens generated: {streaming_tokens}")
    print("#########################################################")
    print("OPUS NON STREAMING")
    print(f"Time to first token: {non_streaming_ttft}")
    print(f"Tokens generated: {non_streaming_tokens}")

        
```

```python
# DO NOT RUN THIS! It takes over a minute to run and generates around 2000 tokens with Opus! 
compare_ttft()
```

```
OPUS STREAMING
Time to first token: 1.8863098621368408
Tokens generated: 997
#########################################################
OPUS NON STREAMING
Time to first token: 47.03177309036255
Tokens generated: 998
```

當我們用 Opus 生成較長的文字時，串流對 TTFT 的影響更加明顯。非串流方式需要 47 秒才能收到第一個 token；串流方式只需 1.8 秒！

**注意：請記住，串流並不能神奇地縮短模型生成回應的整體時間。我們能更快獲得初始資料，但從請求開始到收到最後一個生成的 token，所需的總時間是相同的。**



## 串流輔助方法

Python SDK 提供了幾種便利的串流訊息方法。我們可以使用 `client.messages.stream` 取代帶有 `stream=True` 的 `client.messages.create`，從而存取實用的輔助方法。`client.messages.stream()` 回傳一個 MessageStreamManager，它是一個 context manager，會 yield 一個 MessageStream，該 MessageStream 可迭代、能發送事件，並能累積訊息。

下方程式碼使用 `client.messages.stream`，讓我們可以使用 `stream.text_stream` 等輔助方法，輕鬆存取串流傳入的文字內容，無需手動檢查串流事件類型。`stream.text_stream` 提供一個只針對串流中文字增量的迭代器。

還有其他有用的輔助方法，例如 `get_final_message`，它在串流讀取完畢後回傳最終累積的訊息。如果你既想使用串流，又需要在生成完成時存取完整的文字，這個方法非常有用。當然，你也可以自己撰寫程式碼來累積訊息，但這個輔助方法讓操作更加簡便。

以下範例在接收到每一段傳入文字時即時列印，並在串流完成時列印最終完整的訊息：


```python
from anthropic import AsyncAnthropic

client = AsyncAnthropic()

async def streaming_with_helpers():
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Write me sonnet about orchids",
            }
        ],
        model="claude-3-opus-20240229",
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)

    final_message = await stream.get_final_message()
    print("\n\nSTREAMING IS DONE.  HERE IS THE FINAL ACCUMULATED MESSAGE: ")
    print(final_message.to_json())

await streaming_with_helpers()
```

```
In gardens fair, where beauty reigns supreme,
The orchid stands, a queen among the blooms,
Her delicate petals, like a lovely dream,
Adorned in nature's most exquisite plumes.

With colors ranging from pure white to bold,
And patterns intricate, a work of art,
Each blossom tells a story, bright and old,
Of evolution's path, a world apart.

From rainforests dense to mountain peaks so high,
The orchid thrives, a testament to grace,
Her beauty captivates the wandering eye,
And in our hearts, she finds a cherished place.

Oh, orchid fair, your splendor knows no bounds,
Forever in our gardens and hearts you'll be found.

STREAMING IS DONE.  HERE IS THE FINAL ACCUMULATED MESSAGE: 
{
  "id": "msg_018x1nZcs3sfq15zKaS4z4gD",
  "content": [
    {
      "text": "In gardens fair, where beauty reigns supreme,\nThe orchid stands, a queen among the blooms,\nHer delicate petals, like a lovely dream,\nAdorned in nature's most exquisite plumes.\n\nWith colors ranging from pure white to bold,\nAnd patterns intricate, a work of art,\nEach blossom tells a story, bright and old,\nOf evolution's path, a world apart.\n\nFrom rainforests dense to mountain peaks so high,\nThe orchid thrives, a testament to grace,\nHer beauty captivates the wandering eye,\nAnd in our hearts, she finds a cherished place.\n\nOh, orchid fair, your splendor knows no bounds,\nForever in our gardens and hearts you'll be found.",
      "type": "text"
    }
  ],
  "model": "claude-3-opus-20240229",
  "role": "assistant",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "input_tokens": 14,
    "output_tokens": 171
  }
}
```


使用 `client.messages.stream()` 時，我們也可以定義自訂事件處理器，在任何串流事件發生時、或只有在生成文字時執行。

下方範例使用了兩個自訂事件處理器。我們使用 `client.messages.stream()` 並要求模型「生成一首 5 個字的詩」，並定義了自己的 `MyStream` 類別，其中包含兩個事件處理器：

* `on_text` — 當 text ContentBlock 物件正在累積時觸發。第一個參數是文字增量，第二個是當前累積的文字。在下方範例中，我們使用這個事件處理器在文字串流傳入時即時列印。文字以綠色顯示，方便視覺辨識。
* `on_stream_event` — 每當從 API 收到任何事件時觸發。在下方範例中，每次收到事件時都會列印事件類型。

接著我們將 `event_handler` 參數傳給 `client.messages.stream` 以註冊回呼方法，在特定事件發生時觸發：


```python
from anthropic import AsyncAnthropic, AsyncMessageStream

client = AsyncAnthropic()

green = '\033[32m'
reset = '\033[0m'

class MyStream(AsyncMessageStream):
    async def on_text(self, text, snapshot):
        # This runs only on text delta stream messages
        print(green + text + reset, flush=True) #model generated content is printed in green

    async def on_stream_event(self, event):
        # This runs on any stream event
        print("on_event fired:", event.type)

async def streaming_events_demo():
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Generate a 5-word poem",
            }
        ],
        model="claude-3-opus-20240229",
        event_handler=MyStream,
    ) as stream:
        # Get the final accumulated message, after the stream is exhausted
        message = await stream.get_final_message()
        print("accumulated final message: ", message.to_json())

await streaming_events_demo()
```

```
on_event fired: message_start
on_event fired: content_block_start
on_event fired: content_block_delta
[32mWhis[0m
on_event fired: content_block_delta
[32mpers[0m
on_event fired: content_block_delta
[32m dance[0m
on_event fired: content_block_delta
[32m,[0m
on_event fired: content_block_delta
[32m secrets[0m
on_event fired: content_block_delta
[32m unf[0m
on_event fired: content_block_delta
[32mol[0m
on_event fired: content_block_delta
[32md,[0m
on_event fired: content_block_delta
[32m love[0m
on_event fired: content_block_delta
[32m.[0m
on_event fired: content_block_stop
on_event fired: message_delta
on_event fired: message_stop
accumulated final message:  {
  "id": "msg_014G44rr3M14DzadHXPn9Xaj",
  "content": [
    {
      "text": "Whispers dance, secrets unfold, love.",
      "type": "text"
    }
  ],
  "model": "claude-3-opus-20240229",
  "role": "assistant",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "input_tokens": 14,
    "output_tokens": 14
  }
}
```

Python SDK 還提供了其他幾個可用的事件處理器，包括：

##### `on_message(message: Message)`
當完整的 Message 物件累積完成時觸發，對應 message_stop SSE。

##### `on_content_block(content_block: ContentBlock)`
當完整的 ContentBlock 物件累積完成時觸發，對應 content_block_stop SSE。

##### `on_exception(exception: Exception)`
在串流回應時遇到例外時觸發。

##### `on_timeout()`
當請求逾時時觸發。

##### `on_end()`
串流中最後觸發的事件。

***

## 練習

撰寫一個使用串流的簡單 Claude 聊天機器人。以下 gif 展示了它應如何運作。請注意，輸出的顏色標注完全是可選的，主要是為了讓 gif 更易於閱讀和觀看：

![streaming_chat_exercise.gif](images/streaming_chat_exercise.gif)

### 參考解答
以下解答是上述練習的一個簡單實作。為了獲得最佳體驗，請以獨立的 Python 腳本執行，而非在 Notebook 的 cell 中執行：

```python
from anthropic import Anthropic

# Initialize the Anthropic client
client = Anthropic()

# ANSI color codes
BLUE = "\033[94m"
GREEN = "\033[92m"
RESET = "\033[0m"

def chat_with_claude():
    print("Welcome to the Claude Chatbot!")
    print("Type 'quit' to exit the chat.")
    
    conversation = []
    
    while True:
        user_input = input(f"{BLUE}You: {RESET}")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        print(f"{GREEN}Claude: {RESET}", end="", flush=True)
        
        stream = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=conversation,
            stream=True
        )
        
        assistant_response = ""
        for chunk in stream:
            if chunk.type == "content_block_delta":
                content = chunk.delta.text
                print(f"{GREEN}{content}{RESET}", end="", flush=True)
                assistant_response += content
        
        print()  # New line after the complete response
        
        conversation.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    chat_with_claude()
```

***
