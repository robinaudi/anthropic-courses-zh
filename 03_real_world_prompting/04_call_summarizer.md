# 第四課：客服通話摘要工具

在本課中，我們將為一個常見的客戶使用案例撰寫一個複雜的提示：摘要。具體而言，我們將摘要冗長的客服通話記錄。我們的目標是為客服支援指標生成摘要，對完整的客服通話進行摘要，以評估客服團隊的效能。這意味著我們將排除有連線問題、語言障礙和其他妨礙有效摘要的通話。

讓我們假設我們在 Acme Corporation 工作，這是一家銷售智慧家居裝置的公司。公司每天處理數百通客服電話，需要一種方式將這些對話快速轉化為**有用的結構化資料**。

一些重要的考量包括：
* 通話可能短而簡單，也可能長而複雜。
* 客戶可能致電詢問從簡單的 Wi-Fi 連線問題到複雜的系統故障等各種情況。
* 我們需要特定格式的摘要，以便後續分析。
* 我們必須謹慎，不在摘要中包含任何客戶個人資訊。

為了協助我們完成任務，我們將遵循先前描述的最佳實踐：
* 使用系統提示設定背景脈絡。
* 結構化提示以達到最佳表現。
* 給出清楚的指令並定義所需的輸出。
* 使用 XML 標籤組織資訊。
* 處理特殊情況和邊緣案例。
* 提供範例來引導模型。

---

## 了解資料

現在我們了解了任務，讓我們看看將要處理的資料。在本課中，我們將使用各種模擬的客服通話記錄，來自 Acme Corporation 智慧家居裝置支援團隊。這些記錄將幫助我們建立一個能處理不同情境的強健提示。

讓我們看看可能遇到的通話記錄類型：

一個簡短且簡單的記錄：

```python
call1 = """
Agent: Thank you for calling Acme Smart Home Support. This is Alex. How can I help you?
Customer: Hi, I can't turn on my smart light bulb.
Agent: I see. Have you tried resetting the bulb?
Customer: Oh, no. How do I do that?
Agent: Just turn the power off for 5 seconds, then back on. It should reset.
Customer: Ok, I'll try that. Thanks!
Agent: You're welcome. Call us back if you need further assistance.
"""
```

一個中等長度、最終解決問題的記錄：

```python
call2 = """
Agent: Acme Smart Home Support, this is Jamie. How may I assist you today?
Customer: Hi Jamie, my Acme SmartTherm isn't maintaining the temperature I set. It's set to 72 but the house is much warmer.
Agent: I'm sorry to hear that. Let's troubleshoot. Is your SmartTherm connected to Wi-Fi?
Customer: Yes, the Wi-Fi symbol is showing on the display.
Agent: Great. Let's recalibrate your SmartTherm. Press and hold the menu button for 5 seconds.
Customer: Okay, done. A new menu came up.
Agent: Perfect. Navigate to "Calibration" and press select. Adjust the temperature to match your room thermometer.
Customer: Alright, I've set it to 79 degrees to match.
Agent: Great. Press select to confirm. It will recalibrate, which may take a few minutes. Check back in an hour to see if it's fixed.
Customer: Okay, I'll do that. Thank you for your help, Jamie.
Agent: You're welcome! Is there anything else I can assist you with today?
Customer: No, that's all. Thanks again.
Agent: Thank you for choosing Acme Smart Home. Have a great day!
"""
```

一個較長且未解決問題的通話：

```python
call3 = """
Agent: Thank you for contacting Acme Smart Home Support. This is Sarah. How can I help you today?
Customer: Hi Sarah, I'm having trouble with my Acme SecureHome system. The alarm keeps going off randomly.
Agent: I'm sorry to hear that. Can you tell me when this started happening?
Customer: It started about two days ago. It's gone off three times now, always in the middle of the night.
Agent: I see. Are there any error messages on the control panel when this happens?
Customer: No, I didn't notice any. But I was pretty groggy each time.
Agent: Understood. Let's check a few things. First, can you confirm that all your doors and windows are closing properly?
Customer: Yes, I've checked all of them. They're fine.
Agent: Okay. Next, let's check the battery in your control panel. Can you tell me if the low battery indicator is on?
Customer: Give me a moment... No, the battery indicator looks normal.
Agent: Alright. It's possible that one of your sensors is malfunctioning. I'd like to run a diagnostic, but I'll need to transfer you to our technical team for that. Is that okay?
Customer: Yes, that's fine. I just want this fixed. It's really disruptive.
Agent: I completely understand. I'm going to transfer you now. They'll be able to run a full system diagnostic and hopefully resolve the issue for you.
Customer: Okay, thank you.
Agent: You're welcome. Thank you for your patience, and I hope you have a great rest of your day.
"""
```

這些範例展示了我們需要處理的通話多樣性：
* 通話長度差異懸殊。
* 通話涉及各種支援問題（簡單修復、裝置故障、複雜問題）。
* 有些通話以解決問題作結，有些則是未解決的待辦案例。
* 有些通話需要後續跟進。

在建立提示時，我們需要確保它能有效摘要所有這些類型的通話，提取關鍵資訊並以一致、結構化的格式呈現。
在下一節中，我們將開始逐步建立提示，以處理這些多樣化的通話記錄。

---

## 簡易版提示
現在我們了解了任務和要處理的資料類型，讓我們開始建立提示。我們將從基本版本開始，逐步精煉以處理通話摘要任務的複雜性。

讓我們從這個非常簡單、概述基本任務的提示開始：

```python
prompt = """
Summarize the following customer service call transcript. Focus on the main issue, how it was resolved, and any required follow-up.

{transcript}
"""
```

這個基本提示給了 Claude 一個大致的方向，但有幾個局限性：

