# 使用 promptfoo 進行模型評分評估

**注意：本課程位於一個包含相關程式碼檔案的資料夾中。若想跟著操作並自行執行評估，請下載整個資料夾。**


到目前為止，我們只撰寫了基於程式碼的評估。在可行的情況下，基於程式碼的評估是最簡單、成本最低的評估方式。它們提供清晰、客觀的評估，基於預定義的標準，非常適合結果直接明確、可量化的任務。問題在於，基於程式碼的評估只能評分某些類型的輸出，主要是那些可以簡化為完全比對、數值比較或其他可程式化邏輯的輸出。

然而，許多語言模型的真實世界應用需要更細緻的評估。假設我們想要建構一個供國中教室使用的聊天機器人，我們可能希望評估輸出，確保它們使用符合年齡的語言、維持教育性的語調、避免回答非學術性的問題，或以適合國中生的複雜程度提供解釋。這些標準是主觀的且依情境而定，使得傳統的基於程式碼的方法難以評估。這正是模型評分評估可以發揮作用的地方！

模型評分評估利用大型語言模型的能力，根據更複雜、更細緻的標準來評估輸出。透過使用另一個模型作為評估者，我們可以利用與生成原始回應相同層次的語言理解和情境感知能力。這種方法讓我們能夠建立更複雜的評估指標，考量語調、相關性、適切性，甚至創意等因素——這些都是基於程式碼的評分系統通常無法處理的。

模型評分評估的核心概念是將評估本身視為一個自然語言處理任務。我們為評估模型提供以下組合：

* 原始提示或問題
* 我們想要評估的模型生成回應
* 評估標準或指導方針
* 如何評估和評分回應的說明

這種方法能夠對輸出進行更全面的評估，不僅考慮事實準確性，還考慮文體元素、對特定指導方針的遵守程度，以及回應在其預期使用情境中的整體品質。

常見的模型評分評估技術包括詢問模型：

* 這個回應有多道歉（apologetic）？
* 根據所提供的情境，這個回應在事實上是否準確？
* 這個回應是否過度提及其情境/資訊？
* 這個回應是否真正適當地回答了問題？
* 這個輸出有多符合我們的語調/品牌/風格指導方針？

在本課程中，我們將使用 promptfoo 撰寫自己簡單的模型評分評估。

---

---

## 使用 promptfoo 進行模型評分評估

與 promptfoo 中大多數事項一樣，撰寫模型評分評估有多種有效的方法。在本課程中，我們將看到最簡單的模式：利用內建斷言。在下一課，我們將看到如何撰寫自訂的模型評分斷言函式。

首先，我們將使用一個名為 `llm-rubric` 的內建斷言，這是 promptfoo 用於「LLM 擔任評審」評估的通用評分器。使用方式很簡單，只需將以下內容加入你的 `promptfooconfig.yaml` 檔案：

```yaml
assert:
  - type: llm-rubric
    # The model we want to use as the grader
    provider: anthropic:messages:claude-3-opus-20240229
    # Specify the criteria for grading the LLM output:
    value: Is not apologetic
```
上述斷言將使用 Claude 3 Opus 根據回應是否帶有歉意的態度來評分輸出。

讓我們試著在自己的評估中使用 `llm-rubric`！

---

---

## 撰寫自己的評估
在本課程中，我們將專注於評估供國中生使用的學術助理提示。我們正在建構一個聊天機器人，它應該回答與學校科目相關的問題，但應避免回答無關的問題。我們將從如下這個簡單的提示開始：

```
You are an interactive tutor assistant for middle school children.
Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
Only answer questions related to middle school academics.
This is the student question: {{question}}
```

我們將撰寫一個模型評分評估，確保模型拒絕回答諸如「我怎麼讓我父母幫我買手機？」或「有哪些有趣的免費電玩遊戲？」這類問題。理論上我們可以嘗試撰寫基於程式碼的評估，使用正規表達式尋找關鍵的拒絕用語，如「I'm sorry」、「I can't help」等，但這種方法非常脆弱。使用模型來評分回應能提供更好的結果。

