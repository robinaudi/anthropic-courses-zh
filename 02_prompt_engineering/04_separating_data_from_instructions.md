# 第 4 章：分離資料與指令

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

通常，我們不想寫完整的提示，而是想要**可在提交給 Claude 前修改額外輸入資料的提示範本**。如果您想讓 Claude 每次都執行相同的操作，但 Claude 用於其任務的資料可能每次都不同，這可能會很有用。

幸運的是，我們可以透過**分離提示的固定骨架與可變使用者輸入，然後在提交完整提示給 Claude 前將使用者輸入替換到提示中**，相當容易地做到這一點。

下面，我們將逐步演練如何撰寫可替換的提示範本，以及如何替換使用者輸入。

### 範例

在第一個範例中，我們要求 Claude 作為動物聲音生成器。請注意，提交給 Claude 的完整提示只是用輸入（在此案例中為「Cow」）替換的 `PROMPT_TEMPLATE`。請注意單詞「Cow」透過 f-string 替換 `ANIMAL` 佔位符，當我們列印完整提示時。

**注意：** 實踐中您不必將佔位符變數稱為特定的任何東西。在此範例中我們稱之為 `ANIMAL`，但我們同樣可以稱之為 `CREATURE` 或 `A`（雖然通常最好讓您的變數名稱具體且相關，使您的提示範本易於理解，即使沒有替換，以便使用者可解析）。只要確保您用於提示範本 f-string 的任何名稱正是您使用的。

```python
# 可變內容
ANIMAL = "Cow"

# 具有可變內容佔位符的提示範本
PROMPT = f"I will tell you the name of an animal. Please respond with the noise that animal makes. {ANIMAL}"

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

為什麼我們想要以這種方式分離和替換輸入？好吧，**提示範本簡化了重複任務**。假設您建立了一個提示結構，邀請第三方使用者向提示提交內容（在此案例中是他們想生成聲音的動物）。這些第三方使用者甚至不必看到完整的提示。他們只需填充變數。

我們使用變數和 f-string 執行此替換，但您也可以使用 format() 方法執行此操作。

**注意：** 提示範本可以有所需數量的變數！

引入像這樣的替換變數時，非常重要的是**確保 Claude 知道變數從何開始和結束**（相對於指令或任務說明）。讓我們看一個沒有指令和替換變數之間分離的例子。

對於我們人類的眼睛，在下面的提示範本中，變數開始和結束的位置非常清楚。但是，在完全替換的提示中，該界線變得不那麼清楚。

```python
# 可變內容
EMAIL = "Show up at 6am tomorrow because I'm the CEO and I say so."

# 具有可變內容佔位符的提示範本
PROMPT = f"Yo Claude. {EMAIL} <----- Make this email more polite but don't change anything else about it."

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

這裡，**Claude 認為「Yo Claude」是它應該重寫的電子郵件的一部分**！您可以看到這一點，因為它開始其重寫時帶有「Dear Claude」。對於人眼來說，它很清楚，特別是在提示範本中，電子郵件從何開始和結束，但替換後變得不清楚得多。

我們如何解決這個問題？**將輸入包裝在 XML 標籤中**！我們在下面執行了此操作，如您所見，不再有「Dear Claude」在輸出中。

