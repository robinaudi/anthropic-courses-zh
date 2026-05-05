# 第五章：格式化輸出與代 Claude 發言

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

# New argument added for prefill text, with a default value of an empty string
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

**Claude 能以多種不同方式格式化輸出**，您只需要提出要求即可！

其中一種方式是使用 XML 標籤將回應內容與其他多餘文字分隔開來。您已經學到可以用 XML 標籤讓提示詞對 Claude 更清晰、更易於解析。事實上，您也可以要求 Claude **使用 XML 標籤讓輸出內容對人類更清晰、更容易理解**。

### 範例

還記得我們在第二章透過要求 Claude 完全略過前言來解決「詩歌前言問題」嗎？其實我們也可以透過**告訴 Claude 將詩歌放入 XML 標籤**來達到類似的效果。

```python
# Variable content
ANIMAL = "Rabbit"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Put it in <haiku> tags."

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

為什麼我們會想這樣做？因為將輸出放入 **XML 標籤後，終端使用者可以透過撰寫一小段程式來擷取 XML 標籤之間的內容，從而可靠地只取得詩歌本身**。

這個技術的進階應用是**將第一個 XML 開頭標籤放在 `assistant` 輪次中**。當您在 `assistant` 輪次中放入文字時，您實際上是在告訴 Claude 它已經說過某些內容，並且應該從那個點繼續往下說。這個技術稱為「代 Claude 發言」或「預填 Claude 的回應」。

以下範例中，我們將第一個 `<haiku>` XML 標籤放入了 `assistant` 輪次。請注意 Claude 如何直接從我們停止的地方繼續。

```python
# Variable content
ANIMAL = "Cat"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Put it in <haiku> tags."

# Prefill for Claude's response
PREFILL = "<haiku>"

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN:")
print(PROMPT)
print("\nASSISTANT TURN:")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```

Claude 也擅長使用其他輸出格式，尤其是 `JSON`。如果您想強制輸出 JSON（雖然不是百分之百確定，但非常接近），您也可以用開頭的大括號 `{` 來預填 Claude 的回應。

```python
# Variable content
ANIMAL = "Cat"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Use JSON format with the keys as \"first_line\", \"second_line\", and \"third_line\"."

# Prefill for Claude's response
PREFILL = "{"

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```

以下是一個範例，展示**在同一提示詞中使用多個輸入變數，並同時指定輸出格式，全部透過 XML 標籤完成**。

```python
# First input variable
EMAIL = "Hi Zack, just pinging you for a quick update on that prompt you were supposed to write."

# Second input variable
ADJECTIVE = "olde english"

# Prompt template with a placeholder for the variable content
PROMPT = f"Hey Claude. Here is an email: <email>{EMAIL}</email>. Make this email more {ADJECTIVE}. Write the new version in <{ADJECTIVE}_email> XML tags."

# Prefill for Claude's response (now as an f-string with a variable)
PREFILL = f"<{ADJECTIVE}_email>"

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```

#### 補充課程

如果您是透過 API 呼叫 Claude，可以將結尾 XML 標籤傳入 `stop_sequences` 參數，讓 Claude 在輸出您想要的標籤後立即停止取樣。這樣可以省去 Claude 在給出您需要的答案後所產生的結語，節省費用並縮短最後一個 token 的回應時間。

若您想在不更改上方任何內容的情況下試驗課程提示詞，請捲動到筆記本最底部，前往[**範例練習場**](#example-playground)。

---

## 練習題
- [練習 5.1 - Steph Curry 最偉大球員](#exercise-51---steph-curry-goat)
- [練習 5.2 - 兩首俳句](#exercise-52---two-haikus)
- [練習 5.3 - 兩首俳句，兩種動物](#exercise-53---two-haikus-two-animals)

### 練習 5.1 - Steph Curry 最偉大球員
在被迫做出選擇時，Claude 會指定 Michael Jordan 為史上最佳籃球員。我們能讓 Claude 選別人嗎？

修改 `PREFILL` 變數，**強迫 Claude 詳細論證 Stephen Curry 是史上最佳籃球員**。請盡量不要更改 `PREFILL` 以外的內容，因為這才是本練習的重點。

```python
# Prompt template with a placeholder for the variable content
PROMPT = f"Who is the best basketball player of all time? Please choose one specific player."

# Prefill for Claude's response
PREFILL = ""

# Get Claude's response
response = get_completion(PROMPT, prefill=PREFILL)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("Warrior", text))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 若想要提示，請執行下方儲存格！