---

--- 

## 初始化 promptfoo

如同以往，第一步是初始化 promptfoo。在一個新資料夾中，執行以下指令：

```bash
npx promptfoo@latest init
```

---

---

## 基本設定

為了保持簡單，我們不會像之前那樣將提示放在獨立的檔案中。我們將直接在 `promptfooconfig.yaml` 檔案中撰寫提示和測試。刪除檔案中現有的所有內容，並替換為以下內容：

```yaml
description: "School Assistant Eval"

prompts:
  - >- 
    You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    This is the student question {{question}}

providers: [anthropic:messages:claude-3-5-sonnet-20240620]
  # - anthropic:messages:claude-3-haiku-20240307

defaultTest:
  assert:
    - type: llm-rubric
      provider: anthropic:messages:claude-3-opus-20240229
      value: 'Refuses to answer the question and instead redirects to academic topics'

tests:
  - vars:
      question: What's the best free mobile video game?
  - vars:
      question: How can I convince my parents to let me stay up later?
  - vars:
      question: What are some fun theme ideas for a sleepover?
  - vars:
      question: What are some good prank ideas that won't get me in trouble?
  - vars:
      question: Who are some famous left footed soccer players?
```

上述設定包含以下內容：

* `prompts` - 包含我們想要評估的初始基本提示。請記住，我們通常會把提示放在 Python 檔案中，但也可以選擇直接內聯在設定檔中。
* `providers` - 告訴 promptfoo 我們要透過 Claude 3.5 Sonnet 執行提示。
* `defaultTest` - 對於 promptfoo 執行的每個測試，我們都想使用 `llm-rubric` 評分，確保輸出拒絕回答問題，並將討論引導回學術主題。在此案例中，我們告訴 promptfoo 使用 Claude 3 Opus 來執行評分。
* `tests` - 我們要執行的測試集。我們通常在 CSV 檔案中指定這些，但也可以直接在 YAML 檔案中撰寫測試。這些測試都包含我們希望模型拒絕回答的問題。


---

下一步是執行評估：

```bash
npx promptfoo@latest eval
```

以下是我們第一次執行此評估時產生的輸出：

![eval1.png](images/eval1.png)

我們的提示在大多數評估資料集上都能正常運作（雖然這是一個非常小的資料集），但模型似乎很樂意回答關於足球球員的問題。以下是來自 promptfoo 網頁視圖的截圖，展示了模型的回應以及評分模型的評分邏輯：

![soccer_players.png](images/soccer_players.png)

讓我們試著加入第二個更詳細的提示，看看是否能讓模型堅守學術主題。

---

---

## 第二個提示
讓我們加入第二個提示，其中包含一些關於模型應討論哪些主題的具體指導方針：

>  You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    Acceptable topics you should respond to include: math, reading, science, foreign languages, social students, and art.
    Refuse to answer questions not related to the above topics in an academic context.
    This is the student question: {{question}}

將 `promptfooconfig.yaml` 檔案更新為如下所示：

```yaml
description: "School Assistant Eval"

prompts:
  - >- 
    You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    This is the student question: {{question}}
  - >- 
    You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    Acceptable topics you should respond to include: math, reading, science, foreign languages, social students, and art.
    Refuse to answer questions not related to the above topics in an academic context.
    This is the student question: {{question}}


providers: [anthropic:messages:claude-3-5-sonnet-20240620]

defaultTest:
  assert:
    - type: llm-rubric
      provider: anthropic:messages:claude-3-opus-20240229
      value: 'Refuses to answer the question and instead redirects to academic topics'

tests:
  - vars:
      question: What's the best free mobile video game?
  - vars:
      question: How can I convince my parents to let me stay up later?
  - vars:
      question: What are some fun theme ideas for a sleepover?
  - vars:
      question: What are some good prank ideas that won't get me in trouble?
  - vars:
      question: Who are some famous left footed soccer players?
```

我們現在有兩個提示要評估！讓我們再次執行評估：

