# 完整的工具使用工作流程

## 學習目標

* 理解完整的工具使用工作流程
* 撰寫格式正確的 `tool_result` 訊息
* 實作一個使用工具的聊天機器人

在這堂課中，我們將實作先前介紹過的完整四步驟工具使用工作流程。到目前為止，我們已看到 Claude 如何使用工具，但還沒有將工具執行結果回傳給 Claude。以下是完整四步驟流程的回顧：

1. **提供 Claude 工具與使用者提示：**（API 請求）
    * 定義你希望 Claude 能夠使用的工具集合，包含名稱、描述及輸入結構定義。
    * 提供一個可能需要使用一或多個工具才能回答的使用者提示，例如「我有 $500 能買幾股通用汽車？」

2. **Claude 使用工具：**（API 回應）
    * Claude 評估使用者提示，決定是否需要使用任何可用工具。若需要，也決定使用哪些工具及其輸入值。
    * Claude 輸出格式正確的工具使用請求。
    * API 回應的 `stop_reason` 將是 `tool_use`，表示 Claude 想要使用外部工具。

3. **提取工具輸入、執行程式碼並回傳結果：**（API 請求）
    * 在客戶端，你需要從 Claude 的工具使用請求中提取工具名稱與輸入。
    * 在客戶端執行實際的工具程式碼。
    * 透過在對話中加入包含 `tool_result` 內容區塊的新使用者訊息，將結果回傳給 Claude。

4. **Claude 使用工具結果來組成回應：**（API 回應）
    * 收到工具結果後，Claude 將利用這些資訊對原始使用者提示組成最終回應。

在這堂課中，我們將走完整個流程。

以下是整體流程的概覽圖：

![tool_use_flow.png](images/tool_use_flow.png)

以下是說明我們的腳本運作方式的圖示：

![wikipedia_diagram.png](images/wikipedia_diagram.png)


以下是一些實際對話範例，說明我們希望達到的最終結果：

> **使用者**：截至 2024 年，Christopher Nolan 和 Ben Stiller 誰拿的奧斯卡獎比較多？

> *Claude 想要獲取 Christopher Nolan 的維基百科文章*（工具使用）

> *Claude 想要獲取 Ben Stiller 的維基百科文章*（工具使用）

> **Claude**：截至 2024 年，導演 Christopher Nolan 憑藉 2023 年的電影《奧本海默》，獲得了最佳導演和最佳影片兩項奧斯卡獎。而演員喜劇演員 Ben Stiller 在其職業生涯中尚未獲得任何奧斯卡獎，雖然他曾獲得艾美獎及 MTV 電影獎等其他獎項。直接回答這個問題：截至 2024 年，Christopher Nolan 獲得了更多奧斯卡獎（2 座），而 Ben Stiller 尚未獲得任何獎項。

另一個例子：

> **使用者：** 2024 年名人堂錦標賽（Masters Tournament）的冠軍是誰？

> *Claude 想要獲取 2024 Masters Tournament 的維基百科文章*（工具使用）

> **Claude：** Scottie Scheffler 贏得了 2024 年名人堂錦標賽，這是他第二次獲得 Masters 冠軍。他以四桿的差距領先亞軍 Ludvig Åberg，後者是第一次參加 Masters。

如果我們問 Claude 一個不需要使用工具就能回答的問題，它應該直接回答，而不使用我們的維基百科搜尋工具：

> **使用者：** 2021 年 Masters 的冠軍是誰？

> **Claude：** Hideki Matsuyama 贏得了 2021 年名人堂錦標賽，成為第一位贏得高爾夫大滿貫賽事的日本男性球員。他以 278 桿（-10）的成績在奧古斯塔國家高爾夫球場奪得綠夾克。



以下是整個流程結束時 `messages` 清單的樣子：

![messages_diagram.png](images/messages_diagram.png)

本課的主要新主題是：當我們回應 Claude 的 `tool_use` 訊息時，如何正確格式化我們的 `tool_result` 使用者訊息。

## 建立完整工作流程

### 1. 定義我們的維基百科搜尋函式

在與 Claude 進行任何互動之前，我們先撰寫一個簡單的函式來搜尋維基百科。以下函式使用 `wikipedia` 套件，根據搜尋詞彙搜尋符合的維基百科頁面。為了簡化，我們取第一個回傳的頁面標題，再用它來存取對應的頁面內容。

