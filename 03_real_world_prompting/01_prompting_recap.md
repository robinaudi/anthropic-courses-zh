# 第一課：核心提示技巧回顧

## 簡介
歡迎來到「實戰提示工程」課程的第一課！本課程專為有經驗的開發者設計，適合已初步涉足提示工程領域的學員，尤其是完成過我們完整 **[提示工程互動教學](../prompt_engineering_interactive_tutorial/README.md)** 的學員。若你尚未完成該教學，我們強烈建議先行閱讀，因為它提供了多種提示技巧的深入探索與實作練習。

在本課「核心提示技巧回顧」中，我們將複習貫穿整個課程的基礎提示知識。本課程的目標並非重述基礎，而是透過示範這些技巧在高風險、大規模生產環境中的關鍵重要性來加深理解。

讓我們立即開始，看看這些基本技巧如何改變你在生產環境中與 Claude 的互動方式。

## 核心提示技巧
本課將涵蓋以下關鍵提示技巧：

0. [使用 Prompt Generator](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-generator)
1. [清楚直接地表達](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/be-clear-and-direct)
4. [使用 XML 標籤](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)
2. [提供範例（多範例提示）](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/multishot-prompting)
3. [讓 Claude 思考（思維鏈提示）](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
5. [賦予 Claude 角色（系統提示）](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
7. [長上下文提示技巧](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/long-context-tips)

## 0 使用 Prompt Generator

開始撰寫有效提示最簡單的方式，就是使用我們的新 Prompt Generator 工具。我們建立了一個工具，能引導 Claude 為你的特定任務生成高品質的提示。Prompt Generator 特別適合解決「空白頁問題」，為你提供一個符合最佳實踐（如思維鏈與指令資料分離）的測試與迭代起點。

使用方式：前往 Console 並選擇「Generate a prompt」。

![console.png](images/console.png)

接著，輸入你對目標提示的初步想法。可以盡量詳細——Claude 在建立提示時會考量你提供的所有情境。

![prompt_generator_input.png](images/prompt_generator_input.png)

點擊「Generate prompt」並等待 Claude 生成如下所示的高品質提示：

![prompt_generator_output.png](images/prompt_generator_output.png)

讓我們仔細看看它為我們生成的提示：

| 輸入文字 | 生成的提示 |
|------------|-----------------|
| 判斷某篇新聞是否為假新聞 | Your task is to determine whether a given news article is fake news or legitimate news. I will provide you with the text of the article, and you will need to carefully read and analyze it to make a determination. <br/><br/> Here is the text of the article: <br/> \<article> <br/> \{\{ARTICLE_TEXT}} <br/> \</article> <br/> <br/> Please begin by thoroughly reading the article, looking for any potential signs that it may be fake news. Pay attention to things like: <br/> - The use of sensationalized or emotionally charged language <br/> - A lack of credible sources or evidence to support claims <br/> - Extreme political bias or the promotion of conspiracy theories <br/> - Claims that seem outlandish, implausible or contrary to other known facts <br/> - Factual inaccuracies or errors in basic information that a legitimate news source would get right <br/> <br/> After analyzing the article, please write out your reasoning and the key points you noticed in a \<reasoning> section. Explain what specifically in the article led you to believe it may be fake or legitimate. <br/> <br/> Finally, based on your analysis, make a clear determination of whether you believe this article is FAKE news or REAL news. State your final answer in an \<answer> section. <br/> <br/> Remember, fake news can be tricky to spot, so think critically and don't jump to any conclusions before carefully weighing the evidence. If you're not sure, err on the side of caution in your determination. |

這個提示融入了許多重要的提示工程技巧，包括：
- 清楚直接的任務定義
- 結構化輸出的說明
- 使用 XML 標籤清楚劃分提示的各個部分

**注意：Prompt Generator 生成的提示最好作為起點，仍需進一步迭代優化。理解核心提示技巧及其原理依然非常重要，這將幫助你改善 Prompt Generator 所生成提示的效果。**

接下來，讓我們複習一些最重要的提示工程技巧。

## 1\. 清楚直接地表達

### 定義：
毫無疑問，最重要的提示技巧也是最簡單的：撰寫明確、詳細、不留任何模糊空間的指令。這意味著需要指定所需的輸出格式、長度和風格，且不能假設 Claude 已了解你的使用情境。說來容易做來難，但值得認真對待。

### 重要性：
清晰與精確至關重要。模糊或含糊的提示會導致誤解、浪費時間，以及潛在的高代價錯誤。透過清楚直接的表達，你能確保 Claude 準確理解你的需求，減少來回澄清的次數，提升整體提示效果。

### 不良範例：分析客戶回饋
假設你是一位產品經理，想要分類並摘要新軟體版本的客戶回饋。

| 角色 | 內容 |
| ---- | -------------------------------------------------------------------------------------------------------- |
| User | Here's some customer feedback. Can you tell me what people think? <br/> \{\{CUSTOMER_FEEDBACK}} |

這個提示含糊不清，缺乏具體指令。Claude 可能會提供一般性摘要，但未必包含你做決策所需的結構化洞見。

### 良好範例：分析客戶回饋

| 角色 | 內容 |
| ---- | -------- |
| User | I need you to analyze this customer feedback for our recent software release: <br/> \<feedback>\{\{CUSTOMER_FEEDBACK}}\</feedback> <br/> <br/> Please provide a detailed report with the following sections: <br/> <br/> 1\. Summary (50-100 words): Concise overview of the general sentiment and main themes. <br/> 2\. Feature Analysis: <br/> - List top 3 most praised features (bullet points) <br/> - List top 3 most criticized features (bullet points) <br/> 3\. User Experience Issues: <br/> - List top 3 reported usability problems (bullet points) <br/> - For each issue, suggest a potential fix (in parentheses) <br/> 4\. Sentiment Breakdown: <br/> - Positive: X% <br/> - Neutral: Y% <br/> - Negative: Z% <br/> 5\. Actionable Insights (3-5 bullet points): Key takeaways and recommended actions based on the feedback. <br/> <br/> Use XML tags to structure your response for easy parsing: <br/> \<summary>\</summary> <br/> \<feature_analysis>\</feature_analysis> <br/> \<ux_issues>\</ux_issues> <br/> \<sentiment>\</sentiment> <br/> \<insights>\</insights> |

這個提示之所以清楚直接，因為它：
- 明確說明輸入的性質（軟體版本的客戶回饋）
- 規定所需的輸出格式（摘要、項目符號、編號清單）
- 設定明確的字數限制（摘要 50-100 字）
- 提供詳細的回應結構

Prompt Generator 在這方面幫助有限。撰寫提示之前，關鍵是要先規劃清楚你的需求。Prompt Generator 可以建議潛在的提示指令，但最好先自行釐清需求，再借助 Prompt Generator。

### 重點整理
#### 適用時機
* **任何時候**，尤其是複雜或關鍵的任務
* 需要非常特定輸出時
* 處理多步驟流程時

#### 解決的問題：

* 指令被誤解
* 回應模糊或不相關
* 任務執行不完整


---

## 2\. 使用 XML 結構化提示

### 定義：
使用 XML 標籤（如 `<tag></tag>`）包覆並劃分提示的不同部分，例如指令、輸入資料或範例。此技巧有助於組織含有多個組成要素的複雜提示。

### 重要性：

值得注意的是，撰寫有效的 Claude 提示並非一定要使用 XML 標籤。一般而言，複雜提示之所以困難，是因為它們通常將指令與注入的外部資料混合在單一的非結構化文字串中。當這些元素合併在一個提示中，模型便難以區分你的指令與輸入資料，進而造成混亂。

XML 標籤透過在提示中將資料與指令分離，提供了解決此問題的方案。我們喜歡使用 XML 標籤，因為它們簡短且具有說明性，但你也可以自行設計結構化提示的系統。重要的是使用某種語法來分隔複雜提示的各個部分。本課程中我們將使用 XML 標籤，因為這是最「Claude 風格」的做法。

### 不良範例：產品缺陷分析

你是一家電子製造商的品保主管。在客訴激增後，你需要分析新款智慧手錶的缺陷報告：

| 角色 | 內容 |
| ---- | -------- |
| User | Here's a summary of defect reports for the SmartTime 3000 smartwatch: Manufacturing quality issues - 30% of units. Battery life only 12 hours vs advertised 48 hours. Health tracking data inaccurate by 25%. Software bugs causing app crashes. <br/> <br/> Here's our current inventory: 50,000 units in the warehouse, 100,000 in transit from suppliers. <br/> <br/> Retail price is 299. Production cost is 120 per unit. <br/> <br/> Analyze the defects, their impact on our brand, and recommend actions. |

這個提示有以下問題：
- 資料、指令和預期輸出格式全部混在一起。
- Claude 可能將部分輸入資料誤判為指令，或遺漏關鍵資料點。
- 未指定輸出結構，Claude 的回應可能難以解析或整合進管理報告。

### 良好範例：產品缺陷分析

現在，讓我們用 XML 標籤結構化提示：

| 角色 | 內容 |
| ---- | -------- |
| User | I need you to analyze the quality issues with our SmartTime 3000 smartwatch and recommend actions. Here's the data: <br/> <br/> \<defect_report> <br/> - Manufacturing quality issues: 30% of units affected <br/> - Battery life: 12 hours (advertised: 48 hours) <br/> - Health tracking data: 25% inaccuracy <br/> - Software: Multiple app crashes reported <br/> \</defect_report> <br/> <br/> \<inventory> <br/> - Warehouse stock: 50,000 units <br/> - In transit: 100,000 units <br/> \</inventory> <br/> <br/> \<financials> <br/> - Retail price: 299 <br/> - Production cost: 120 per unit <br/> \</financials> <br/> <br/> Please provide a detailed report with the following sections: <br/> <br/> 1\. \<defect_analysis> Analyze each defect's severity and potential impact on user experience and brand reputation. \</defect_analysis> <br/> 2\. \<financial_impact> Calculate potential losses due to returns, warranty claims, and lost sales. Consider both immediate impact and long-term brand damage. \</financial_impact> <br/> 3\. \<action_plan> Recommend prioritized actions to address these issues. Include timelines, cost estimates, and expected outcomes. \</action_plan> |

這個改寫後的提示有顯著改善：

1. **結構化資料**：每項資訊都用描述性 XML 標籤包覆（`<defect_report>`、`<inventory>`、`<financials>`），讓 Claude 清楚了解正在處理的資訊類型。
2. **清楚的回應結構**：`<defect_analysis>`、`<financial_impact>` 和 `<action_plan>` 標籤引導 Claude 以便於你和團隊審閱及行動的方式組織回應。

### 重點整理
#### 適用時機

* 包含多個區段的複雜提示
* 需要清楚區分指令與資料時
* 在提示中組織不同類型的資訊時

#### 解決的問題：

* 指令與輸入資料混淆
* 提示各組成部分處理不一致
* 複雜提示難以解析或理解
---

## 3\. 使用範例：以示範方式學習的力量

### 定義：
提供 Claude 所需輸出格式、風格或內容的範例。這些範例作為 Claude 遵循的模板，幫助它準確理解應期待什麼樣的輸入，以及生成的輸出應該長什麼樣。範例確實可能讓提示變長，但幾乎任何生產品質的提示都值得加入。

### 重要性：
範例作為具體模板，讓 Claude 更容易理解並複製所需的輸出。這在需要一致格式、特定術語或遵循行業標準的任務中尤為關鍵。透過提供範例，你降低了誤解的可能性，確保 Claude 的輸出符合你的特定需求。相較於試圖用文字描述捕捉所有細微差別，直接展示一兩個所需輸出的範例通常更有效率。

### 不良範例：建立產品公告電子郵件

假設你是一位行銷總監，需要為一家科技公司撰寫一系列產品公告電子郵件。沒有範例的情況下，提示可能如下：

| 角色 | 內容 |
| ---- | -------- |
| User | Please write a product announcement email for our new AI-powered CRM software, 'AcmeAI'. Include its key features, benefits, and a call to action. The email should be professional, engaging, and highlight how this product can transform customer relationships. Make sure to mention its AI capabilities, pricing, and availability. |

雖然 Claude 可能會產出不錯的電子郵件，但它未必能完全符合你公司的風格、語調或格式偏好，也可能遺漏你通常在此類郵件中會包含的關鍵元素。

### 良好範例：建立產品公告電子郵件

現在，讓我們提供範例來引導 Claude：

| 角色 | 內容 |
| ---- | -------- |
| User | Please write a product announcement email for our tech company's latest innovation. Follow the style and structure of these examples: <br/> <br/> \<examples> <br/> \<example> <br/> Subject: Introducing AcmeDataPulse: Real-time Analytics Reimagined <br/> <br/> Dear Valued Partner, <br/> <br/> We are thrilled to announce the launch of AcmeDataPulse, our groundbreaking real-time analytics platform designed to transform the way businesses harness data. <br/> <br/> \[Key Features\] <br/> - Live Data Streaming: Process and analyze data in real-time, reducing decision latency by up to 80%. <br/> - AI-Driven Insights: Our proprietary machine learning algorithms uncover hidden patterns, giving you a competitive edge. <br/> - Scalable Infrastructure: Whether it's gigabytes or petabytes, AcmeDataPulse grows with your data. <br/> <br/> \[Benefits\] <br/> - Faster Decision-Making: Turn data into actionable insights within seconds. <br/> - Cost Efficiency: Our pay-as-you-go model means you only pay for what you use. <br/> - Seamless Integration: REST APIs and pre-built connectors for your existing stack. <br/> <br/> AcmeDataPulse is now available, starting at 499/month. Schedule a demo today to see how we can supercharge your data strategy. <br/> <br/> Best regards, <br/> The Acme Team <br/> \</example> <br/> <br/> \<example> <br/> Subject: Elevate Your eCommerce with AcmeSmartCart Pro <br/> <br/> Hello eCommerce Leaders, <br/> <br/> We're excited to introduce AcmeSmartCart Pro, the next-gen shopping cart solution that's set to revolutionize online retail. <br/> <br/> \[Key Features\] <br/> - AI-powered Recommendations: Boost cross-sells by 30% with our advanced recommendation engine. <br/> - One-Click Checkout: Reduce cart abandonment by 25% with our streamlined process. <br/> - Multi-currency Support: Tap into global markets with automatic currency conversion. <br/> <br/> \[Benefits\] <br/> - Increased Conversions: Frictionless checkout means more sales. <br/> - Global Reach: Sell to customers worldwide without currency hassles. <br/> - Future-Proof: Regular AI updates keep you ahead of the curve. <br/> <br/> Get AcmeSmartCart Pro today starting at \$299/month. First 30 days are on us. Ready to upgrade? Contact sales@acme.com. <br/> <br/> Cheers, <br/> The eComCo Innovations Team <br/> \</example> <br/> \</examples> <br/> <br/> Please draft a product announcement email for our new AI-powered CRM software, 'AcmeAI'. Focus on its key features, benefits, and a call to action. |


在這個範例中，提供的示範清楚呈現了其他科技公司產品公告電子郵件的結構與語調。它們突出了主要功能與優勢、使用可量化的指標展示價值、包含定價資訊，並以明確的行動呼籲作結。Claude 可以利用這些範例生成類似的 AcmeAI 電子郵件，完全符合此類公告預期的風格、結構和內容類型。

透過提供這些範例，我們確保了 Claude：

1. 使用能吸引讀者注意並摘要公告內容的主旨行。
2. 強調產品創新性地介紹產品。
3. 列出含有技術細節與可量化優勢的主要功能。
4. 突出能呼應業務目標（如客戶滿意度和銷售增長）的整體優勢。
5. 提供定價資訊與行動呼籲。
6. 全篇維持專業且吸引人的語調。

這種結構化方式使生成的電子郵件幾乎不需修改即可直接使用，節省時間並確保所有產品公告的一致性。


為了充分發揮提示中範例的效果，請考慮以下提供最有效範例的準則：

* **相關性**：確保範例與你期望 Claude 處理的輸入輸出類型高度相似。範例越接近你的實際使用情境，Claude 的表現就越好。
* **多樣性**：包含涵蓋不同情境、邊緣案例和潛在挑戰的多樣範例。這有助於 Claude 更好地泛化，應對更廣泛的輸入。
* **數量**：雖然沒有最佳範例數量的硬性規定，但目標是至少提供 3-5 個範例，給 Claude 一個紮實的基礎。若 Claude 的表現未達預期，可隨時補充更多針對性範例。請記住，即使是單一範例也比沒有範例好。

### 重點整理

#### 適用時機
* 示範所需的輸出格式或風格時
* 解釋複雜或需要細膩處理的任務時
* 提升各種輸入下回應的一致性時

#### 解決的問題

* 回應不一致
* 對所需輸出格式的誤解
* 對陌生或複雜任務結構的困難
---


## 4\. 讓 Claude 思考：提升分析與問題解決能力

### 定義：
「讓 Claude 思考」或「思維鏈提示」是一種技巧，你明確指示 Claude 將複雜問題或問題拆解為一系列邏輯步驟，在每個步驟中闡述其推理過程，然後用這個推理提供最終答案或解決方案。這類似於請同事在解決問題時「大聲思考」。

### 重要性：
在撰寫高風險提示時，得出結果的過程往往與決策本身同等重要。當 Claude 展示其思考過程，我們可以獲得：

1. **提升準確性**：透過將複雜問題拆解為步驟，Claude 較不容易做出可能導致錯誤的邏輯跳躍或假設。
2. **強化決策品質**：我們身為開發者可以審閱 Claude 的推理過程，了解它如何得出結論，並做出更明智的疑難排解或提示改進決策。
3. **風險管控**：在金融、法律或醫療等領域，理解建議背後的邏輯對評估潛在風險和責任至關重要。
4. **問責與透明**：在審計或審查的情況下，你有清楚的決策記錄，這對治理和合規性至關重要。

### 不良範例：市場進入策略

假設你是一位 CEO，正在考慮將成功的美國軟體公司拓展至亞洲市場。若不要求逐步分析，你的查詢可能如下：

| 角色 | 內容 |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User | Our software company, AcmeFlow, has seen great success in the U.S. with our project management platform. We're considering expanding into Asia. Is this a good move? Provide a report for the board. |

這個提示過於模糊。Claude 可能會給出缺乏深度和針對性的一般性回應，而這樣的回應並不足以支撐國際擴張這類重大商業決策。

### 良好範例：市場進入策略

現在，讓我們使用「讓 Claude 思考」技巧來引導更深入的分析。實現此目的主要有兩種方式：
1. 在提示中明確告訴 Claude「逐步思考」（請務必包含額外的指導、說明或考量，幫助 Claude 評估「如何」思考）。Claude 將在提供最終答案之前先拆解其思考過程。
2. 為 Claude 提供一個放置思考內容的空間，然後再生成答案。考慮使用 XML 標籤如 \<thinking> 和 \<answer>。你可以指示 Claude 將思考過程放在 \<thinking> 標籤內，最終答案放在 \<answer> 標籤內。Claude 將在標籤內完成思考過程並提供最終答案。

**注意：在實際實作中，我們會希望提供 Claude 工具來取得亞洲市場、財經新聞等最新資訊。**

讓我們嘗試用這個策略更新上面的「不良」提示：

| 角色 | 內容 |
| ---- | -------- |
| User | Our software company, AcmeFlow, has seen great success with our project management platform in the U.S. We're considering expanding into Asia. I need a comprehensive analysis to present to the board. <br/> <br/> Here's our company data: <br/> \<company_data> <br/> \{\{ACMEFLOW_DATA}} <br/> \</company_data> <br/> <br/> Here's market research on the Asian tech sector: <br/> \<market_research> <br/> \{\{ASIA_TECH_MARKET}} <br/> \</market_research> <br/> <br/> Please analyze whether expanding into Asia is a good move for AcmeFlow. Think through your analysis before you answer, considering all factors around market potential, competition, regulatory challenges, and financial projections that might be relevant to creating a holistic and complete strategic analysis. For each step, provide your thought process within \<thinking>\</thinking> tags. After your analysis, provide a clear recommendation for the board in \<recommendation>\</recommendation> tags. <br/> <br/> Remember, the board needs a well-reasoned argument to make an informed decision, so be thorough in your analysis. |

以下是上述提示生成的範例輸出：

> \<thinking> <br/> Step 1: Analyze market potential <br/> - AcmeFlow's U.S. revenue of 150M shows strong product-market fit in a mature market. <br/> - Asia's tech sector is growing rapidly, with a 12% YoY growth and a 500B market size. This indicates significant potential for expansion. <br/> - High smartphone penetration (80%) and increasing digital transformation suggest a strong demand for tech solutions like AcmeFlow's project management platform. <br/> <br/> Step 2: Assess competition <br/> - Only two major local competitors in Asia with a combined 30% market share. This leaves 70% of the market open, a substantial opportunity for AcmeFlow. <br/> - Competitors lack key features like real-time collaboration and AI-driven insights, which are AcmeFlow's USPs. This differentiation could be a significant advantage. <br/> <br/> Step 3: Evaluate regulatory challenges <br/> - Data privacy laws in Asia are diverse and evolving. In China and Singapore, laws are stringent (similar to GDPR), while in India and Indonesia, they're still developing. <br/> - AcmeFlow's existing compliance with GDPR and SOC 2 is advantageous, but we'll need to invest in region-specific compliance to mitigate risks. Estimated cost: 300,000-500,000. <br/> <br/> Step 4: Project financials <br/> - Initial investment for market entry: 2.5M (includes localization, marketing, legal fees) <br/> - Projected first-year revenue (conservative): 2% of market share = 10B * 0.02 = 200M <br/> - Estimated growth rate: 20% YoY for first 3 years, based on our U.S. growth and Asia's market trend <br/> - 5-year projected revenue: 200M (Y1) \* 1.2^4 ≈ 415M (Y5) <br/> - Break-even analysis: Assuming 30% profit margin, we'll break even within the first year. <br/> \</thinking> <br/> <br/> \<recommendation> <br/> Based on the analysis, I strongly recommend that AcmeFlow expands into the Asian market. The potential rewards far outweigh the risks. <br/> <br/> Key points: <br/> 1\. Massive market opportunity: 500B market with rapid 12% YoY growth. <br/> 2\. Competitive advantage: Our real-time and AI features outshine local competitors. <br/> 3\. High ROI: Initial 2.5M investment could yield 200M in first year, with strong YoY growth. <br/> 4\. Manageable risks: Compliance costs are significant but manageable given the revenue potential. <br/> <br/> The market is ripe, our product is superior, and the financials are compelling. Early entry will allow us to establish a strong foothold before the market becomes more saturated. I recommend proceeding with a phased rollout, starting with Singapore and India where we have the strongest market research data. <br/> \</recommendation> 

這個回應展示了「讓 Claude 思考」的力量：

1. **結構化分析**：`<thinking>` 標籤包含逐步分析，邏輯性地拆解決策過程。這讓董事會能跟隨 Claude 的推理並評估每個要點。同時也讓我們這些開發者能洞悉 Claude 的思考過程，並在必要時補充或修改提示。
2. **關鍵洞見**：Claude 突出了市場規模、競爭格局、法規挑戰和財務預測等關鍵因素，顯示對商業情境的深入理解。
3. **清楚的建議**：`<recommendation>` 標籤包含簡潔、可執行的建議，並由分析中的關鍵要點支撐。分階段展開的策略展現了策略性思維，在進取心與謹慎之間取得平衡。`<recommendation>` 標籤也讓我們能輕鬆提取相關的「最終」資訊供其他用途使用。

透過使用「讓 Claude 思考」技巧，我們將原本可能是模糊的單句回應，轉化為全面、適合董事會呈現的分析。這種層次的細節與清晰度，對於國際擴張這類高風險商業決策而言極為寶貴。


### 重點整理

#### 適用時機
* 複雜推理任務
* 需要理解 Claude 的邏輯時（用於除錯）
* 引導 Claude 完成多步驟問題解決的最佳方式

#### 解決的問題

* 決策缺乏透明度
* 邏輯不一致
* 在複雜流程中跳過步驟



---

## 5\. 賦予 Claude 角色

### 定義：
Claude 是一個能力強大的助理，但有時在對話中提供角色扮演資訊會有所助益。透過為 Claude 指定角色，你可以促使它以特定方式回應、提升其準確性與表現，並調整其語調和態度以符合所需情境。這個技巧也稱為角色提示（role prompting）。

一種選擇是直接在主要 user 提示中加入角色提示語言，但我們建議將角色資訊放在 `system_prompt` 中。請注意，角色資訊是我們建議放在 `system_prompt` 中的唯一資訊類型。

### 重要性：
在生產環境的提示中，一致性至關重要：Claude 的語調、專業程度和角色資訊應在多次互動中保持一致。透過系統提示使用角色提示，可確保 Claude 在多次互動中維持一致的聲音和專業程度。

角色提示在以下情況特別有用：
- **高度技術性任務**：若需要 Claude 執行與邏輯、數學或程式設計相關的複雜任務，指定適當的角色能幫助它在任務中表現出色，即使沒有角色提示可能會有困難。
- **特定溝通風格**：當你需要 Claude 回應中呈現特定語調或風格時，角色提示是達成所需輸出的有效方式。
- **提升基準表現**：除非嚴重受到 token 數量限制，否則若想嘗試提升 Claude 的基準表現，幾乎沒有理由不使用角色提示。


### 不良範例：應對產品危機

你的公司 AcmeEV 剛發現其最新電動車型號中存在嚴重軟體漏洞，可能導致意外加速。公關團隊需要起草公開聲明，但他們已不堪重負。他們在沒有提供太多指引的情況下向 Claude 求助：

| 角色 | 內容 |
| ---- | -------------------------------------------------------------------------------------------------------- |
| User | Our new EV has a bug that can cause sudden acceleration. We need a public statement ASAP. Can you write something for us? It's a serious issue, so make sure it sounds ok. |

這個提示有以下問題：
- 缺乏任何角色或情境，Claude 可能無法掌握情況的嚴重性。
- 「Make sure it sounds ok」含糊不清。Claude 需要知道在這個關鍵情境中「ok」意味著什麼。
- **沒有關於語調、核心訊息或目標受眾的指引，可能導致回應與公司的危機溝通策略不符。**

### 良好範例：應對產品危機

現在，讓我們使用角色提示來獲得更適切的回應：

| 角色 | 內容 |
| ---- | -------- |
| System | You are the Chief Communications Officer (CCO) at AcmeEV, a leading electric vehicle manufacturer known for innovation and safety. You have 20 years of experience in crisis communications, having handled issues from product recalls to CEO scandals. Your communication style is empathetic yet authoritative, always prioritizing public safety while maintaining brand integrity. <br/>  |
| User  | We've discovered a critical software bug in our new Model E that can cause unintended acceleration. The issue affects 70% of cars sold in the last quarter. Our engineering team is working on it, but the fix may take up to two weeks. Draft a public statement for immediate release. <br/> \<crisis_communication_guidelines> <br/> 1\. Acknowledge the issue promptly and express concern for affected parties. <br/> 2\. Clearly state the problem and its potential impact, avoiding technical jargon. <br/> 3\. Outline immediate actions taken to ensure safety. <br/> 4\. Provide a clear timeline for resolution and regular updates. <br/> 5\. Reaffirm company values (safety, innovation) and commitment to customers. <br/> 6\. Offer a direct line of communication for concerns. <br/> 7\. Close with a forward-looking statement to rebuild trust. <br/> <br/> Remember, in a crisis, speed, transparency, and empathy are key. Your words will be scrutinized by the media, customers, and shareholders alike. The goal is to protect public safety, maintain brand reputation, and set the stage for recovery.<br/> \</crisis_communication_guidelines><br/><br/> Follow these steps: <br/> 1\. Review the provided information and identify key facts (percentage affected, timeframe for fix). <br/> 2\. Draft the statement following our crisis communication guidelines. Use a tone that balances concern with confidence. <br/> 3\. Include a quote from the CEO that reinforces our commitment to safety. <br/> <br/> Write your analysis within \<analysis>\</analysis> tags, and your final statement within \<statement>\</statement> tags.                                   |

### 重點整理

#### 適用時機
* 設定特定情境或視角時
* 需要具備特定專業知識的回應時
* 影響回應的語調或風格時

#### 解決的問題

* 缺乏符合情境的回應
* 語調或風格不一致
* 回應未符合特定專業要求




***

## 6. 長上下文提示

Claude 的延伸上下文視窗使其能夠處理需要大量資料的複雜任務。當在提示中結合大量資訊（尤其是 30K+ tokens）與指令時，以清楚區分輸入資料與指令的方式結構化提示非常重要。我們建議使用 XML 標籤包覆每個文件，讓 Claude 清楚知道輸入資料在哪裡結束，指令、範例或提示的其他部分從哪裡開始。

此外，**我們建議將長文件和上下文放在提示的最前面**，指令和範例放在後面。若將文件放在詳細指令或使用者查詢之前，Claude 的表現通常會明顯較好。


### 良好範例：分析市場趨勢

| 角色 | 內容 |
| ---- | -------- |
| User | I need a comprehensive analysis for our upcoming launch of 'AcmeAI', an AI-powered CRM. Please review these market research reports and provide insights: <br/> <br/>\<reports> <br/> \<report_1> <br/> \{\{GLOBAL_TECH_TRENDS_2023}} <br/> </report_1> <br/> \<report_2> <br/> \{\{CRM_MARKET_ANALYSIS}} <br/> </report_2> <br/> \<report_3> <br/> \{\{COMPETITOR_LANDSCAPE}} <br/> \</report_3> <br/> \</reports> <br/> <br/> Generate a detailed report with the following sections: <br/> <br/> 1\. Executive Summary (100-150 words): Synthesize the key findings and their implications for AcmeAI's launch. <br/> 2\. Market Opportunity: <br/> - Global CRM market size and growth rate <br/> - AI adoption in CRM: current and projected <br/> - Region-wise market potential (focus on North America, Europe, and Asia-Pacific) <br/> 3\. Competitor Analysis: <br/> - Top 3 competitors' market share and growth rates <br/> - Their AI capabilities vs. ours (use a comparison table) <br/> - Gaps in their offerings that AcmeAI can exploit <br/> 4\. Launch Strategy (timeline view): <br/> - Q3 2024: Key milestones and marketing initiatives <br/> - Q4 2024: Sales targets and partnership goals <br/> - Q1 2025: Post-launch review and product roadmap <br/> 5\. Risk Assessment: <br/> - SWOT analysis focusing on AI-specific factors <br/> - Mitigation strategies for top 3 risks <br/> <br/> Use \<section>\</section> tags for each main section to make the report easy to parse.|

這個提示效果顯著，原因如下：

1. **文件優先**：長文件排在詳細提示指令之前。
2. **結構化資料**：每份報告都以 XML 標籤清楚劃分（`<report_1>`、`<report_2>`、`<report_3>`），巢狀在更大的 `<reports>` 標籤組中，讓 Claude 容易區分和參照不同的資料來源。
3. **清楚的指令**：提示明確指定 Claude 應從每份報告中提取什麼資訊（市場規模、AI 採用率、競爭對手分析），降低遺漏關鍵資料的可能性。
4. **XML 標籤用於輸出**：`<section>` 標籤讓 Claude 的回應能以程式方式解析，這在將輸出整合進其他業務流程或簡報時非常有用。


### 重點整理

#### 適用時機
* 處理大量輸入資料時



#### 解決的問題
* 難以處理大型、複雜的輸入

---


## 結語

這些技巧構成了提升 Claude 在各種任務中表現的強大工具組。透過深思熟慮地運用這些技巧，你可以顯著提升 Claude 輸出的準確性、一致性和相關性。隨著你持續與 Claude 合作，你將培養出對不同情境應用哪些技巧的直覺。

我們鼓勵你在自己的專案中應用這些技巧，並持續探索優化與 Claude 互動的新方式。AI 領域正在快速演進，提示工程的最佳實踐也在不斷更新。
