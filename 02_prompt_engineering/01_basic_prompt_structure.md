# 第 1 章：基本提示結構

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

Anthropic 提供兩個 API，舊版的 [Text Completions API](https://docs.anthropic.com/claude/reference/complete_post) 與目前的 [Messages API](https://docs.anthropic.com/claude/reference/messages_post)。在本教學中，我們將專門使用 Messages API。

至少，呼叫 Claude 的 Messages API 需要以下參數：
- `model`：您要使用的模型的 [API 模型名稱](https://docs.anthropic.com/claude/docs/models-overview#model-recommendations)

- `max_tokens`：生成前停止的最大令牌數。請注意，Claude 可能會在達到此最大值之前停止。此參數僅指定要生成的絕對最大令牌數。此外，這是一個*硬*停止，意味著它可能會導致 Claude 在單詞或句子中途停止生成。

- `messages`：輸入訊息的陣列。我們的模型經過訓練可在交替的 `user` 與 `assistant` 對話輪次上運作。建立新 `Message` 時，您透過 messages 參數指定先前的對話輪次，然後模型生成對話中的下一個 `Message`。
  - 每個輸入訊息必須是具有 `role` 與 `content` 的物件。您可以指定單個 `user` 角色訊息，或可以包含多個 `user` 與 `assistant` 訊息（如果是這樣，它們必須交替）。第一個訊息必須始終使用 `user` 角色。

還有選用參數，例如：
- `system`：系統提示 — 稍後會詳細討論。
  
- `temperature`：Claude 回應中的變異程度。對於這些課程與練習，我們已將 `temperature` 設定為 0。

如需所有 API 參數的完整清單，請造訪我們的 [API 文檔](https://docs.anthropic.com/claude/reference/messages_post)。

### 範例

讓我們看看 Claude 如何回應某些格式正確的提示。對於以下每個儲存格，執行該儲存格（`shift+enter`），Claude 的回應將出現在區塊下方。

```python
# 提示
PROMPT = "Hi Claude, how are you?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "Can you tell me the color of the ocean?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "What year was Celine Dion born in?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

現在讓我們看一些不包含正確 Messages API 格式的提示。對於這些格式不正確的提示，Messages API 會傳回錯誤。

首先，我們有一個 Messages API 呼叫範例，其在 `messages` 陣列中缺少 `role` 與 `content` 欄位。

```python
# 取得 Claude 的回應
response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"Hi Claude, how are you?"}
        ]
    )

# 列印 Claude 的回應
print(response[0].text)
```

這是一個未能在 `user` 與 `assistant` 角色之間交替的提示。

```python
# 取得 Claude 的回應
response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"role": "user", "content": "What year was Celine Dion born in?"},
          {"role": "user", "content": "Also, can you tell me some other facts about her?"}
        ]
    )

# 列印 Claude 的回應
print(response[0].text)
```

`user` 與 `assistant` 訊息**必須交替**，訊息**必須以 `user` 輪次開始**。您可以有多個 `user` 與 `assistant` 對（如同模擬多輪對話）。您也可以在末尾 `assistant` 訊息中放入單詞，以便 Claude 從您停止的地方繼續（稍後章節會詳細討論）。

#### 系統提示

您也可以使用**系統提示**。系統提示是在向使用者提問或在「使用者」輪次中進行任務之前**向 Claude 提供背景、指令與準則**的一種方式。

在結構上，系統提示與 `user` 與 `assistant` 訊息清單分離，因此屬於單獨的 `system` 參數（查看設定部分中 `get_completion` 協助函式的結構）。

在本教學中，無論何時我們可能使用系統提示，我們都為您的完成函式提供了 `system` 欄位。如果您不想使用系統提示，只需將 `SYSTEM_PROMPT` 變數設定為空字串。

#### 系統提示範例

```python
# 系統提示
SYSTEM_PROMPT = "Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question."

# 提示
PROMPT = "Why is the sky blue?"

# 列印 Claude 的回應
print(get_completion(PROMPT, SYSTEM_PROMPT))
```

為什麼使用系統提示？**寫得好的系統提示可以以多種方式改善 Claude 的效能**，例如增強 Claude 遵循規則與指令的能力。如需更多資訊，請造訪我們的[如何使用系統提示](https://docs.anthropic.com/claude/docs/how-to-use-system-prompts)文檔。

現在我們將進行練習。如果您想在不更改上述任何內容的情況下實驗課程提示，請向下捲動到本課程筆記本底部以造訪[**範例遊樂場**](#範例遊樂場)。

---

## 練習
- [練習 1.1 - 數到三](#練習-11---數到三)
- [練習 1.2 - 系統提示](#練習-12---系統提示)

### 練習 1.1 - 數到三
使用適當的 `user` 與 `assistant` 格式，編輯下面的 `PROMPT` 以使 Claude **數到三**。輸出還會指示您的解決方案是否正確。

```python
# 提示 - 這是您應該變更的唯一欄位
PROMPT = "[Replace this text]"

# 取得 Claude 的回應
response = get_completion(PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    pattern = re.compile(r'^(?=.*1)(?=.*2)(?=.*3).*$', re.DOTALL)
    return bool(pattern.match(text))

# 列印 Claude 的回應與相應的分級
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_1_1_hint; print(exercise_1_1_hint)
```

### 練習 1.2 - 系統提示

修改 `SYSTEM_PROMPT` 使 Claude 的回應就像是 3 歲小孩。

```python
# 系統提示 - 這是您應該變更的唯一欄位
SYSTEM_PROMPT = "[Replace this text]"

# 提示
PROMPT = "How big is the sky?"

# 取得 Claude 的回應
response = get_completion(PROMPT, SYSTEM_PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    return bool(re.search(r"giggles", text) or re.search(r"soo", text))

# 列印 Claude 的回應與相應的分級
print(response)
print("\n--------------------------- GRADING ---------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_1_2_hint; print(exercise_1_2_hint)
```

### 恭喜！

如果您已解決到此為止的所有練習，您已準備好進入下一章。祝您提示工程愉快！

---

## 範例遊樂場

這是一個區域，供您自由試驗本課程所示的提示範例，並調整提示以查看它如何影響 Claude 的回應。

```python
# 提示
PROMPT = "Hi Claude, how are you?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "Can you tell me the color of the ocean?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 提示
PROMPT = "What year was Celine Dion born in?"

# 列印 Claude 的回應
print(get_completion(PROMPT))
```

```python
# 取得 Claude 的回應
response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"Hi Claude, how are you?"}
        ]
    )

# 列印 Claude 的回應
print(response[0].text)
```

```python
# 取得 Claude 的回應
response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"role": "user", "content": "What year was Celine Dion born in?"},
          {"role": "user", "content": "Also, can you tell me some other facts about her?"}
        ]
    )

# 列印 Claude 的回應
print(response[0].text)
```

```python
# 系統提示
SYSTEM_PROMPT = "Your answer should always be a series of critical thinking questions that further the conversation (do not provide answers to your questions). Do not actually answer the user question."

# 提示
PROMPT = "Why is the sky blue?"

# 列印 Claude 的回應
print(get_completion(PROMPT, SYSTEM_PROMPT))
```
