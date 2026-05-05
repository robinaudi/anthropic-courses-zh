# 程式碼評分評估：分類任務

本課程將從頭實作一個稍微複雜的程式碼評分評估，用來測試客戶投訴分類提示詞。我們的目標是撰寫一個能可靠地將客戶投訴分類到以下類別的提示詞：

* Software Bug（軟體錯誤）
* Hardware Malfunction（硬體故障）
* User Error（用戶操作錯誤）
* Feature Request（功能需求）
* Service Outage（服務中斷）

例如，以下投訴文字：

> The website is completely down, I can't access any pages

應分類為 `Service Outage`

在某些情況下，我們可能允許最多兩個適用的分類類別，例如：

> I think I installed something incorrectly, and now my computer won't start at all

應同時分類為 `User Error` 和 `Hardware Malfunction`

---


---

## 評估資料集

首先定義包含輸入和黃金答案的評估資料集。請記得，理想的評估資料集通常需要約 100 筆輸入，但為了讓這些課程保持簡單（同時快速且經濟實惠），我們使用了精簡版的資料集。

這個測試集由字典列表組成，每個字典包含 `complaint` 和 `golden_answer` 兩個鍵：

---

```python
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

--- 

## 初版提示詞

我們從一個基礎提示詞開始，衡量其表現。以下提示詞生成函式接收 `complaint` 作為引數，並返回提示詞字串：

---

```python
def basic_prompt(complaint):
    return f"""
    Classify the following customer complaint into one or more of these categories: 
    Software Bug, Hardware Malfunction, User Error, Feature Request, or Service Outage.
    Only respond with the matching category or categories and nothing else.

    Complaint: {complaint}

    Classification:
    """
```

---

---

## 收集輸出

接下來撰寫評估提示詞的邏輯。這個邏輯比前一課程的「腿數計算」範例稍微複雜：

---

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def get_model_response(prompt, model_name):
    response = client.messages.create(
        model=model_name,
        max_tokens=200,
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.content[0].text

def calculate_accuracy(eval_data, model_responses):
    correct_predictions = 0
    total_predictions = len(eval_data)
    
    for item, response in zip(eval_data, model_responses):
        golden_set = set(category.lower() for category in item["golden_answer"])
        prediction_set = set(category.strip().lower() for category in response.split(','))
        
        if golden_set == prediction_set:
            correct_predictions += 1
    
    return correct_predictions / total_predictions

def evaluate_prompt(prompt_func, eval_data, model_name):
    print(f"Evaluating with model: {model_name}")
    model_responses = [get_model_response(prompt_func(item['complaint']), model_name) for item in eval_data]
    accuracy = calculate_accuracy(eval_data, model_responses)
    
    print(f"Accuracy: {accuracy:.2%}")
    
    for item, response in zip(eval_data, model_responses):
        print(f"\nComplaint: {item['complaint']}")
        print(f"Golden Answer: {item['golden_answer']}")
        print(f"Model Response: {response}")
    return accuracy
```

---

`evaluate_prompt` 函式的運作流程如下：

1. 將每個輸入傳入提示詞生成函式，使用 `get_model_response` 函式將結果提示詞執行於模型，並在產生時收集回應。
2. 透過比較模型輸出答案與資料集中的黃金答案來計算準確率，為此呼叫 `calculate_accuracy` 函式。
3. `calculate_accuracy` 函式使用 `set` 來檢查模型輸出中是否存在正確的分類類別。請記得，這不像前一課程的「腿數計算」評估那樣使用精確字串比對。
4. `calculate_accuracy` 返回準確率分數
5. `evaluate_prompt` 印出最終結果

**請注意，與前一課程使用精確字串比對不同，我們的評分邏輯使用 `set` 來檢查模型輸出中是否存在特定值。**

---

用初版 `basic_prompt` 測試：

---

```python
evaluate_prompt(basic_prompt, eval_data, model_name="claude-3-haiku-20240307")
```

---

