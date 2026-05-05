# 模型

## 課程目標
* 理解各種 Claude 模型
* 比較 Claude 模型的速度和能力


讓我們從匯入 `anthropic` SDK 和載入 API 金鑰開始：

```python
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()
```

## Claude 模型

Claude Python SDK 支援多個模型，每個模型都有不同的能力和效能特性。此視覺化比較了 Claude 3 和 3.5 模型的成本與速度，展示了成本與智能之間權衡的範圍：

![models.png](images/models.png)

選擇模型時，有幾個重要因素要考慮：

* 模型的延遲（速度如何？）
* 模型的能力（智能程度如何？）
* 模型的成本（成本如何？）



請參閱 [此表格](https://docs.anthropic.com/en/docs/about-claude/models#model-comparison-table) 以比較 Claude 家族中每個模型的主要功能和能力。

## 比較模型速度

下面是一個簡單函數，為所有 4 個模型執行相同的提示，並列印出模型回應和每個請求花費的時間。

```python
import time
def compare_model_speeds():
    models = ["claude-3-5-sonnet-20240620","claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
    task = "Explain the concept of photosynthesis in a concise paragraph."

    for model in models:
        start_time = time.time()

        response = client.messages.create(
            model=model,
            max_tokens=500,
            messages=[{"role": "user", "content": task}]
        )

        end_time = time.time()
        execution_time = end_time - start_time
        tokens = response.usage.output_tokens
        time_per_token = execution_time/tokens

        print(f"Model: {model}")
        print(f"Response: {response.content[0].text}")
        print(f"Generated Tokens: {tokens}")
        print(f"Execution Time: {execution_time:.2f} seconds")
        print(f"Time Per Token: {time_per_token:.2f} seconds\n")
```

```python
compare_model_speeds()
```

```
Model: claude-3-5-sonnet-20240620
Response: Photosynthesis is the process by which plants, algae, and some bacteria convert light energy into chemical energy. These organisms use sunlight, water, and carbon dioxide to produce glucose (a type of sugar) and oxygen. The process occurs primarily in the chloroplasts of plant cells, where chlorophyll, a green pigment, absorbs light energy. This energy is then used to drive a series of chemical reactions that ultimately result in the production of glucose, which serves as food for the plant and can be stored for later use. Oxygen is released as a byproduct of this process, making photosynthesis crucial for maintaining Earth's atmosphere and supporting life on the planet.
Generated Tokens: 146
Execution Time: 2.56 seconds
Time Per Token: 0.02 seconds

Model: claude-3-opus-20240229
Response: Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize nutrients from carbon dioxide and water. In plants, photosynthesis occurs mainly within the leaves. This process involves the green pigment chlorophyll and generates oxygen as a byproduct. The energy from light is used to convert water, carbon dioxide, and minerals into oxygen and energy-rich organic compounds such as glucose, which are used by the plant for growth and reproduction. Photosynthesis is essential for life on Earth as it provides food for plants, which in turn provide food for other organisms, and it also releases oxygen into the atmosphere, which most living creatures need to survive.
Generated Tokens: 146
Execution Time: 7.32 seconds
Time Per Token: 0.05 seconds

Model: claude-3-sonnet-20240229
Response: Photosynthesis is the process by which plants and certain other organisms convert light energy from the sun into chemical energy in the form of glucose (sugar). During this process, carbon dioxide from the air and water from the soil are absorbed by the plant's leaves. With the aid of chlorophyll (a green pigment) and sunlight, these raw materials are transformed into oxygen, which is released into the atmosphere, and glucose, which serves as the plant's food source and building block for growth and development.
Generated Tokens: 108
Execution Time: 2.64 seconds
Time Per Token: 0.02 seconds

Model: claude-3-haiku-20240307
Response: Photosynthesis is the process by which plants, algae, and some bacteria convert light energy from the sun into chemical energy in the form of carbohydrates. During this process, carbon dioxide and water, with the aid of chlorophyll, are converted into glucose and oxygen through a series of chemical reactions driven by the energy from sunlight. The glucose produced is used by the plant as a source of energy, while the oxygen is released into the atmosphere. This process is essential for the survival of most life on Earth, as it provides the primary source of food and oxygen for many organisms.
Generated Tokens: 126
Execution Time: 1.09 seconds
Time Per Token: 0.01 seconds
```

執行上述程式碼時您獲得的確切回應會有所不同，但以下是執行上述程式碼時我們獲得的輸出摘要：


| 模型 | 生成的符號 | 執行時間（秒） | 每個符號的時間（秒） |
|-------|------------------|--------------------------|--------------------------|
| claude-3-5-sonnet-20240620 | 146 | 2.56 | 0.02 |
| claude-3-opus-20240229 | 146 | 7.32 | 0.05 |
| claude-3-sonnet-20240229 | 108 | 2.64 | 0.02 |
| claude-3-haiku-20240307 | 126 | 1.09 | 0.01 |

同樣重要的是要注意，對於「解釋光合作用的概念為簡潔的段落」這樣簡單的提示，所有模型都表現良好。在這種特定情況下，選擇最快和最便宜的選項可能是有意義的。



上面的例子是模型速度差異的簡單說明，但它不是非常嚴格的演示。以下是我們生成的圖表，為所有 3 個模型提供相同輸入提示 50 次，並平均每個模型的回應時間。為了確保「公平」比較，我們提示模型生成非常長的輸出，然後使用 `max_tokens` 將所有模型回應切割到相同的符號數量（我們在下一堂課中介紹這一點）。

![speed_comparison.png](images/speed_comparison.png)

## 比較模型能力

顯然 Haiku 是最快的模型，那為什麼我們還要費力使用其他的？這一切都歸結於模型速度、成本和整體能力之間的權衡。Haiku 是最快的，但在某些情況下其輸出的質量可能不如 Opus 的好。也就是說，重要的是要注意，在許多情況下，Haiku 的效能可能與一些更有能力的模型一樣好。真正確定哪個模型是您特定用例「最佳」的唯一方法是嘗試它們並評估它們的效能。

一般來說，我們建議對涉及以下情況的用例使用最強大的模型 Claude 3.5 Sonnet：
* **編碼：** Claude 3.5 Sonnet 自主編寫、編輯和執行程式碼，簡化程式碼翻譯以提高速度和準確性，並進行遷移。
* **客戶支援：** Claude 3.5 Sonnet 理解使用者背景並協調多步工作流程，實現 24/7 支援、更快的回應和改進的客戶滿意度。
* **資料科學與分析：** Claude 3.5 Sonnet 導覽非結構化資料、生成見解並生成視覺化和預測以增強資料科學專業知識。
* **視覺處理：** Claude 3.5 Sonnet 擅於解釋圖表、圖形和影像，準確轉錄文字以獲得超越文字的見解。
* **寫作：** Claude 3.5 Sonnet 代表了對細微差別和幽默理解的重大進步，生成高品質、真實且有關聯的內容。

如果您對我們的 Claude 家族模型之間的基準比較感興趣，請閱讀我們的 [Claude 家族模型卡片](https://www-cdn.anthropic.com/f2986af8d052f26236f6251da62d16172cfabd6e/claude-3-model-card.pdf) 以取得更多資訊。

### 展示能力

用單個演示展示每個模型的各種能力很困難，但下面的函數試圖這樣做。
我們要求三個模型解決以下數學問題：

```
What is the geometric monthly fecal coliform mean of a distribution system with the following FC
 counts: 24, 15, 7, 16, 31 and 23? The result will be inputted into a NPDES DMR, therefore, round
 to the nearest whole number
```

**注意：正確答案是 18**

我們要求每個模型解決數學問題 7 次，並記錄每次的答案：

```python
def compare_model_capabilities():
    models = ["claude-3-5-sonnet-20240620", "claude-3-opus-20240229", "claude-3-sonnet-20240229", "claude-3-haiku-20240307"]
    task = """
    What is the geometric monthly fecal coliform mean of a distribution system with the following FC
 counts: 24, 15, 7, 16, 31 and 23? The result will be inputted into a NPDES DMR, therefore, round
 to the nearest whole number.  Respond only with a number and nothing else.
    """

    for model in models:
        answers = []
        for attempt in range(7):
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[{"role": "user", "content": task}]
            )
            answers.append(response.content[0].text)

        print(f"Model: {model}")
        print(f"Answers: ", answers)
```

```python
compare_model_capabilities()
```

```
Model: claude-3-5-sonnet-20240620
Answers:  ['18', '18', '18', '18', '18', '18', '18']
Model: claude-3-opus-20240229
Answers:  ['18', '18', '18', '18', '18', '18', '18']
Model: claude-3-sonnet-20240229
Answers:  ['18', '17', '16', '17', '19', '18', '18']
Model: claude-3-haiku-20240307
Answers:  ['17', '17', '18', '17', '17', '17', '18']
```

我們從每個模型獲得的確切輸出會有所不同，但以下是單次執行結果的摘要：

* `claude-3-5-sonnet-20240620` - 正確獲得答案 **7/7** 次
* `claude-3-opus-20240229` - 正確獲得答案 **7/7** 次
* `claude-3-sonnet-20240229` - 正確獲得答案 **3/7** 次
* `claude-3-haiku-20240307` - 正確獲得答案 **2/7** 次

顯然 Claude 3.5 Sonnet 和 Claude 3 Opus 在這個特定的數學問題上表現最好。

**注意：這是一個非常簡化的模型能力演示。它根本不是嚴格的比較，只是作為可訪問的教育演示。請參閱 Claude 3 模型卡片，以獲得使用業界標準基準的更嚴格、定量的比較**


## 選擇一個模型

下一個邏輯問題是：您應該使用哪個模型？在不了解給定應用程式的特定任務和需求的情況下，這是一個難以回答的問題。模型的選擇可以顯著影響應用程式的效能、使用者體驗和成本效益：

* **能力**
  * 首要考慮是模型是否具備必要的能力來處理應用程式特定的任務和使用案例。不同的模型在不同領域的性能變化，例如一般語言理解、特定任務知識、推理能力和生成質量。必須使模型的優勢與應用程式的需求相一致，以確保最佳結果。
* **速度**
  * 模型處理和生成回應的速度是另一個關鍵因素，特別是對於需要即時或接近即時互動的應用程式。更快的模型可以提供更靈敏和無縫的使用者體驗，減少延遲並改進整體可用性。但是，必須在速度和模型能力之間取得平衡，因為最快的模型可能並不總是最適合您的具體需求。
* **成本**
  * 使用特定模型相關的成本是一個實際考慮，可能會影響應用程式的可行性和可擴展性。具有更高能力的模型通常會有更高的價格標籤，無論是 API 使用成本還是所需的計算資源。評估不同模型的成本影響並確定仍然符合應用程式要求的最具成本效益的選項至關重要。

#### 一種方法：從 Haiku 開始

進行實驗時，我們通常建議從 Haiku 模型開始。Haiku 是一個輕量級且快速的模型，可以作為許多應用程式的絕佳起點。它的速度和成本效益使其成為初始實驗和原型設計的有吸引力的選項。在許多使用案例中，Haiku 被證明能夠生成完全符合應用程式需求的高質量回應。透過從 Haiku 開始，您可以快速迭代您的應用程式、測試不同的提示和配置，並評估模型的效能，而無需承擔大量成本或延遲。如果您對回應不滿意，很容易「升級」到 Claude 3.5 Sonnet 等模型。


#### 評估和升級
在開發和精煉應用程式時，建立針對您的使用案例和提示的全面評估套件至關重要。這些評估將作為衡量所選模型效能的基準，幫助您做出有關潛在升級的明智決定。

如果您發現 Haiku 的回應不符合應用程式的要求，或者您希望獲得更高的複雜性和準確性，您可以輕鬆過渡到更有能力的模型，如 Sonnet 或 Opus。這些模型提供增強的能力，可以處理更複雜的任務和更細緻的語言理解。

透過建立嚴格的評估框架，您可以客觀地比較不同模型在您特定使用案例中的效能。這個實證證據將指導您的決策過程，並確保您選擇最符合應用程式需求的模型。

***
