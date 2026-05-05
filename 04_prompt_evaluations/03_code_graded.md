# 簡單的程式碼評分評估

本課程先從一個非常簡單的程式碼評分評估範例出發，再於下一課程介紹更貼近實際的提示詞。我們將遵循下圖所示的流程：

![process.png](images/process.png)

大致步驟如下：
1. 定義評估測試集
1. 撰寫初版提示詞
2. 執行評估流程並取得分數
3. 根據評估結果修改提示詞
4. 將修改後的提示詞再次執行評估，期望獲得更好的分數！

讓我們按照這個流程進行！

---

---

## 輸入資料

我們將評估 Claude 能否正確識別動物的腿數。後續課程會看到更複雜且更貼近實際的提示詞和評估，但這裡刻意保持簡單，以聚焦於實際的評估流程。

第一步是撰寫包含輸入及對應黃金答案的評估資料集。讓我們使用這個簡單的字典列表，每個字典包含 `animal_statement` 和 `golden_answer` 兩個鍵：

---

```python
eval_data = [
    {"animal_statement": "The animal is a human.", "golden_answer": "2"},
    {"animal_statement": "The animal is a snake.", "golden_answer": "0"},
    {"animal_statement": "The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.", "golden_answer": "5"},
    {"animal_statement": "The animal is a dog.", "golden_answer": "4"},
    {"animal_statement": "The animal is a cat with two extra legs.", "golden_answer": "6"},
    {"animal_statement": "The animal is an elephant.", "golden_answer": "4"},
    {"animal_statement": "The animal is a bird.", "golden_answer": "2"},
    {"animal_statement": "The animal is a fish.", "golden_answer": "0"},
    {"animal_statement": "The animal is a spider with two extra legs", "golden_answer": "10"},
    {"animal_statement": "The animal is an octopus.", "golden_answer": "8"},
    {"animal_statement": "The animal is an octopus that lost two legs and then regrew three legs.", "golden_answer": "9"},
    {"animal_statement": "The animal is a two-headed, eight-legged mythical creature.", "golden_answer": "8"},
]
```

---

注意其中有些評估問題稍微有點刁鑽，像這一題：
> The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.

這在後面會很重要！

---

---

## 初版提示詞
接下來定義初版提示詞。以下函式接收一個動物陳述，返回一個包含我們第一次提示詞嘗試的格式化訊息列表：

---

```python
def build_input_prompt(animal_statement):
    user_content = f"""You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement.
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? Please respond with a number"""

    messages = [{'role': 'user', 'content': user_content}]
    return messages
```

---

先用 `eval` 資料集的第一筆資料快速測試：

---

```python
build_input_prompt(eval_data[0]['animal_statement'])
```

---

```
[{'role': 'user',
  'content': 'You will be provided a statement about an animal and your job is to determine how many legs that animal has.\n    \n    Here is the animal statement.\n    <animal_statement>The animal is a human.</animal_statement>\n    \n    How many legs does the animal have? Please respond with a number'}]
```

---

接下來撰寫一個簡單函式，接收訊息列表並將其送至 Anthropic API：

---

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

MODEL_NAME = "claude-3-haiku-20240307"

def get_completion(messages):
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=200,
        messages=messages
    )
    return response.content[0].text
```

---

用 `eval_data` 列表的第一筆資料（包含動物陳述 `'The animal is a human.'`）測試：

---

```python
full_prompt = build_input_prompt(eval_data[0]['animal_statement'])
get_completion(full_prompt)
```

---

```
'2'
```

---

我們得到 `2` 作為回應，通過眼球測試！人類通常有兩條腿。下一步是建立並執行涵蓋 `eval_data` 集所有 12 筆資料的完整評估。

---

---

## 撰寫評估邏輯

我們將把 `eval_data` 列表中的每個輸入與提示詞模板結合，將最終「完整」提示詞傳送給模型，並收集所有回傳的輸出：

---

```python

outputs = [get_completion(build_input_prompt(question['animal_statement'])) for question in eval_data]

```

---

快速查看我們得到的結果：

---

```python
outputs
```

---

```
['2',
 '0',
 '5',
 '4',
 '6',
 '4',
 'Based on the provided animal statement, "The animal is a bird.", the animal has 2 legs.\n\nResponse: 2',
 '0',
 '8',
 'An octopus has 8 legs.',
 '5',
 '8']