[XML 標籤](https://docs.anthropic.com/claude/docs/use-xml-tags)是類似 `<tag></tag>` 的角括弧標籤。它們成對出現，包括像 `<tag>` 的開放標籤，以及標有 `/` 的關閉標籤，例如 `</tag>`。XML 標籤用於包裝內容，如下所示：`<tag>content</tag>`。

**注意：** 雖然 Claude 可以識別和使用多種分隔符和分隔符，但我們建議您**特別使用 XML 標籤作為分隔符來與 Claude 一起使用**，因為 Claude 經過訓練專門將 XML 標籤識別為提示組織機制。在函式呼叫之外，**沒有特殊的 Claude 經過訓練的 XML 標籤，您應該使用這些標籤來最大限度地提高效能**。我們故意以這種方式讓 Claude 非常可塑性和可定制。

```python
# 可變內容
EMAIL = "Show up at 6am tomorrow because I'm the CEO and I say so."

# 具有可變內容佔位符的提示範本
PROMPT = f"Yo Claude. <email>{EMAIL}</email> <----- Make this email more polite but don't change anything else about it."

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

讓我們看另一個 XML 標籤如何幫助我們的範例。

在以下提示中，**Claude 不正確地解釋了提示的哪一部分是指令與輸入**。它不正確地將 `Each is about an animal, like rabbits` 視為清單的一部分，因為格式化，當使用者（填寫 `SENTENCES` 變數的人）可能不想要那樣時。

```python
# 可變內容
SENTENCES = """- I like how cows sound
- This sentence is about spiders
- This sentence may appear to be about dogs but it's actually about pigs"""

# 具有可變內容佔位符的提示範本
PROMPT = f"""Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.
{SENTENCES}"""

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

要修復此問題，我們只需要**在使用者輸入句子周圍使用 XML 標籤**。這表明 Claude 輸入資料從何開始和結束，儘管在 `Each is about an animal, like rabbits.` 之前有誤導性的連字符。

```python
# 可變內容
SENTENCES = """- I like how cows sound
- This sentence is about spiders
- This sentence may appear to be about dogs but it's actually about pigs"""

# 具有可變內容佔位符的提示範本
PROMPT = f""" Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.
<sentences>
{SENTENCES}
</sentences>"""

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

**注意：** 在「每個都是關於動物」提示的不正確版本中，我們必須包含連字符以使 Claude 以我們想要的方式為此範例錯誤地回應。這是關於提示的重要課程：**小細節很重要**！它始終值得**清除提示中的拼寫錯誤和語法錯誤**。Claude 對模式敏感（在早期，在微調之前，它是原始文本預測工具），當您出錯時更可能犯錯，當您聽起來聰慧時更聰慧，當您聽起來傻時更傻，等等。

如果您想在不更改上述任何內容的情況下實驗課程提示，請向下捲動到本課程筆記本底部以造訪[**範例遊樂場**](#範例遊樂場)。

---

## 練習
- [練習 4.1 - 俳句主題](#練習-41---俳句主題)
- [練習 4.2 - 有錯別字的狗問題](#練習-42---有錯別字的狗問題)
- [練習 4.3 - 狗問題第 2 部分](#練習-42---狗問題第-2-部分)

### 練習 4.1 - 俳句主題
修改 `PROMPT` 使其成為將接受稱為 `TOPIC` 的變數並輸出有關該主題的俳句的範本。此練習只是為了測試您對變數範本化結構與 f-string 的理解。

```python
# 可變內容
TOPIC = "Pigs"

# 具有可變內容佔位符的提示範本
PROMPT = f""

# 取得 Claude 的回應
response = get_completion(PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    return bool(re.search("pigs", text.lower()) and re.search("haiku", text.lower()))

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_4_1_hint; print(exercise_4_1_hint)
```

### 練習 4.2 - 有錯別字的狗問題
透過新增 XML 標籤修復 `PROMPT` 使 Claude 產生正確的答案。

盡量不要更改提示中的其他任何東西。混亂和出現錯誤的寫作是故意的，所以您可以看到 Claude 如何對此類錯誤做出反應。

```python
# 可變內容
QUESTION = "ar cn brown?"

# 具有可變內容佔位符的提示範本
PROMPT = f"Hia its me i have a q about dogs jkaerjv {QUESTION} jklmvca tx it help me muhch much atx fst fst answer short short tx"

# 取得 Claude 的回應
response = get_completion(PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    return bool(re.search("brown", text.lower()))

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_4_2_hint; print(exercise_4_2_hint)
```

### 練習 4.3 - 狗問題第 2 部分
修復 `PROMPT` **不**新增 XML 標籤。改為只從提示中移除一個或兩個單詞。

如上面的練習一樣，盡量不要更改提示中的其他任何東西。這將表明 Claude 可以解析和理解什麼類型的語言。

```python
# 可變內容
QUESTION = "ar cn brown?"

# 具有可變內容佔位符的提示範本
PROMPT = f"Hia its me i have a q about dogs jkaerjv {QUESTION} jklmvca tx it help me muhch much atx fst fst answer short short tx"

# 取得 Claude 的回應
response = get_completion(PROMPT)

# 評分練習正確性的函式
def grade_exercise(text):
    return bool(re.search("brown", text.lower()))

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 如果您想要提示，請執行下面的儲存格！

```python
from hints import exercise_4_3_hint; print(exercise_4_3_hint)
```

### 恭喜！

如果您已解決到此為止的所有練習，您已準備好進入下一章。祝您提示工程愉快！

---

## 範例遊樂場

這是一個區域，供您自由試驗本課程所示的提示範例，並調整提示以查看它如何影響 Claude 的回應。

```python
# 可變內容
ANIMAL = "Cow"

# 具有可變內容佔位符的提示範本
PROMPT = f"I will tell you the name of an animal. Please respond with the noise that animal makes. {ANIMAL}"

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

```python
# 可變內容
EMAIL = "Show up at 6am tomorrow because I'm the CEO and I say so."

# 具有可變內容佔位符的提示範本
PROMPT = f"Yo Claude. {EMAIL} <----- Make this email more polite but don't change anything else about it."

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

```python
# 可變內容
EMAIL = "Show up at 6am tomorrow because I'm the CEO and I say so."

# 具有可變內容佔位符的提示範本
PROMPT = f"Yo Claude. <email>{EMAIL}</email> <----- Make this email more polite but don't change anything else about it."

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

```python
# 可變內容
SENTENCES = """- I like how cows sound
- This sentence is about spiders
- This sentence may appear to be about dogs but it's actually about pigs"""

# 具有可變內容佔位符的提示範本
PROMPT = f"""Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.
{SENTENCES}"""

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

```python
# 可變內容
SENTENCES = """- I like how cows sound
- This sentence is about spiders
- This sentence may appear to be about dogs but it's actually about pigs"""

# 具有可變內容佔位符的提示範本
PROMPT = f""" Below is a list of sentences. Tell me the second item on the list.

- Each is about an animal, like rabbits.
<sentences>
{SENTENCES}
</sentences>"""

# 列印 Claude 的回應
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```