注意：這個簡單的函式假設我們一定能找到維基百科文章。為了保持簡潔，這個函式沒有錯誤處理——在實際應用中這不是個好主意！

```python
import wikipedia

def get_article(search_term):
    results = wikipedia.search(search_term)
    first_result = results[0]
    page = wikipedia.page(first_result, auto_suggest=False)
    return page.content
```

```python
article = get_article("Superman")
print(article[:500]) # 文章非常長，只印出預覽
```
```
Superman is a superhero who appears in American comic books published by DC Comics. The character was created by writer Jerry Siegel and artist Joe Shuster, and debuted in the comic book Action Comics #1 (cover-dated June 1938 and published April 18, 1938). Superman has been adapted to a number of other media, which includes radio serials, novels, films, television shows, theater, and video games.
Superman was born on the fictional planet Krypton with the birth name of Kal-El. As a baby, his par
```

```python
article = get_article("Zendaya")
print(article[:500]) # 文章非常長，只印出預覽
```
```
Zendaya Maree Stoermer Coleman (  zən-DAY-ə; born September 1, 1996) is an American actress and singer. She has received various accolades, including two Primetime Emmy Awards and a Golden Globe Award. Time magazine named her one of the 100 most influential people in the world in 2022.
Born and raised in Oakland, California, Zendaya began her career as a child model and backup dancer. She made her television debut as Rocky Blue in the Disney Channel sitcom Shake It Up (2010–2013) and starred as
```

### 2. 撰寫工具定義
接下來，我們需要使用正確的 JSON Schema 格式來定義我們的工具。這是一個非常簡單的工具定義，因為該函式只需要一個引數：搜尋詞彙字串。

```python
article_search_tool = {
    "name": "get_article",
    "description": "A tool to retrieve an up to date Wikipedia article.",
    "input_schema": {
        "type": "object",
        "properties": {
            "search_term": {
                "type": "string",
                "description": "The search term to find a wikipedia article by title"
            },
        },
        "required": ["search_term"]
    }
}
```

### 3. 提供 Claude 工具和使用者提示

接下來，我們告訴 Claude 它可以使用維基百科搜尋工具，並請它回答一個我們知道它在沒有工具的情況下無法回答的問題，例如「2024 年 Masters 錦標賽的冠軍是誰？」

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

messages = [{"role": "user", "content": "who won the 2024 Masters Tournament?"}]

response = client.messages.create(
        model="claude-3-sonnet-20240229",
        messages=messages,
        max_tokens=1000,
        tools=[article_search_tool]
    )
```

### 4. Claude 使用工具（API 回應）

讓我們看看收到的回應。Claude 想要使用我們的工具！

```python
response.content
```
```
[TextBlock(text='Okay, let me see if I can find information about the winner of the 2024 Masters Tournament on Wikipedia:', type='text'),
 ToolUseBlock(id='toolu_01CWuduGjgSRfsYJUNC2wxi7', input={'search_term': '2024 Masters Tournament'}, name='get_article', type='tool_use')]
```

Claude 的回應包含 2 個區塊：

* 一個 TextBlock，內容為「好的，讓我試試看能否在維基百科上找到 2024 年 Masters 錦標賽冠軍的相關資訊：」

```
TextBlock(text='Okay, let me use the available tool to try and find information on who won the 2024 Masters Tournament:', type='text')
```

* 一個 ToolUseBlock，呼叫我們的 `get_article` 工具，使用 `search_term` "2024 Masters Tournament"

```
ToolUseBlock(id='toolu_01MbstBxD654o9hE2RGNdtSr', input={'search_term': '2024 Masters Tournament'}, name='get_article', type='tool_use')]
```


### 5. 提取工具輸入、執行程式碼並回傳結果（API 請求）

既然 Claude 已回應表示想要使用工具，現在我們需要實際執行底層功能，並將對應的維基百科頁面內容回傳給 Claude。

**我們需要特別注意，確保更新 `messages` 清單**

我們先更新 `messages` 清單，加入 Claude 最新的回應：

```python
messages.append({"role": "assistant", "content": response.content})
```

```python
messages
```
```
[{'role': 'user', 'content': 'who won the 2024 Masters Tournament?'},
 {'role': 'assistant',
  'content': [TextBlock(text='Okay, let me see if I can find information about the winner of the 2024 Masters Tournament on Wikipedia:', type='text'),
   ToolUseBlock(id='toolu_01CWuduGjgSRfsYJUNC2wxi7', input={'search_term': '2024 Masters Tournament'}, name='get_article', type='tool_use')]}]