* 未指定所需的輸出格式，可能導致摘要不一致。
* 未提供如何處理不同情境的指引（例如未解決問題或資訊不足的情況）。
* 未對長度或內容設定任何限制，可能導致摘要過長或過於詳細。
* 未指示 Claude 省略個人資訊，可能引發隱私問題。

話雖如此，讓我們先測試一下，了解它的表現：

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

def summarize_call(transcript):
    final_prompt = prompt.format(transcript=transcript)
    # Make the API call
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )
    print(response.content[0].text)
```

```python
summarize_call(call1)
```

```
Here is a summary of the customer service call transcript:

Main Issue:
The customer was unable to turn on their Acme smart light bulb.

Resolution:
The service agent instructed the customer to reset the bulb by turning the power off for 5 seconds and then back on. This should reset the bulb and allow it to turn on.

Follow-Up:
The agent told the customer to call back if they continued to have issues after trying the reset procedure. No other follow-up was mentioned.
```

```python
summarize_call(call2)
```

```
Summary:

Main Issue: The customer's Acme SmartTherm thermostat was not maintaining the set temperature of 72°F, and the house was much warmer.

Resolution: The agent guided the customer through the process of recalibrating the SmartTherm thermostat. This involved accessing the "Calibration" menu, adjusting the temperature to match the customer's room thermometer (79°F in this case), and confirming the new setting. The recalibration process may take a few minutes to complete.

Follow-up Required: The customer was advised to check the thermostat in an hour to see if the issue was resolved after the recalibration process completed.
```

```python
summarize_call(call3)
```

```
Here is a summary of the customer service call transcript:

Main Issue:
The customer was having an issue with their Acme SecureHome alarm system going off randomly in the middle of the night, even though all doors and windows were closed properly.

How It Was Resolved:
The customer service agent first had the customer check for any error messages on the control panel and confirm that the battery was not low. When those basic troubleshooting steps did not reveal the issue, the agent determined that one of the sensors may be malfunctioning and needed to transfer the customer to the technical support team for a full system diagnostic.

Required Follow-Up:
The technical support team needs to run a diagnostic on the customer's SecureHome system to identify which sensor(s) may be causing the false alarms and then repair or replace those components. The customer should be contacted again once the diagnostic is complete and the repair/replacement has been performed to ensure the random alarms have been resolved.
```

如你所見，雖然 Claude 確實提供了摘要，但格式不適合系統性分析。摘要可能過長或過短，且未必一致涵蓋我們所關注的所有要點。


在接下來的步驟中，我們將開始在提示中加入更多結構和指引，以解決這些局限性。我們將看到每項新增內容如何提升 Claude 摘要的品質和一致性。

請記住，提示工程是一個迭代的過程。我們從簡單的版本開始，逐步精煉。

---

## 加入系統提示

最容易的起點是使用系統提示，設定 Claude 的整體情境和角色，幫助引導其在整個互動過程中的行為。

讓我們從這個系統提示開始：

```python
system = """
You are an expert customer service analyst, skilled at extracting key information from call transcripts and summarizing them in a structured format.
Your task is to analyze customer service call transcripts and generate concise, accurate summaries while maintaining a professional tone.
"""
```

--- 

## 建構主要提示

接下來，我們將開始撰寫主要提示。我們將依賴以下這些提示技巧：

- 將長文件（我們的通話記錄）放在最前面。
- 加入詳細的指令和輸出格式要求。
- 引入 XML 標籤來結構化提示和輸出。
- 給 Claude 「大聲思考」的空間。

由於這個提示可能相當長，我們將各個部分單獨撰寫，然後再組合在一起。


### 輸入資料
在使用 Claude 等大型語言模型時，將長文件（如我們的通話記錄）放在提示的開頭至關重要。這確保了 Claude 在收到具體指令之前已具備所有必要的上下文。我們也應使用 XML 標籤在提示中標識記錄：

```python
prompt_pt1 = """
Analyze the following customer service call transcript and generate a JSON summary of the interaction:

<transcript>
[INSERT CALL TRANSCRIPT HERE]
</transcript>
"""
```

### 指令與輸出格式

在進一步推進之前，讓我們清楚思考一個好的結構化輸出格式應該是什麼樣子。為了方便解析結果，通常最簡單的做法是要求 Claude 提供 JSON 回應。在這個案例中，好的 JSON 應該包含什麼？

我們的 JSON 輸出至少應包含以下內容：
- 一個狀態欄位，說明 Claude 是否有足夠資訊生成摘要。我們稍後會回頭討論這點。目前先假設所有摘要的狀態均為「COMPLETE」，表示 Claude 可以生成摘要。
- 客戶問題的摘要
- 通話是否需要後續跟進
- 任何後續跟進行動的詳情（如需要回電給客戶等）
- 問題如何被解決
- 對話中的模糊或不清楚之處的清單

以下是建議的 JSON 結構範例：

```json
{
  "summary": {
    "customerIssue": "Brief description of the main problem or reason for the call",
    "resolution": "How the issue was addressed or resolved, if applicable",
    "followUpRequired": true/false,
    "followUpDetails": "Description of any necessary follow-up actions, or null if none required"
  },
  "status": "COMPLETE",
  "ambiguities": ["List of any unclear or vague points in the conversation, or an empty array if none"]
}
```

讓我們建立提示的一個新部分，包含具體指令，包括：
- 建立摘要，聚焦於主要問題、解決方案和任何所需的後續跟進行動。
- 依照我們特定的標準化格式生成 JSON 輸出。
- 在摘要中省略客戶特定資訊。
- 保持摘要每個部分的簡短。

以下是提供輸出指令（包含我們特定的輸出 JSON 格式）的嘗試：

```python
prompt_pt2 = """
Instructions:
1. Read the transcript carefully.
2. Analyze the transcript, focusing on the main issue, resolution, and any follow-up required.
3. Generate a JSON object summarizing the key aspects of the interaction according to the specified structure.

Important guidelines:
- Confidentiality: Omit all specific customer data like names, phone numbers, and email addresses.
- Character limit: Restrict each text field to a maximum of 100 characters.
- Maintain a professional tone in your summary.

Output format:
Generate a JSON object with the following structure:
<json>
{
  "summary": {
    "customerIssue": "Brief description of the main problem or reason for the call",
    "resolution": "How the issue was addressed or resolved, if applicable",
    "followUpRequired": true/false,
    "followUpDetails": "Description of any necessary follow-up actions, or null if none required"
  },
  "status": "COMPLETE",
  "ambiguities": ["List of any unclear or vague points in the conversation, or an empty array if none"]
}
</json>
"""
```

--- 

## 使用 XML 標籤並給 Claude 思考空間
接下來，我們將採用另外兩個提示策略：給 Claude 思考空間以及使用 XML 標籤。
- 我們將要求 Claude 先輸出包含分析的 `<thinking>` 標籤。
- 然後，我們將要求 Claude 在 `<json>` 內輸出其 JSON 輸出。

以下是第一稿提示的最後部分：

```python
prompt_pt3 = """
Before generating the JSON, please analyze the transcript in <thinking> tags. 
Include your identification of the main issue, resolution, follow-up requirements, and any ambiguities. 
Then, provide your JSON output in <json> tags.
"""
```


透過要求 Claude 將分析放在 `<thinking>` 標籤內，我們促使它在制定最終 JSON 輸出之前先拆解其思考過程。這鼓勵了更徹底且結構化的記錄分析方式。
`<thinking>` 部分讓我們（以及潛在的其他審閱者或系統）能看到 Claude 的推理過程。這種透明度對除錯和品質保證目的至關重要。


透過將分析（`<thinking>`）與結構化輸出（`<json>`）分離，我們在 Claude 對記錄的詮釋與其格式化摘要之間建立了清楚的區別。在我們可能想要獨立審閱分析而非 JSON 輸出的情況下，這很有幫助；同時，將 JSON 內容隔離在 `<json>` 標籤內，使我們能輕鬆解析最終回應並擷取所需的 JSON。


--- 

## 測試更新後的提示

以下是完整版本的提示，由我們到目前為止撰寫的各個提示片段組合而成：

```python
system = """
You are an expert customer service analyst, skilled at extracting key information from call transcripts and summarizing them in a structured format.
Your task is to analyze customer service call transcripts and generate concise, accurate summaries while maintaining a professional tone.
"""

