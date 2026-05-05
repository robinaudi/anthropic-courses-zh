# 第九章：從零開始構建複雜提示詞

- [課程](#lesson)
- [練習](#exercises)
- [範例練習場](#example-playground)

## 設定

執行以下設定儲存格以載入你的 API 金鑰並建立 `get_completion` 輔助函式。


```python
%pip install anthropic

# Import python's built-in regular expression library
import re
import anthropic

# Retrieve the API_KEY & MODEL_NAME variables from the IPython store
%store -r API_KEY
%store -r MODEL_NAME

client = anthropic.Anthropic(api_key=API_KEY)

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
```python
######################################## INPUT VARIABLES ########################################

# First input variable - the conversation history (this can also be added as preceding `user` and `assistant` messages in the API call)
HISTORY = """Customer: Give me two possible careers for sociology majors.

Joe: Here are two potential careers for sociology majors:

- Social worker - Sociology provides a strong foundation for understanding human behavior and social systems. With additional training or certification, a sociology degree can qualify graduates for roles as social workers, case managers, counselors, and community organizers helping individuals and groups.

- Human resources specialist - An understanding of group dynamics and organizational behavior from sociology is applicable to careers in human resources. Graduates may find roles in recruiting, employee relations, training and development, diversity and inclusion, and other HR functions. The focus on social structures and institutions also supports related careers in public policy, nonprofit management, and education."""

# Second input variable - the user's question
QUESTION = "Which of the two careers requires more than a Bachelor's degree?"

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = "You will be acting as an AI career coach named Joe created by the company AdAstra Careers. Your goal is to give career advice to users. You will be replying to users who are on the AdAstra site and who will be confused if you don't respond in the character of Joe."

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = "You should maintain a friendly customer service tone."

##### Prompt element 4: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = """Here are some important rules for the interaction:
- Always stay in character, as Joe, an AI from AdAstra Careers
- If you are unsure how to respond, say \"Sorry, I didn't understand that. Could you rephrase your question?\"
- If someone asks something irrelevant, say, \"Sorry, I am Joe and I give career advice. Do you have a career question today I can help you with?\""""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in <example></example> XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = """Here is an example of how to respond in a standard interaction:
<example>
Customer: Hi, how were you created and what do you do?
Joe: Hello! My name is Joe, and I was created by AdAstra Careers to give career advice. What can I help you with today?
</example>"""

##### Prompt element 6: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = f"""Here is the conversational history (between the user and you) prior to the question. It could be empty if there is no history:
<history>
{HISTORY}
</history>

Here is the user's question:
<question>
{QUESTION}
</question>"""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = "How do you respond to the user's question?"

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = "Think about your answer first before you respond."

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = "Put your response in <response></response> tags."

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
PREFILL = "[Joe] <response>"

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
```


---

## 課程

恭喜你來到最後一章！現在是時候把所有內容整合起來，學習如何**建立獨特且複雜的提示詞**。

在下面，你將使用我們為複雜提示詞推薦的**引導式結構**。在本章後半部分，我們將展示一些特定行業的提示詞，並說明這些提示詞是如何以相似方式構建的。

**注意：** **並非所有提示詞都需要以下複雜結構中的每個元素**。我們鼓勵你嘗試加入或移除各元素，看看這如何影響 Claude 的回應。通常**最好先使用多個提示詞元素讓提示詞正常運作，再進行精煉和精簡**。

### 範例 — 職涯教練聊天機器人

以下結構結合了多種提示詞工程元素，是複雜提示詞的良好起點。**某些元素的排序很重要**，其他則否。我們會說明最佳實踐對排序的要求，但一般來說，**只要遵循此排序，就是出色提示詞的好起點**。

在以下範例中，我們將為一個受控角色扮演場景構建提示詞，讓 Claude 承擔特定任務的情境角色。我們的目標是提示 Claude 扮演一位友善的職涯教練。

閱讀並執行下方儲存格，將各個提示詞元素組合成一個完整提示詞。


```python
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```
```python
######################################## INPUT VARIABLES ########################################

# First input variable - the legal document
LEGAL_RESEARCH = """<search_results>
<search_result id=1>
The animal health industry became caught up in a number of patent and trademark lawsuits during the past year. In 1994, Barclay Slocum obtained patents for the tibial plateau leveling osteotomy procedure, which is used in the treatment of dogs with cranial cruciate ligament rupture, and for the devices used in the procedure. During 2006, Slocum Enterprises filed a patent infringement suit against New Generation Devices, arguing that the Unity Cruciate Plate manufactured by New Generation infringed on the patent for the Slocum TPLO plate. However, the court never reached a decision on the issue of patent infringement, ruling that it did not have jurisdiction on the basis of the small number of plates sold in the state in which the case was filed and the information provided on a Web site maintained by Slocum Enterprises. Other patent battles waged during 2006 concerned the use of laser technology for onychectomy in cats, pet identification chips, pig vaccines, and pet “deshedding” tools.
</search_result>
<search_result id=2>
In Canada, the British Columbia Veterinary Medical Association brought suit against a nonveterinarian, claiming that he engaged in cutting or otherwise removing hooks from horses' teeth and floating horses' teeth with power and manual tools, provided advice and diagnoses in return for a fee, and held himself out as being qualified and willing to provide treatment with respect to these activities. The court held that the intention of the legislature in passing the Veterinary Profession Act was the protection of the public and animals and further held that monopolistic statutes serve the purpose of protecting the public. In addition, the court concluded that dentistry, at its core, relates to the health of the teeth and gums; is distinct from cosmetic and other types of care of animals; and, therefore, falls under the definition of the practice of veterinary medicine. The nonveterinarian was enjoined from providing services without a veterinarian supervising the procedures.
</search_result>
<search_result id=3>
The aftermath of Hurricane Katrina, which hit the Gulf Coast of the United States during 2005, spurred changes to the way animals are treated during natural disasters. In 2006, Hawaii, Louisiana, and New Hampshire all enacted laws that address issues regarding the care of animals during disasters, such as providing shelters for pets and allowing service animals to be kept with the people they serve. In addition, Congress passed, and the President signed, the Pet Evacuation and Transportation Standards Act during 2006, which requires state and local emergency preparedness authorities to include in their evacuation plans information on how they will accommodate household pets and service animals in case of a disaster. California passed a law that will require its Office of Emergency Services, Department of Agriculture, and other agencies involved with disaster response preparation to develop a plan for the needs of service animals, livestock, equids, and household pets in the event of a disaster or major emergency.
</search_result>
</search_results>"""

# Second input variable - the user's question
QUESTION = "Are there any laws about what to do with pets during a hurricane?"

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = "You are an expert lawyer."

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = ""

##### Prompt element 4: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = f"""Here is some research that's been compiled. Use it to answer a legal question from the user.
<legal_research>
{LEGAL_RESEARCH}
</legal_research>"""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in <example></example> XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = """When citing the legal research in your answer, please use brackets containing the search index ID, followed by a period. Put these at the end of the sentence that's doing the citing. Examples of proper citation format:

<examples>
<example>
The statute of limitations expires after 10 years for crimes like this. [3].
</example>
<example>
However, the protection does not apply when it has been specifically waived by both parties. [5].
</example>
</examples>"""

##### Prompt element 6: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = f"""Write a clear, concise answer to this question:

<question>
{QUESTION}
</question>

It should be no more than a couple of paragraphs. If possible, it should conclude with a single sentence directly answering the user's question. However, if there is not sufficient information in the compiled research to produce such an answer, you may demur and write "Sorry, I do not have sufficient information at hand to answer this question."."""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = ""

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = "Before you answer, pull out the most relevant quotes from the research in <relevant_quotes> tags."

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = "Put your two-paragraph response in <answer> tags."

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
PREFILL = "<relevant_quotes>"

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
```


現在來執行提示詞！執行下方儲存格查看 Claude 的輸出。


```python
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```
```python
######################################## INPUT VARIABLES ########################################

# First input variable - the user's question
QUESTION = "How long do I have to make an 83b election?"

# Second input variable - the tax code document that Claude will be using to answer the user's question
TAX_CODE = """
(a)General rule
If, in connection with the performance of services, property is transferred to any person other than the person for whom such services are performed, the excess of—
(1)the fair market value of such property (determined without regard to any restriction other than a restriction which by its terms will never lapse) at the first time the rights of the person having the beneficial interest in such property are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier, over
(2)the amount (if any) paid for such property,
shall be included in the gross income of the person who performed such services in the first taxable year in which the rights of the person having the beneficial interest in such property are transferable or are not subject to a substantial risk of forfeiture, whichever is applicable. The preceding sentence shall not apply if such person sells or otherwise disposes of such property in an arm’s length transaction before his rights in such property become transferable or not subject to a substantial risk of forfeiture.
(b)Election to include in gross income in year of transfer
(1)In general
Any person who performs services in connection with which property is transferred to any person may elect to include in his gross income for the taxable year in which such property is transferred, the excess of—
(A)the fair market value of such property at the time of transfer (determined without regard to any restriction other than a restriction which by its terms will never lapse), over
(B)the amount (if any) paid for such property.
If such election is made, subsection (a) shall not apply with respect to the transfer of such property, and if such property is subsequently forfeited, no deduction shall be allowed in respect of such forfeiture.
(2)Election
An election under paragraph (1) with respect to any transfer of property shall be made in such manner as the Secretary prescribes and shall be made not later than 30 days after the date of such transfer. Such election may not be revoked except with the consent of the Secretary.

(c)Special rules
For purposes of this section—
(1)Substantial risk of forfeiture
The rights of a person in property are subject to a substantial risk of forfeiture if such person’s rights to full enjoyment of such property are conditioned upon the future performance of substantial services by any individual.

(2)Transferability of property
The rights of a person in property are transferable only if the rights in such property of any transferee are not subject to a substantial risk of forfeiture.

(3)Sales which may give rise to suit under section 16(b) of the Securities Exchange Act of 1934
So long as the sale of property at a profit could subject a person to suit under section 16(b) of the Securities Exchange Act of 1934, such person’s rights in such property are—
(A)subject to a substantial risk of forfeiture, and
(B)not transferable.
(4)For purposes of determining an individual’s basis in property transferred in connection with the performance of services, rules similar to the rules of section 72(w) shall apply.
(d)Certain restrictions which will never lapse
(1)Valuation
In the case of property subject to a restriction which by its terms will never lapse, and which allows the transferee to sell such property only at a price determined under a formula, the price so determined shall be deemed to be the fair market value of the property unless established to the contrary by the Secretary, and the burden of proof shall be on the Secretary with respect to such value.

(2)Cancellation
If, in the case of property subject to a restriction which by its terms will never lapse, the restriction is canceled, then, unless the taxpayer establishes—
(A)that such cancellation was not compensatory, and
(B)that the person, if any, who would be allowed a deduction if the cancellation were treated as compensatory, will treat the transaction as not compensatory, as evidenced in such manner as the Secretary shall prescribe by regulations,
the excess of the fair market value of the property (computed without regard to the restrictions) at the time of cancellation over the sum of—
(C)the fair market value of such property (computed by taking the restriction into account) immediately before the cancellation, and
(D)the amount, if any, paid for the cancellation,
shall be treated as compensation for the taxable year in which such cancellation occurs.
(e)Applicability of section
This section shall not apply to—
(1)a transaction to which section 421 applies,
(2)a transfer to or from a trust described in section 401(a) or a transfer under an annuity plan which meets the requirements of section 404(a)(2),
(3)the transfer of an option without a readily ascertainable fair market value,
(4)the transfer of property pursuant to the exercise of an option with a readily ascertainable fair market value at the date of grant, or
(5)group-term life insurance to which section 79 applies.
(f)Holding period
In determining the period for which the taxpayer has held property to which subsection (a) applies, there shall be included only the period beginning at the first time his rights in such property are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier.

(g)Certain exchanges
If property to which subsection (a) applies is exchanged for property subject to restrictions and conditions substantially similar to those to which the property given in such exchange was subject, and if section 354, 355, 356, or 1036 (or so much of section 1031 as relates to section 1036) applied to such exchange, or if such exchange was pursuant to the exercise of a conversion privilege—
(1)such exchange shall be disregarded for purposes of subsection (a), and
(2)the property received shall be treated as property to which subsection (a) applies.
(h)Deduction by employer
In the case of a transfer of property to which this section applies or a cancellation of a restriction described in subsection (d), there shall be allowed as a deduction under section 162, to the person for whom were performed the services in connection with which such property was transferred, an amount equal to the amount included under subsection (a), (b), or (d)(2) in the gross income of the person who performed such services. Such deduction shall be allowed for the taxable year of such person in which or with which ends the taxable year in which such amount is included in the gross income of the person who performed such services.

(i)Qualified equity grants
(1)In general
For purposes of this subtitle—
(A)Timing of inclusion
If qualified stock is transferred to a qualified employee who makes an election with respect to such stock under this subsection, subsection (a) shall be applied by including the amount determined under such subsection with respect to such stock in income of the employee in the taxable year determined under subparagraph (B) in lieu of the taxable year described in subsection (a).

(B)Taxable year determined
The taxable year determined under this subparagraph is the taxable year of the employee which includes the earliest of—
(i)the first date such qualified stock becomes transferable (including, solely for purposes of this clause, becoming transferable to the employer),
(ii)the date the employee first becomes an excluded employee,
(iii)the first date on which any stock of the corporation which issued the qualified stock becomes readily tradable on an established securities market (as determined by the Secretary, but not including any market unless such market is recognized as an established securities market by the Secretary for purposes of a provision of this title other than this subsection),
(iv)the date that is 5 years after the first date the rights of the employee in such stock are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier, or
(v)the date on which the employee revokes (at such time and in such manner as the Secretary provides) the election under this subsection with respect to such stock.
(2)Qualified stock
(A)In general
For purposes of this subsection, the term “qualified stock” means, with respect to any qualified employee, any stock in a corporation which is the employer of such employee, if—
(i)such stock is received—
(I)in connection with the exercise of an option, or
(II)in settlement of a restricted stock unit, and
(ii)such option or restricted stock unit was granted by the corporation—
(I)in connection with the performance of services as an employee, and
(II)during a calendar year in which such corporation was an eligible corporation.
(B)Limitation
The term “qualified stock” shall not include any stock if the employee may sell such stock to, or otherwise receive cash in lieu of stock from, the corporation at the time that the rights of the employee in such stock first become transferable or not subject to a substantial risk of forfeiture.

(C)Eligible corporation
For purposes of subparagraph (A)(ii)(II)—
(i)In general
The term “eligible corporation” means, with respect to any calendar year, any corporation if—
(I)no stock of such corporation (or any predecessor of such corporation) is readily tradable on an established securities market (as determined under paragraph (1)(B)(iii)) during any preceding calendar year, and
(II)such corporation has a written plan under which, in such calendar year, not less than 80 percent of all employees who provide services to such corporation in the United States (or any possession of the United States) are granted stock options, or are granted restricted stock units, with the same rights and privileges to receive qualified stock.
(ii)Same rights and privileges
For purposes of clause (i)(II)—
(I)except as provided in subclauses (II) and (III), the determination of rights and privileges with respect to stock shall be made in a similar manner as under section 423(b)(5),
(II)employees shall not fail to be treated as having the same rights and privileges to receive qualified stock solely because the number of shares available to all employees is not equal in amount, so long as the number of shares available to each employee is more than a de minimis amount, and
(III)rights and privileges with respect to the exercise of an option shall not be treated as the same as rights and privileges with respect to the settlement of a restricted stock unit.
(iii)Employee
For purposes of clause (i)(II), the term “employee” shall not include any employee described in section 4980E(d)(4) or any excluded employee.

(iv)Special rule for calendar years before 2018
In the case of any calendar year beginning before January 1, 2018, clause (i)(II) shall be applied without regard to whether the rights and privileges with respect to the qualified stock are the same.

(3)Qualified employee; excluded employee
For purposes of this subsection—
(A)In general
The term “qualified employee” means any individual who—
(i)is not an excluded employee, and
(ii)agrees in the election made under this subsection to meet such requirements as are determined by the Secretary to be necessary to ensure that the withholding requirements of the corporation under chapter 24 with respect to the qualified stock are met.
(B)Excluded employee
The term “excluded employee” means, with respect to any corporation, any individual—
(i)who is a 1-percent owner (within the meaning of section 416(i)(1)(B)(ii)) at any time during the calendar year or who was such a 1 percent owner at any time during the 10 preceding calendar years,
(ii)who is or has been at any prior time—
(I)the chief executive officer of such corporation or an individual acting in such a capacity, or
(II)the chief financial officer of such corporation or an individual acting in such a capacity,
(iii)who bears a relationship described in section 318(a)(1) to any individual described in subclause (I) or (II) of clause (ii), or
(iv)who is one of the 4 highest compensated officers of such corporation for the taxable year, or was one of the 4 highest compensated officers of such corporation for any of the 10 preceding taxable years, determined with respect to each such taxable year on the basis of the shareholder disclosure rules for compensation under the Securities Exchange Act of 1934 (as if such rules applied to such corporation).
(4)Election
(A)Time for making election
An election with respect to qualified stock shall be made under this subsection no later than 30 days after the first date the rights of the employee in such stock are transferable or are not subject to a substantial risk of forfeiture, whichever occurs earlier, and shall be made in a manner similar to the manner in which an election is made under subsection (b).

(B)Limitations
No election may be made under this section with respect to any qualified stock if—
(i)the qualified employee has made an election under subsection (b) with respect to such qualified stock,
(ii)any stock of the corporation which issued the qualified stock is readily tradable on an established securities market (as determined under paragraph (1)(B)(iii)) at any time before the election is made, or
(iii)such corporation purchased any of its outstanding stock in the calendar year preceding the calendar year which includes the first date the rights of the employee in such stock are transferable or are not subject to a substantial risk of forfeiture, unless—
(I)not less than 25 percent of the total dollar amount of the stock so purchased is deferral stock, and
(II)the determination of which individuals from whom deferral stock is purchased is made on a reasonable basis.
(C)Definitions and special rules related to limitation on stock redemptions
(i)Deferral stock
For purposes of this paragraph, the term “deferral stock” means stock with respect to which an election is in effect under this subsection.

(ii)Deferral stock with respect to any individual not taken into account if individual holds deferral stock with longer deferral period
Stock purchased by a corporation from any individual shall not be treated as deferral stock for purposes of subparagraph (B)(iii) if such individual (immediately after such purchase) holds any deferral stock with respect to which an election has been in effect under this subsection for a longer period than the election with respect to the stock so purchased.

(iii)Purchase of all outstanding deferral stock
The requirements of subclauses (I) and (II) of subparagraph (B)(iii) shall be treated as met if the stock so purchased includes all of the corporation’s outstanding deferral stock.

(iv)Reporting
Any corporation which has outstanding deferral stock as of the beginning of any calendar year and which purchases any of its outstanding stock during such calendar year shall include on its return of tax for the taxable year in which, or with which, such calendar year ends the total dollar amount of its outstanding stock so purchased during such calendar year and such other information as the Secretary requires for purposes of administering this paragraph.

(5)Controlled groups
For purposes of this subsection, all persons treated as a single employer under section 414(b) shall be treated as 1 corporation.

(6)Notice requirement
Any corporation which transfers qualified stock to a qualified employee shall, at the time that (or a reasonable period before) an amount attributable to such stock would (but for this subsection) first be includible in the gross income of such employee—
(A)certify to such employee that such stock is qualified stock, and
(B)notify such employee—
(i)that the employee may be eligible to elect to defer income on such stock under this subsection, and
(ii)that, if the employee makes such an election—
(I)the amount of income recognized at the end of the deferral period will be based on the value of the stock at the time at which the rights of the employee in such stock first become transferable or not subject to substantial risk of forfeiture, notwithstanding whether the value of the stock has declined during the deferral period,
(II)the amount of such income recognized at the end of the deferral period will be subject to withholding under section 3401(i) at the rate determined under section 3402(t), and
(III)the responsibilities of the employee (as determined by the Secretary under paragraph (3)(A)(ii)) with respect to such withholding.
(7)Restricted stock units
This section (other than this subsection), including any election under subsection (b), shall not apply to restricted stock units.
"""

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = ""

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = ""

##### Prompt element 4: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = ""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in <example></example> XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = ""

##### Prompt element 6: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = ""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = ""

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = ""

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = ""

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
PREFILL = ""

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```


### 範例 — 法律服務

**法律行業的提示詞可能相當複雜**，因為需要：
- 解析長篇文件
- 處理複雜主題
- 以非常特定的方式格式化輸出
- 遵循多步驟分析流程

讓我們看看如何使用複雜提示詞範本來建構特定法律使用情境的提示詞。下方我們為法律使用情境提供了一個範例提示詞，讓 Claude 根據法律文件中的資訊回答法律問題。

我們**調整了幾個元素的排序**，以展示提示詞結構可以靈活調整！

**提示詞工程是關於科學的試驗與錯誤**。我們鼓勵你混搭、移動（排序不重要的元素），找出最適合你和你需求的方式。


```python
from hints import exercise_9_1_solution; print(exercise_9_1_solution)
```
```python
######################################## INPUT VARIABLES ########################################

# Input variable - the code that Claude needs to read and assist the user with correcting
CODE = """
# Function to print multiplicative inverses
def print_multiplicative_inverses(x, n):
  for i in range(n):
    print(x / i) 
"""

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = ""

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = ""

##### Prompt element 4: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = ""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in <example></example> XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = ""

##### Prompt element 6: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = ""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = ""

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = ""

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = ""

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
PREFILL = ""

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```


現在來執行提示詞！執行下方儲存格查看 Claude 的輸出。


```python
from hints import exercise_9_2_solution; print(exercise_9_2_solution)
```
```python
# Prompt
PROMPT = "Write an ode to a fabulous student who has just completed a course on prompt engineering, in the form of a sonnet."

# Print Claude's response
print(get_completion(PROMPT))
```


如果你想在不更改上方任何內容的情況下試驗課程提示詞，請捲動到課程 notebook 的最底部訪問[**範例練習場**](#example-playground)。

---

## 練習
- [練習 9.1 — 金融服務聊天機器人](#exercise-91---financial-services-chatbot)
- [練習 9.2 — 程式碼機器人](#exercise-92---codebot)

### 練習 9.1 — 金融服務聊天機器人
金融行業的提示詞也可能相當複雜，原因與法律提示詞類似。這是一個金融使用情境的練習，讓 Claude **分析稅務資訊並回答問題**。就像法律服務範例一樣，我們調整了幾個元素的排序，因為我們的解答提示詞在不同流程下更合理（不過其他結構也適用）。

我們建議你閱讀變數內容（此例為 `{QUESTION}` 和 `{TAX_CODE}`），了解 Claude 預期處理的內容。請確保在你的提示詞中直接引用 `{QUESTION}` 和 `{TAX_CODE}`（使用像其他範例中的 f-string 語法），以便實際變數內容可以被替換進去。

在提示詞元素欄位中填入符合描述及前面複雜提示詞範例的內容。填完所有你想填的提示詞元素後，執行儲存格查看串接後的提示詞及 Claude 的回應。

記住，提示詞工程很少是純粹按公式的，尤其是大型複雜提示詞！重要的是開發測試案例，並**嘗試各種提示詞和提示詞結構，看看哪種最適合每種情況**。注意，如果你*確實*改變了提示詞元素的排序，你也應該記得更改 `COMBINE ELEMENTS` 段落中串接的排序。


```python
######################################## INPUT VARIABLES ########################################

# First input variable - the conversation history (this can also be added as preceding `user` and `assistant` messages in the API call)
HISTORY = """Customer: Give me two possible careers for sociology majors.

Joe: Here are two potential careers for sociology majors:

- Social worker - Sociology provides a strong foundation for understanding human behavior and social systems. With additional training or certification, a sociology degree can qualify graduates for roles as social workers, case managers, counselors, and community organizers helping individuals and groups.

- Human resources specialist - An understanding of group dynamics and organizational behavior from sociology is applicable to careers in human resources. Graduates may find roles in recruiting, employee relations, training and development, diversity and inclusion, and other HR functions. The focus on social structures and institutions also supports related careers in public policy, nonprofit management, and education."""

# Second input variable - the user's question
QUESTION = "Which of the two careers requires more than a Bachelor's degree?"

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = "You will be acting as an AI career coach named Joe created by the company AdAstra Careers. Your goal is to give career advice to users. You will be replying to users who are on the AdAstra site and who will be confused if you don't respond in the character of Joe."

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = "You should maintain a friendly customer service tone."

##### Prompt element 4: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = """Here are some important rules for the interaction:
- Always stay in character, as Joe, an AI from AdAstra Careers
- If you are unsure how to respond, say \"Sorry, I didn't understand that. Could you rephrase your question?\"
- If someone asks something irrelevant, say, \"Sorry, I am Joe and I give career advice. Do you have a career question today I can help you with?\""""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in <example></example> XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = """Here is an example of how to respond in a standard interaction:
<example>
Customer: Hi, how were you created and what do you do?
Joe: Hello! My name is Joe, and I was created by AdAstra Careers to give career advice. What can I help you with today?
</example>"""

##### Prompt element 6: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = f"""Here is the conversational history (between the user and you) prior to the question. It could be empty if there is no history:
<history>
{HISTORY}
</history>

Here is the user's question:
<question>
{QUESTION}
</question>"""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = "How do you respond to the user's question?"

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = "Think about your answer first before you respond."

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = "Put your response in <response></response> tags."

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
PREFILL = "[Joe] <response>"

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```
```python
######################################## INPUT VARIABLES ########################################

# First input variable - the legal document
LEGAL_RESEARCH = """<search_results>
<search_result id=1>
The animal health industry became caught up in a number of patent and trademark lawsuits during the past year. In 1994, Barclay Slocum obtained patents for the tibial plateau leveling osteotomy procedure, which is used in the treatment of dogs with cranial cruciate ligament rupture, and for the devices used in the procedure. During 2006, Slocum Enterprises filed a patent infringement suit against New Generation Devices, arguing that the Unity Cruciate Plate manufactured by New Generation infringed on the patent for the Slocum TPLO plate. However, the court never reached a decision on the issue of patent infringement, ruling that it did not have jurisdiction on the basis of the small number of plates sold in the state in which the case was filed and the information provided on a Web site maintained by Slocum Enterprises. Other patent battles waged during 2006 concerned the use of laser technology for onychectomy in cats, pet identification chips, pig vaccines, and pet “deshedding” tools.
</search_result>
<search_result id=2>
In Canada, the British Columbia Veterinary Medical Association brought suit against a nonveterinarian, claiming that he engaged in cutting or otherwise removing hooks from horses' teeth and floating horses' teeth with power and manual tools, provided advice and diagnoses in return for a fee, and held himself out as being qualified and willing to provide treatment with respect to these activities. The court held that the intention of the legislature in passing the Veterinary Profession Act was the protection of the public and animals and further held that monopolistic statutes serve the purpose of protecting the public. In addition, the court concluded that dentistry, at its core, relates to the health of the teeth and gums; is distinct from cosmetic and other types of care of animals; and, therefore, falls under the definition of the practice of veterinary medicine. The nonveterinarian was enjoined from providing services without a veterinarian supervising the procedures.
</search_result>
<search_result id=3>
The aftermath of Hurricane Katrina, which hit the Gulf Coast of the United States during 2005, spurred changes to the way animals are treated during natural disasters. In 2006, Hawaii, Louisiana, and New Hampshire all enacted laws that address issues regarding the care of animals during disasters, such as providing shelters for pets and allowing service animals to be kept with the people they serve. In addition, Congress passed, and the President signed, the Pet Evacuation and Transportation Standards Act during 2006, which requires state and local emergency preparedness authorities to include in their evacuation plans information on how they will accommodate household pets and service animals in case of a disaster. California passed a law that will require its Office of Emergency Services, Department of Agriculture, and other agencies involved with disaster response preparation to develop a plan for the needs of service animals, livestock, equids, and household pets in the event of a disaster or major emergency.
</search_result>
</search_results>"""

# Second input variable - the user's question
QUESTION = "Are there any laws about what to do with pets during a hurricane?"

######################################## PROMPT ELEMENTS ########################################

##### Prompt element 1: `user` role
# Make sure that your Messages API call always starts with a `user` role in the messages array.
# The get_completion() function as defined above will automatically do this for you.

##### Prompt element 2: Task context
# Give Claude context about the role it should take on or what goals and overarching tasks you want it to undertake with the prompt.
# It's best to put context early in the body of the prompt.
TASK_CONTEXT = "You are an expert lawyer."

##### Prompt element 3: Tone context
# If important to the interaction, tell Claude what tone it should use.
# This element may not be necessary depending on the task.
TONE_CONTEXT = ""

##### Prompt element 4: Input data to process
# If there is data that Claude needs to process within the prompt, include it here within relevant XML tags.
# Feel free to include multiple pieces of data, but be sure to enclose each in its own set of XML tags.
# This element may not be necessary depending on task. Ordering is also flexible.
INPUT_DATA = f"""Here is some research that's been compiled. Use it to answer a legal question from the user.
<legal_research>
{LEGAL_RESEARCH}
</legal_research>"""

##### Prompt element 5: Examples
# Provide Claude with at least one example of an ideal response that it can emulate. Encase this in <example></example> XML tags. Feel free to provide multiple examples.
# If you do provide multiple examples, give Claude context about what it is an example of, and enclose each example in its own set of XML tags.
# Examples are probably the single most effective tool in knowledge work for getting Claude to behave as desired.
# Make sure to give Claude examples of common edge cases. If your prompt uses a scratchpad, it's effective to give examples of how the scratchpad should look.
# Generally more examples = better.
EXAMPLES = """When citing the legal research in your answer, please use brackets containing the search index ID, followed by a period. Put these at the end of the sentence that's doing the citing. Examples of proper citation format:

<examples>
<example>
The statute of limitations expires after 10 years for crimes like this. [3].
</example>
<example>
However, the protection does not apply when it has been specifically waived by both parties. [5].
</example>
</examples>"""

##### Prompt element 6: Detailed task description and rules
# Expand on the specific tasks you want Claude to do, as well as any rules that Claude might have to follow.
# This is also where you can give Claude an "out" if it doesn't have an answer or doesn't know.
# It's ideal to show this description and rules to a friend to make sure it is laid out logically and that any ambiguous words are clearly defined.
TASK_DESCRIPTION = """Write a clear, concise answer to this question:

<question>
{QUESTION}
</question>

It should be no more than a couple of paragraphs. If possible, it should conclude with a single sentence directly answering the user's question. However, if there is not sufficient information in the compiled research to produce such an answer, you may demur and write "Sorry, I do not have sufficient information at hand to answer this question."."""

##### Prompt element 7: Immediate task description or request #####
# "Remind" Claude or tell Claude exactly what it's expected to immediately do to fulfill the prompt's task.
# This is also where you would put in additional variables like the user's question.
# It generally doesn't hurt to reiterate to Claude its immediate task. It's best to do this toward the end of a long prompt.
# This will yield better results than putting this at the beginning.
# It is also generally good practice to put the user's query close to the bottom of the prompt.
IMMEDIATE_TASK = ""

##### Prompt element 8: Precognition (thinking step by step)
# For tasks with multiple steps, it's good to tell Claude to think step by step before giving an answer
# Sometimes, you might have to even say "Before you give your answer..." just to make sure Claude does this first.
# Not necessary with all prompts, though if included, it's best to do this toward the end of a long prompt and right after the final immediate task request or description.
PRECOGNITION = "Before you answer, pull out the most relevant quotes from the research in <relevant_quotes> tags."

##### Prompt element 9: Output formatting
# If there is a specific way you want Claude's response formatted, clearly tell Claude what that format is.
# This element may not be necessary depending on the task.
# If you include it, putting it toward the end of the prompt is better than at the beginning.
OUTPUT_FORMATTING = "Put your two-paragraph response in <answer> tags."

##### Prompt element 10: Prefilling Claude's response (if any)
# A space to start off Claude's answer with some prefilled words to steer Claude's behavior or response.
# If you want to prefill Claude's response, you must put this in the `assistant` role in the API call.
# This element may not be necessary depending on the task.
PREFILL = "<relevant_quotes>"

######################################## COMBINE ELEMENTS ########################################

PROMPT = ""

if TASK_CONTEXT:
    PROMPT += f"""{TASK_CONTEXT}"""

if TONE_CONTEXT:
    PROMPT += f"""\n\n{TONE_CONTEXT}"""

if INPUT_DATA:
    PROMPT += f"""\n\n{INPUT_DATA}"""

if EXAMPLES:
    PROMPT += f"""\n\n{EXAMPLES}"""

if TASK_DESCRIPTION:
    PROMPT += f"""\n\n{TASK_DESCRIPTION}"""

if IMMEDIATE_TASK:
    PROMPT += f"""\n\n{IMMEDIATE_TASK}"""

if PRECOGNITION:
    PROMPT += f"""\n\n{PRECOGNITION}"""

if OUTPUT_FORMATTING:
    PROMPT += f"""\n\n{OUTPUT_FORMATTING}"""

# Print full prompt
print("--------------------------- Full prompt with variable substutions ---------------------------")
print("USER TURN")
print(PROMPT)
print("\nASSISTANT TURN")
print(PREFILL)
print("\n------------------------------------- Claude's response -------------------------------------")
print(get_completion(PROMPT, prefill=PREFILL))
```


❓ 如果你想查看可能的解答，執行下方儲存格！





### 練習 9.2 — 程式碼機器人
在此練習中，我們將為一個**能閱讀程式碼並在適當時提供引導性修正的程式碼輔助與教學機器人**撰寫提示詞。在提示詞元素欄位中填入符合描述及前面複雜提示詞範例的內容。填完所有你想填的提示詞元素後，執行儲存格查看串接後的提示詞及 Claude 的回應。

我們建議你閱讀變數內容（此例為 `{CODE}`），了解 Claude 預期處理的內容。請確保在你的提示詞中直接引用 `{CODE}`（使用像其他範例中的 f-string 語法），以便實際變數內容可以被替換進去。





❓ 如果你想查看可能的解答，執行下方儲存格！





---

## 恭喜，繼續前進！

如果你完成了所有練習，**你現在已躋身 LLM 低語者中的頂尖 0.1%**。精英之一！

你所學到的技術——從逐步思考、指派角色、使用範例到整體清晰的寫作——可以**以無數方式合併、重組和調整**。

提示詞工程是一門非常新的學科，請保持開放的心態。你可能就是發現下一個偉大提示技巧的人。

如果你想看**更多好的提示詞範例**以獲取靈感：
- 從我們的 [cookbook](https://anthropic.com/cookbook) 中學習生產就緒的提示詞範例
- 閱讀我們的[提示詞指南](https://docs.anthropic.com/claude/docs/prompt-engineering)
- 查看我們的[提示詞庫](https://anthropic.com/prompts)獲取靈感
- 嘗試我們的實驗性 [metaprompt](https://docs.anthropic.com/claude/docs/helper-metaprompt-experimental)，讓 Claude 為你撰寫提示詞範本！
- 在我們的 [discord 伺服器](https://anthropic.com/discord)提問
- 了解[Anthropic API 參數](https://docs.anthropic.com/claude/reference/complete_post)，如 temperature 和 `max_tokens`
- 如果你有學術興趣，可以閱讀一些提示詞工程的[論文](https://www.promptingguide.ai/papers)
- 練習構建提示詞，讓 Claude 做你感興趣的事

如果你想了解本教程範圍之外的一些真正進階提示詞技術，請點擊進入附錄！但首先，執行下方儲存格。





---

## 範例練習場

這是一個讓你自由試驗本課程所示提示詞範例並調整提示詞的區域，看看這如何影響 Claude 的回應。