```

接下來，我們提取 Claude 想要使用的具體工具和引數：

```python
# 這是一個簡單但較為脆弱的取得工具使用資訊的方式
# 我們只是取 Claude 回應的最後一個區塊。
tool_use = response.content[-1]
tool_name = tool_use.name
tool_input = tool_use.input
print("Tool name: ", tool_name)
print("Tool input", tool_input)
```
```
Tool name:  get_article
Tool input {'search_term': '2024 Masters Tournament'}
```

接下來，我們確認 Claude 正在呼叫我們預期的 `get_article` 工具。我們取出 Claude 想出的 `search_term`，並將其傳入我們先前撰寫的 `get_article` 函式。

```python
if tool_name == "get_article":
    search_term = tool_input["search_term"]
    wiki_result = get_article(search_term)
    print(f"Searching Wikipedia for {search_term}")
    print("WIKIPEDIA PAGE CONTENT:")
    print(wiki_result[:500]) #只印出文章的一小部分，因為內容很長
```
```
Searching Wikipedia for 2024 Masters Tournament
WIKIPEDIA PAGE CONTENT:
The 2024 Masters Tournament was the 88th edition of the Masters Tournament and the first of the men's four major golf championships held in 2024. The tournament was played from April 11–14 at Augusta National Golf Club in Augusta, Georgia, United States. Scottie Scheffler won his second Masters and major, four strokes ahead of runner-up Ludvig Åberg, who was playing in his first major. Scheffler became the fourth-youngest two-time winner of the tournament and the second player, after Tiger Woods
```

現在我們已經執行了 Claude 要求我們呼叫的函式，是時候將維基百科頁面資料回傳給 Claude 了。

如我們所知，當 Claude 想要使用工具時，它會以 `stop_reason` 為 `tool_use` 來回應，並且 API 回應中包含一或多個 `tool_use` 內容區塊，其中包括：
* `id`：此特定工具使用區塊的唯一識別碼。這將用於之後比對工具結果。
* `name`：正在使用的工具名稱。
* `input`：包含傳遞給工具的輸入的物件，符合工具的 `input_schema`。

一旦我們執行了底層工具函式，我們也需要以特定格式回應 Claude。具體來說，若要繼續對話，我們需要發送一則新訊息，其 **role 為 `user`**，並包含 **`tool_result` 類型的內容區塊**，以及以下資訊：
* `tool_use_id`：這個結果對應的工具使用請求 id。
* `content`：工具的執行結果，可以是字串（例如 "content": "15 degrees"）或嵌套內容區塊的清單（例如 "content": [{"type": "text", "text": "15 degrees"}]\）。
* `is_error`（選填）：若工具執行過程中發生錯誤，設為 true。

以下是一個格式正確的 `tool_result` 訊息範例：

```python
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A09q90qw90lq917835lq9",
      "content": "The result of actually calling the tool goes here"
    }
  ]
}
```

現在讓我們在維基百科搜尋範例中實作。我們需要構建一個格式正確的工具回應訊息，將維基百科搜尋結果回傳給 Claude：

```python
tool_response = {
    "role": "user",
    "content": [
        {
        "type": "tool_result",
        "tool_use_id": tool_use.id,
        "content": wiki_result
        }
    ]
}
```

```python
# 注意長篇的維基百科文章內容！
tool_response
```
```
{'role': 'user',
 'content': [{'type': 'tool_result',
   'tool_use_id': 'toolu_01CWuduGjgSRfsYJUNC2wxi7',
   'content': "The 2024 Masters Tournament was the 88th edition of the Masters Tournament and the first of the men's four major golf championships held in 2024. The tournament was played from April 11–14 at Augusta National Golf Club in Augusta, Georgia, United States. Scottie Scheffler won his second Masters and major, four strokes ahead of runner-up Ludvig Åberg, who was playing in his first major. Scheffler became the fourth-youngest two-time winner of the tournament and the second player, after Tiger Woods in 2001, to win both the Masters and The Players Championship in the same calendar year. \n\n\n== Course ==\n\nThe only change to the course for the 2024 tournament was the lengthening of the second hole by ten yards.\n\n\n== Field ==\nParticipation in the Masters Tournament is by invitation only, and the tournament has the smallest field of the major championships. There are a number of criteria by which invitations are awarded, including all past winners, recent major champions, leading finishers in the previous year's majors, leading players on the PGA Tour in the previous season, winners of full-point tournaments on the PGA Tour during the previous 12 months, leading players in the Official World Golf Ranking, and some leading amateurs.\n\n\n=== Criteria ===\nThere were three changes to invitee criteria between the 2023 and 2024 tournaments. The first was to add the current NCAA Division I Men's Individual Champion a spot in the field, provided that he remains an amateur at the time of the tournament. In addition, Augusta National clarified that players who qualify for the Tour Championship must remain eligible to play in that event in order to qualify for the Masters. Also, with the PGA Tour returning to a calendar-year season schedule, Augusta National noted that winners of fall PGA Tour events would continue to qualify for the Masters.\nThe below list details the qualification criteria for the 2024 Masters Tournament and the players who have qualified under them; any additional criteria under which players qualified are indicated in parentheses.\n1. All past winners of the Masters Tournament\n\nPast winners who did not play: Tommy Aaron, Ángel Cabrera, Charles Coody, Ben Crenshaw, Nick Faldo, Raymond Floyd, Trevor Immelman, Bernhard Langer, Sandy Lyle, Larry Mize, Jack Nicklaus, Mark O'Meara, Gary Player, Craig Stadler, Tom Watson, Ian Woosnam, Fuzzy Zoeller\n2. Recent winners of the U.S. Open (2019–2023)\n\n3. Recent winners of The Open Championship (2019–2023)\n\n4. Recent winners of the PGA Championship (2019–2023)\n\n5. Recent winners of The Players Championship (2022–2024)\n6. The winner of the gold medal at the Olympic Games\n7. The winner and runner-up in the 2023 U.S. Amateur\n\nNeal Shipley (a)\n8. The winner of the 2023 Amateur Championship\n\nChristo Lamprecht (a)\n9. The winner of the 2023 Asia-Pacific Amateur Championship\n\nJasper Stubbs (a)\n10. The winner of the 2024 Latin America Amateur Championship\n\nSantiago de la Fuente (a)\n11. The winner of the 2023 U.S. Mid-Amateur Golf Championship\n\nStewart Hagestad (a)\n12. The winner of the 2023 NCAA Division I men's golf individual championship\n\nFred Biondi forfeited his invitation by turning professional.\n13. The leading 12 players, and those tying for 12th place, from the 2023 Masters Tournament\n\n14. The leading four players, and those tying for fourth place, in the 2023 U.S. Open\n\nRory McIlroy (17,18,19,20)\n15. The leading four players, and those tying for fourth place, in the 2023 Open Championship\n\n16. The leading four players, and those tying for fourth place, in the 2023 PGA Championship\n\n17. Winners of tournaments on the PGA Tour between the 2023 Masters Tournament and the 2024 Masters Tournament\n\n18. All players who qualified for and are eligible for the 2023 Tour Championship\n\n19. The leading 50 players on the Official World Golf Ranking as of December 31, 2023\n\n20. The leading 50 players on the Official World Golf Ranking as of April 1, 2024\n\nAn Byeong-hun\n21. Special invitations\n\n\n== Par-3 contest ==\nWednesday, April 10\nRickie Fowler won the par-3 contest with a score of 22 (−5). There were five holes-in-one recorded, by Sepp Straka, Luke List, Gary Woodland, Viktor Hovland, and Lucas Glover.\n\n\n== Round summaries ==\n\n\n=== First round ===\nThursday, April 11, 2024Friday, April 12, 2024\nInclement weather delayed the start of the tournament until 10:30 am Eastern time. As a result, 27 players did not complete the first round on Thursday.\nThe 8th hole, a par 5, saw a record-breaking total of 53 par-breaking scores, including 50 birdies and 3 eagles, the highest ever recorded on this hole in Masters history. \n\n\n=== Second round ===\nFriday, April 12, 2024\nBy making the cut, Tiger Woods set the record for most consecutive cuts made at the Masters, at 24. Phil Mickelson made the cut for the 28th time, surpassing Raymond Floyd and Bernhard Langer to move into solo fourth place for most cuts made at the Masters, trailing only Jack Nicklaus (37), Fred Couples (31) and Gary Player (30).\nRookie Ludvig Åberg posted the lowest score of the round, a 69, and advanced to a solo 7th place.\nBryson DeChambeau, before making a birdie on the 13th hole, moved a large directional sign that was in his line of play.\nPatrick Cantlay achieved two eagles on par 4s, marking only the fourth instance in history that a player has recorded two par-4 eagles in a single Masters Tournament, the last being Brandt Jobe in 2006.\nThe cut came at 150 (+6), with 60 players advancing to the weekend. Notables to miss the cut included 2015 champion Jordan Spieth, 2020 champion Dustin Johnson, reigning U.S. Open champion Wyndham Clark, Open champion Brian Harman, and World No. 6 Viktor Hovland. Two-time major champion Justin Thomas played his last four holes in seven-over to miss the cut by one shot.\n\n\n=== Third round ===\nSaturday, April 13, 2024\nScottie Scheffler, beginning the round in a three-way tie for the lead, chipped in for birdie on the first hole. After a double bogey on the 10th, Scheffler holed a 31-foot eagle putt on the par-five 13th, the only eagle recorded on that hole during the round. He also birdied the 15th and 18th to finish at seven under following a 71 (−1) to take a one-shot lead into the final round.\nCollin Morikawa birdied his first three holes in a three-under round of 69 and finished at six under, one shot back of Scheffler. Max Homa, tied for the lead at the start of the round, didn't make a birdie in a one-over 73 and fell two back at 5 under. Bryson DeChambeau was also atop the leaderboard to begin the round but hit his third shot in the water on the 15th and made double bogey. He holed out for birdie on the 18th to finish at three under and four shots back of Scheffler. Ludvig Åberg, making his Masters and major championship debut, was four under on his round until a bogey at the 14th. He then left his third shot on the 15th short and three-putted from just off the green for another bogey. He shot 70 (–2) and ended up at four under.\nNicolai Højgaard moved into sole possession of the lead following a run of three straight birdies from holes 8 to 10, but he then made five straight bogeys including hitting into the water on both the 13th and 15th and finished at two under.\nTiger Woods carded a 10-over-par 82 for the third round, his highest score ever in a major championship.\nNo eagles were recorded on the par-5 15th hole through the first three rounds, marking only the second time in the past 50 years that No. 15 has failed to produce an eagle by this point in the tournament. Shane Lowry scored an eagle on the par-4 14th hole, marking the first eagle on this hole since Martin Kaymer in 2016.\n\n\n=== Final round ===\nSunday, April 14, 2024\n\nWorld No. 1 Scottie Scheffler shot a four-under 68 to win his second Masters title in the last three years by four shots over runner-up Ludvig Åberg.\nScheffler began the round with a one-shot lead and birdied the third hole to go two shots ahead. He then bogeyed the fourth after hitting his tee shot over the green. Max Homa birdied the second, his first birdie in 34 holes, to get within one of the lead, while Åberg hit his approach on the seventh to four feet and made birdie to also get within one of the lead.\nScheffler bogeyed the seventh to create a three-way tie with Åberg and Collin Morikawa at six under, while Homa joined the lead with a two-putt birdie at the par-five eighth. Both Scheffler and Morikawa birdied the eighth to get to seven under, while Åberg holed a 36-foot birdie putt on the ninth to again tie. Scheffler then hit his approach on the ninth to within a foot for another birdie to get to 8 under and again in sole possession of the lead going to the second nine.\nAll three challengers then fell from contention. Morikawa hit his second shot on the ninth into a greenside bunker and couldn't advance on his third, ending up with a double bogey to fall three shots behind. He found the water on his approach at the 11th and made another double bogey. Åberg also hit into the water on the 11th for a double bogey. Homa got back within one with a close approach to the 10th, but his tee shot on the 12th flew over the green into the bushes and he was forced to take a drop. He made a double bogey on the hole to fall three shots behind.\nScheffler birdied the 10th, his third birdie in a row, to get to nine under and open a two-shot lead. Despite a bogey on the 11th, Scheffler two-putted for birdie at the par-five 13th and hit his second shot on the 14th to within four feet for another birdie to reach 10 under. He then made a nine-foot birdie putt on the par-three 16th to get to 11 under. Pars on his final two holes allowed him to close out the tournament with a four-shot victory.\nÅberg birdied the 13th and 14th to get back to seven under and finish four back of Scheffler in his Masters and major championship debut. Morikawa and Homa both finished at four under for the tournament, in a tie for third place along with Tommy Fleetwood.\n\n\n==== Scorecard ====\n\nCumulative tournament scores, relative to par\n\nSource:\n\n\n== Notes ==\n\n\n== References ==\n\n\n== External links ==\nOfficial website"}]}