prompt = """
Analyze the following customer service call transcript and generate a JSON summary of the interaction:

<transcript>
[INSERT CALL TRANSCRIPT HERE]
</transcript>

Instructions:
1. Read the transcript carefully.
2. Analyze the transcript, focusing on the main issue, resolution, and any follow-up required.
3. Generate a JSON object summarizing the key aspects of the interaction according to the specified structure.

Important guidelines:
- Confidentiality: Omit all specific customer data like names, phone numbers, and email addresses.
- Character limit: Restrict each text field to a maximum of 100 characters.
- Maintain a professional tone in your summary.

Output format:
Generate a JSON object with the following structure:
<json>
{
  "summary": {
    "customerIssue": "Brief description of the main problem or reason for the call",
    "resolution": "How the issue was addressed or resolved, if applicable",
    "followUpRequired": true/false,
    "followUpDetails": "Description of any necessary follow-up actions, or null if none required"
  },
  "status": "COMPLETE",
  "ambiguities": ["List of any unclear or vague points in the conversation, or an empty array if none"]
}
</json>

Before generating the JSON, please analyze the transcript in <thinking> tags. 
Include your identification of the main issue, resolution, follow-up requirements, and any ambiguities. 
Then, provide your JSON output in <json> tags.
"""
```

以下是我們可以用來測試提示的函式：

```python
def summarize_call_with_improved_prompt(transcript):
    final_prompt = prompt.replace("[INSERT CALL TRANSCRIPT HERE]", transcript)
    # Make the API call
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        system=system,
        max_tokens=4096,
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )
    print(response.content[0].text)
```

讓我們使用先前定義的一些通話記錄變數來測試提示：

```python
summarize_call_with_improved_prompt(call1)
```

```
<thinking>
From the transcript, the main issue appears to be that the customer could not turn on their smart light bulb. The resolution provided by the agent was to reset the bulb by turning the power off for 5 seconds and then back on.

The agent did offer for the customer to call back if they needed further assistance, indicating potential follow-up may be required if the reset did not resolve the issue. However, no specific follow-up details were provided.

There do not seem to be any significant ambiguities in the conversation.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Unable to turn on smart light bulb",
    "resolution": "Agent instructed customer to reset the bulb by turning power off for 5 seconds, then back on",
    "followUpRequired": true,
    "followUpDetails": "Customer was advised to call back if the reset did not resolve the issue"
  },
  "status": "COMPLETE",
  "ambiguities": []
}
</json>
```

```python
summarize_call_with_improved_prompt(call2)
```

```
<thinking>
Main issue: The customer's Acme SmartTherm thermostat is not maintaining the set temperature of 72°F, and the house is much warmer.

Resolution: The agent guided the customer through recalibrating the SmartTherm thermostat by:
1. Having the customer press and hold the menu button for 5 seconds.
2. Navigating to the "Calibration" menu and selecting it.
3. Adjusting the temperature to match the customer's room thermometer reading of 79°F.
4. Confirming the new calibration setting.

Follow-up required: Yes, the agent instructed the customer to check back in an hour to see if the recalibration resolved the temperature issue.