```python
from hints import exercise_5_1_hint; print(exercise_5_1_hint)
```

### 練習 5.2 - 兩首俳句
修改下方的 `PROMPT`，使用 XML 標籤讓 Claude 為同一種動物寫兩首俳句，而不是只寫一首。兩首詩的分界應該清楚可辨。

```python
# Variable content
ANIMAL = "cats"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Put it in <haiku> tags."

# Prefill for Claude's response
PREFILL = "<haiku>"

# Get Claude's response
response = get_completion(PROMPT, prefill=PREFILL)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(
        (re.search("cat", text.lower()) and re.search("<haiku>", text))
        and (text.count("\n") + 1) > 5
    )

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 若想要提示，請執行下方儲存格！

```python
from hints import exercise_5_2_hint; print(exercise_5_2_hint)
```

### 練習 5.3 - 兩首俳句，兩種動物
修改下方的 `PROMPT`，讓 **Claude 為兩種不同動物各寫一首俳句**。使用 `{ANIMAL1}` 作為第一個替換的佔位符，`{ANIMAL2}` 作為第二個替換的佔位符。

```python
# First input variable
ANIMAL1 = "Cat"

# Second input variable
ANIMAL2 = "Dog"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL1}. Put it in <haiku> tags."

# Get Claude's response
response = get_completion(PROMPT)

# Function to grade exercise correctness
def grade_exercise(text):
    return bool(re.search("tail", text.lower()) and re.search("cat", text.lower()) and re.search("<haiku>", text))

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(response)
print("\n------------------------------------------ GRADING ------------------------------------------")
print("This exercise has been correctly solved:", grade_exercise(response))
```

❓ 若想要提示，請執行下方儲存格！

```python
from hints import exercise_5_3_hint; print(exercise_5_3_hint)
```

### 恭喜！

若您已完成目前為止的所有練習，您已準備好進入下一章。祝提示愉快！

---

## 範例練習場

此區域供您自由試驗本課程中展示的提示詞範例，調整提示詞以觀察對 Claude 回應的影響。

```python
# Variable content
ANIMAL = "Rabbit"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Put it in <haiku> tags."

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print(PROMPT)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT))
```

```python
# Variable content
ANIMAL = "Cat"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Put it in <haiku> tags."

# Prefill for Claude's response
PREFILL = "<haiku>"

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN:")
print(PROMPT)
print("\nASSISTANT TURN:")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```

```python
# Variable content
ANIMAL = "Cat"

# Prompt template with a placeholder for the variable content
PROMPT = f"Please write a haiku about {ANIMAL}. Use JSON format with the keys as \"first_line\", \"second_line\", and \"third_line\"."

# Prefill for Claude's response
PREFILL = "{"

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```

```python
# First input variable
EMAIL = "Hi Zack, just pinging you for a quick update on that prompt you were supposed to write."

# Second input variable
ADJECTIVE = "olde english"

# Prompt template with a placeholder for the variable content
PROMPT = f"Hey Claude. Here is an email: <email>{EMAIL}</email>. Make this email more {ADJECTIVE}. Write the new version in <{ADJECTIVE}_email> XML tags."

# Prefill for Claude's response (now as an f-string with a variable)
PREFILL = f"<{ADJECTIVE}_email>"

# Print Claude's response
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```