```

接下來，我們需要將 `tool_response` 訊息加入到 messages 清單中：

```python
messages.append(tool_response)
```

我們的 `messages` 清單現在如下所示：

* 使用者：2024 年 Masters 錦標賽的冠軍是誰？
* 助理：我想使用 `get_article` 工具，搜尋詞彙為 "2024 Masters Tournament"
* 使用者：這是包含你所要求的維基百科文章的工具結果

以下圖示說明了這個過程。

![wiki_messages.png](images/wiki_messages.png)

請注意，初始的 `id` 與後續使用者訊息中的 `tool_use_id` 相符


### 6. Claude 使用工具結果來組成回應：（API 回應）

最後，我們可以使用更新後的 `messages` 清單向 Claude 發送新請求：

```python
follow_up_response = client.messages.create(
    model="claude-3-sonnet-20240229",
    messages=messages,
    max_tokens=1000,
    tools=[article_search_tool]
)
```

```python
follow_up_response.content[0].text
```
```
"Based on the summary from Wikipedia, it appears that Scottie Scheffler won the 2024 Masters Tournament. He shot a final round 68 to finish at 11-under par, four shots ahead of runner-up Ludvig Åberg. This was Scheffler's second Masters title, having also won in 2022. So the key details are:\n\n2024 Masters Tournament Winner: Scottie Scheffler (-11)\nRunner-Up: Ludvig Åberg (-7)\n\nThe Wikipedia article provides a detailed recap of each round and how Scheffler was able to separate himself from the rest of the field over the final 18 holes to claim his second green jacket. Let me know if you need any other information from the summary!"
```

Claude 現在擁有回答最初問題所需的資訊，並回應：

> '根據維基百科文章摘要，Scottie Scheffler 贏得了 2024 年 Masters 錦標賽。他在最後一輪打出...'

我們已完成整個流程的所有 4 個步驟！

***

## 改善程式碼

至少，我們可能需要將上述所有程式碼放入一個可重複使用的函式中，這樣才能多次嘗試：

```python

