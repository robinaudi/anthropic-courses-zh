# 第 2 章：清晰直接表達

- [課程](#課程)
- [練習](#練習)
- [範例遊樂場](#範例遊樂場)

## 設定

執行以下設定儲存格以載入您的 API 金鑰並建立 `get_completion` 協助函式。

```python
%pip install anthropic

# 匯入 Python 的內建正規表達式庫
import re
import anthropic

# 從 IPython store 中取回 API_KEY 與 MODEL_NAME 變數
%store -r API_KEY
%store -r MODEL_NAME

client = anthropic.Anthropic(api_key=API_KEY)

# 注意，在本課程中我們將 max_tokens 變更為 4K，以允許練習中有較長的完成
def get_completion(prompt: str, system_prompt=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4000,
        temperature=0.0,
        system=system_prompt,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
```

---

## 課程

**Claude 對清晰和直接的指令反應最佳。**

把 Claude 當作任何新進工作的人類。**Claude 除了您直接告訴它的以外，沒有任何背景知訊**。就像您第一次指導人類完成任務時一樣，您越詳細地用直接的方式解釋您想要什麼，Claude 的回應就越好越準確。

當有疑問時，遵循**清晰提示的黃金法則**：
- 向同事或朋友展示您的提示，讓他們按照指令完成來看他們能否產生您想要的結果。如果他們感到困惑，Claude 也會感到困惑。

### 範例

讓我們以詩歌創作為例。（忽略任何音節不匹配 - LLM 還不太善於計算音節。）

```python
# 提示
PROMPT = "Write a haiku about robots."

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

這首俳句不錯，但使用者可能想讓 Claude 直接進入詩歌，而不是「這是一首俳句」的前言。

我們如何實現這一點？我們**要求它**！

```python
# 提示
PROMPT = "Write a haiku about robots. Skip the preamble; go straight into the poem."

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

還有另一個例子。讓我們問 Claude 誰是有史以來最偉大的籃球運動員。您可以看到，雖然 Claude 列出了幾個名字，但**它沒有用明確的「最佳」來回應**。

```python
# 提示
PROMPT = "Who is the best basketball player of all time?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

我們可以讓 Claude 下定決心並決定最佳選手嗎？當然！只需要求它！

```python
# 提示
PROMPT = "Who is the best basketball player of all time? Yes, there are differing opinions, but if you absolutely had to pick one player, who would it be?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

如果您想在不更改上述任何內容的情況下實驗課程提示，請向下捲動到本課程筆記本底部以造訪[**範例遊樂場**](#範例遊樂場)。

---

## 練習
- [練習 2.1 - 西班牙語](#練習-21---西班牙語)
- [練習 2.2 - 僅一名選手](#練習-22---僅一名選手)
- [練習 2.3 - 撰寫故事](#練習-23---撰寫故事)

### 練習 2.1 - 西班牙語
修改 `SYSTEM_PROMPT` 使 Claude 以西班牙語輸出其答案。

```python
# 系統提示 - 這是您應該變更的唯一欄位
SYSTEM_PROMPT = "[Replace this text]"

# 提示
PROMPT = "Hello Claude, how are you?"

# 取得 Claude 的回應
response = get_completion(PROMPT, SYSTEM_PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    return "hola" in text.lower()

# 列印 Claude 的回應與相應的分級
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_2_1_hint; print(exercise_2_1_hint)
```

### 練習 2.2 - 僅一名選手

修改 `PROMPT` 使 Claude 完全不含糊地回應，**僅**包含一個特定選手的名稱，**不包含其他單詞或標點符號**。

```python
# 提示 - 這是您應該變更的唯一欄位
PROMPT = "[Replace this text]"

# 取得 Claude 的回應
response = get_completion(PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    return text == "Michael Jordan"

# 列印 Claude 的回應與相應的分級
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_2_2_hint; print(exercise_2_2_hint)
```

### 練習 2.3 - 撰寫故事

修改 `PROMPT` 使 Claude 以盡可能長的回應做出回應。如果您的答案**超過 800 個單詞**，Claude 的回應將被評分為正確。

```python
# 提示 - 這是您應該變更的唯一欄位
PROMPT = "[Replace this text]"

# 取得 Claude 的回應
response = get_completion(PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    trimmed = text.strip()
    words = len(trimmed.split())
    return words >= 800

# 列印 Claude 的回應與相應的分級
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_2_3_hint; print(exercise_2_3_hint)
```

### 恭喜！

如果您已解決到此為止的所有練習，您已準備好進入下一章。祝您提示工程愉快！

---

## 範例遊樂場

這是一個區域，供您自由試驗本課程所示的提示範例，並調整提示以查看它如何影響 Claude 的回應。

```python
# 提示
PROMPT = "Write a haiku about robots."

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "Write a haiku about robots. Skip the preamble; go straight into the poem."

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "Who is the best basketball player of all time?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "Who is the best basketball player of all time? Yes, there are differing opinions, but if you absolutely had to pick one player, who would it be?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```