```

---

可以看出提示詞需要改進，因為有些答案不是純數字！讓我們仔細對照每個對應的黃金答案查看結果：

---

```python
for output, question in zip(outputs, eval_data):
    print(f"Animal Statement: {question['animal_statement']}\nGolden Answer: {question['golden_answer']}\nOutput: {output}\n")
```

---

```
Animal Statement: The animal is a human.
Golden Answer: 2
Output: 2

Animal Statement: The animal is a snake.
Golden Answer: 0
Output: 0

Animal Statement: The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.
Golden Answer: 5
Output: 5

Animal Statement: The animal is a dog.
Golden Answer: 4
Output: 4

Animal Statement: The animal is a cat with two extra legs.
Golden Answer: 6
Output: 6

Animal Statement: The animal is an elephant.
Golden Answer: 4
Output: 4

Animal Statement: The animal is a bird.
Golden Answer: 2
Output: Based on the provided animal statement, "The animal is a bird.", the animal has 2 legs.

Response: 2

Animal Statement: The animal is a fish.
Golden Answer: 0
Output: 0

Animal Statement: The animal is a spider with two extra legs
Golden Answer: 10
Output: 8

Animal Statement: The animal is an octopus.
Golden Answer: 8
Output: An octopus has 8 legs.

Animal Statement: The animal is an octopus that lost two legs and then regrew three legs.
Golden Answer: 9
Output: 5

Animal Statement: The animal is a two-headed, eight-legged mythical creature.
Golden Answer: 8
Output: 8
```

---

這個資料集夠小，我們可以輕鬆掃描結果找出有問題的回應，但讓我們系統性地評分：

---

```python
def grade_completion(output, golden_answer):
    return output == golden_answer

grades = [grade_completion(output, question['golden_answer']) for output, question in zip(outputs, eval_data)]
print(f"Score: {sum(grades)/len(grades)*100}%")
```

---

```
Score: 66.66666666666666%
```

---

我們現在有了基準分數！初版提示詞的準確率為 66.6%。掃描上述結果後，可以發現目前輸出存在兩個明顯問題：

### 問題一：輸出格式問題
我們的目標是讓提示詞產生純數字輸出，但有些輸出並非純數字：

```
Animal Statement: The animal is a bird.
Golden Answer: 2
Output: Based on the provided animal statement, "The animal is a bird.", the animal has 2 legs.
```
可以透過提示工程來解決這個問題！

### 問題一：答案錯誤

此外，有些答案完全錯誤：

```
Animal Statement: The animal is an octopus that lost two legs and then regrew three legs.
Golden Answer: 9
Output: 5
```

以及

```
Animal Statement: The animal is a spider with two extra legs
Golden Answer: 10
Output: 8
```
這些輸入有點「刁鑽」，似乎讓模型產生了問題。我們也會嘗試透過提示工程來解決這個問題！

---

--- 

## 第二次嘗試

有了初版提示詞的基準表現後，讓我們嘗試改進提示詞，看看評估分數是否能提升。我們先解決模型有時輸出額外文字而非純數字的問題。以下是第二個提示詞生成函式：

---

```python
def build_input_prompt2(animal_statement):
    user_content = f"""You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement.
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? Respond only with a numeric digit, like 2 or 6, and nothing else."""

    messages = [{'role': 'user', 'content': user_content}]
    return messages
```

---

提示詞的關鍵新增內容是這一行：

> Respond only with a numeric digit, like 2 or 6, and nothing else.

---

用新版提示詞測試每個輸入：

---

```python
outputs2 = [get_completion(build_input_prompt2(question['animal_statement'])) for question in eval_data]
```

---

快速查看輸出：

---

```python
outputs2
```

---

```
['2', '0', '6', '4', '6', '4', '2', '0', '8', '8', '5', '8']
```

---

現在所有輸出都是純數字！讓我們仔細查看結果：

---

```python
for output, question in zip(outputs2, eval_data):
    print(f"Animal Statement: {question['animal_statement']}\nGolden Answer: {question['golden_answer']}\nOutput: {output}\n")
```

---

```
Animal Statement: The animal is a human.
Golden Answer: 2
Output: 2

Animal Statement: The animal is a snake.
Golden Answer: 0
Output: 0