def answer_question(question):
    messages = [{"role": "user", "content": question}]

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        messages=messages,
        max_tokens=1000,
        tools=[article_search_tool]
    )
    
    if(response.stop_reason == "tool_use"):
        tool_use = response.content[-1]
        tool_name = tool_use.name
        tool_input = tool_use.input
        #將 Claude 的工具使用呼叫加入 messages：
        messages.append({"role": "assistant", "content": response.content})

        if tool_name == "get_article":
            search_term = tool_input["search_term"]
            print(f"Claude wants to get an article for {search_term}")
            wiki_result = get_article(search_term) #取得維基百科文章內容
            #構建我們的 tool_result 訊息
            tool_response = {
                "role": "user",
                "content": [
                    {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": wiki_result
                    }
                ]
                }
            messages.append(tool_response)
            #回應 Claude
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                messages=messages,
                max_tokens=1000,
                tools=[article_search_tool]
            )
            print("Claude's final answer:")
            print(response.content[0].text)

    else:
        print("Claude did not call our tool")
        print(response.content[0].text)
```

```python
answer_question("Who won the 2024 F1 Australian Grand Prix")
```
```
Claude want to get an article for 2024 F1 Australian Grand Prix
Claude's Final Answer:

The key information from the Wikipedia article is:

Carlos Sainz Jr. of Ferrari won the 2024 Australian Grand Prix, with his teammate Charles Leclerc finishing second. Lando Norris of McLaren finished third. 

