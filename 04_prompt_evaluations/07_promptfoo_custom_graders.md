# Promptfoo：自訂程式碼評分器

**注意：本課程位於一個包含相關程式碼檔案的資料夾中。若想跟著操作並自行執行評估，請下載整個資料夾。**


到目前為止，我們已經看過如何使用一些 promptfoo 內建的評分器，例如 `exact-match` 和 `contains-all`。這些功能通常很實用，但 promptfoo 也讓我們能夠為更特定的評分任務撰寫自訂評分邏輯。

為了示範這一點，我們將使用一個非常簡單的提示模板：

> Write a short paragraph about {{topic}}. Make sure you mention {{topic}} exactly {{count}} times, no more or fewer. 

我們將把 `{{topic}}` 和 `{{count}}` 填入像是 `"tweezers"` 和 `7` 這樣的值，產生如下的提示：

> Write a short paragraph about tweezers. Make sure you mention tweezers exactly 7 times, no more or fewer. 

為了評分這個輸出，我們需要撰寫一些自訂邏輯，確保模型的輸出剛好提到「tweezers」7 次。

對於以下提示：

> Write a short paragraph about sheep. Make sure you mention sheep exactly 3 times, no more or fewer. 

我們需要撰寫評分邏輯，確保「sheep」這個詞在模型輸出中剛好出現 3 次。

---

---

## 初始化 promptfoo

如同以往，第一步是使用以下指令初始化 promptfoo：


```bash
npx promptfoo@latest init
```


如我們之前所見，這會建立一個 `promptfooconfig.yaml` 檔案。我們可以刪除其中的現有內容。

接下來，我們要設定 providers。將以下內容新增至 `promptfooconfig.yaml`：

```yaml
description: Count mentions

providers:
  - anthropic:messages:claude-3-haiku-20240307
  - anthropic:messages:claude-3-5-sonnet-20240620
```
這告訴 promptfoo 我們想要同時使用 Claude 3 Haiku 和 Claude 3.5 Sonnet 執行評估。我們將比較它們在這個特定任務上的表現！

請確保您已設定 `ANTHROPIC_API_KEY` 環境變數。您可以在終端機中執行以下指令來設定環境變數：

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

---

---

## 準備提示

到目前為止，我們已經看到可以將提示寫成 Python 檔案中的函式。這是我們推薦的做法，但 promptfoo 也提供了其他幾種指定提示的方式。最簡單的方式是直接在 YAML 檔案中以文字撰寫。

讓我們試試這種內聯方式。更新 `promptfooconfig.yaml` 檔案，加入以下內容：


```yaml
description: Count mentions
prompts:
  - >-
    Write a short paragraph about {{topic}}. Make sure you mention {{topic}} exactly {{count}} times, no more or fewer. Only use lower case letters in your output.
providers:
  - anthropic:messages:claude-3-haiku-20240307
  - anthropic:messages:claude-3-5-sonnet-20240620
```


注意 `prompts` 欄位，其中直接在 YAML 檔案中包含了我們的文字提示。請留意 `{{topic}}` 和 `{{count}}` 變數，它們使用雙大括號。這些提示使用 Nunjucks 模板語法，這在接下來的內容中非常重要！

---

---

## 撰寫測試案例

在先前的課程中，我們將測試案例和評分邏輯寫入 CSV 檔案中。如先前所討論，promptfoo 非常靈活，提供了多種指定測試的方式。

我們可以直接在 YAML 設定檔中撰寫測試案例。將 `promptfooconfig.yaml` 檔案更新為如下所示：

```yaml
description: Count mentions
prompts:
  - >-
    Write a short paragraph about {{topic}}. Make sure you mention {{topic}} exactly {{count}} times, no more or fewer. Only use lower case letters in your output.
providers:
  - anthropic:messages:claude-3-haiku-20240307
  - anthropic:messages:claude-3-5-sonnet-20240620
tests:
  - vars:
      topic: sheep
      count: 3
  - vars:
      topic: fowl
      count: 2
  - vars:
      topic: gallows
      count: 4
  - vars:
      topic: tweezers
      count: 7
  - vars:
      topic: jeans
      count: 6
```

在底部，我們定義了 5 個測試案例，每個測試案例都有各自的 `topic` 和 `count` 值。Promptfoo 會自動執行每個測試，並在提示模板中替換 `{{topic}}` 和 `{{count}}`。

