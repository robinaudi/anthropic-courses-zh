# Promptfoo：分類評估

**注意：本課程位於一個包含相關程式碼檔案的資料夾中。若想跟著操作並自行執行評估，請下載整個資料夾。**


在先前的課程中，我們評估了用來分類客戶投訴的提示，例如：

> 每次我開啟你們的 app，我的手機就變得非常慢

以及

> 我不知道如何更改密碼

這些投訴被分類為五個不同類別：
- 軟體錯誤（Software Bug）
- 硬體故障（Hardware Malfunction）
- 使用者操作錯誤（User Error）
- 服務中斷（Service Outage）
- 功能請求（Feature Request）

在本課程中，我們將把這個提示評估移植到 promptfoo，讓批次執行和比較結果變得更加容易。

---


---

## 初始化 promptfoo

第一步是使用以下指令初始化 promptfoo：

```bash
npx promptfoo@latest init
```

如同上一課所見，這會建立一個 `promptfooconfig.yaml` 檔案。我們可以刪除其中的現有內容。

接下來，我們要設定我們的 provider。將以下內容新增至 `promptfooconfig.yaml`：


```yaml
description: "Complaint Classification Eval"
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"
```

我們將使用 Claude 3 Haiku 來節省 API 費用，因為我們在本課程中會多次執行此評估。

**請確保您已設定 `ANTHROPIC_API_KEY` 環境變數。您可以在終端機中執行以下指令來設定環境變數：**

```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

---

---

## 準備提示

接下來，我們要收集提示並確保 promptfoo 知道這些提示的存在。我們將沿用前一段影片中看到的相同模式：

- 將每個提示寫成一個 Python 函式。
- 每個提示函式都會回傳一個提示字串。
- 所有提示函式都存放在 `prompts.py` 檔案中。

建立一個名為 `prompts.py` 的新檔案，並將以下提示函式加入該檔案。這是我們在原始投訴分類課程中撰寫的兩個提示：


```py
def basic_prompt(complaint):
    return f"""
    Classify the following customer complaint into one or more of these categories: 
    Software Bug, Hardware Malfunction, User Error, Feature Request, or Service Outage.
    Only respond with the classification.

    Complaint: {complaint}

    Classification:
    """

def improved_prompt(complaint):
    return f"""
    You are an AI assistant specializing in customer support issue classification. Your task is to analyze customer complaints and categorize them into one or more of the following categories:

    1. Software Bug: Issues related to software not functioning as intended.
    2. Hardware Malfunction: Problems with physical devices or components.
    3. User Error: Difficulties arising from user misunderstanding or misuse.
    4. Feature Request: Suggestions for new functionalities or improvements.
    5. Service Outage: System-wide issues affecting service availability.

    Important Guidelines:
    - A complaint may fall into multiple categories. If so, list all that apply but try to prioritize picking a single category when possible.

    Examples:
    1. Complaint: "The app crashes when I try to save my progress."
    Classification: Software Bug

    2. Complaint: "My keyboard isn't working after I spilled coffee on it."
    Classification: Hardware Malfunction

    3. Complaint: "I can't find the login button on your website."
    Classification: User Error

    4. Complaint: "It would be great if your app had a dark mode."
    Classification: Feature Request

    5. Complaint: "None of your services are loading for me or my colleagues."
    Classification: Service Outage

    6. Complaint "Complaint: The app breaks every time I try to change my profile picture"
    Classification: Software Bug

    7. Complaint "The app is acting buggy on my phone and it seems like your website is down, so I'm completely stuck!"
    Classification: Software Bug, Service Outage

    8. Complaint: "Your software makes my computer super laggy and awful, I hate it!"
    Classification: Software Bug

    9. Complaint: "Your dumb app always breaks when I try to do anything with images."
    Classification: 'Software Bug'

    Now, please classify the following customer complaint:

    <complaint>{complaint}</complaint>

    Only respond with the appropriate categories and nothing else.
    Classification:
    """
```


接下來，我們需要告訴 promptfoo 我們要使用這兩個提示。更新 `promptfooconfig.yaml` 檔案：

```yaml
description: "Complaint Classification Eval"