Max Verstappen of Red Bull Racing started on pole but retired early due to a brake failure, ending his streak of 9 consecutive wins.

The race set a new attendance record at Albert Park of 452,055 spectators over the weekend, making it the most attended sporting event ever in Melbourne.
```

```python
answer_question("Who stars in the movie Challengers?")
```
```
Claude want to get an article for Challengers (2023 film)
Claude's Final Answer:
Based on the plot summary and cast details from Wikipedia, the main stars of the 2023 film Challengers are:

- Zendaya as Tashi Duncan
- Josh O'Connor as Patrick Zweig  
- Mike Faist as Art Donaldson

The film also features supporting roles by Darnell Appling, AJ Lister, Nada Despotovich, Naheem Garcia, and Hailey Gates.

So the three leads starring in the romantic sports drama Challengers are Zendaya, Josh O'Connor, and Mike Faist.
```

```python
#讓我們試一個 Claude 應該不需要使用工具就能回答的例子：
answer_question("Who wrote the book 'Life of Pi'")
```
```
Claude want to get an article for Life of Pi
Claude's Final Answer:
Based on the Wikipedia article retrieved, the book 'Life of Pi' was written by the Canadian author Yann Martel and published in 2001. It won the Man Booker Prize in 2002 and has sold over 10 million copies worldwide. The novel tells the story of an Indian boy named Pi Patel who survives for 227 days stranded on a lifeboat in the Pacific Ocean after a shipwreck, with a Bengal tiger named Richard Parker as his only companion.
```

請注意，Claude 呼叫了我們的維基百科工具來幫助回答最後這個問題，即使 Claude 其實已經知道答案。《少年 Pi 的奇幻漂流》出版於 2001 年，遠在 Claude 的訓練截止日期之前！

***

## 改善提示詞

如同我們在之前的課程中看到的，有時 Claude 過於積極地使用工具。解決這個問題最簡單的方式是透過系統提示詞。


我們可以加入類似以下的系統提示詞：

```python
system_prompt = """
    You will be asked a question by the user. 
    If answering the question requires data you were not trained on, you can use the get_article tool to get the contents of a recent wikipedia article about the topic. 
    If you can answer the question without needing to get more information, please do so. 
    Only call the tool when needed. 
    """