```bash
npx promptfoo@latest eval
```



---

以下是我們得到的結果：

![eval2.png](images/eval2.png)

看起來對第二個提示所做的更改確實產生了效果！請注意，這個評估資料集太小，在真實世界中並不實用。

---

---

## 評估道歉語氣

仔細觀察模型的輸出後，我們注意到大多數輸出都以「I'm sorry」或「I apologize」等道歉語開頭。這對使用者來說並不是理想的體驗，所以我們決定嘗試改善！我們想要評估第三個提示：

> You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    Acceptable topics you should respond to include: math, reading, science, foreign languages, social students, and art.
    Refuse to answer questions not related to the above topics in an academic context.
    Do not apologize or use an apologetic tone when refusing.  Instead, gently nudge students to focus on school-related topics.
    This is the student question: {{question}}

上述提示特別告訴模型避免道歉，而是溫和地引導學生專注於學術主題。

接下來，讓我們新增第二個 `llm-rubric` 斷言，測試模型的輸出是否帶有歉意。將 `promptfooconfig.yaml` 更新為如下所示：

```yaml
description: "School Assistant Eval"

prompts:
  - >- 
    You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    This is the student question: {{question}}
  - >- 
    You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    Acceptable topics you should respond to include: math, reading, science, foreign languages, social students, and art.
    Refuse to answer questions not related to the above topics in an academic context.
    This is the student question: {{question}}
  - >- 
    You are an interactive tutor assistant for middle school children.
    Students will ask you a question and your job is to respond with explanations that are understandable to a middle school audience.
    Only answer questions related to middle school academics.
    Acceptable topics you should respond to include: math, reading, science, foreign languages, social students, and art.
    Refuse to answer questions not related to the above topics in an academic context.
    Do not apologize or use an apologetic tone when refusing.  Instead, gently nudge students to focus on school-related topics.
    This is the student question: {{question}}


providers: [anthropic:messages:claude-3-5-sonnet-20240620]

defaultTest:
  assert:
    - type: llm-rubric
      provider: anthropic:messages:claude-3-opus-20240229
      value: 'Refuses to answer the question and instead redirects to academic topics'
    - type: llm-rubric
      provider: anthropic:messages:claude-3-opus-20240229
      value: 'Is not apologetic'

tests:
  - vars:
      question: What's the best free mobile video game?
  - vars:
      question: How can I convince my parents to let me stay up later?
  - vars:
      question: What are some fun theme ideas for a sleepover?
  - vars:
      question: What are some good prank ideas that won't get me in trouble?
  - vars:
      question: Who are some famous left footed soccer players?
```

我們現在有三個正在測試的提示。對於每個測試案例，我們使用模型評分兩個獨立的面向：
* 模型應拒絕回答問題
* 模型不應帶有歉意

讓我們執行評估：

```bash
npx promptfoo@latest eval
```


---

以下是我們得到的結果：

![eval3.png](images/eval3.png)

如預期所料，前兩個提示在道歉斷言上失敗，但第三個提示似乎有效！

---

讓我們使用以下指令啟動網頁視圖：

```bash
npx promptfoo@latest view
```

![web_view.png](images/web_view.png)

---

請記得，我們可以點擊放大鏡圖示查看每個模型輸出和對應斷言評分的更多詳情。讓我們仔細看看第一列的第二個條目：

![details1.png](images/details1.png)

我們可以看到輸出通過了原始的模型評分斷言，確實拒絕回答離題的問題。我們也可以看到輸出未通過我們新增的第二個斷言，因為「回應以『I'm sorry』開頭，這是一個道歉用語」。

---

現在讓我們放大第一列的第三個條目：

![details2.png](images/details2.png)

這個輸出通過了兩個斷言！

**請記住，這個資料集對於真實的評估來說遠遠太小了。**

Promptfoo 的內建模型評分斷言非常實用，但在某些情況下，我們可能需要對精確的模型評分指標和流程有更多控制。在下一課中，我們將看看如何定義自己的自訂模型評分器函式！
