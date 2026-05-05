# 開始使用 Claude SDK

## 課程目標
在第一堂課中，您將學習如何：
* 安裝必要的套件並使用 API 進行身份驗證
* 向 Claude AI 助手發送您的第一個請求

## 安裝 SDK

在深入 SDK 之前，請確保您的系統上安裝了 Python。

Claude Python SDK 需要 Python 3.7.1 或更新版本。

您可以在終端中執行以下命令來檢查目前的 Python 版本：

```
python --version
```

如果您沒有安裝 Python 或版本早於 3.7.1，請造訪 [官方 Python 網站](https://www.python.org) 並按照您的作業系統安裝說明進行。

準備好 Python 後，您現在可以使用 pip 安裝 Anthropic 套件

```python
# 如果從筆記本內部安裝套件，請使用此命令
%pip install anthropic 
# 使用此命令從命令列安裝套件
# pip install anthropic
```

## 取得 API 金鑰

要向 Claude API 驗證您的請求，您需要一個 API 金鑰。

請按照以下步驟取得您的 API 金鑰：

1. 如果您還沒有的話，請造訪 https://console.anthropic.com 註冊 Anthropic 帳戶
2. 建立帳戶並登入後，導覽至 API 設定頁面。您可以透過點選右上角的設定檔圖示並從下拉選單中選擇「API 金鑰」，或在「設定」頁籤中導覽至「API 金鑰」選單來找到此頁面。
3. 在 API 設定頁面上，點選「建立金鑰」按鈕。將出現一個模式視窗，提示您為金鑰提供描述性名稱。選擇反映您將金鑰用於的目的或專案的名稱。您可以在帳戶內建立任意數量的金鑰（請注意，速率和訊息限制適用於帳戶層級，而不是 API 金鑰層級）。
4. 輸入名稱後，點選「建立」按鈕。您的新 API 金鑰將被產生並顯示在螢幕上。
   > 請務必複製此金鑰，因為導覽離開此頁面後您將無法再次檢視它。

![signup.png](images/signup.png)

請記住，您的 API 金鑰是授予您 Anthropic 帳戶存取權限的敏感資訊。像對待密碼一樣對待它，切勿在公開場合分享或提交到版本控制系統（如 Git）。


## 安全地存儲 API 金鑰

雖然您可以直接在 Python 指令碼中硬編碼 API 金鑰，但將敏感資訊（如 API 金鑰）與程式碼庫分開存儲通常被視為最佳實踐。一種常見的方法是將 API 金鑰存儲在 `.env` 檔案中，並使用 `python-dotenv` 套件載入它。以下是設定方法：

在與您的筆記本相同的目錄中建立一個名為 `.env` 的新檔案。


將您的 API 金鑰新增至新建立的 `.env` 檔案，使用以下格式：

```
ANTHROPIC_API_KEY=put-your-api-key-here
```

確保儲存 `.env` 檔案

在您的終端或筆記本中執行以下命令以安裝 python-dotenv 套件：

```python
# 要從筆記本安裝套件：
%pip install python-dotenv

# 要從您的終端安裝：
# pip install python-dotenv
```

現在我們可以使用 dotenv 模組中的 `load_dotenv()` 函數從 .env 檔案載入 API 金鑰：

```python
from dotenv import load_dotenv
import os

load_dotenv()
my_api_key = os.getenv("ANTHROPIC_API_KEY")

```

## 使用用戶端進行基本請求

安裝了 `anthropic` 套件並載入了 API 金鑰後，您已準備好開始向 Claude API 發出請求。

第一步是建立一個用戶端物件，它作為與 API 互動的主要入口點。

```python
from anthropic import Anthropic

client = Anthropic(
    api_key=my_api_key
)
```

請注意，`anthropic` SDK 會自動尋找名為「ANTHROPIC_API_KEY」的環境變數，因此您實際上不需要手動傳遞它，可以改為這樣做：

```py
from anthropic import Anthropic

client = Anthropic()
```

現在我們已初始化了用戶端，是時候發出我們的第一個請求了。

要向 Claude 發送訊息並接收回應，我們將使用用戶端物件的 `messages.create()` 方法。
我們將在下一堂課中討論具體的參數和回應格式。現在，嘗試執行以下程式碼，您應該會從 Claude 收到您的第一條訊息！

```python
our_first_message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hi there! Please write me a haiku about a pet chicken"}
    ]
)

print(our_first_message.content[0].text)

```

```
Feathered friend clucking,
Scratching in the dirt all day,
Loyal pet chicken.
```


***

## 練習

我們才剛開始，所以這個練習可能感覺有點乏味。但總是好的實踐一下基礎。

請執行以下操作：
1. 建立一個新的筆記本或 Python 指令碼。
2. 匯入適當的套件
3. 載入您的 Anthropic API 金鑰
4. 要求 Claude 講一個笑話，然後列印結果（您可以複製/貼上上面的程式碼並進行調整）

***