Animal Statement: The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.
Golden Answer: 5
Output: 6

Animal Statement: The animal is a dog.
Golden Answer: 4
Output: 4

Animal Statement: The animal is a cat with two extra legs.
Golden Answer: 6
Output: 6

Animal Statement: The animal is an elephant.
Golden Answer: 4
Output: 4

Animal Statement: The animal is a bird.
Golden Answer: 2
Output: 2

Animal Statement: The animal is a fish.
Golden Answer: 0
Output: 0

Animal Statement: The animal is a spider with two extra legs
Golden Answer: 10
Output: 8

Animal Statement: The animal is an octopus.
Golden Answer: 8
Output: 8

Animal Statement: The animal is an octopus that lost two legs and then regrew three legs.
Golden Answer: 9
Output: 5

Animal Statement: The animal is a two-headed, eight-legged mythical creature.
Golden Answer: 8
Output: 8
```

---

數字答案仍然存在明顯問題，例如：

```
Animal Statement: The animal is a spider with two extra legs
Golden Answer: 10
Output: 8
```

在解決這個問題之前，先取得正式分數，看看效能（希望）有所提升：

---

```python
grades = [grade_completion(output, question['golden_answer']) for output, question in zip(outputs2, eval_data)]
print(f"Score: {sum(grades)/len(grades)*100}%")
```

---

```
Score: 75.0%
```

---

分數有所提升！**注意：這個資料集非常小，請對這些結果持保留態度**

---

---

## 第三次嘗試

接下來處理邏輯錯誤的問題，例如：

```
Animal Statement: The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.
Golden Answer: 5
Output: 6
```
一個可用的技術是思維鏈（chain of thought）提示，讓 Claude 在生成最終答案前，先遵循特定指令逐步推理。現在我們有了評估機制，可以測試思維鏈提示是否真的有效果！

讓我們撰寫一個新提示詞，要求模型在 `<thinking>` 標籤內「大聲思考」。由於需要方便地提取模型的最終答案，這會使邏輯稍微複雜一些。我們將指示模型把最終答案也放在 `<answer>` 標籤內，以便輕鬆提取「最終」數字答案：


---

```python
def build_input_prompt3(animal_statement):
    user_content = f"""You will be provided a statement about an animal and your job is to determine how many legs that animal has.
    
    Here is the animal statement.
    <animal_statement>{animal_statement}</animal_statement>
    
    How many legs does the animal have? 
    Start by reasoning about the numbers of legs the animal has, thinking step by step inside of <thinking> tags.  
    Then, output your final answer inside of <answer> tags. 
    Inside the <answer> tags return just the number of legs as an integer and nothing else."""

    messages = [{'role': 'user', 'content': user_content}]
    return messages
```

---

用這個新版提示詞收集輸出：

---

```python
outputs3 = [get_completion(build_input_prompt3(question['animal_statement'])) for question in eval_data]
```

---

查看部分輸出：

---

```python
for output, question in zip(outputs3, eval_data):
    print(f"Animal Statement: {question['animal_statement']}\nGolden Answer: {question['golden_answer']}\nOutput: {output}\n")
```

---

```
Animal Statement: The animal is a human.
Golden Answer: 2
Output: <thinking>
The animal is a human, and based on this information, we can reasonably conclude that a human has 2 legs. Humans are bipedal, meaning they have two legs that they use for locomotion and standing upright. This is a characteristic of the human species.
</thinking>

<answer>2</answer>

Animal Statement: The animal is a snake.
Golden Answer: 0
Output: <thinking>
The animal stated in the given statement is a snake. Snakes are known to be legless reptiles, as they do not have any legs. They move by slithering on the ground using their body and scales.
</thinking>

<answer>0</answer>

Animal Statement: The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.
Golden Answer: 5
Output: Here is my step-by-step reasoning:
<thinking>
1. The initial statement says the fox lost a leg.
2. But then the fox "magically grew back the leg he lost and a mysterious extra leg on top of that."
3. This means the fox originally had 4 legs, lost 1 leg, and then grew back the lost leg plus an extra leg, for a total of 5 legs.
</thinking>
<answer>5</answer>

Animal Statement: The animal is a dog.
Golden Answer: 4
Output: <thinking>
The animal statement says the animal is a dog. Dogs are quadrupeds, meaning they have four legs. Therefore, the number of legs the dog has is 4.
</thinking>