prompts:
  - prompts.py:basic_prompt
  - prompts.py:improved_prompt
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"
```

---


---

## 準備評估測試資料集

最後一步是將我們的評估資料集整理成 promptfoo 相容的格式。提醒一下，這是我們在先前課程中使用的原始 `eval_data` Python 清單：

```py
eval_data = [
    {
        "complaint": "The app crashes every time I try to upload a photo",
        "golden_answer": ["Software Bug"]
    },
    {
        "complaint": "My printer isn't recognized by my computer",
        "golden_answer": ["Hardware Malfunction"]
    },
    {
        "complaint": "I can't figure out how to change my password",
        "golden_answer": ["User Error"]
    },
    {
        "complaint": "The website is completely down, I can't access any pages",
        "golden_answer": ["Service Outage"]
    },
    {
        "complaint": "It would be great if the app had a dark mode option",
        "golden_answer": ["Feature Request"]
    },
    {
        "complaint": "The software keeps freezing when I try to save large files",
        "golden_answer": ["Software Bug"]
    },
    {
        "complaint": "My wireless mouse isn't working, even with new batteries",
        "golden_answer": ["Hardware Malfunction"]
    },
    {
        "complaint": "I accidentally deleted some important files, can you help me recover them?",
        "golden_answer": ["User Error"]
    },
    {
        "complaint": "None of your servers are responding, is there an outage?",
        "golden_answer": ["Service Outage"]
    },
    {
        "complaint": "Could you add a feature to export data in CSV format?",
        "golden_answer": ["Feature Request"]
    },
    {
        "complaint": "The app is crashing and my phone is overheating",
        "golden_answer": ["Software Bug", "Hardware Malfunction"]
    },
    {
        "complaint": "I can't remember my password!",
        "golden_answer": ["User Error"]
    },
    {
        "complaint": "The new update broke something and the app no longer works for me",
        "golden_answer": ["Software Bug"]
    },
    {
        "complaint": "I think I installed something incorrectly, now my computer won't start at all",
        "golden_answer": ["User Error", "Hardware Malfunction"]
    },
    {
        "complaint": "Your service is down, and I urgently need a feature to batch process files",
        "golden_answer": ["Service Outage", "Feature Request"]
    },
    {
        "complaint": "The graphics card is making weird noises",
        "golden_answer": ["Hardware Malfunction"]
    },
    {
        "complaint": "My keyboard just totally stopped working out of nowhere",
        "golden_answer": ["Hardware Malfunction"]
    },
    {
        "complaint": "Whenever I open your app, my phone gets really slow",
        "golden_answer": ["Software Bug"]
    },
    {
        "complaint": "Can you make the interface more user-friendly? I always get lost in the menus",
        "golden_answer": ["Feature Request", "User Error"]
    },
    {
        "complaint": "The cloud storage isn't syncing and I can't access my files from other devices",
        "golden_answer": ["Software Bug", "Service Outage"]
    }
]
```

---

如同上一課所做的，我們將把資料集轉換為 CSV 檔案。這裡的關鍵差異在於，我們的評估邏輯不再是簡單的完全比對。為了評分，我們希望 promptfoo 確保每個模型輸出都包含正確的分類結果。

舉例來說，給定資料集中的這一筆資料：

```py
{
    "complaint": "The cloud storage isn't syncing and I can't access my files from other devices",
    "golden_answer": ["Software Bug", "Service Outage"]
}
```

我們要撰寫一個提示，接收這個輸入 `complaint`：

>The cloud storage isn't syncing and I can't access my files from other devices

對於上述範例，我們需要 promptfoo 確認模型的回應中包含「Software Bug」和「Service Outage」。我們無法使用完全比對。如果模型輸出兩個分類的順序不同怎麼辦？所幸，promptfoo 內建了許多斷言（assertion）供我們使用。這些斷言包括：

* `contains` - 輸出包含子字串
* `contains-all` - 輸出包含清單中的所有子字串
* `contains-any` - 輸出包含清單中的任意子字串
* `contains-json` - 輸出包含有效的 JSON（可選 JSON schema 驗證）
* `contains-sql` - 輸出包含有效的 SQL
* `contains-xml` - 輸出包含有效的 XML
* `equals` - 輸出完全匹配
* `icontains` - 輸出包含子字串（不區分大小寫）
* `icontains-all` - 輸出包含清單中的所有子字串（不區分大小寫）
* `icontains-any` - 輸出包含清單中的任意子字串（不區分大小寫）
* `regex` - 輸出符合正規表達式
* 以及許多其他選項

[在這裡查看完整的內建指標清單。](https://www.promptfoo.dev/docs/configuration/expected-outputs/deterministic/)

針對我們的使用情境，我們將使用 `contains-all` 來確保給定的輸出包含所有適當的分類標籤。

載入並結構化 promptfoo 評估資料集的一種方式是透過 CSV。如我們先前所見，可以在 CSV 中提供一個名為 `__expected` 的特殊欄位名稱來指定評分邏輯。在這個欄位中，我們可以使用上述任何內建斷言，包括 `contains-all`。


---

建立一個名為 `dataset.csv` 的新檔案，並將以下程式碼貼入：

```csv
complaint,__expected
The app crashes every time I try to upload a photo,contains-all:Software Bug
My printer isn't recognized by my computer,contains-all:Hardware Malfunction
I can't figure out how to change my password,contains-all:User Error
The website is completely down I can't access any pages,contains-all:Service Outage
It would be great if the app had a dark mode option,contains-all:Feature Request
The software keeps freezing when I try to save large files,contains-all:Software Bug
My wireless mouse isn't working even with new batteries,contains-all:Hardware Malfunction
I accidentally deleted some important files can you help me recover them?,contains-all:User Error
None of your servers are responding is there an outage?,contains-all:Service Outage
Could you add a feature to export data in CSV format?,contains-all:Feature Request
"The app is crashing and my phone is overheating","contains-all:Software Bug,Hardware Malfunction"
I can't remember my password!,contains-all:User Error
The new update broke something and the app no longer works for me,contains-all:Software Bug
"I think I installed something incorrectly now my computer won't start at all","contains-all:User Error,Hardware Malfunction"
"Your service is down and I urgently need a feature to batch process files","contains-all:Service Outage,Feature Request"
The graphics card is making weird noises,contains-all:Hardware Malfunction
My keyboard just totally stopped working out of nowhere,contains-all:Hardware Malfunction
Whenever I open your app my phone gets really slow,contains-all:Software Bug
Can you make the interface more user-friendly? I always get lost in the menus,"contains-all:Feature Request,User Error"
The cloud storage isn't syncing and I can't access my files from other devices,"contains-all:Software Bug,Service Outage"
```

我們的 CSV 包含兩個欄位：
- `complaint` - 實際輸入的投訴內容
- `__expected` - 包含 `contains-all` 斷言

看一下其中一列，例如：

> "Your service is down and I urgently need a feature to batch process files","contains-all:Service Outage,Feature Request"

這列資料集指定：給定輸入「Your service is down and I urgently need a feature to batch process files」，我們希望 promptfoo 檢查模型的輸出，確保它同時包含「Service Outage」和「Feature Request」。


最後一步是更新 `promptfooconfig.yaml` 檔案，加入我們剛剛撰寫的測試。該檔案現在應如下所示：

```yaml
description: "Complaint Classification Eval"

prompts:
  - prompts.py:basic_prompt
  - prompts.py:improved_prompt
  
providers:
  - "anthropic:messages:claude-3-haiku-20240307"

tests: dataset.csv

```

---

---

## 執行評估

要執行評估，我們使用與之前相同的指令：

```bash
npx promptfoo@latest eval
```

---

以下是我們第一次執行上述評估時得到的輸出：

![eval_output.png](images/eval_output.png)

很明顯，包含範例的改良版提示比我們最初的基本提示表現更好。範例幫助模型理解在哪些情況下我們希望輸出包含多個分類：

![output_row.png](images/output_row.png)

---

如同以往，我們也可以使用以下指令開啟評估結果的互動式網頁介面：

```bash
npx promptfoo@latest view
```

![web_view.png](images/web_view.png)

---

我們可以看到 `basic_prompt` 得到了 80% 的正確率，而 `improved_prompt` 則達到了 100%。

**如同以往，請記住我們使用的是小型教育資料集，不代表真實世界的評估情況。我們強烈建議評估資料集至少包含 100 列。**

接下來，我們將學習如何在 promptfoo 中撰寫自訂評分邏輯！
