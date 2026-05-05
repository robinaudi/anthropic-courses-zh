# 自訂模型評分評估

**注意：本課程位於一個包含相關程式碼檔案的資料夾中。若想跟著操作並自行執行評估，請下載整個資料夾。**


在本課程中，我們將學習如何使用 promptfoo 撰寫自訂模型評分評估。我們從一個簡單的提示目標開始：撰寫一個提示，能將冗長、技術複雜的 Wikipedia 文章轉換為適合小學生閱讀的短篇摘要。

例如，給定完整的[卷積神經網路 Wikipedia 條目](https://en.wikipedia.org/wiki/Convolutional_neural_network)，我們希望輸出如下的簡單摘要：

> Convolutional neural networks, or CNNs, are a special type of computer program that can learn to recognize images and patterns. They work a bit like the human brain, using layers of artificial "neurons" to process information.
CNNs are really good at tasks like identifying objects in pictures or recognizing faces. They do this by breaking down images into smaller pieces and looking for important features, kind of like putting together a puzzle.
What makes CNNs special is that they can learn these features on their own by looking at lots of examples. This allows them to get better and better at recognizing things, sometimes even matching human-level performance.
Scientists and engineers use CNNs for all sorts of cool applications, like helping self-driving cars see the road, finding new medicines, or even teaching computers to play games like chess and Go.

為了評估提示的有效性，我們將撰寫一個自訂模型評分斷言，依據三個指標評估生成的摘要：

* 簡潔性（1-5）- 摘要是否盡可能簡潔？
* 準確性（1-5）- 摘要是否完全基於原始文章而準確？
* 語調（1-5）- 摘要是否適合沒有技術背景的小學生閱讀？

這三個指標各自會得出 1 到 5 之間的分數。我們將取平均值，目標是達到至少 4.5/5 的平均分。為此，我們將定義一個自訂模型評分器函式！

---
    


---

## 輸入資料

我們的目標是撰寫一個提示，將複雜的 Wikipedia 文章摘要為簡短易懂的內容。我們首先收集要在評估中摘要的文章。

在這個資料夾中，我們提供了一個 `articles` 目錄，其中包含八個不同的 txt 檔案。每個檔案包含來自一篇 Wikipedia 文章的文字內容。我們將使用這些文章作為評估的輸入。可以查看一些文章檔案，了解它們的長度和複雜程度。

這個資料集只有八個測試案例，對於真實世界的評估來說遠遠不夠。如同我們在本課程中多次提到的，我們強烈建議評估資料集至少包含 100 筆資料。

---

---

## 提示

查看 `prompts.py` 檔案。它包含三個不同的提示生成函式，我們將使用 promptfoo 進行評估：

```py
def basic_summarize(article):
  return f"Summarize this article {article}"

def better_summarize(article):
  return f"""
  Summarize this article for a grade-school audience: {article}"""

def best_summarize(article):
  return f"""
  You are tasked with summarizing long wikipedia articles for a grade-school audience.
  Write a short summary, keeping it as concise as possible. 
  The summary is intended for a non-technical, grade-school audience. 
  This is the article: {article}"""
```
**重要提示：這些提示整體上都是品質偏差的提示。我們刻意將提示保持簡短，沒有遵循最佳實踐（例如加入完整範例），以盡量減少執行此評估集時使用的 token 數量。**

---

---

## 更新設定檔

`promptfooconfig.yaml` 檔案包含我們大多已見過的欄位：


```yaml
description: 'Summarization Evaluation'

prompts:
  - prompts.py:basic_summarize
  - prompts.py:better_summarize
  - prompts.py:best_summarize

providers:
  - id: anthropic:messages:claude-3-5-sonnet-20240620
    label: "3.5 Sonnet"

tests:
  - vars:
      article: file://articles/article1.txt
  - vars:
      article: file://articles/article2.txt
  - vars:
      article: file://articles/article3.txt
  - vars:
      article: file://articles/article4.txt
  - vars:
      article: file://articles/article5.txt
  - vars:
      article: file://articles/article6.txt
  - vars:
      article: file://articles/article7.txt
  - vars:
      article: file://articles/article8.txt

defaultTest:
  assert:
    - type: python
      value: file://custom_llm_eval.py

```

我們告訴 promptfoo 要使用在 `prompts.py` 中定義的三個提示。接下來，我們設定 promptfoo 使用 Claude 3.5 Sonnet 作為 provider。

我們撰寫了一系列 `tests`，在每個測試中為 `article` 提供不同的值。這裡新增的內容是從文字檔案載入值。文章非常長，直接將它們放在 YAML 檔案中並不合適。例如，設定檔中的這段內容：

```yaml
tests:
  - vars:
      article: file://articles/article1.txt
```

告訴 promptfoo 我們要執行一個測試，其中 `article` 變數設定為 `article1.txt` 檔案的文字內容。我們對所有八篇文章重複這個過程。

---

---

## 撰寫自訂模型評分器函式

接下來，讓我們將注意力轉向 YAML 檔案的最後一個欄位：

```yaml
defaultTest:
  assert:
    - type: python
      value: file://custom_llm_eval.py
```

這個欄位告訴 promptfoo，對於每一個測試，我們都希望執行在 `custom_llm_eval.py` 檔案中定義的特定 Python 斷言。我們之前在定義自訂程式碼評分斷言時見過這個語法。唯一的差別是，這次我們要撰寫一個使用另一個模型來評分模型輸出的函式。

讓我們查看 `custom_llm_eval.py` 檔案的內容。它包含相當多的程式碼：

```py
import anthropic
import os
import json

def llm_eval(summary, article):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""Evaluate the following summary based on these criteria:
    1. Conciseness (1-5) - is the summary as concise as possible?
        - Conciseness of 1: The summary is unnecessarily long, including excessive details, repetitions, or irrelevant information. It fails to distill the key points effectively.
        - Conciseness of 3:  The summary captures most key points but could be more focused. It may include some unnecessary details or slightly over explain certain concepts.
        - Conciseness of 5: The summary effectively condenses the main ideas into a brief, focused text. It includes all essential information without any superfluous details or explanations.
    2. Accuracy (1-5) - is the summary completely accurate based on the initial article'?
        - Accuracy of 1: The summary contains significant errors, misrepresentations, or omissions that fundamentally alter the meaning or key points of the original article.
        - Accuracy of 3:  The summary captures some key points correctly but may have minor inaccuracies or omissions. The overall message is generally correct, but some details may be wrong.
        - Accuracy of 5: The summary faithfully represents the main gist of the original article without any errors or misinterpretations. All included information is correct and aligns with the source material.
    3. Tone (1-5) - is the summary appropriate for a grade school student with no technical training?
        - Tone of 1: The summary uses language or concepts that are too complex, technical, or mature for a grade school audience. It may contain jargon, advanced terminology, or themes that are not suitable for young readers.
        - Tone of 2:  The summary mostly uses language suitable for grade school students but occasionally includes terms or concepts that may be challenging. Some explanations might be needed for full comprehension.
        - Tone of 3: The summary consistently uses simple, clear language that is easily understandable by grade school students. It explains complex ideas in a way that is accessible and engaging for young readers.
    4. Explanation - a general description of the way the summary is evaluated

    <examples>
    <example>
    This summary:
    <summary>
    Artificial neural networks are computer systems inspired by how the human brain works. They are made up of interconnected "neurons" that process information. These networks can learn to do tasks by looking at lots of examples, similar to how humans learn. 

    Some key things about neural networks:
    - They can recognize patterns and make predictions
    - They improve with more data and practice
    - They're used for things like identifying objects in images, translating languages, and playing games

    Neural networks are a powerful tool in artificial intelligence and are behind many of the "smart" technologies we use today. While they can do amazing things, they still aren't as complex or capable as the human brain.
    <summary>
    Should receive a 5 for tone, a 5 for accuracy, and a 5 for conciseness
    </example>

    <example>
    This summary:
    <summary>
    Here is a summary of the key points from the article on artificial neural networks (ANNs):

    1. ANNs are computational models inspired by biological neural networks in animal brains. They consist of interconnected artificial neurons that process and transmit signals.

    2. Basic structure:
    - Input layer receives data
    - Hidden layers process information 
    - Output layer produces results
    - Neurons are connected by weighted edges

    3. Learning process:
    - ANNs learn by adjusting connection weights
    - Use techniques like backpropagation to minimize errors
    - Can perform supervised, unsupervised, and reinforcement learning

    4. Key developments:
    - Convolutional neural networks (CNNs) for image processing
    - Recurrent neural networks (RNNs) for sequential data
    - Deep learning with many hidden layers

    5. Applications:
    - Pattern recognition, classification, regression
    - Computer vision, speech recognition, natural language processing
    - Game playing, robotics, financial modeling

    6. Advantages:
    - Can model complex non-linear relationships
    - Ability to learn and generalize from data
    - Adaptable to many different types of problems

    7. Challenges:
    - Require large amounts of training data
    - Can be computationally intensive
    - "Black box" nature can make interpretability difficult

    8. Recent advances:
    - Improved hardware (GPUs) enabling deeper networks
    - New architectures like transformers for language tasks
    - Progress in areas like generative AI

    The article provides a comprehensive overview of ANN concepts, history, types, applications, and ongoing research areas in this field of artificial intelligence and machine learning.
    </summary>
    Should receive a 1 for tone, a 5 for accuracy, and a 3 for conciseness
    </example>
    </examples>

    Provide a score for each criterion in JSON format. Here is the format you should follow always:

    <json>
    {{
    "conciseness": <number>,
    "accuracy": <number>,
    "tone": <number>,
    "explanation": <string>,
    }}
    </json>


    Original Text: <original_article>{article}</original_article>
    
    Summary to Evaluate: <summary>{summary}</summary>
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": "<json>" 
            }
        ],
        stop_sequences=["</json>"]
    )
    
    evaluation = json.loads(response.content[0].text)
    # Filter out non-numeric values and calculate the average
    numeric_values = [value for key, value in evaluation.items() if isinstance(value, (int, float))]
    avg_score = sum(numeric_values) / len(numeric_values)
    return avg_score, response.content[0].text

def get_assert(output: str, context, threshold=4.5):
    article = context['vars']['article']
    score, evaluation = llm_eval(output, article )
    return {
        "pass": score >= threshold,
        "score": score,
        "reason": evaluation
    }

```

---

### `get_assert()`

這裡有很多內容需要討論，但讓我們從檔案底部的函式開始：`get_assert`

```py
def get_assert(output: str, context, threshold=4.5):
    article = context['vars']['article']
    score, evaluation = llm_eval(output, article )
    return {
        "pass": score >= threshold,
        "score": score,
        "reason": evaluation
    }
```

回憶一下我們在先前課程中提到的，promptfoo 會自動在斷言檔案中尋找名為 `get_assert` 的函式。它會傳入以下兩個參數：

- 來自特定模型回應的 `output`
- `context` 字典，包含產生該輸出的變數和提示

Promptfoo 期望我們的函式回傳以下其中一種：
- 布林值（通過/失敗）
- 浮點數（分數）
- GradingResult 字典

我們選擇回傳 GradingResult 字典，其中必須包含以下屬性：

- `pass`：布林值
- `score`：浮點數
- `reason`：說明字串

以下是附有註解的函式版本，說明其運作原理：

```py
def get_assert(output: str, context, threshold=4.5):
    # Get the specific article from the context
    article = context['vars']['article']
    #Pass the model output and the article to a function we've defined called llm_eval
    score, evaluation = llm_eval(output, article ) #capture the resulting score it returns and the evaluation explanation
    #return a dictionary indicating whether the output passed the test, its score, and the explanation behind the score
    return {
        "pass": score >= threshold,
        "score": score,
        "reason": evaluation
    }
```

### `llm_eval()`
接下來，讓我們仔細看看實際執行評分的 `llm_eval` 函式。這個函式執行以下操作：

1. 定義一個非常詳細的評分規則提示，說明摘要應如何評分
2. 透過向 Anthropic API 發送請求來執行評分提示
3. 解析回應並計算平均分數
4. 回傳平均分數和模型的完整文字回應

以下是完整程式碼：

```py
def llm_eval(summary, article):
    """
    Evaluate summary using an LLM (Claude).
    
    Args:
    summary (str): The summary to evaluate.
    article (str): The original text that was summarized.
    
    Returns:
    bool: True if the average score is above the threshold, False otherwise.
    """
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    prompt = f"""Evaluate the following summary based on these criteria:
    1. Conciseness (1-5) - is the summary as concise as possible?
        - Conciseness of 1: The summary is unnecessarily long, including excessive details, repetitions, or irrelevant information. It fails to distill the key points effectively.
        - Conciseness of 3:  The summary captures most key points but could be more focused. It may include some unnecessary details or slightly overexplain certain concepts.
        - Conciseness of 5: The summary effectively condenses the main ideas into a brief, focused text. It includes all essential information without any superfluous details or explanations.
    2. Accuracy (1-5) - is the summary completely accurate based on the initial article'?
        - Accuracy of 1: The summary contains significant errors, misrepresentations, or omissions that fundamentally alter the meaning or key points of the original article.
        - Accuracy of 3:  The summary captures some key points correctly but may have minor inaccuracies or omissions. The overall message is generally correct, but some details may be wrong.
        - Accuracy of 5: The summary faithfully represents the main gist of the original article without any errors or misinterpretations. All included information is correct and aligns with the source material.
    4. Tone (1-5) - is the summary appropriate for a grade school student with no technical training?
        - Tone of 1: The summary uses language or concepts that are too complex, technical, or mature for a grade school audience. It may contain jargon, advanced terminology, or themes that are not suitable for young readers.
        - Tone of 2:  The summary mostly uses language suitable for grade school students but occasionally includes terms or concepts that may be challenging. Some explanations might be needed for full comprehension.
        - Tone of 3: The summary consistently uses simple, clear language that is easily understandable by grade school students. It explains complex ideas in a way that is accessible and engaging for young readers.
    5. Explanation - a general description of the way the summary is evaluated

    <examples>
    <example>
    This summary:
    <summary>
    Artificial neural networks are computer systems inspired by how the human brain works. They are made up of interconnected "neurons" that process information. These networks can learn to do tasks by looking at lots of examples, similar to how humans learn. 

    Some key things about neural networks:
    - They can recognize patterns and make predictions
    - They improve with more data and practice
    - They're used for things like identifying objects in images, translating languages, and playing games

    Neural networks are a powerful tool in artificial intelligence and are behind many of the "smart" technologies we use today. While they can do amazing things, they still aren't as complex or capable as the human brain.
    <summary>
    Should receive a 5 for tone, a 5 for accuracy, and a 5 for conciseness
    </example>

    <example>
    This summary:
    <summary>
    Here is a summary of the key points from the article on artificial neural networks (ANNs):

    1. ANNs are computational models inspired by biological neural networks in animal brains. They consist of interconnected artificial neurons that process and transmit signals.

    2. Basic structure:
    - Input layer receives data
    - Hidden layers process information 
    - Output layer produces results
    - Neurons are connected by weighted edges

    3. Learning process:
    - ANNs learn by adjusting connection weights
    - Use techniques like backpropagation to minimize errors
    - Can perform supervised, unsupervised, and reinforcement learning

    4. Key developments:
    - Convolutional neural networks (CNNs) for image processing
    - Recurrent neural networks (RNNs) for sequential data
    - Deep learning with many hidden layers

    5. Applications:
    - Pattern recognition, classification, regression
    - Computer vision, speech recognition, natural language processing
    - Game playing, robotics, financial modeling

    6. Advantages:
    - Can model complex non-linear relationships
    - Ability to learn and generalize from data
    - Adaptable to many different types of problems

    7. Challenges:
    - Require large amounts of training data
    - Can be computationally intensive
    - "Black box" nature can make interpretability difficult

    8. Recent advances:
    - Improved hardware (GPUs) enabling deeper networks
    - New architectures like transformers for language tasks
    - Progress in areas like generative AI

    The article provides a comprehensive overview of ANN concepts, history, types, applications, and ongoing research areas in this field of artificial intelligence and machine learning.
    </summary>
    Should receive a 1 for tone, a 5 for accuracy, and a 3 for conciseness
    </example>
    </examples>

    Provide a score for each criterion in JSON format. Here is the format you should follow always:

    <json>
    {{
    "conciseness": <number>,
    "accuracy": <number>,
    "tone": <number>,
    "explanation": <string>,
    }}
    </json>


    Original Text: <original_article>{article}</original_article>
    
    Summary to Evaluate: <summary>{summary}</summary>
    """
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": "<json>" 
            }
        ],
        stop_sequences=["</json>"]
    )
    
    evaluation = json.loads(response.content[0].text)
    # Filter out non-numeric values and calculate the average
    numeric_values = [value for key, value in evaluation.items() if isinstance(value, (int, float))]
    avg_score = sum(numeric_values) / len(numeric_values)
    # Return the average score and the overall model response
    return avg_score, response.content[0].text
```

---

---

## 執行評估

我們使用之前見過的相同指令來執行評估：

```bash
npx promptfoo@latest eval
```
這個過程可能需要一段時間才能完成，因為我們先向模型發送初始請求以生成文章摘要，然後再發送額外的請求來評分這些摘要！

以下是我們得到的評估結果截圖：

![eval_result.png](images/eval_result.png)

讓我們啟動網頁視圖，更好地了解結果：

```bash
npx promptfoo@latest view
```
以下是網頁儀表板的截圖：

![web_view.png](images/web_view.png)

---

我們可以點擊每個儲存格中的放大鏡，查看測試結果的更多資訊：

![explanation.png](images/explanation.png)

我們可以看到這個特定的輸出未通過我們的自訂 llm-eval 函式，因為其語調分數非常低。

---

此外，結果的第一列顯示每個提示的評分摘要：

![overall_scores.png](images/overall_scores.png)

毫不意外地，`best_summary` 提示表現最佳！

---

儀表板頂部也顯示了一些圖表，幫助視覺化分數：

![distribution.png](images/distribution.png)

在上面的截圖中：

* 紅色是我們的 `basic_summarize` 提示
* 藍色是我們的 `better_summarize` 提示
* 綠色是我們的 `best_summarize` 提示

圖表顯示，`best_summarize` 提示不僅從未在我們的測試中失敗，在所有輸入上的分數也都高於其他提示。