Ambiguities: None
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Thermostat not maintaining set temperature, causing house to be much warmer.",
    "resolution": "Agent guided customer through recalibrating the thermostat to match room temperature.",
    "followUpRequired": true,
    "followUpDetails": "Customer to check back in an hour to see if recalibration resolved the temperature issue."
  },
  "status": "COMPLETE",
  "ambiguities": []
}
</json>
```

```python
summarize_call_with_improved_prompt(call3)
```

```
<thinking>
Main issue: The customer's Acme SecureHome system alarm is going off randomly in the middle of the night, even though doors and windows are closed properly.

Resolution: The agent suggests running a diagnostic on the system to identify potential sensor malfunctions. The customer is transferred to the technical team to perform the diagnostic and resolve the issue.

Follow-up required: Yes, the technical team needs to follow up with the customer to diagnose and fix the alarm system problem.

Ambiguities: None identified in the conversation.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Customer's home security alarm system is going off randomly at night without apparent cause.",
    "resolution": "Agent suggests running a diagnostic to check for sensor malfunction and transfers customer to technical team.",
    "followUpRequired": true,
    "followUpDetails": "Technical team to diagnose and resolve the issue with the customer's alarm system."
  },
  "status": "COMPLETE",
  "ambiguities": []
}
</json>
```

這些回應看起來都很棒！讓我們再試試另一個帶有一些模糊性的通話記錄，看看 JSON 結果是否包含這些模糊之處：

```python
ambiguous_call = """
Agent: Thank you for calling Acme Smart Home Support. This is Alex. How may I assist you today?
Customer: Hi Alex, I'm having an issue with my SmartLock. It's not working properly.
Agent: I'm sorry to hear that. Can you tell me more about what's happening with your SmartLock?
Customer: Well, sometimes it doesn't lock when I leave the house. I think it might be related to my phone, but I'm not sure.
Agent: I see. When you say it doesn't lock, do you mean it doesn't respond to the auto-lock feature, or are you trying to lock it manually through the app?
Customer: Uh, both, I think. Sometimes one works, sometimes the other. It's inconsistent.
Agent: Okay. And you mentioned it might be related to your phone. Have you noticed any pattern, like it works better when you're closer to the door?
Customer: Maybe? I haven't really paid attention to that.
Agent: Alright. Let's try to troubleshoot this. First, can you tell me what model of SmartLock you have?
Customer: I'm not sure. I bought it about six months ago, if that helps.
Agent: That's okay. Can you see a model number on the lock itself?
Customer: I'd have to go check. Can we just assume it's the latest model?
Agent: Well, knowing the exact model would help us troubleshoot more effectively. But let's continue with what we know. Have you tried resetting the lock recently?
Customer: I think so. Or maybe that was my SmartTherm. I've been having issues with that too.
Agent: I see. It sounds like we might need to do a full diagnostic on your SmartLock. Would you be comfortable if I walked you through that process now?
Customer: Actually, I have to run to an appointment. Can I call back later?
Agent: Of course. Before you go, is there a good contact number where our technical team can reach you for a more in-depth troubleshooting session?
Customer: Sure, you can reach me at 555... oh wait, that's my old number. Let me check my new one... You know what, I'll just call back when I have more time.
Agent: I understand. We're here 24/7 when you're ready to troubleshoot. Is there anything else I can help with before you go?
Customer: No, that's it. Thanks.
Agent: You're welcome. Thank you for choosing Acme Smart Home. Have a great day!
"""

summarize_call_with_improved_prompt(ambiguous_call)
```

```
<thinking>
Main Issue: The customer is experiencing issues with their Acme SmartLock not consistently locking automatically or manually through the app.

Resolution: The agent attempted to troubleshoot by asking for the specific SmartLock model and suggesting a reset, but the customer had to leave before completing the troubleshooting process.

Follow-Up Required: Yes, the customer needs to call back to complete a full diagnostic and troubleshooting session with the technical team.

Ambiguities:
- The customer was unsure if the issue was related to their phone or not, suggesting a potential connectivity problem.
- The customer mentioned having issues with another Acme product (SmartTherm), but it's unclear if those issues are related to the SmartLock problem.
- The customer's contact number was not clearly provided, which could make follow-up more difficult.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "SmartLock not consistently locking automatically or manually through the app.",
    "resolution": "Attempted troubleshooting but customer had to leave before completing the process.",
    "followUpRequired": true,
    "followUpDetails": "Customer needs to call back for full diagnostic and troubleshooting session with technical team."
  },
  "status": "COMPLETE",
  "ambiguities": [
    "Potential connectivity issue with customer's phone",
    "Unclear if issues with other Acme product are related",
    "Customer's contact number not clearly provided"
  ]
}
</json>
```

很好！一切都按預期運作。

--- 

## 邊緣案例

到目前為止，我們嘗試的所有通話記錄都是相對直接的客服電話。在現實世界中，我們預期也會遇到可能不想摘要的記錄，包括：

- 有連線問題的通話
- 有語言障礙的通話
- 記錄內容混亂的通話
- 客戶情緒激動或非理性的通話

請記住，我們的目標是摘要這些通話，以幫助評估我們所提供客服的效能。若將這些邊緣案例通話納入摘要，可能會得到偏斜的結果。

讓我們看看當前提示對這些邊緣案例的處理情況。以下我們定義了一些新的通話記錄：

```python
wrong_number_call = """
Agent: Acme Smart Home Support, Lisa speaking. How can I help you?
Customer: Is this tech support?
Agent: Yes, this is technical support for Acme Smart Home devices. What can I help you with?
Customer: Sorry, wrong number.
Agent: No problem. Have a nice day.
"""

incomplete_call = """
Agent: Acme Smart Home Support, this is Sarah. How can I assist you today?
Customer: The thing isn't working.
Agent: I'm sorry to hear that. Could you please specify which device you're having trouble with?
Customer: You know, the usual one. Gotta go, bye.
Agent: Wait, I need more infor... [call disconnected]
"""

