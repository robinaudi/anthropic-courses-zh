# 第 3 章：指派角色（角色提示法）

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

def get_completion(prompt: str, system_prompt=""):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
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

延續 Claude 除了您直接告訴它的以外沒有背景的主題，有時重要的是**提示 Claude 進行特定角色（包括所有必要的背景）**。這也稱為角色提示法。背景資訊越詳細越好。

**使用角色提示為 Claude 建立基礎可以在多個領域改善 Claude 的效能**，從寫作到編碼再到總結。就像人類有時被告訴「像 ________ 一樣思考」時可以受到幫助一樣。角色提示法還可以改變 Claude 回應的風格、語氣和方式。

**注意：** 角色提示可以在系統提示或使用者訊息輪次中進行。

### 範例

在下面的範例中，我們看到在沒有角色提示的情況下，Claude 在被要求用一句話給出滑板的看法時提供了**直接和非風格化的答案**。

但是，當我們為 Claude 設置一個貓的角色時，Claude 的視角會改變，因此**Claude 的回應語氣、風格、內容會適應新角色**。

**注意：** 您可以使用的一種獎勵技巧是**為 Claude 提供關於其預期對象的背景**。下面，我們可以調整提示以告訴 Claude 與誰溝通。「你是一隻貓」產生的回應與「你是一隻在向滑冰者人群說話的貓」完全不同。

以下是系統提示中沒有角色提示的提示：

```python
# 提示
PROMPT = "In one sentence, what do you think about skateboarding?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

這是同一使用者提問，除了使用角色提示。

```python
# 系統提示
SYSTEM_PROMPT = "You are a cat."

# 提示
PROMPT = "In one sentence, what do you think about skateboarding?"

# 列印 Claude 的回應
print(get_completion(PROMPT, SYSTEM_PROMPT))
```

您可以使用角色提示作為一種方式讓 Claude 模擬寫作中的某些風格，用特定的聲音說話，或指導其答案的複雜性。**角色提示法也可以使 Claude 更善於執行數學或邏輯任務。**

例如，在下面的範例中，有明確的正確答案，即是的。但是**Claude 理解錯了，認為它缺少信息，而它沒有**：

```python
# 提示
PROMPT = "Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

現在，如果我們**為 Claude 設置邏輯機器人的角色**會發生什麼呢？這將如何改變 Claude 的答案？

事實證明，使用這個新角色指派，Claude 得到了正確的答案。（雖然不一定出於所有正確的原因）

```python
# 系統提示
SYSTEM_PROMPT = "You are a logic bot designed to answer complex logic problems."

# 提示
PROMPT = "Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?"

# 列印 Claude 的回應
print(get_completion(PROMPT, SYSTEM_PROMPT))
```

**注意：** 在本課程中您會學到的是，有**許多提示工程技巧可用來獲得類似的結果**。您使用哪些技巧取決於您的偏好！我們鼓勵您**實驗以找到您自己的提示工程風格**。

如果您想在不更改上述任何內容的情況下實驗課程提示，請向下捲動到本課程筆記本底部以造訪[**範例遊樂場**](#範例遊樂場)。

---

## 練習
- [練習 3.1 - 數學修正](#練習-31---數學修正)

### 練習 3.1 - 數學修正
在某些情況下，**Claude 可能在數學上遇到困難**，即使是簡單的數學。下面，Claude 不正確地將數學問題評估為正確解決，儘管第二步中有明顯的算術錯誤。請注意，Claude 實際上在逐步進行時確實發現了錯誤，但並未跳到得出整體解決方案是錯誤的結論。

修改 `PROMPT` 和/或 `SYSTEM_PROMPT` 使 Claude 將解決方案評分為**不正確**解決，而不是正確解決。

```python
# 系統提示 - 如果您不想使用系統提示，可以將此變數留為空字串
SYSTEM_PROMPT = ""

# 提示
PROMPT = """Is this equation solved correctly below?

2x - 3 = 9
2x = 6
x = 3"""

# 取得 Claude 的回應
response = get_completion(PROMPT, SYSTEM_PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    if "incorrect" in text or "not correct" in text.lower():
        return True
    else:
        return False

# 列印 Claude 的回應與相應的分級
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_3_1_hint; print(exercise_3_1_hint)
```

### 恭喜！

如果您已解決到此為止的所有練習，您已準備好進入下一章。祝您提示工程愉快！

---

## 範例遊樂場

這是一個區域，供您自由試驗本課程所示的提示範例，並調整提示以查看它如何影響 Claude 的回應。

```python
# 提示
PROMPT = "In one sentence, what do you think about skateboarding?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 系統提示
SYSTEM_PROMPT = "You are a cat."

# 提示
PROMPT = "In one sentence, what do you think about skateboarding?"

# 列印 Claude 的回應
print(get_completion(PROMPT, SYSTEM_PROMPT))
```

```python
# 提示
PROMPT = "Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 系統提示
SYSTEM_PROMPT = "You are a logic bot designed to answer complex logic problems."

# 提示
PROMPT = "Jack is looking at Anne. Anne is looking at George. Jack is married, George is not, and we don't know if Anne is married. Is a married person looking at an unmarried person?"

# 列印 Claude 的回應
print(get_completion(PROMPT, SYSTEM_PROMPT))
```
