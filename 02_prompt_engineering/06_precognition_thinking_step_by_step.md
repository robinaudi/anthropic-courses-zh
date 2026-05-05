# 第六章：預認知（逐步思考）

- [課程內容](#lesson)
- [練習題](#exercises)
- [範例練習場](#example-playground)

## 環境設定

執行以下設定儲存格，載入您的 API 金鑰並建立 `get_completion` 輔助函式。

```python
%pip install anthropic

# Import python's built-in regular expression library
import re
import anthropic

# Retrieve the API_KEY & MODEL_NAME variables from the IPython store
%store -r API_KEY
%store -r MODEL_NAME

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str, system_prompt="", prefill=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt},
          {"role": "assistant", "content": prefill}
        ]
    )
    return message.content[0].text
```

---

## 課程內容

如果有人將您從睡夢中叫醒，立刻要求您回答幾個複雜問題，您的表現會如何？大概不如先給您**一些時間思考答案**後那麼好。

猜猜怎麼著？Claude 也是一樣的。

**讓 Claude 逐步思考，有時能讓 Claude 的答案更準確**，尤其在面對複雜任務時。然而，**思考必須公開表達才算數**。您不能要求 Claude 思考但只輸出答案——在這種情況下，實際上根本沒有發生任何思考。

### 範例

在下方的提示詞中，人類讀者很清楚第二句話否定了第一句。但 **Claude 把「無關」（unrelated）這個詞理解得太過字面**。

```python
# Prompt
PROMPT = """Is this movie review sentiment positive or negative?

This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since the year 1900."""

# Print Claude's response
print(get_completion(PROMPT))
```

為了改善 Claude 的回應，讓我們**允許 Claude 在回答前先思考一番**。我們透過明確列出 Claude 應該依序執行的步驟來做到這一點，搭配一點角色提示，讓 Claude 能更深入地理解這則評論。

```python
# System prompt
SYSTEM_PROMPT = "You are a savvy reader of movie reviews."

# Prompt
PROMPT = """Is this review sentiment positive or negative? First, write the best arguments for each side in <positive-argument> and <negative-argument> XML tags, then answer.

This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since 1900."""

# Print Claude's response
print(get_completion(PROMPT, SYSTEM_PROMPT))
```

**Claude 有時對順序很敏感**。這個範例處於 Claude 理解細膩文本能力的邊界，當我們將上例的論點順序對調，改成負面論點在前、正面論點在後時，Claude 的整體判斷就會轉為正面。

在大多數情況下（但並非所有情況），**Claude 更傾向選擇兩個選項中的第二個**，這可能是因為在它訓練所用的網路資料中，第二個選項往往更有可能是正確答案。

```python
# Prompt
PROMPT = """Is this review sentiment negative or positive? First write the best arguments for each side in <negative-argument> and <positive-argument> XML tags, then answer.

This movie blew my mind with its freshness and originality. Unrelatedly, I have been living under a rock since 1900."""

# Print Claude's response
print(get_completion(PROMPT))
```

**讓 Claude 思考可以將錯誤的答案糾正為正確的答案**。在許多 Claude 出錯的情況下，就是這麼簡單！

讓我們來看一個 Claude 答錯的例子，觀察如何透過要求 Claude 思考來修正錯誤。

```python
# Prompt
PROMPT = "Name a famous movie starring an actor who was born in the year 1956."

# Print Claude's response
print(get_completion(PROMPT))
```

讓我們透過要求 Claude 逐步思考來修正這個問題，這次使用 `<brainstorm>` 標籤。

```python
# Prompt
PROMPT = "Name a famous movie starring an actor who was born in the year 1956. First brainstorm about some actors and their birth years in <brainstorm> tags, then give your answer."

# Print Claude's response
print(get_completion(PROMPT))
```

若您想在不更改上方任何內容的情況下試驗課程提示詞，請捲動到筆記本最底部，前往[**範例練習場**](#example-playground)。

---

## 練習題
- [練習 6.1 - 電子郵件分類](#exercise-61---classifying-emails)
- [練習 6.2 - 電子郵件分類格式化](#exercise-62---email-classification-formatting)

### 練習 6.1 - 電子郵件分類
在本練習中，我們將指示 Claude 將電子郵件分類到以下類別：
- (A) 售前問題
- (B) 損壞或有缺陷的商品
- (C) 帳單問題
- (D) 其他（請說明）

練習的第一部分，修改 `PROMPT`，讓 **Claude 只輸出正確的分類標籤**。您的答案需要**包含正確選項的字母（A 到 D），並附帶括號，以及分類名稱**。

請參考 `EMAILS` 清單中每封電子郵件旁邊的備註，以確認各封電子郵件應歸屬的類別。

```python
# Prompt template with a placeholder for the variable content
PROMPT = """Please classify this email as either green or blue: {email}"""

# Prefill for Claude's response, if any
PREFILL = ""

# Variable content stored as a list
EMAILS = [
    "Hi -- My Mixmaster4000 is producing a strange noise when I operate it. It also smells a bit smoky and plasticky, like burning electronics.  I need a replacement.", # (B) Broken or defective item
    "Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?", # (A) Pre-sale question OR (D) Other (please explain)
    "I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???", # (C) Billing question
    "How did I get here I am not good with computer.  Halp." # (D) Other (please explain)
]

# Correct categorizations stored as a list of lists to accommodate the possibility of multiple correct categorizations per email
ANSWERS = [
    ["B"],
    ["A","D"],
    ["C"],
    ["D"]
]

# Dictionary of string values for each category to be used for regex grading
REGEX_CATEGORIES = {
    "A": "A\) P",
    "B": "B\) B",
    "C": "C\) B",
    "D": "D\) O"
}

# Iterate through list of emails
for i,email in enumerate(EMAILS):
    
    # Substitute the email text into the email placeholder variable
    formatted_prompt = PROMPT.format(email=email)
   
    # Get Claude's response
    response = get_completion(formatted_prompt, prefill=PREFILL)

    # Grade Claude's response
    grade = any([bool(re.search(REGEX_CATEGORIES[ans], response)) for ans in ANSWERS[i]])
    
    # Print Claude's response
    print("--------------------------- Full prompt with variable substutions ---------------------------")
    print("USER TURN")
    print(formatted_prompt)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print("\n------------------------------------- Claude's response -------------------------------------")
    print(response)
    print("\n------------------------------------------ GRADING ------------------------------------------")
    print("This exercise has been correctly solved:", grade, "\n\n\n\n\n\n")
```

❓ 若想要提示，請執行下方儲存格！

```python
from hints import exercise_6_1_hint; print(exercise_6_1_hint)
```

仍然卡住了嗎？執行下方儲存格查看範例解法。

```python
from hints import exercise_6_1_solution; print(exercise_6_1_solution)
```

### 練習 6.2 - 電子郵件分類格式化
在本練習中，我們將精修上述提示詞的輸出，使其格式完全符合我們的需求。

使用您最喜歡的輸出格式化技術，讓 Claude 將正確分類的字母（僅字母）包裹在 `<answer></answer>` 標籤中。例如，第一封電子郵件的答案應包含確切字串 `<answer>B</answer>`。

若您忘記每封電子郵件對應的正確字母類別，請參考 `EMAILS` 清單中各電子郵件旁邊的備註。

```python
# Prompt template with a placeholder for the variable content
PROMPT = """Please classify this email as either green or blue: {email}"""

# Prefill for Claude's response, if any
PREFILL = ""

# Variable content stored as a list
EMAILS = [
    "Hi -- My Mixmaster4000 is producing a strange noise when I operate it. It also smells a bit smoky and plasticky, like burning electronics.  I need a replacement.", # (B) Broken or defective item
    "Can I use my Mixmaster 4000 to mix paint, or is it only meant for mixing food?", # (A) Pre-sale question OR (D) Other (please explain)
    "I HAVE BEEN WAITING 4 MONTHS FOR MY MONTHLY CHARGES TO END AFTER CANCELLING!!  WTF IS GOING ON???", # (C) Billing question
    "How did I get here I am not good with computer.  Halp." # (D) Other (please explain)
]

# Correct categorizations stored as a list of lists to accommodate the possibility of multiple correct categorizations per email
ANSWERS = [
    ["B"],
    ["A","D"],
    ["C"],
    ["D"]
]

# Dictionary of string values for each category to be used for regex grading
REGEX_CATEGORIES = {
    "A": "<answer>A</answer>",
    "B": "<answer>B</answer>",
    "C": "<answer>C</answer>",
    "D": "<answer>D</answer>"
}

# Iterate through list of emails
for i,email in enumerate(EMAILS):
    
    # Substitute the email text into the email placeholder variable
    formatted_prompt = PROMPT.format(email=email)
   
    # Get Claude's response
    response = get_completion(formatted_prompt, prefill=PREFILL)

    # Grade Claude's response
    grade = any([bool(re.search(REGEX_CATEGORIES[ans], response)) for ans in ANSWERS[i]])
    
    # Print Claude's response
    print("--------------------------- Full prompt with variable substutions ---------------------------")
    print("USER TURN")
    print(formatted_prompt)
    print("\nASSISTANT TURN")
    print(PREFILL)
    print("\n------------------------------------- Claude's response -------------------------------------")
    print(response)
    print("\n------------------------------------------ GRADING ------------------------------------------")
    print("This exercise has been correctly solved:", grade, "\n\n\n\n\n\n")
```

❓ 若想要提示，請執行下方儲存格！

```python
from hints import exercise_6_2_hint; print(exercise_6_2_hint)
```

### 恭喜！

若您已完成目前為止的所有練習，您已準備好進入下一章。祝提示愉快！

---

## 範例練習場

此區域供您自由試驗本課程中展示的提示詞範例，調整提示詞以觀察對 Claude 回應的影響。

```python
# Prompt
PROMPT = """Is this movie review sentiment positive or negative?

This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since the year 1900."""

# Print Claude's response
print(get_completion(PROMPT))
```

```python
# System prompt
SYSTEM_PROMPT = "You are a savvy reader of movie reviews."

# Prompt
PROMPT = """Is this review sentiment positive or negative? First, write the best arguments for each side in <positive-argument> and <negative-argument> XML tags, then answer.

This movie blew my mind with its freshness and originality. In totally unrelated news, I have been living under a rock since 1900."""

# Print Claude's response
print(get_completion(PROMPT, SYSTEM_PROMPT))
```

```python
# Prompt
PROMPT = """Is this review sentiment negative or positive? First write the best arguments for each side in <negative-argument> and <positive-argument> XML tags, then answer.

This movie blew my mind with its freshness and originality. Unrelatedly, I have been living under a rock since 1900."""

# Print Claude's response
print(get_completion(PROMPT))
```

```python
# Prompt
PROMPT = "Name a famous movie starring an actor who was born in the year 1956."

# Print Claude's response
print(get_completion(PROMPT))
```

```python
# Prompt
PROMPT = "Name a famous movie starring an actor who was born in the year 1956. First brainstorm about some actors and their birth years in <brainstorm> tags, then give your answer."

# Print Claude's response
print(get_completion(PROMPT))
```