garbled_call = """
Agent: Thank you for calling Acme Smart Home Support. This is Alex. How may I assist you today?
Customer: [garbled voice]
Agent: Hello? Are you there?
"""

language_barrier_call = """
Agent: Acme Smart Home Support, Sarah speaking. How can I help you today?
Customer: [Speaking in Spanish]
Agent: I apologize, but I don't speak Spanish. Do you speak English?
Customer: [Continues Spanish]
Agent: One moment please, I'll try to get a translator on the line...
"""

```

讓我們將這些邊緣案例記錄輸入我們的提示，看看會得到什麼結果：

```python
summarize_call_with_improved_prompt(wrong_number_call)
```

```
<thinking>
Issue: The customer appears to have dialed the wrong number for technical support.
Resolution: Since it was a wrong number, there was no issue to resolve. The agent politely concluded the call.
Follow-up: No follow-up is required since it was a misdialed call.
Ambiguities: There are no apparent ambiguities in this brief conversation.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "The customer dialed the wrong number for technical support",
    "resolution": "The agent concluded the call politely since it was a misdialed number",
    "followUpRequired": false,
    "followUpDetails": null
  },
  "status": "COMPLETE",
  "ambiguities": []
}
</json>
```

```python
summarize_call_with_improved_prompt(incomplete_call)
```

```
<thinking>
In this transcript, the main issue is unclear as the customer does not provide sufficient details about the device they are having trouble with. The agent attempts to clarify the issue, but the customer disconnects the call before providing more information.

There is no resolution since the issue is not clearly identified. However, follow-up is required to gather more details from the customer about the specific device and the problem they are experiencing.

