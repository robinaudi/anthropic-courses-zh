# Anthropic Workbench 評估
本課程將示範如何使用 Anthropic Workbench 執行人工評分評估。這是一個極易上手的視覺化介面，可快速原型測試提示詞並執行人工評分評估。雖然我們通常建議在正式評估中採用更具擴展性的方案，但 Anthropic Workbench 是開始進行人工評分評估的絕佳起點，之後再進階到更嚴謹的程式碼評分或模型評分。

本課程將示範如何使用 Workbench 測試提示詞、執行簡單評估，以及比較不同版本的提示詞。

---

---

## Anthropic Workbench

[Anthropic Workbench](https://console.anthropic.com/workbench/) 是快速原型測試提示詞並執行人工評分評估的理想場所。以下是 Workbench 首次載入時的樣貌：

![empty_workbench.png](images/empty_workbench.png)

左側可以輸入提示詞。假設我們正在開發一個程式碼翻譯應用程式，想撰寫最佳提示詞，透過 Anthropic API 將任何程式語言的程式碼翻譯成 Python。以下是一個初步嘗試：

---

```
You are a skilled programmer tasked with translating code from one programming language to Python. Your goal is to produce an accurate and idiomatic Python translation of the provided source code.

Here is the source code to translate:

<source_code>
{{SOURCE_CODE}}
</source_code>

The source code is written in the following language:

<source_language>
{{SOURCE_LANGUAGE}}
</source_language>

Please translate this code to Python
```

注意 `{{SOURCE_CODE}}` 和 `{{SOURCE_LANGUAGE}}` 變數，稍後會以動態值取代它們。

---

我們可以將這個提示詞輸入到 Workbench 左側：

![workbench_with_prompt.png](images/workbench_with_prompt.png)

---

接著，點擊變數（`{ }`）按鈕，為變數設定測試值：

![variables_button.png](images/variables_button.png)

這會開啟一個對話框，要求輸入 `{{SOURCE_CODE}}` 和 `{{SOURCE_LANGUAGE}}` 的值：

![adding_variables.png](images/adding_variables.png)


---

接著點擊執行，查看模型輸出的結果：

![first_output.png](images/first_output.png)

---

---

## Workbench 評估

每次只用一組變數測試提示詞是個好的開始，但 Workbench 也內建了評估工具，協助我們針對多組輸入執行提示詞。點擊頂部的「Evaluate」切換按鈕，切換到評估檢視：

![evaluate_button.png](images/evaluate_button.png)

---

這會開啟評估檢視，並預先填入初始結果：

![evaluate1.png](images/evaluate1.png)

---

接下來，點擊「Add Row」按鈕新增測試案例。讓我們新增兩個測試案例：Ruby 程式碼和 C# 程式碼：

![evaluate2.png](images/evaluate2.png)


---

接著，可以點擊每個測試案例旁的個別「Run」按鈕，或點擊橘色「Run Remaining」按鈕執行所有尚未執行的測試案例：

![run_remaining.png](images/run_remaining.png)

點擊「Run Remaining」按鈕，查看模型回應：

---

以下是我們得到的結果：

![evaluate3.png](images/evaluate3.png)

---

--- 

## 人工評分

現在是仔細審閱模型輸出並給分的時候了。右欄提供了為每個輸出評分的選項：

![score.png](images/score.png)


---

讓我們仔細看看部分輸出。

### JavaScript 測試案例結果

以下是 JavaScript 翻譯測試案例的結果：

```
Here's the Python translation of the provided JavaScript code:

chicken_count = 99


In Python:
1. We don't use the `const` keyword to declare constants. By convention, constants in Python are typically written in all uppercase, but this isn't enforced by the language.
2. We don't need to use any keyword (like `let` or `var` in JavaScript) to declare variables.
3. The variable name uses snake_case, which is already consistent with Python naming conventions.

If you want to emphasize that this is intended to be a constant (i.e., a value that shouldn't be changed), you could use the all-uppercase convention:


CHICKEN_COUNT = 99


Both versions are valid Python code, with the uppercase version signaling to other developers that this value is intended to be constant.
```

### Ruby 測試案例結果


以下是 Ruby 翻譯測試案例的結果：

```
Certainly! Here's the Python translation of the provided Ruby code:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def introduce(self):
        print(f"Hello, I'm {self.name} and I'm {self.age} years old.")

    @classmethod
    def create_family(cls, members):
        return [cls(name, age) for name, age in members]

# Create a family
family = Person.create_family([
    ["Alice", 35],
    ["Bob", 40],
    ["Charlie", 12]
])

# Introduce family members
for person in family:
    person.introduce()

# Celebrate Charlie's birthday
charlie = next(person for person in family if person.name == "Charlie")
charlie.birthday()
charlie.introduce()


Here are the key changes and explanations:

1. In Python, we don't need to explicitly declare attribute readers. The attributes are accessible by default.

2. The `initialize` method in Ruby becomes `__init__` in Python.

3. The `birthday!` method is renamed to `birthday` in Python, as the exclamation mark is not typically used in Python method names.

4. The `self.` prefix is used explicitly in Python method definitions and when accessing instance attributes.

5. String interpolation uses f-strings in Python (e.g., `f"Hello, I'm {self.name}"`).

6. The `create_family` class method is defined using the `@classmethod` decorator in Python.

7. List comprehension is used instead of `map` for creating the family members.

8. The `each` method with `&:introduce` is replaced by a simple `for` loop in Python.

9. The `find` method is replaced with `next()` and a generator expression to find Charlie.

This Python code maintains the functionality of the original Ruby code while adhering to Python's syntax and conventions.
```

---

### 為提示詞評分

目前所有輸出在翻譯程式碼方面表現尚可，但存在幾個關鍵問題：

* 我們不需要「Certainly! Here's the Python translation of the provided Ruby code.」這類討人厭的開場白。它們只是在浪費輸出 token！
* 目前的格式非常難以程式化解析。我們要怎麼寫程式碼來單獨提取翻譯後的 Python 程式碼？
* 我們不需要輸出末尾那長長的說明。對我們的使用情境來說，只需要翻譯後的程式碼即可。

讓我們為這些輸出評分，每個都給 3 分（滿分 5 分）。

---

--- 

## 更新提示詞

下一步是修改提示詞並再次執行評估！讓我們根據前面發現的問題更新提示詞。

```
You are a skilled programmer tasked with translating code from one programming language to Python. Your goal is to produce an accurate and idiomatic Python translation of the provided source code.

Here is the source code to translate:

<source_code>
{{SOURCE_CODE}}
</source_code>

The source code is written in the following language:

<source_language>
{{SOURCE_LANGUAGE}}
</source_language>

Please translate this code to Python.
Format your response as follows:

<python_code>
Your Python translation here
</python_code>

Only output the <python_code> tags without any other text content
```


---

切換回「Prompt」檢視後，可以在介面中更新提示詞：

![updated_prompt.png](images/updated_prompt.png)

以綠色高亮顯示的文字是我們新增的部分

---

接著點擊橘色「Run」按鈕測試新提示詞。以下是新的結果：

![updated_response.png](images/updated_response.png)

這正是我們期望的結果！回應中沒有開場白，也沒有冗長的程式碼說明。

---

---

## 重新執行評估
接著切換回評估檢視：

![evaluate4.png](images/evaluate4.png)

注意左上角顯示「v2」，表示這是第二版提示詞。點擊「Run Remaining」，查看其他測試案例的輸出：

![evaluate5.png](images/evaluate5.png)



---

新的輸出看起來很棒！所有輸出都跳過了開場白和說明文字，只包含帶有翻譯後 Python 程式碼的 `<python_code>` 標籤。讓我們將所有輸出都評為 5/5！

![evaluate6.png](images/evaluate6.png)

---

---

## 比較結果

試用了兩個不同的提示詞後，我們可以並排比較結果。點擊右上角的「+ Add Comparison」按鈕，選擇之前的提示詞版本（v1），與 v2 的結果進行比較。這會並排展示兩個提示詞的模型輸出和人工評分：

![comparison.png](images/comparison.png)

---

顯然可以看出，v2 提示詞在我們的特定使用情境上表現好得多！

Workbench 及其評估工具是快速原型測試提示詞並並排比較結果的絕佳場所。在開始評估之旅時，這是理想的起點，之後再轉向更完善的解決方案。在後續課程中，我們將了解如何自動化大規模的程式碼評分和模型評分課程。
