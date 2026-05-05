# 教學說明

本教學 **需要 API 金鑰** 才能進行互動。如果您還沒有 API 金鑰，可以透過 [Anthropic 主控台](https://console.anthropic.com/) 註冊，或查看我們的[靜態教學答案集](https://docs.google.com/spreadsheets/u/0/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit)。

## 如何開始

1. 將此 repository 複製到您的本機。

2. 執行以下命令安裝必需的相依性：
 

```python
%pip install anthropic
```

3. 設定您的 API 金鑰與模型名稱。將 `"your_api_key_here"` 替換成您的實際 Anthropic API 金鑰。

```python
API_KEY = "your_api_key_here"
MODEL_NAME = "claude-3-haiku-20240307"

# 將 API_KEY 與 MODEL_NAME 變數儲存在 IPython store 中，以便在筆記本中重複使用
%store API_KEY
%store MODEL_NAME
```

4. 按順序執行筆記本儲存格，遵循提供的操作說明。

---

## 使用說明與技巧 💡

- 本課程使用 Claude 3 Haiku，溫度設定為 0。稍後課程將更詳細地討論溫度設定。目前只需了解，這些設定會產生更具決定性的結果。本課程的所有提示工程技巧也適用於先前版本的 Claude 模型，例如 Claude 2 和 Claude Instant 1.2。

- 您可以使用 `Shift + Enter` 執行儲存格並移至下一個。

- 到達教學頁面底部時，導覽至資料夾中編號的下一個檔案，或如果您已完成該章節中的內容，導覽至下一個編號的資料夾。

### Anthropic SDK 與 Messages API
我們將在整個教學中使用 [Anthropic Python SDK](https://docs.anthropic.com/claude/reference/client-sdks) 與 [Messages API](https://docs.anthropic.com/claude/reference/messages_post)。

以下是此教學中執行提示的範例。首先，我們建立 `get_completion`，這是一個協助函式，將提示傳送給 Claude 並返回 Claude 的生成回應。現在執行該儲存格。

```python
import anthropic

client = anthropic.Anthropic(api_key=API_KEY)

def get_completion(prompt: str):
    message = client.messages.create(
        model=MODEL_NAME,
        max_tokens=2000,
        temperature=0.0,
        messages=[
          {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
```

現在我們將寫出一個提示範例給 Claude，並透過執行我們的 `get_completion` 協助函式來列印 Claude 的輸出。執行下面的儲存格會列印 Claude 在其下方的回應。

```python
# 提示
prompt = "Hello, Claude!"

# 取得 Claude 的回應
print(get_completion(prompt))
```

歡迎嘗試修改提示字串以從 Claude 引發不同的回應。

```python
# Prompt
prompt = "Hello, Claude!"

# Get Claude's response
print(get_completion(prompt))
```

稍早定義的 `API_KEY` 與 `MODEL_NAME` 變數將在整個教學中使用。只要確保從每個教學頁面的上到下執行儲存格。