The key ambiguity is the lack of clarity about the device and the nature of the problem. The customer's vague statements ("the thing isn't working" and "the usual one") do not provide enough information for the agent to diagnose or resolve the issue.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Customer reported an unspecified device was not working but did not provide further details.",
    "resolution": "No resolution was possible due to lack of information from the customer.",
    "followUpRequired": true,
    "followUpDetails": "Agent needs to contact the customer again to gather details about the specific device and issue."
  },
  "status": "COMPLETE",
  "ambiguities": ["The device the customer was referring to", "The nature of the problem with the device"]
}
</json>
```

```python
summarize_call_with_improved_prompt(garbled_call)
```

```
<thinking>
From the transcript, it appears the customer called Acme Smart Home Support, but their voice was garbled, and the agent could not understand them. With this limited information, it is unclear what the main issue or reason for the call was. There was no resolution provided, and it is ambiguous whether follow-up is required since the issue itself is unknown. The key ambiguity is the lack of clear communication from the customer, preventing the agent from understanding the problem.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Unclear due to garbled voice from the customer",
    "resolution": "No resolution provided since the issue could not be understood",
    "followUpRequired": true,
    "followUpDetails": "Agent should try to reconnect with the customer for clearer communication"
  },
  "status": "COMPLETE",
  "ambiguities": ["The customer's voice was garbled, preventing understanding of the issue"]
}
</json>
```

```python
summarize_call_with_improved_prompt(language_barrier_call)
```

```
<thinking>
Main issue: The customer called and spoke in Spanish, but the agent could not understand Spanish.
Resolution: The agent tried to get a translator on the line to resolve the language barrier.
Follow-up required: Yes, the agent needs to connect with a Spanish translator to assist the customer.
Ambiguities: It is unclear why the customer called, as the reason for their call is not stated in the transcript.
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Customer spoke in a language the agent did not understand (Spanish).",
    "resolution": "Agent attempted to get a translator to resolve the language barrier.",
    "followUpRequired": true,
    "followUpDetails": "Agent needs to connect the customer with a Spanish translator."
  },
  "status": "COMPLETE",
  "ambiguities": ["Reason for the customer's call is not stated in the transcript."]
}
</json>
```

不幸的是，這些邊緣案例記錄都得到了完整的摘要。以下是一些有問題的回應部分：

>  "customerIssue": "Customer spoke in a language the agent did not understand (Spanish)."

> "customerIssue": "Unclear due to garbled voice from the customer"

> "customerIssue": "The customer dialed the wrong number for technical support" 

請記住，我們的目標是摘要客服電話，以了解客服團隊的效能。這些邊緣案例記錄正在產生完整的摘要，在分析所有摘要時會造成問題。我們需要決定一個處理這些通話的策略。

--- 

## 進一步優化提示

如前所示，我們的提示目前正在為邊緣案例記錄生成完整摘要。我們想要改變這個行為。處理這些邊緣案例有幾個選項：

- 以某種方式標記它們，表示無法摘要，允許後續人工審閱。
- 將它們分別歸類（例如「技術問題」、「語言障礙」等）。

為了簡便起見，我們將選擇標記這些邊緣案例通話，要求模型輸出如下的 JSON：

```json
{
  "status": "INSUFFICIENT_DATA"
}
```

為了實現這一點，我們需要以以下方式更新提示：
- 加入說明所需「INSUFFICIENT_DATA」輸出的指令
- 加入範例，展示可摘要和不可摘要的記錄及其對應的 JSON 輸出。


### 更新指令

讓我們撰寫提示指令部分的新內容，說明模型何時應輸出我們的「INSUFFICIENT_DATA」JSON。

```python
# Just the new content.  We'll look at the entire prompt in a moment
new_instructions_addition = """
Insufficient data criteria:
   If either of these conditions are met:
   a) The transcript has fewer than 5 total exchanges, or
   b) The customer's issue is unclear
   c) The call is garbled, incomplete, or is hindered by a language barrier
   Then return ONLY the following JSON:
   {
     "status": "INSUFFICIENT_DATA"
   }
"""
```

### 加入範例

正如我們在本課程先前所討論的，在提示中加入範例幾乎總是個好主意。在這個特定使用案例中，範例將幫助 Claude 普遍理解我們對可摘要和不可摘要通話記錄所需的摘要類型。

以下是我們可以在提示中包含的一組範例：

```python
examples_for_prompt = """
<examples>
1. Complete interaction:
<transcript>
Agent: Thank you for calling Acme Smart Home Support. This is Alex. How may I assist you today?
Customer: Hi Alex, my Acme SmartTherm isn't maintaining the temperature I set. It's set to 72 but the house is much warmer.
Agent: I'm sorry to hear that. Let's troubleshoot. Is your SmartTherm connected to Wi-Fi?
Customer: Yes, the Wi-Fi symbol is showing on the display.
Agent: Great. Let's recalibrate your SmartTherm. Press and hold the menu button for 5 seconds.
Customer: Okay, done. A new menu came up.
Agent: Perfect. Navigate to "Calibration" and press select. Adjust the temperature to match your room thermometer.
Customer: Alright, I've set it to 79 degrees to match.
Agent: Great. Press select to confirm. It will recalibrate, which may take a few minutes. Check back in an hour to see if it's fixed.
Customer: Okay, I'll do that. Thank you for your help, Alex.
Agent: You're welcome! Is there anything else I can assist you with today?
Customer: No, that's all. Thanks again.
Agent: Thank you for choosing Acme Smart Home. Have a great day!
</transcript>

<thinking>
Main issue: SmartTherm not maintaining set temperature
Resolution: Guided customer through recalibration process
Follow-up: Not required, but customer should check effectiveness after an hour
Ambiguities: None identified
</thinking>

<json>
{
  "summary": {
    "customerIssue": "SmartTherm not maintaining set temperature, showing higher than set 72 degrees",
    "resolution": "Guided customer through SmartTherm recalibration process",
    "followUpRequired": false,
    "followUpDetails": null
  },
  "status": "COMPLETE",
  "ambiguities": []
}
</json>

2. Interaction requiring follow-up:
<transcript>
Agent: Acme Smart Home Support, this is Jamie. How can I help you?
Customer: Hi, I just installed my new Acme SmartCam, but I can't get it to connect to my Wi-Fi.
Agent: I'd be happy to help. Are you using the Acme Smart Home app?
Customer: Yes, I have the app on my phone.
Agent: Great. Make sure your phone is connected to the 2.4GHz Wi-Fi network, not the 5GHz one.
Customer: Oh, I'm on the 5GHz network. Should I switch?
Agent: Yes, please switch to the 2.4GHz network. The SmartCam only works with 2.4GHz.
Customer: Okay, done. Now what?
Agent: Open the app, select 'Add Device', choose 'SmartCam', and follow the on-screen instructions.
Customer: It's asking for a password now.
Agent: Enter your Wi-Fi password and it should connect.
Customer: It's still not working. I keep getting an error message.
Agent: I see. In that case, I'd like to escalate this to our technical team. They'll contact you within 24 hours.
Customer: Okay, that sounds good. Thank you for trying to help.
Agent: You're welcome. Is there anything else you need assistance with?
Customer: No, that's all for now. Thanks again.
Agent: Thank you for choosing Acme Smart Home. Have a great day!
</transcript>

<thinking>
Main issue: Customer unable to connect new SmartCam to Wi-Fi
Resolution: Initial troubleshooting unsuccessful, issue escalated to technical team
Follow-up: Required, technical team to contact customer within 24 hours
Ambiguities: Specific error message customer is receiving not mentioned
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Unable to connect new SmartCam to Wi-Fi",
    "resolution": "Initial troubleshooting unsuccessful, issue escalated to technical team",
    "followUpRequired": true,
    "followUpDetails": "Technical team to contact customer within 24 hours for further assistance"
  },
  "status": "COMPLETE",
  "ambiguities": ["Specific error message customer is receiving not mentioned"]
}
</json>

3. Insufficient data:
<transcript>
Agent: Acme Smart Home Support, this is Sam. How may I assist you?
Customer: Hi, my smart lock isn't working.
Agent: I'm sorry to hear that. Can you tell me more about the issue?
Customer: It just doesn't work. I don't know what else to say.
Agent: Okay, when did you first notice the problem? And what model of Acme smart lock do you have?
Customer: I don't remember. Listen, I have to go. I'll call back later.
Agent: Alright, we're here 24/7 if you need further assistance. Have a good day.
</transcript>

<thinking>
This transcript has fewer than 5 exchanges and the customer's issue is unclear. The customer doesn't provide specific details about the problem with the smart lock or respond to the agent's questions. This interaction doesn't provide sufficient information for a complete summary.
</thinking>

<json>
{
  "status": "INSUFFICIENT_DATA"
}
</json>
</examples>
"""
```

請注意，這些範例涵蓋三種不同情境：
* 不需要後續跟進的完整互動
* 需要後續跟進且包含模糊之處的完整互動
* 包含資料不足的不可摘要互動

向 Claude 提供範例時，涵蓋多樣化的輸入/輸出配對非常重要。

--- 

## 最終提示

讓我們將初始提示與前一節所做的新增內容結合在一起：
* 處理資料不足通話的指令
* 範例輸入和輸出集

以下是新的完整提示：

```python
system = """
You are an expert customer service analyst, skilled at extracting key information from call transcripts and summarizing them in a structured format.
Your task is to analyze customer service call transcripts and generate concise, accurate summaries while maintaining a professional tone.
"""