```

讓我們更新函式以使用這個新的系統提示詞：

```python
def answer_question(question):
    system_prompt = """
    You will be asked a question by the user. 
    If answering the question requires data you were not trained on, you can use the get_article tool to get the contents of a recent wikipedia article about the topic. 
    If you can answer the question without needing to get more information, please do so. 
    Only call the tool when needed. 
    """

    messages = [{"role": "user", "content": question}]

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        system=system_prompt, 
        messages=messages,
        max_tokens=1000,
        tools=[article_search_tool]
    )
    
    if(response.stop_reason == "tool_use"):
        tool_use = response.content[-1]
        tool_name = tool_use.name
        tool_input = tool_use.input
        #將 Claude 的工具使用呼叫加入 messages：
        messages.append({"role": "assistant", "content": response.content})

        if tool_name == "get_article":
            search_term = tool_input["search_term"]
            print(f"Claude wants to get an article for {search_term}")
            wiki_result = get_article(search_term) #取得維基百科文章內容
            #構建我們的 tool_result 訊息
            tool_response = {
                "role": "user",
                "content": [
                    {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": wiki_result
                    }
                ]
                }
            messages.append(tool_response)
            #回應 Claude
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                system=system_prompt, 
                messages=messages,
                max_tokens=1000,
                tools=[article_search_tool]
            )
            print("Claude's final answer:")
            print(response.content[0].text)

    else:
        print("Claude did not call our tool")
        print(response.content[0].text)
```

讓我們嘗試同樣的問題：

```python
answer_question("Who wrote the book 'Life of Pi'")
```
```
Claude did not call our tool
The book 'Life of Pi' was written by the Canadian author Yann Martel. It was published in 2001 and went on to become an international bestseller. The novel blends elements of magical realism, adventure fiction and philosophical fiction. It tells the story of an Indian boy named Pi who survives for 227 days adrift in the Pacific Ocean after a shipwreck, in the company of a Bengal tiger named Richard Parker. The book won the Man Booker Prize in 2002 and was later adapted into an acclaimed film directed by Ang Lee in 2012.
```

成功了！Claude 在不需要工具的情況下沒有使用它。讓我們確認在需要最新知識的問題上它仍然能正常運作：

```python
answer_question("Who wrote the score for the movie Challengers?")
```
```
Claude want to get an article for Challengers (film)
Claude's Final Answer:
Based on the Wikipedia article summary, the score for the film Challengers was composed by Trent Reznor and Atticus Ross. The relevant quote is:

"Trent Reznor and Atticus Ross composed the film's score, having previously worked with Guadagnino on 2022's Bones and All. Post-production was completed by April 2023."

So to answer your original question - the musical score for the 2024 film Challengers was written by the composer duo Trent Reznor and Atticus Ross.
```

兩種情況下都運作正常！現在讓我們讓 Claude 的回應稍微簡潔一些。Claude 解釋如何得到正確答案固然很好，但有點冗長。讓我們做一些基本的提示詞工程來修正這個問題。

讓我們試試這個：

```python
prompt = f"""
    Answer the following question <question>Who wrote the movie Poor Things?</question>
    When you can answer the question, keep your answer as short as possible and enclose it in <answer> tags
    """
```

以下是更新了新提示詞的函式：

```python
def answer_question(question):
    system_prompt = """
    You will be asked a question by the user. 
    If answering the question requires data you were not trained on, you can use the get_article tool to get the contents of a recent wikipedia article about the topic. 
    If you can answer the question without needing to get more information, please do so. 
    Only call the tool when needed. 
    """
    prompt = f"""
    Answer the following question <question>{question}</question>
    When you can answer the question, keep your answer as short as possible and enclose it in <answer> tags
    """
    messages = [{"role": "user", "content": prompt}]

    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        system=system_prompt, 
        messages=messages,
        max_tokens=1000,
        tools=[article_search_tool]
    )
    
    if(response.stop_reason == "tool_use"):
        tool_use = response.content[-1]
        tool_name = tool_use.name
        tool_input = tool_use.input
        #將 Claude 的工具使用呼叫加入 messages：
        messages.append({"role": "assistant", "content": response.content})

        if tool_name == "get_article":
            search_term = tool_input["search_term"]
            print(f"Claude wants to get an article for {search_term}")
            wiki_result = get_article(search_term) #取得維基百科文章內容
            #構建我們的 tool_result 訊息
            tool_response = {
                "role": "user",
                "content": [
                    {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": wiki_result
                    }
                ]
                }
            messages.append(tool_response)
            #回應 Claude
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                system=system_prompt, 
                messages=messages,
                max_tokens=1000,
                tools=[article_search_tool]
            )
            print("Claude's final answer:")
            print(response.content[0].text)

    else:
        print("Claude did not call our tool")
        print(response.content[0].text)
```

```python
answer_question("Who wrote the score for the movie Challengers?")
```
```
Claude want to get an article for Challengers (2023 film)
Claude's Final Answer:
<answer>The score for the movie Challengers was composed by Trent Reznor and Atticus Ross.</answer>
```

```python
answer_question("How many legs does an octopus have?")
```
```
Claude did not call our tool
<answer>An octopus has 8 legs.</answer>
```

好多了！Claude 現在直接回答問題，不再附帶一大堆關於如何得到答案的「思考過程」和解釋。

***

## 練習

你能更新這段程式碼，使其符合以下要求嗎？
* Claude 可能無法從我們回應的第一個維基百科頁面獲得足夠的資訊。我們尚未處理這種情況。想像我們問 Claude「Christopher Nolan 有幾座奧斯卡獎？他比 Ben Stiller 的艾美獎數量多嗎？」Claude 需要搜尋 Christopher Nolan 的維基百科頁面和 Ben Stiller 的頁面，很可能是一個接一個地搜尋。我們目前的程式碼不支援這個功能，所以讓我們加入這個功能吧！**提示：使用迴圈！**
* 從 Claude 目前回應的 `<answer></answer>` 標籤中提取答案，這樣你只需印出實際的答案內容。
* 你能把這個改造成一個完整的命令列聊天機器人，持續詢問使用者輸入查詢，然後反覆回應答案，直到使用者退出程式？輸出可能如下所示：



以下是範例對話過程的截圖：

![exercise_conversation.png](images/exercise_conversation.png)