我們尚未加入任何評分邏輯，但仍然可以執行評估，確認變數是否被正確填入。

要執行評估，我們使用與之前相同的指令：

```bash
npx promptfoo@latest eval
```

---

以下是我們得到的輸出：

![initial_eval_output.png](images/initial_eval_output.png)

放大單一列，我們可以看到模型輸出整體上看起來不錯。在這個例子中，`{{topic}}` 設定為「sheep」，對應的模型輸出是關於綿羊的段落！

![single_row-2.png](images/single_row-2.png)

現在我們只需要實作自訂評分邏輯，測試輸出是否提到主題正確的次數！

---

---

## 新增自訂評分器函式

Promptfoo 允許我們定義自己的 Python 評分器函式。對於這個特定範例，我們想定義一個函式，確保模型輸出提到特定主題的次數是正確的。我們先建立一個名為 `count.py` 的新 Python 檔案。在這個檔案中，我們加入以下函式：

```py
import re

def get_assert(output, context):
    topic = context["vars"]["topic"]
    goal_count = int(context["vars"]["count"])
    pattern = fr'(^|\s)\b{re.escape(topic)}\b'

    actual_count = len(re.findall(pattern, output.lower()))

    pass_result = goal_count == actual_count

    result = {
        "pass": pass_result,
        "score": 1 if pass_result else 0,
        "reason": f"Expected {topic} to appear {goal_count} times. Actual: {actual_count}",
    }
    return result
```

讓我們說明上述程式碼的功能。Promptfoo 會自動在我們的檔案中尋找名為 `get_assert` 的函式，並傳入兩個參數：

- 來自特定模型的輸出
- `context` 字典，包含產生該輸出的變數和提示

Promptfoo 期望我們的函式回傳以下其中一種：
- 布林值（通過/失敗）
- 浮點數（分數）
- GradingResult 字典

我們選擇回傳 GradingResult 字典，其中必須包含以下屬性：

- `pass_`：布林值
- `score`：浮點數
- `reason`：說明字串

在上述函式中，我們從 `context` 參數中提取主題和計數，然後使用正規表達式計算主題在輸出中出現的次數，最後回傳 `result`。

---

現在我們已經定義好評分器，是時候告訴 promptfoo 了。更新 `promptfooconfig.yaml` 檔案：

```yaml
description: Count mentions
prompts:
  - >-
    Write a short paragraph about {{topic}}. Make sure you mention {{topic}} exactly {{count}} times, no more or fewer. Only use lower case letters in your output.
providers:
  - anthropic:messages:claude-3-haiku-20240307
  - anthropic:messages:claude-3-5-sonnet-20240620
defaultTest:
  assert:
    - type: python
      value: file://count.py
tests:
  - vars:
      topic: sheep
      count: 3
  - vars:
      topic: fowl
      count: 2
  - vars:
      topic: gallows
      count: 4
  - vars:
      topic: tweezers
      count: 7
  - vars:
      topic: jeans
      count: 6
```
`defaultTest` 告訴 promptfoo，對於它執行的每個測試，我們都希望使用在 `count.py` 檔案中定義的 Python 評分器。

---


---

## 執行評估

要執行評估，我們使用與之前相同的指令：

```bash
npx promptfoo@latest eval
```


---

以下是執行評估後得到的輸出：

![final_eval.png](images/final_eval.png)

執行以下指令啟動網頁介面：

```bash
npx promptfoo@latest view
```

![final_view.png](images/final_view.png)

---

我們可以看到 Claude 3.5 在這個任務上得到了 100%，而 Claude 3 Haiku 只得到 20%。要驗證結果，可以點擊放大鏡圖示查看完整的輸入提示和對應的輸出。

以下是 Claude 3 Haiku 的錯誤輸出：

![tweezers_haiku_closeup.png](images/tweezers_haiku_closeup.png)

以及 Claude 3.5 Sonnet 的正確輸出：

![tweezers_sonnet_closeup.png](images/tweezers_sonnet_closeup.png)

---

這個特定評估有點刻意設計，但其目的是示範定義自訂 Python 評分邏輯的過程。結合 promptfoo 的內建斷言和自訂評分器函式，我們幾乎可以撰寫任何基於程式碼的評估。

在下一課中，我們將學習 promptfoo 中的模型評分評估。
