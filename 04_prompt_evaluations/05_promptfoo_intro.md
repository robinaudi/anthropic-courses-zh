# promptfoo 介紹

**注意：本課程所在資料夾包含相關程式碼檔案。如果想跟著操作並自行執行評估，請下載整個資料夾**

我們已經學過如何從頭撰寫評估，這雖然有效，但有點繁瑣。實際上，利用專門為此目的設計的工具往往更為實用。目前有許多評估工具和函式庫可供選擇（而且還在持續增加！），包括：
- [promptfoo](https://github.com/promptfoo/promptfoo)
- [Vellum](https://www.vellum.ai/#playground)
- [Scale Evaluation](https://scale.com/evaluation/model-developers)
- [Prompt Layer](https://promptlayer.com/)
- [Chain Forge](https://github.com/ianarawjo/ChainForge)
- 以及許多其他工具！

其中一個開源且易於使用的選項是 promptfoo。promptfoo 提供了一個精簡、開箱即用的解決方案，可大幅減少全面提示詞測試所需的時間和精力。它提供了簡單、現成的批次測試、版本控制和效能分析基礎設施，讓開發者能更專注於優化提示詞，而不是建立和維護測試框架。它讓跨多個提示詞、模型和供應商執行評估變得輕鬆，並提供視覺化和比較評估結果的工具。相較於從頭撰寫評估邏輯，promptfoo 和其他評估工具是一大進步！

執行評估後，promptfoo 會產生如下圖所示的儀表板：

![prompt_foo.png](images/prompt_foo.png)

讓我們開始吧！

---

## 第一個 promptfoo 評估

本課程後續幾堂課將專注於使用 promptfoo 撰寫評估。在這第一堂課中，我們將學習一種簡單的方法，使用 promptfoo 來評估前幾堂課中的「這隻動物有幾條腿？」提示詞。這是一個非常簡單的提示詞和評估。我們的重點在於使用 promptfoo 執行評估的實際工具和流程。

回顧一下，在那堂課中我們使用了這個小型評估資料集：

```py
eval_data = [
    {"animal_statement": "The animal is a human.", "golden_answer": "2"},
    {"animal_statement": "The animal is a snake.", "golden_answer": "0"},
    {"animal_statement": "The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.", "golden_answer": "5"},
    {"animal_statement": "The animal is a dog.", "golden_answer": "4"},
    {"animal_statement": "The animal is a cat with two extra legs.", "golden_answer": "6"},
    {"animal_statement": "The animal is an elephant.", "golden_answer": "4"},
    {"animal_statement": "The animal is a bird.", "golden_answer": "2"},
    {"animal_statement": "The animal is a fish.", "golden_answer": "0"},
    {"animal_statement": "The animal is a spider with two extra legs", "golden_answer": "10"},
    {"animal_statement": "The animal is an octopus.", "golden_answer": "8"},
    {"animal_statement": "The animal is an octopus that lost two legs and then regrew three legs.", "golden_answer": "9"},
    {"animal_statement": "The animal is a two-headed, eight-legged mythical creature.", "golden_answer": "8"},
]
```

在那堂課中，我們撰寫了三個準確率逐步提升的提示詞。在本課程中，我們將把評估資料集和提示詞移植到 promptfoo，看看執行和比較輸出有多容易。

---

---

## 安裝 promptfoo

使用 promptfoo 的第一步是透過命令列安裝它。進入要撰寫評估程式碼的資料夾，執行以下命令：

```bash
npx promptfoo@latest init
```

這會在當前目錄建立一個 `promptfooconfig.yaml` 檔案。這個檔案是所有魔法發生的地方。我們在其中設定以下內容：
- 要在評估中使用的供應商（Anthropic API 模型）
- 要評估的提示詞
- 要執行的測試

---



---

## 設定供應商

接下來，可以設定 promptfoo 使用我們想要執行評估的特定 Anthropic API 模型。為此，在 `promptfooconfig.yaml` 檔案中指定 `providers` 欄位，並設定為一個或多個 Anthropic 模型。promptfoo 使用特定格式來指定模型名稱。目前支援的 Anthropic 模型字串為：

- `anthropic:messages:claude-3-5-sonnet-20240620`
- `anthropic:messages:claude-3-haiku-20240307`
- `anthropic:messages:claude-3-sonnet-20240229`
- `anthropic:messages:claude-3-opus-20240229`
- `anthropic:messages:claude-2.0`
- `anthropic:messages:claude-2.1`
- `anthropic:messages:claude-instant-1.2`

我們將在第一個評估中使用 Haiku。刪除 `promptfooconfig.yaml` 的現有內容，替換為以下內容：

```yaml
description: "Animal Legs Eval"
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"
```

各部分的說明：

- `description` 是描述評估任務的可選標籤。
- `providers` 告訴 promptfoo 要在此評估中使用 Haiku。我們可以指定多個模型，後續課程會介紹。



---

執行評估時，promptfoo 會尋找 `ANTHROPIC_API_KEY` 環境變數。可以在命令列執行以下命令來設定環境變數：

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

---

---

## 指定提示詞
下一步是告訴 promptfoo 我們想要評估的提示詞。有許多方法可以做到，包括：
- 直接在 YAML 檔案中以文字形式放入提示詞
- 從 JSON 檔案載入提示詞
- 從文字檔載入提示詞
- 從另一個 YAML 檔案載入提示詞
- 從 Python 檔案載入提示詞

我們偏好將所有相關提示詞放在單一 Python 檔案中，以各自返回提示詞字串的函式形式存放。後續課程會介紹其他方法。正如你將在本課程中看到的，promptfoo 相當靈活！

---

建立一個名為 `prompts.py` 的 Python 檔案，並放入以下提示詞函式：

```py
def simple_prompt(animal_statement):
    return f"""You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement.
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? Please respond with a number"""

def better_prompt(animal_statement):
    return f"""You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement.
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? Please only respond with a single digit like 2 or 9"""
```

注意每個函式都接受 `animal_statement` 參數，將其插入提示詞，然後返回最終提示詞字串

---

下一步是告訴 promptfoo 設定檔，我們想從剛建立的 `prompts.py` 檔案載入提示詞。為此，更新 `promptfooconfig.yaml` 檔案，加入以下程式碼：

```yaml
description: "Animal Legs Eval"

prompts:
  - prompts.py:simple_prompt
  - prompts.py:better_prompt
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"
```

注意我們為每個加入 `prompts.py` 的提示詞函式各加一行。我們已告訴 promptfoo 要評估兩個提示詞：`simple_prompt` 和 `better_prompt`，兩者都存放在 `prompts.py` 檔案中。

---

---

## 設定測試

下一步是告訴 promptfoo 要針對特定提示詞和供應商執行的測試。promptfoo 提供了許多定義測試的方式，我們先從最常見的方法之一開始：在 CSV 檔案中指定測試。

建立一個名為 `dataset.csv` 的新 CSV 檔案，並在其中撰寫測試輸入。

promptfoo 允許我們直接在 CSV 檔案中定義評估邏輯。在後續課程中，我們會看到 promptfoo 內建的一些測試斷言，但對於這個特定評估，我們只需要對模型輸出與預期腿數輸出進行精確字串比對。

為此，我們的 CSV 將包含兩個欄位標題：
- `animal_statement` ——包含如「The animal is an elephant」這樣的輸入動物陳述
- `__expected` ——包含預期的正確輸出（注意 __expected 使用雙底線）。這是 promptfoo 特有的語法。


---

建立 `dataset.csv` 檔案並加入以下內容：

```csv
animal_statement,__expected
"The animal is a human.","2"
"The animal is a snake.","0"
"The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.","5"
"The animal is a dog.","4"
"The animal is a cat with two extra legs.","6"
"The animal is an elephant.","4"
"The animal is a bird.","2"
"The animal is a fish.","0"
"The animal is a spider with two extra legs","10"
"The animal is an octopus.","8"
"The animal is an octopus that lost two legs and then regrew three legs.","9"
"The animal is a two-headed, eight-legged mythical creature.","8"
```

---

最後，告訴 promptfoo 從 `dataset.csv` 檔案載入測試。為此，更新 `promptfooconfig.yaml` 檔案，加入以下程式碼：

```yaml
description: "Animal Legs Eval"

prompts:
  - prompts.py:simple_prompt
  - prompts.py:better_prompt
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"

tests: animal_legs_tests.csv
```

---


---

## 執行評估

指定好供應商、提示詞和測試之後，是時候執行評估了！

在終端機執行以下命令：

```bash
npx promptfoo@latest eval
```
這將啟動評估流程。對於每個提示詞，promptfoo 將：
- 從 CSV 檔案取得每個 `animal_statement`
- 建構包含 `animal_statement` 的完整提示詞
- 以個別提示詞向 Anthropic API 發送請求
- 檢查輸出是否符合 CSV 檔案中的預期輸出

評估完成後，promptfoo 會在終端機顯示結果。


---

以下是執行上述兩段程式碼的 promptfoo 輸出範例：

![eval_output1.png](images/eval_output1.png)

---

上方截圖只顯示前四行，但評估確實對所有十二個輸入執行。
- 左欄顯示特定的 `animal_statement`
- 中欄顯示 `simple_prompt` 的輸出和分數，似乎每個測試案例都失敗了！
- 右欄顯示 `better_prompt` 的輸出和分數，在大多數測試案例上都成功，除了邏輯較複雜的那些。

---

---

## 檢視評估結果

promptfoo 讓在瀏覽器中啟動儀表板來視覺化和檢查評估結果變得非常容易。執行上述評估後，在終端機執行以下命令：

```bash
npx promptfoo@latest view
```

這會詢問是否要啟動伺服器（輸入「y」），然後在瀏覽器中開啟儀表板。

![eval_view1.png](images/eval_view1.png)

---

最相關的摘要資訊在頂部：

![eval_results1.png](images/eval_results1.png)

---

我們也可以深入查看特定結果，了解失敗原因。讓我們看看其中一個 `simple_prompt` 的結果（中欄）。這個提示詞的每一行都標記為失敗。這是怎麼回事？

點擊儲存格中的放大鏡按鈕了解更多：

![toolbar.png](images/toolbar.png)

---

這會開啟一個包含輸出和評分詳細資訊的模態視窗：

![details.png](images/details.png)

---

可以清楚看到 `simple_prompt` 得到了正確答案 0，但輸出包含了大量額外的解釋文字，導致評估失敗。

仔細查看最右欄（包含 `better_prompt` 結果），我們得到了好得多的回應，全都是 `5` 或 `0` 這樣的單一數字。它在需要更多推理才能回答的複雜 `animal_statements` 上似乎失敗了，例如：

> The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.

---


---

## 新增第三個提示詞
回想一下之前程式碼評分評估課程，我們最終透過在提示詞中加入思維鏈（Chain of Thought）推理取得了最佳結果。讓我們加入一個包含思維鏈的改良版第三個提示詞，看看它在「刁鑽」問題上的表現！

在 `prompts.py` 中加入以下提示詞函式：

```py
def chain_of_thought_prompt(animal_statement):
    return f"""You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement.
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? 
    Start by reasoning about the numbers of legs the animal has, thinking step by step inside of <thinking> tags.  
    Then, output your final answer inside of <answer> tags. 
    Inside the <answer> tags return just the number of legs as an integer and nothing else."""
```

---

接著更新 `promptfooconfig.yaml` 檔案，加入新提示詞：


```yaml
description: "Animal Legs Eval"

prompts:
  - prompts.py:simple_prompt
  - prompts.py:better_prompt
  - prompts.py:chain_of_thought_prompt
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"

tests: animal_legs_tests.csv
```


---

在執行這個評估之前，需要解決一個問題：新的 `chain_of_thought_prompt` 在輸出中帶有 `<thinking>` 和 `<answer>` 標籤。為了真正評估模型在這個提示詞上的表現，我們需要提取模型放在 `<answer>` 標籤內的數字答案，與預期值進行比較。

promptfoo 允許我們定義自訂的 `transforms`（轉換函式），用於在實際比較邏輯之前操作模型的輸出。為此，我們將撰寫一個簡單的 Python 函式，從 `<answer>` 標籤之間提取答案。

建立一個名為 `transform.py` 的新檔案，並加入以下程式碼：


```py
def get_transform(output, context):
    if "<thinking>" in output:
        try:
            return output.split("<answer>")[1].split("</answer>")[0].strip()
        except Exception as e:
            print(f"Error in get_transform: {e}")
            return output
    return output
```


這個名為 `get_transform` 的函式期望接收模型的輸出（後續課程會說明 `context` 參數）。我們可以在返回之前將模型的輸出轉換成任何形式。在這個特定情況下，我們執行以下其中一項操作：

- 如果輸出包含 `<thinking>` 標籤，我們知道這是思維鏈提示詞的輸出。提取 `<answer>` 標籤之間的數字並作為新輸出返回。
- 否則直接返回原始輸出（適用於不使用思維鏈的其他提示詞）

---

最後一步是告訴 promptfoo 要使用這個轉換函式。更新 `promptfooconfig.yaml` 檔案如下：

```yaml
description: "Animal Legs Eval"

prompts:
  - prompts.py:simple_prompt
  - prompts.py:better_prompt
  - prompts.py:chain_of_thought_prompt
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"

tests: animal_legs_tests.csv

defaultTest:
  options:
    transform: file://transform.py
```

---

末尾的設定告訴 promptfoo 始終對所有測試套用來自 `transform.py` 的轉換函式。預設情況下，promptfoo 會在 `transform.py` 檔案中尋找名為 `get_transform` 的函式。

---

現在可以再次執行評估：

```bash
npx promptfoo@latest eval
```

---

將看到類似以下的輸出，現在包含 4 欄：

![three_prompt_eval.png](images/three_prompt_eval.png)

---

可以再次使用以下命令在瀏覽器中查看結果：

```bash
npx promptfoo@latest view
```
將看到如下所示的網頁：

![final_view.png](images/final_view.png)

---

可以清楚看到，包含思維鏈的提示詞正確回答了所有問題！

---

---

## 比較模型
promptfoo 的一個優點是跨不同模型執行評估非常容易。我們做了一些提示工程才讓使用 Haiku 的提示詞達到 100% 分數，但讓我們看看改用更強大的模型（如 Claude 3.5 Sonnet）會有什麼結果。

我們所要做的就是更新 `promptfooconfig.yaml` 檔案，加入符合有效 Anthropic 供應商字串的第二個供應商。更新 `promptfooconfig.yaml`，加入兩個供應商：


```yaml
description: "Animal Legs Eval"

prompts:
  - prompts.py:simple_prompt
  - prompts.py:better_prompt
  - prompts.py:chain_of_thought_prompt
  
providers:
  - anthropic:messages:claude-3-haiku-20240307
  - anthropic:messages:claude-3-5-sonnet-20240620

tests: animal_legs_tests.csv

defaultTest:
  options:
    transform: file://transform.py
```

然後用相同的命令再次執行評估：

```bash
npx promptfoo@latest eval
```

---

查看網頁儀表板時，我們看到了一些有趣的結果！

![multi_model_eval_view.png](images/multi_model_eval_view.png)

---

只需在 YAML 檔案中加入一行，我們就能跨兩個模型執行評估集。前三個輸出欄是 Claude 3 Haiku 的輸出，最後三個是 Claude 3.5 Sonnet 的輸出。Claude 3.5 Sonnet 即使使用在 Claude 3 Haiku 上得到 0% 的 `simple_prompt`，也能以 100% 通過評估。

這類資訊非常有價值：不只是哪個提示詞表現最好，更是哪個模型與提示詞的組合在特定任務上表現最好。

**補充說明：** 如果你想知道為什麼 Claude 3.5 Sonnet 在思維鏈提示詞上沒有得到 100%，這裡有個解釋！它在 `animal_statement` 為「The animal is an octopus.」的測試上答錯了。在 `<thinking>` 標籤內，Claude 3.5 Sonnet 推理認為章魚（octopus）實際上沒有任何腿，它的附肢通常稱為「arms（臂）」而非「legs（腿）」。升級到「更聰明」的模型後，我們在思維鏈提示詞上的表現反而略有下降，因為模型「太聰明了」。如果想確保所有模型上的表現，可以更新提示詞，更明確地定義什麼算作「腿」。

本課程只是 promptfoo 的初體驗。在後續課程中，我們將學習如何使用更複雜的程式碼評分邏輯、定義自訂評分器，以及執行模型評分評估。