<answer>4</answer>

Animal Statement: The animal is a cat with two extra legs.
Golden Answer: 6
Output: <thinking>
The animal statement says that the animal is a cat with two extra legs. A typical cat has four legs, so with the two extra legs, the animal must have six legs in total.
</thinking>

<answer>6</answer>

Animal Statement: The animal is an elephant.
Golden Answer: 4
Output: <thinking>
An elephant is a large mammal that belongs to the order Proboscidea. Elephants are known to have four legs, one for each of their four limbs. Therefore, based on the given animal statement, the animal is an elephant, and elephants have four legs.
</thinking>

<answer>4</answer>

Animal Statement: The animal is a bird.
Golden Answer: 2
Output: <thinking>
The statement provided indicates that the animal is a bird. Birds typically have two legs, as they are bipedal animals that walk and perch on two legs.
</thinking>

<answer>2</answer>

Animal Statement: The animal is a fish.
Golden Answer: 0
Output: <thinking>
Based on the given animal statement, the animal is a fish. Fish are aquatic vertebrates that typically have fins and gills to help them swim and breathe in the water. Fish do not have legs, as they move through the water using their fins and tails.
</thinking>

<answer>0</answer>

Animal Statement: The animal is a spider with two extra legs
Golden Answer: 10
Output: <thinking>
The animal statement says that the animal is a spider with two extra legs. 
A spider typically has 8 legs, so with two extra legs, the total number of legs would be 8 + 2 = 10 legs.
</thinking>

<answer>10</answer>

Animal Statement: The animal is an octopus.
Golden Answer: 8
Output: <thinking>
The animal statement says the animal is an octopus. An octopus is a marine invertebrate with eight tentacles that are often referred to as legs. Therefore, the animal has 8 legs.
</thinking>

<answer>8</answer>

Animal Statement: The animal is an octopus that lost two legs and then regrew three legs.
Golden Answer: 9
Output: <thinking>
The animal is described as an octopus that lost two legs and then regrew three legs. Initially, an octopus has eight legs.
Since the animal lost two legs, it would have had six legs remaining.
Then, the animal regrew three legs, so the final number of legs the animal has is nine.
</thinking>

<answer>9</answer>

Animal Statement: The animal is a two-headed, eight-legged mythical creature.
Golden Answer: 8
Output: <thinking>
The animal statement mentions that the animal is a two-headed, eight-legged mythical creature. This means that the animal has two heads and eight legs.
</thinking>

<answer>8</answer>
```

---

以下是我們得到的一個典型回應：

```
Animal Statement: The fox lost a leg, but then magically grew back the leg he lost and a mysterious extra leg on top of that.
Golden Answer: 5
Output: Here is my step-by-step reasoning:
<thinking>
1. The initial statement says the fox lost a leg.
2. But then the fox "magically grew back the leg he lost and a mysterious extra leg on top of that."
3. This means the fox originally had 4 legs, lost 1 leg, and then grew back the lost leg plus an extra leg, for a total of 5 legs.
</thinking>
<answer>5</answer>
```

至少在這個特定範例中，邏輯明顯有所改善。現在需要讓這個提示詞「可評分」。我們必須在評分之前提取 `answer` 標籤之間的數字。

以下函式用於提取兩個 `<answer>` 標籤之間的文字：

---

```python
import re
def extract_answer(text):
    pattern = r'<answer>(.*?)</answer>'
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        return None
```

---

從最新一批輸出中提取答案：

---

```python
extracted_outputs3 = [extract_answer(output) for output in outputs3]
```

---

```python
extracted_outputs3
```

---

```
['2', '0', '5', '4', '6', '4', '2', '0', '10', '8', '9', '8']
```

---

接著取得分數，看看加入思維鏈是否有所改變！

---

```python
grades3 = [grade_completion(output, question['golden_answer']) for output, question in zip(extracted_outputs3, eval_data)]
print(f"Score: {sum(grades3)/len(grades3)*100}%")
```

---

```
Score: 100.0%
```

---

我們的分數提升到 100%！

這次評估讓我們確信，對提示詞所做的修改確實帶來了更好的輸出。這是一個使用精確比對評分的簡單範例，但在下一課程中，我們將看到稍微複雜一些的例子。