```
Evaluating with model: claude-3-haiku-20240307
Accuracy: 85.00%

Complaint: The app crashes every time I try to upload a photo
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: My printer isn't recognized by my computer
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: I can't figure out how to change my password
Golden Answer: ['User Error']
Model Response: User Error

Complaint: The website is completely down, I can't access any pages
Golden Answer: ['Service Outage']
Model Response: Service Outage

Complaint: It would be great if the app had a dark mode option
Golden Answer: ['Feature Request']
Model Response: Feature Request

Complaint: The software keeps freezing when I try to save large files
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: My wireless mouse isn't working, even with new batteries
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: I accidentally deleted some important files, can you help me recover them?
Golden Answer: ['User Error']
Model Response: User Error

Complaint: None of your servers are responding, is there an outage?
Golden Answer: ['Service Outage']
Model Response: Service Outage

Complaint: Could you add a feature to export data in CSV format?
Golden Answer: ['Feature Request']
Model Response: Feature Request

Complaint: The app is crashing and my phone is overheating
Golden Answer: ['Software Bug', 'Hardware Malfunction']
Model Response: Hardware Malfunction
Software Bug

Complaint: I can't remember my password!
Golden Answer: ['User Error']
Model Response: User Error

Complaint: The new update broke something and the app no longer works for me
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: I think I installed something incorrectly, now my computer won't start at all
Golden Answer: ['User Error', 'Hardware Malfunction']
Model Response: User Error, Hardware Malfunction

Complaint: Your service is down, and I urgently need a feature to batch process files
Golden Answer: ['Service Outage', 'Feature Request']
Model Response: Feature Request, Service Outage

Complaint: The graphics card is making weird noises
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: My keyboard just totally stopped working out of nowhere
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: Whenever I open your app, my phone gets really slow
Golden Answer: ['Software Bug']
Model Response: Hardware Malfunction

Complaint: Can you make the interface more user-friendly? I always get lost in the menus
Golden Answer: ['Feature Request', 'User Error']
Model Response: Feature Request

Complaint: The cloud storage isn't syncing and I can't access my files from other devices
Golden Answer: ['Software Bug', 'Service Outage']
Model Response: Software Bug, Service Outage
```

```
0.85
```

---

---

## 改良版提示詞
初版提示詞的準確率為 85%。讓我們對提示詞進行修改，重新執行評估，期望獲得更好的分數。

以下改良版提示詞加入了對各類別的詳細說明，以及 9 組輸入/輸出範例：

---

```python
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

---

用改良版提示詞執行評估：

---

```python
evaluate_prompt(improved_prompt, eval_data, model_name="claude-3-haiku-20240307")
```

---

```
Evaluating with model: claude-3-haiku-20240307
Accuracy: 100.00%

Complaint: The app crashes every time I try to upload a photo
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: My printer isn't recognized by my computer
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: I can't figure out how to change my password
Golden Answer: ['User Error']
Model Response: User Error

Complaint: The website is completely down, I can't access any pages
Golden Answer: ['Service Outage']
Model Response: Service Outage

Complaint: It would be great if the app had a dark mode option
Golden Answer: ['Feature Request']
Model Response: Feature Request

Complaint: The software keeps freezing when I try to save large files
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: My wireless mouse isn't working, even with new batteries
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: I accidentally deleted some important files, can you help me recover them?
Golden Answer: ['User Error']
Model Response: User Error

Complaint: None of your servers are responding, is there an outage?
Golden Answer: ['Service Outage']
Model Response: Service Outage

Complaint: Could you add a feature to export data in CSV format?
Golden Answer: ['Feature Request']
Model Response: Feature Request

Complaint: The app is crashing and my phone is overheating
Golden Answer: ['Software Bug', 'Hardware Malfunction']
Model Response: Software Bug, Hardware Malfunction

Complaint: I can't remember my password!
Golden Answer: ['User Error']
Model Response: User Error

Complaint: The new update broke something and the app no longer works for me
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: I think I installed something incorrectly, now my computer won't start at all
Golden Answer: ['User Error', 'Hardware Malfunction']
Model Response: Hardware Malfunction, User Error

Complaint: Your service is down, and I urgently need a feature to batch process files
Golden Answer: ['Service Outage', 'Feature Request']
Model Response: Service Outage, Feature Request

Complaint: The graphics card is making weird noises
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: My keyboard just totally stopped working out of nowhere
Golden Answer: ['Hardware Malfunction']
Model Response: Hardware Malfunction

Complaint: Whenever I open your app, my phone gets really slow
Golden Answer: ['Software Bug']
Model Response: Software Bug

Complaint: Can you make the interface more user-friendly? I always get lost in the menus
Golden Answer: ['Feature Request', 'User Error']
Model Response: User Error, Feature Request

Complaint: The cloud storage isn't syncing and I can't access my files from other devices
Golden Answer: ['Software Bug', 'Service Outage']
Model Response: Software Bug, Service Outage
```

```
1.0
```

---

使用改良版提示詞，我們達到了 100% 的準確率！

我們再次遵循了下圖所示的標準提示詞加評估迭代流程：

![process.png](images/process.png)

**請記住，這是一個使用非常小型資料集的簡單評估。本課程旨在說明程式碼評分評估的一般流程，並非正式生產級評估的標準範例！**

這種方法確實可行，但從頭撰寫所有評估邏輯相當費力，且難以並排比較結果。如果有一個工具能產生格式精美的圖表和圖形，並讓跨多個模型執行評估變得輕鬆，那會如何？下一課程我們就來看看這個工具！接下來，我們將介紹一個評估框架，讓你輕鬆撰寫可重複執行、可擴展的正式生產評估。