prompt = """
Analyze the following customer service call transcript and generate a JSON summary of the interaction:

<transcript>
[INSERT CALL TRANSCRIPT HERE]
</transcript>

Instructions:
<instructions>
1. Read the transcript carefully.
2. Analyze the transcript, focusing on the main issue, resolution, and any follow-up required.
3. Generate a JSON object summarizing the key aspects of the interaction according to the specified structure.

Important guidelines:
- Confidentiality: Omit all specific customer data like names, phone numbers, and email addresses.
- Character limit: Restrict each text field to a maximum of 100 characters.
- Maintain a professional tone in your summary.

Output format:
Generate a JSON object with the following structure:
<json>
{
  "summary": {
    "customerIssue": "Brief description of the main problem or reason for the call",
    "resolution": "How the issue was addressed or resolved, if applicable",
    "followUpRequired": true/false,
    "followUpDetails": "Description of any necessary follow-up actions, or null if none required"
  },
  "status": "COMPLETE",
  "ambiguities": ["List of any unclear or vague points in the conversation, or an empty array if none"]
}
</json>

Insufficient data criteria:
   If any of these conditions are met:
   a) The transcript has fewer than 5 total exchanges
   b) The customer's issue is unclear
   c) The call is garbled, incomplete, or is hindered by a language barrier
   Then return ONLY the following JSON:
   {
     "status": "INSUFFICIENT_DATA"
   }

Examples: 
<examples>
1. Complete interaction:
<transcript>
Agent: Thank you for calling Acme Smart Home Support. This is Alex. How may I assist you today?
Customer: Hi Alex, my Acme SmartTherm isn't maintaining the temperature I set. It's set to 72 but the house is much warmer.
Agent: I'm sorry to hear that. Let's troubleshoot. Is your SmartTherm connected to Wi-Fi?
Customer: Yes, the Wi-Fi symbol is showing on the display.
Agent: Great. Let's recalibrate your SmartTherm. Press and hold the menu button for 5 seconds.
Customer: Okay, done. A new menu came up.
Agent: Perfect. Navigate to "Calibration" and press select. Adjust the temperature to match your room thermometer.
Customer: Alright, I've set it to 79 degrees to match.
Agent: Great. Press select to confirm. It will recalibrate, which may take a few minutes. Check back in an hour to see if it's fixed.
Customer: Okay, I'll do that. Thank you for your help, Alex.
Agent: You're welcome! Is there anything else I can assist you with today?
Customer: No, that's all. Thanks again.
Agent: Thank you for choosing Acme Smart Home. Have a great day!
</transcript>

<thinking>
Main issue: SmartTherm not maintaining set temperature
Resolution: Guided customer through recalibration process
Follow-up: Not required, but customer should check effectiveness after an hour
Ambiguities: None identified
</thinking>

<json>
{
  "summary": {
    "customerIssue": "SmartTherm not maintaining set temperature, showing higher than set 72 degrees",
    "resolution": "Guided customer through SmartTherm recalibration process",
    "followUpRequired": false,
    "followUpDetails": null
  },
  "status": "COMPLETE",
  "ambiguities": []
}
</json>

2. Interaction requiring follow-up:
<transcript>
Agent: Acme Smart Home Support, this is Jamie. How can I help you?
Customer: Hi, I just installed my new Acme SmartCam, but I can't get it to connect to my Wi-Fi.
Agent: I'd be happy to help. Are you using the Acme Smart Home app?
Customer: Yes, I have the app on my phone.
Agent: Great. Make sure your phone is connected to the 2.4GHz Wi-Fi network, not the 5GHz one.
Customer: Oh, I'm on the 5GHz network. Should I switch?
Agent: Yes, please switch to the 2.4GHz network. The SmartCam only works with 2.4GHz.
Customer: Okay, done. Now what?
Agent: Open the app, select 'Add Device', choose 'SmartCam', and follow the on-screen instructions.
Customer: It's asking for a password now.
Agent: Enter your Wi-Fi password and it should connect.
Customer: It's still not working. I keep getting an error message.
Agent: I see. In that case, I'd like to escalate this to our technical team. They'll contact you within 24 hours.
Customer: Okay, that sounds good. Thank you for trying to help.
Agent: You're welcome. Is there anything else you need assistance with?
Customer: No, that's all for now. Thanks again.
Agent: Thank you for choosing Acme Smart Home. Have a great day!
</transcript>

<thinking>
Main issue: Customer unable to connect new SmartCam to Wi-Fi
Resolution: Initial troubleshooting unsuccessful, issue escalated to technical team
Follow-up: Required, technical team to contact customer within 24 hours
Ambiguities: Specific error message customer is receiving not mentioned
</thinking>

<json>
{
  "summary": {
    "customerIssue": "Unable to connect new SmartCam to Wi-Fi",
    "resolution": "Initial troubleshooting unsuccessful, issue escalated to technical team",
    "followUpRequired": true,
    "followUpDetails": "Technical team to contact customer within 24 hours for further assistance"
  },
  "status": "COMPLETE",
  "ambiguities": ["Specific error message customer is receiving not mentioned"]
}
</json>

3. Insufficient data:
<transcript>
Agent: Acme Smart Home Support, this is Sam. How may I assist you?
Customer: Hi, my smart lock isn't working.
Agent: I'm sorry to hear that. Can you tell me more about the issue?
Customer: It just doesn't work. I don't know what else to say.
Agent: Okay, when did you first notice the problem? And what model of Acme smart lock do you have?
Customer: I don't remember. Listen, I have to go. I'll call back later.
Agent: Alright, we're here 24/7 if you need further assistance. Have a good day.
</transcript>

<thinking>
This transcript has fewer than 5 exchanges and the customer's issue is unclear. The customer doesn't provide specific details about the problem with the smart lock or respond to the agent's questions. This interaction doesn't provide sufficient information for a complete summary.
</thinking>

<json>
{
  "status": "INSUFFICIENT_DATA"
}
</json>
</examples>
</instructions>

Before generating the JSON, please analyze the transcript in <thinking> tags. 
Include your identification of the main issue, resolution, follow-up requirements, and any ambiguities. 
Then, provide your JSON output in <json> tags.
"""
```

上述提示相當長，以下是整體結構：
- 系統提示設定模型的情境、角色和語調。
- 主要提示包含以下內容：
    - 通話記錄
    - 一組指令，包含：
        - 一般指令
        - 指導方針
        - 輸出格式要求
        - 處理邊緣案例通話的細節
        - 範例
    - 關於輸出中使用 XML 標籤的細節

以下是幫助視覺化提示流程的摘要：

```txt
Analyze the following customer service call transcript and generate a JSON summary of the interaction:

<transcript>
[INSERT CALL TRANSCRIPT HERE]
</transcript>

<instructions>
- General instructions and guidelines
- Output JSON format description
- Insufficient data (edge-case) criteria
<examples>
varied example inputs and outputs
</examples>
</instructions>

Before generating the JSON, please analyze the transcript in <thinking> tags. 
Include your identification of the main issue, resolution, follow-up requirements, and any ambiguities. 
Then, provide your JSON output in <json> tags.

```

讓我們用一個新函式測試最終提示。請注意，這個函式提取 `<json>` 標籤內的 JSON 摘要內容：

```python
import re

def summarize_call_with_final_prompt(transcript):
    final_prompt = prompt.replace("[INSERT CALL TRANSCRIPT HERE]", transcript)
    # Make the API call
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        system=system,
        max_tokens=4096,
        messages=[
            {"role": "user", "content": final_prompt}
        ]
    )
    
    # Extract content between <json> tags
    json_content = re.search(r'<json>(.*?)</json>', response.content[0].text, re.DOTALL)
    
    if json_content:
        print(json_content.group(1).strip())
    else:
        print("No JSON content found in the response.")
```

讓我們使用現有的通話變數進行測試：

```python
summarize_call_with_final_prompt(call1)
```

```
{
  "summary": {
    "customerIssue": "Unable to turn on smart light bulb",
    "resolution": "Agent guided customer to reset the bulb by cycling power off and on",
    "followUpRequired": false,
    "followUpDetails": null
  },
  "status": "COMPLETE",
  "ambiguities": []
}
```

```python
summarize_call_with_final_prompt(call3)
```

```
{
  "summary": {
    "customerIssue": "Acme SecureHome alarm system going off randomly multiple times at night without apparent cause",
    "resolution": "Initial troubleshooting steps taken, but issue unresolved. Customer transferred to technical team for diagnostics",
    "followUpRequired": true,
    "followUpDetails": "Technical team to diagnose and resolve issue with alarm system"
  },
  "status": "COMPLETE",
  "ambiguities": []
}
```

讓我們試試應該產生 `ambiguities` 陣列不為空的通話記錄：

```python
summarize_call_with_final_prompt(ambiguous_call)
```

```
{
  "summary": {
    "customerIssue": "SmartLock not reliably locking automatically or through app, behavior is inconsistent",
    "resolution": "Troubleshooting attempted but incomplete due to lack of model details, customer had to leave",
    "followUpRequired": true,
    "followUpDetails": "Customer to call back for further troubleshooting of SmartLock issue when available"
  },
  "status": "COMPLETE",
  "ambiguities": [
    "Unclear if related SmartTherm issue mentioned",
    "SmartLock model not identified",
    "Customer's contact number not confirmed"
  ]
}
```

現在讓我們試試一些我們不想摘要的邊緣案例提示：

```python
summarize_call_with_final_prompt(garbled_call)
```

```
{
  "status": "INSUFFICIENT_DATA"
}
```

```python
summarize_call_with_final_prompt(language_barrier_call)
```

```
{
  "status": "INSUFFICIENT_DATA"
}
```

```python
summarize_call_with_final_prompt(incomplete_call)
```

```
{
  "status": "INSUFFICIENT_DATA"
}
```

太好了！我們得到了完全符合預期的輸出！讓我們進一步測試極端情況：

```python
summarize_call_with_final_prompt("blah blah blah")
```

```
{
  "status": "INSUFFICIENT_DATA"
}
```

```python
summarize_call_with_final_prompt("")
```

```
{
  "status": "INSUFFICIENT_DATA"
}
```

出色！提示正在處理我們所有的邊緣案例！

---

## 總結

在本課中，我們走過了為摘要客服通話記錄開發複雜提示的過程。讓我們回顧所採用的提示技巧：

* 系統提示：我們使用系統提示為 Claude 設定整體情境和角色。
* 結構化輸入：我們使用 XML 標籤將通話記錄放在提示的開頭。
* 清楚的指令：我們提供了關於應聚焦的重點以及如何結構化輸出的詳細指導方針。
* 輸出格式：我們為摘要指定了 JSON 結構，確保結果一致且易於解析。
* 處理邊緣案例：我們加入了識別資料不足通話的標準。
* 範例：我們包含了多樣化的範例，說明不同情境的預期輸出。
* 大聲思考：我們要求 Claude 在提供最終 JSON 輸出之前，在 `<thinking>` 標籤中展示其分析。


透過採用這些技巧，我們建立了一個強健的提示，能夠為各種客服通話記錄生成結構化摘要，同時適當地處理邊緣案例。這種方法可以應用於通話摘要之外的許多其他複雜提示情境。


**重要提示：** 雖然我們已開發出一個看起來能良好處理測試案例的複雜提示，但關鍵是要理解這個提示尚未準備好用於生產環境。我們所創建的是一個有潛力的起點，但在可靠地用於現實世界的情境之前，還需要進行廣泛的測試和評估。我們目前以肉眼評估為基礎的評估僅建立在少量範例上，無法代表真實客服電話的多樣性和不可預測性。為了確保提示的效能和可靠性，我們需要實施包含量化指標的全面評估流程。強健、以資料驅動的評估是彌合有潛力的原型與可靠生產級解決方案之間差距的關鍵。
