# 使用多個工具的工具使用

現在我們要將工具使用提升到另一個層次！我們將提供 Claude 一套可供選擇的工具。我們的目標是為一家名為 TechNova 的虛構電子公司建立一個簡單的客戶支援聊天機器人。它將可以使用以下簡單工具：

* `get_user`：透過電子郵件、使用者名稱或電話號碼查詢使用者詳細資料
* `get_order_by_id`：直接透過訂單 ID 查詢訂單
* `get_customer_orders`：查詢某位客戶的所有訂單
* `cancel_order`：根據指定的訂單 ID 取消訂單

這個聊天機器人功能相當有限，但它展示了使用多個工具的幾個關鍵要素。

以下是聊天機器人互動範例的圖片。

![conversation1.png](images/conversation1.png)

以下是另一個聊天機器人互動示例，我們明確印出了 Claude 每次使用工具的訊息，以便更容易理解幕後發生的事情：

![conversation2.png](images/conversation2.png)


以下圖示展示了單一聊天訊息的資訊流向：

![chat_diagram.png](images/chat_diagram.png)

**重要提示：這個聊天機器人極其簡單，只要擁有下訂單使用者的使用者名稱或電子郵件，任何人都可以取消訂單。這個實作僅供教育目的，未經修改不應整合到實際的程式碼庫中！**

***

## 我們的假資料庫
在開始使用 Claude 之前，我們先定義一個非常簡單的 `FakeDatabase` 類別，它將保存一些假客戶和訂單資料，並提供與這些資料互動的方法。在現實世界中，聊天機器人可能會連接到一個或多個*真實的*資料庫。

```python
class FakeDatabase:
    def __init__(self):
        self.customers = [
            {"id": "1213210", "name": "John Doe", "email": "john@gmail.com", "phone": "123-456-7890", "username": "johndoe"},
            {"id": "2837622", "name": "Priya Patel", "email": "priya@candy.com", "phone": "987-654-3210", "username": "priya123"},
            {"id": "3924156", "name": "Liam Nguyen", "email": "lnguyen@yahoo.com", "phone": "555-123-4567", "username": "liamn"},
            {"id": "4782901", "name": "Aaliyah Davis", "email": "aaliyahd@hotmail.com", "phone": "111-222-3333", "username": "adavis"},
            {"id": "5190753", "name": "Hiroshi Nakamura", "email": "hiroshi@gmail.com", "phone": "444-555-6666", "username": "hiroshin"},
            {"id": "6824095", "name": "Fatima Ahmed", "email": "fatimaa@outlook.com", "phone": "777-888-9999", "username": "fatimaahmed"},
            {"id": "7135680", "name": "Alejandro Rodriguez", "email": "arodriguez@protonmail.com", "phone": "222-333-4444", "username": "alexr"},
            {"id": "8259147", "name": "Megan Anderson", "email": "megana@gmail.com", "phone": "666-777-8888", "username": "manderson"},
            {"id": "9603481", "name": "Kwame Osei", "email": "kwameo@yahoo.com", "phone": "999-000-1111", "username": "kwameo"},
            {"id": "1057426", "name": "Mei Lin", "email": "meilin@gmail.com", "phone": "333-444-5555", "username": "mlin"}
        ]

        self.orders = [
            {"id": "24601", "customer_id": "1213210", "product": "Wireless Headphones", "quantity": 1, "price": 79.99, "status": "Shipped"},
            {"id": "13579", "customer_id": "1213210", "product": "Smartphone Case", "quantity": 2, "price": 19.99, "status": "Processing"},
            {"id": "97531", "customer_id": "2837622", "product": "Bluetooth Speaker", "quantity": 1, "price": "49.99", "status": "Shipped"}, 
            {"id": "86420", "customer_id": "3924156", "product": "Fitness Tracker", "quantity": 1, "price": 129.99, "status": "Delivered"},
            {"id": "54321", "customer_id": "4782901", "product": "Laptop Sleeve", "quantity": 3, "price": 24.99, "status": "Shipped"},
            {"id": "19283", "customer_id": "5190753", "product": "Wireless Mouse", "quantity": 1, "price": 34.99, "status": "Processing"},
            {"id": "74651", "customer_id": "6824095", "product": "Gaming Keyboard", "quantity": 1, "price": 89.99, "status": "Delivered"},
            {"id": "30298", "customer_id": "7135680", "product": "Portable Charger", "quantity": 2, "price": 29.99, "status": "Shipped"},
            {"id": "47652", "customer_id": "8259147", "product": "Smartwatch", "quantity": 1, "price": 199.99, "status": "Processing"},
            {"id": "61984", "customer_id": "9603481", "product": "Noise-Cancelling Headphones", "quantity": 1, "price": 149.99, "status": "Shipped"},
            {"id": "58243", "customer_id": "1057426", "product": "Wireless Earbuds", "quantity": 2, "price": 99.99, "status": "Delivered"},
            {"id": "90357", "customer_id": "1213210", "product": "Smartphone Case", "quantity": 1, "price": 19.99, "status": "Shipped"},
            {"id": "28164", "customer_id": "2837622", "product": "Wireless Headphones", "quantity": 2, "price": 79.99, "status": "Processing"}
        ]

    def get_user(self, key, value):
        if key in {"email", "phone", "username"}:
            for customer in self.customers:
                if customer[key] == value:
                    return customer
            return f"Couldn't find a user with {key} of {value}"
        else:
            raise ValueError(f"Invalid key: {key}")
        
        return None

    def get_order_by_id(self, order_id):
        for order in self.orders:
            if order["id"] == order_id:
                return order
        return None
    
    def get_customer_orders(self, customer_id):
        return [order for order in self.orders if order["customer_id"] == customer_id]

    def cancel_order(self, order_id):
        order = self.get_order_by_id(order_id)
        if order:
            if order["status"] == "Processing":
                order["status"] = "Cancelled"
                return "Cancelled the order"
            else:
                return "Order has already shipped.  Can't cancel it."
        return "Can't find that order!"
```

我們建立一個 `FakeDatabase` 的實例：

```python
db = FakeDatabase()
```

讓我們確認 `get_user` 方法如預期運作。它預期我們傳入以下其中一個 `key`：

* "email"
* "username"
* "phone"

同時也需要對應的 `value`，用於執行基本搜尋，理想情況下回傳符合的使用者。

```python
db.get_user("email", "john@gmail.com")
```
```
{'id': '1213210',
 'name': 'John Doe',
 'email': 'john@gmail.com',
 'phone': '123-456-7890',
 'username': 'johndoe'}
```

```python
db.get_user("username", "adavis")
```
```
{'id': '4782901',
 'name': 'Aaliyah Davis',
 'email': 'aaliyahd@hotmail.com',
 'phone': '111-222-3333',
 'username': 'adavis'}
```

```python
db.get_user("phone", "666-777-8888")
```
```
{'id': '8259147',
 'name': 'Megan Anderson',
 'email': 'megana@gmail.com',
 'phone': '666-777-8888',
 'username': 'manderson'}
```

我們也可以透過呼叫 `get_customer_orders` 並傳入客戶 ID 來獲取屬於特定客戶的所有訂單清單：

```python
db.get_customer_orders("1213210")
```
```
[{'id': '24601',
  'customer_id': '1213210',
  'product': 'Wireless Headphones',
  'quantity': 1,
  'price': 79.99,
  'status': 'Shipped'},
 {'id': '13579',
  'customer_id': '1213210',
  'product': 'Smartphone Case',
  'quantity': 2,
  'price': 19.99,
  'status': 'Processing'},
 {'id': '90357',
  'customer_id': '1213210',
  'product': 'Smartphone Case',
  'quantity': 1,
  'price': 19.99,
  'status': 'Shipped'}]
```

```python
db.get_customer_orders("9603481")
```
```
[{'id': '61984',
  'customer_id': '9603481',
  'product': 'Noise-Cancelling Headphones',
  'quantity': 1,
  'price': 149.99,
  'status': 'Shipped'}]
```

如果我們有訂單 ID，也可以直接查詢單一訂單：

```python
db.get_order_by_id('24601')
```
```
{'id': '24601',
 'customer_id': '1213210',
 'product': 'Wireless Headphones',
 'quantity': 1,
 'price': 79.99,
 'status': 'Shipped'}
```

最後，我們可以使用 `cancel_order` 方法來取消訂單。訂單只有在「處理中（processing）」狀態時才能取消。已出貨的訂單無法取消！該方法需要我們傳入要取消的訂單 order_id。

```python
#讓我們查詢一個狀態為處理中的訂單：
db.get_order_by_id("47652")
```
```
{'id': '47652',
 'customer_id': '8259147',
 'product': 'Smartwatch',
 'quantity': 1,
 'price': 199.99,
 'status': 'Processing'}
```

```python
#現在讓我們取消它！
db.cancel_order("47652")
```
```
'Cancelled the order'
```

```python
# 狀態現在應該是 "Cancelled"（已取消）
db.get_order_by_id("47652")
```
```
{'id': '47652',
 'customer_id': '8259147',
 'product': 'Smartwatch',
 'quantity': 1,
 'price': 199.99,
 'status': 'Cancelled'}
```

***

## 撰寫我們的工具

現在我們已經測試了（非常）簡單的假資料庫功能，讓我們撰寫定義工具結構的 JSON schema。我們先看一個對應 `get_order_by_id` 方法的非常簡單的工具：

```python
tool1 = {
        "name": "get_order_by_id",
        "description": "Retrieves the details of a specific order based on the order ID. Returns the order ID, product name, quantity, price, and order status.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The unique identifier for the order."
                }
            },
            "required": ["order_id"]
        }
    }
```

如往常一樣，我們包含了名稱、描述以及輸入的概述。在這個案例中，只有一個輸入 `order_id`，而且是必填的。

現在讓我們看一個對應 `get_user` 方法的更複雜的工具。回想一下，這個方法有兩個引數：

1. 一個 `key` 引數，是以下字串之一：
    * "email"
    * "username"
    * "phone"
2. 一個 `value` 引數，是我們用來搜尋的詞彙（實際的電子郵件、電話號碼或使用者名稱）

以下是對應的工具定義：

```python
tool2 = {
        "name": "get_user",
        "description": "Looks up a user by email, phone, or username.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "enum": ["email", "phone", "username"],
                    "description": "The attribute to search for a user by (email, phone, or username)."
                },
                "value": {
                    "type": "string",
                    "description": "The value to match for the specified attribute."
                }
            },
            "required": ["key", "value"]
        }
    }
```

特別留意我們如何在 schema 中使用 `enum` 來定義 `key` 的一組有效選項。

我們還有兩個工具需要撰寫，但為了節省時間，我們直接提供完整的工具清單供你使用。（當然，你也可以先自己試著定義它們作為練習！）

```python
tools = [
    {
        "name": "get_user",
        "description": "Looks up a user by email, phone, or username.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "enum": ["email", "phone", "username"],
                    "description": "The attribute to search for a user by (email, phone, or username)."
                },
                "value": {
                    "type": "string",
                    "description": "The value to match for the specified attribute."
                }
            },
            "required": ["key", "value"]
        }
    },
    {
        "name": "get_order_by_id",
        "description": "Retrieves the details of a specific order based on the order ID. Returns the order ID, product name, quantity, price, and order status.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The unique identifier for the order."
                }
            },
            "required": ["order_id"]
        }
    },
    {
        "name": "get_customer_orders",
        "description": "Retrieves the list of orders belonging to a user based on a user's customer id.",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "The customer_id belonging to the user"
                }
            },
            "required": ["customer_id"]
        }
    },
    {
        "name": "cancel_order",
        "description": "Cancels an order based on a provided order_id.  Only orders that are 'processing' can be cancelled",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The order_id pertaining to a particular order"
                }
            },
            "required": ["order_id"]
        }
    }
]
```

***

## 將工具提供給 Claude

接下來，我們需要做幾件事：
1. 告訴 Claude 我們的工具，並將使用者的聊天訊息發送給 Claude。
2. 處理我們從 Claude 收到的回應：
    * 如果 Claude 不想使用工具：
        * 將 Claude 的輸出印給使用者看。
        * 請使用者輸入下一則訊息。
    * 如果 Claude 想使用工具：
        * 確認 Claude 呼叫了其中一個適當的工具。
        * 執行底層函式，例如 `get_user` 或 `cancel_order`。
        * 將工具的執行結果發送給 Claude。

最終目標是撰寫一個命令列腳本，建立一個在迴圈中執行的互動式聊天機器人。但為了簡單起見，我們先以線性方式撰寫基本程式碼。最後再建立一個互動式聊天機器人腳本。

我們從一個可以將 Claude 的工具使用回應轉換為實際 `db` 方法呼叫的函式開始：

```python
def process_tool_call(tool_name, tool_input):
    if tool_name == "get_user":
        return db.get_user(tool_input["key"], tool_input["value"])
    elif tool_name == "get_order_by_id":
        return db.get_order_by_id(tool_input["order_id"])
    elif tool_name == "get_customer_orders":
        return db.get_customer_orders(tool_input["customer_id"])
    elif tool_name == "cancel_order":
        return db.cancel_order(tool_input["order_id"])
```

讓我們從一個簡單的示範開始，展示 Claude 在面對多個工具清單時能夠決定使用哪個工具。我們問 Claude `Can you look up my orders? My email is john@gmail.com`（你能幫我查詢我的訂單嗎？我的電子郵件是 john@gmail.com），看看會發生什麼！

```python
import anthropic
import json

client = anthropic.Client()
MODEL_NAME = "claude-3-sonnet-20240229"

messages = [{"role": "user", "content": "Can you look up my orders? My email is john@gmail.com"}]

#發送請求給 Claude
response = client.messages.create(
    model=MODEL_NAME,
    max_tokens=4096,
    tools=tools,
    messages=messages
)
```

```python
print(response)
```
```
ToolsBetaMessage(id='msg_0112Ab7iKF2gWeAcAd2XWaBb', content=[TextBlock(text='Sure, let me look up your orders based on your email. To get the user details by email:', type='text'), ToolUseBlock(id='toolu_01CNTeufcesL1sUP2jnwT8TA', input={'key': 'email', 'value': 'john@gmail.com'}, name='get_user', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=574, output_tokens=96))
```

Claude 想要使用 `get_user` 工具。

現在我們將撰寫基本邏輯來更新 messages 清單、呼叫適當的工具，並再次使用工具結果更新 messages 清單。

```python
# 更新 messages 以包含 Claude 的回應
messages.append(
    {"role": "assistant", "content": response.content}
)

#如果 Claude 停止是因為想要使用工具：
if response.stop_reason == "tool_use":
    tool_use = response.content[-1] #簡單方式假設一次只呼叫 1 個工具
    tool_name = tool_use.name
    tool_input = tool_use.input
    print("Claude wants to use the {tool_name} tool")
    print(f"Tool Input:")
    print(json.dumps(tool_input, indent=2))

    #實際在 db 上執行底層工具功能
    tool_result = process_tool_call(tool_name, tool_input)

    print(f"\nTool Result:")
    print(json.dumps(tool_result, indent=2))

    #加入我們的 tool_result 訊息：
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": str(tool_result),
                }
            ],
        },
    )
else: 
    #如果 Claude 不想使用工具，只需印出文字回應
    print("\nTechNova Support:" + f"{response.content[0].text}" )
```
```
Claude wants to use the {tool_name} tool
Tool Input:
{
  "key": "email",
  "value": "john@gmail.com"
}

Tool Result:
{
  "id": "1213210",
  "name": "John Doe",
  "email": "john@gmail.com",
  "phone": "123-456-7890",
  "username": "johndoe"
}
```

以下是我們的 messages 清單現在的樣子：

```python
messages
```
```
[{'role': 'user',
  'content': 'Can you look up my orders? My email is john@gmail.com'},
 {'role': 'assistant',
  'content': [TextBlock(text='Sure, let me look up your orders based on your email. To get the user details by email:', type='text'),
   ToolUseBlock(id='toolu_01CNTeufcesL1sUP2jnwT8TA', input={'key': 'email', 'value': 'john@gmail.com'}, name='get_user', type='tool_use')]},
 {'role': 'user',
  'content': [{'type': 'tool_result',
    'tool_use_id': 'toolu_01CNTeufcesL1sUP2jnwT8TA',
    'content': "{'id': '1213210', 'name': 'John Doe', 'email': 'john@gmail.com', 'phone': '123-456-7890', 'username': 'johndoe'}"}]}]
```

現在我們使用更新後的 messages 清單向 Claude 發送第二個請求：

```python
response2 = client.messages.create(
    model=MODEL_NAME,
    max_tokens=4096,
    tools=tools,
    messages=messages
)
```

```python
response2
```
```
ToolsBetaMessage(id='msg_011Fru6wiViEExPXg7ANQkfH', content=[TextBlock(text='Now that I have your customer ID 1213210, I can retrieve your order history:', type='text'), ToolUseBlock(id='toolu_011eHUmUgCZXwr7swzL1LE6y', input={'customer_id': '1213210'}, name='get_customer_orders', type='tool_use')], model='claude-3-sonnet-20240229', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=733, output_tokens=80))
```

現在 Claude 取得了 `get_user` 工具的結果（包含使用者 ID），它想要呼叫 `get_customer_orders` 來查詢屬於這位特定客戶的訂單。它選擇了正確的工具來完成任務。**注意：** 這裡有許多潛在的問題和 Claude 可能出錯的地方，但這是一個好的開始！

***

## 撰寫互動式腳本

透過互動式命令列腳本與這個聊天機器人互動會方便許多。

以下是將上述所有程式碼組合成一個函式的完整版本，它啟動一個基於迴圈的聊天對話（你可能需要在命令列中作為獨立腳本來執行它）：

```python
import anthropic
import json

client = anthropic.Client()
MODEL_NAME = "claude-3-sonnet-20240229"
# MODEL_NAME = "claude-3-opus-20240229"

class FakeDatabase:
    def __init__(self):
        self.customers = [
            {"id": "1213210", "name": "John Doe", "email": "john@gmail.com", "phone": "123-456-7890", "username": "johndoe"},
            {"id": "2837622", "name": "Priya Patel", "email": "priya@candy.com", "phone": "987-654-3210", "username": "priya123"},
            {"id": "3924156", "name": "Liam Nguyen", "email": "lnguyen@yahoo.com", "phone": "555-123-4567", "username": "liamn"},
            {"id": "4782901", "name": "Aaliyah Davis", "email": "aaliyahd@hotmail.com", "phone": "111-222-3333", "username": "adavis"},
            {"id": "5190753", "name": "Hiroshi Nakamura", "email": "hiroshi@gmail.com", "phone": "444-555-6666", "username": "hiroshin"},
            {"id": "6824095", "name": "Fatima Ahmed", "email": "fatimaa@outlook.com", "phone": "777-888-9999", "username": "fatimaahmed"},
            {"id": "7135680", "name": "Alejandro Rodriguez", "email": "arodriguez@protonmail.com", "phone": "222-333-4444", "username": "alexr"},
            {"id": "8259147", "name": "Megan Anderson", "email": "megana@gmail.com", "phone": "666-777-8888", "username": "manderson"},
            {"id": "9603481", "name": "Kwame Osei", "email": "kwameo@yahoo.com", "phone": "999-000-1111", "username": "kwameo"},
            {"id": "1057426", "name": "Mei Lin", "email": "meilin@gmail.com", "phone": "333-444-5555", "username": "mlin"}
        ]

        self.orders = [
            {"id": "24601", "customer_id": "1213210", "product": "Wireless Headphones", "quantity": 1, "price": 79.99, "status": "Shipped"},
            {"id": "13579", "customer_id": "1213210", "product": "Smartphone Case", "quantity": 2, "price": 19.99, "status": "Processing"},
            {"id": "97531", "customer_id": "2837622", "product": "Bluetooth Speaker", "quantity": 1, "price": "49.99", "status": "Shipped"}, 
            {"id": "86420", "customer_id": "3924156", "product": "Fitness Tracker", "quantity": 1, "price": 129.99, "status": "Delivered"},
            {"id": "54321", "customer_id": "4782901", "product": "Laptop Sleeve", "quantity": 3, "price": 24.99, "status": "Shipped"},
            {"id": "19283", "customer_id": "5190753", "product": "Wireless Mouse", "quantity": 1, "price": 34.99, "status": "Processing"},
            {"id": "74651", "customer_id": "6824095", "product": "Gaming Keyboard", "quantity": 1, "price": 89.99, "status": "Delivered"},
            {"id": "30298", "customer_id": "7135680", "product": "Portable Charger", "quantity": 2, "price": 29.99, "status": "Shipped"},
            {"id": "47652", "customer_id": "8259147", "product": "Smartwatch", "quantity": 1, "price": 199.99, "status": "Processing"},
            {"id": "61984", "customer_id": "9603481", "product": "Noise-Cancelling Headphones", "quantity": 1, "price": 149.99, "status": "Shipped"},
            {"id": "58243", "customer_id": "1057426", "product": "Wireless Earbuds", "quantity": 2, "price": 99.99, "status": "Delivered"},
            {"id": "90357", "customer_id": "1213210", "product": "Smartphone Case", "quantity": 1, "price": 19.99, "status": "Shipped"},
            {"id": "28164", "customer_id": "2837622", "product": "Wireless Headphones", "quantity": 2, "price": 79.99, "status": "Processing"}
        ]

    def get_user(self, key, value):
        if key in {"email", "phone", "username"}:
            for customer in self.customers:
                if customer[key] == value:
                    return customer
            return f"Couldn't find a user with {key} of {value}"
        else:
            raise ValueError(f"Invalid key: {key}")
        
        return None

    def get_order_by_id(self, order_id):
        for order in self.orders:
            if order["id"] == order_id:
                return order
        return None
    
    def get_customer_orders(self, customer_id):
        return [order for order in self.orders if order["customer_id"] == customer_id]

    def cancel_order(self, order_id):
        order = self.get_order_by_id(order_id)
        if order:
            if order["status"] == "Processing":
                order["status"] = "Cancelled"
                return "Cancelled the order"
            else:
                return "Order has already shipped.  Can't cancel it."
        return "Can't find that order!"

tools = [
    {
        "name": "get_user",
        "description": "Looks up a user by email, phone, or username.",
        "input_schema": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "enum": ["email", "phone", "username"],
                    "description": "The attribute to search for a user by (email, phone, or username)."
                },
                "value": {
                    "type": "string",
                    "description": "The value to match for the specified attribute."
                }
            },
            "required": ["key", "value"]
        }
    },
    {
        "name": "get_order_by_id",
        "description": "Retrieves the details of a specific order based on the order ID. Returns the order ID, product name, quantity, price, and order status.",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The unique identifier for the order."
                }
            },
            "required": ["order_id"]
        }
    },
    {
        "name": "get_customer_orders",
        "description": "Retrieves the list of orders belonging to a user based on a user's customer id.",
        "input_schema": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "The customer_id belonging to the user"
                }
            },
            "required": ["customer_id"]
        }
    },
    {
        "name": "cancel_order",
        "description": "Cancels an order based on a provided order_id.  Only orders that are 'processing' can be cancelled",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "string",
                    "description": "The order_id pertaining to a particular order"
                }
            },
            "required": ["order_id"]
        }
    }
]

db = FakeDatabase()

def process_tool_call(tool_name, tool_input):
    if tool_name == "get_user":
        return db.get_user(tool_input["key"], tool_input["value"])
    elif tool_name == "get_order_by_id":
        return db.get_order_by_id(tool_input["order_id"])
    elif tool_name == "get_customer_orders":
        return db.get_customer_orders(tool_input["customer_id"])
    elif tool_name == "cancel_order":
        return db.cancel_order(tool_input["order_id"])
    
def simple_chat():
    user_message = input("\nUser: ")
    messages = [{"role": "user", "content": user_message}]
    while True:
        #如果最後一則訊息來自助理，請求使用者輸入下一則訊息
        if messages[-1].get("role") == "assistant":
            user_message = input("\nUser: ")
            messages.append({"role": "user", "content": user_message})

        #發送請求給 Claude
        response = client.messages.create(
            model=MODEL_NAME,
            max_tokens=4096,
            tools=tools,
            messages=messages
        )
        # 更新 messages 以包含 Claude 的回應
        messages.append(
            {"role": "assistant", "content": response.content}
        )

        #如果 Claude 停止是因為想要使用工具：
        if response.stop_reason == "tool_use":
            tool_use = response.content[-1] #簡單方式假設一次只呼叫 1 個工具
            tool_name = tool_use.name
            tool_input = tool_use.input
            print(f"======Claude wants to use the {tool_name} tool======")

            #實際在 db 上執行底層工具功能
            tool_result = process_tool_call(tool_name, tool_input)

            #加入我們的 tool_result 訊息：
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": str(tool_result),
                        }
                    ],
                },
            )
        else: 
            #如果 Claude 不想使用工具，只需印出文字回應
            print("\nTechNova Support: " + f"{response.content[0].text}" )

# 開始聊天！！
# simple_chat()
```

以下是一個範例對話：

![conversation3.png](images/conversation3.png)

如你所見，聊天機器人在需要時呼叫了正確的工具，但實際的聊天回應並不理想。我們大概不希望面向客戶的聊天機器人告訴使用者它要呼叫哪些具體的工具！

***

## 提示詞改進

我們可以透過提供聊天機器人一個完善的系統提示詞來改善聊天體驗。我們首先應該做的是給 Claude 一些背景，告訴它正在作為 TechNova 的客服助理。

以下是我們系統提示詞的起點：

```python
system_prompt = """
You are a customer support chat bot for an online retailer called TechNova. 
Your job is to help users look up their account, orders, and cancel orders.
Be helpful and brief in your responses.
"""
```

記得在向 Claude 發送請求時，將這個提示詞傳入 `system` 參數！

以下是加入上述系統提示詞後的範例對話：

![conversation4.png](images/conversation4.png)


請注意，助理現在知道自己是 TechNova 的支援機器人，而且不再向使用者提及它的工具。明確告訴 Claude 完全不要提及工具也可能是個好主意。

**注意：** `=======Claude wants to use the cancel_order_tool=======` 這些行是我們加入腳本的日誌記錄，而不是 Claude 的實際輸出！

如果你玩這個腳本玩得夠久，可能會注意到其他問題。以下截圖說明了一個非常明顯且非常有問題的問題：

![conversation5.png](images/conversation5.png)



上方截圖顯示了完整的對話過程。使用者請求幫助取消訂單，並表示不知道訂單 ID。Claude 應該進一步詢問客戶的電子郵件、電話號碼或使用者名稱來查詢客戶，然後找到對應的訂單。但 Claude 決定在沒有任何關於使用者資訊的情況下呼叫 `get_user` 工具。Claude 自行捏造了一個電子郵件地址並試圖使用它，當然沒有找到符合的客戶。

為了防止這種情況，我們將更新系統提示詞，加入以下類似內容：

```python
system_prompt = """
You are a customer support chat bot for an online retailer called TechNova. 
Your job is to help users look up their account, orders, and cancel orders.
Be helpful and brief in your responses.
You have access to a set of tools, but only use them when needed.  
If you do not have enough information to use a tool correctly, ask a user follow up questions to get the required inputs.
Do not call any of the tools unless you have the required data from a user. 
"""
```

以下是使用更新後系統提示詞的助理對話截圖：

![conversation6.png](images/conversation6.png)

好多了！

***

## Opus 特有的問題

使用 Opus 搭配工具時，模型通常在實際回應使用者之前，會在 `<thinking>` 或 `<reflection>` 標籤中輸出它的思考過程。你可以在以下截圖中看到一個例子：

![conversation7.png](images/conversation7.png)

這個思考過程往往能帶來更好的結果，但它顯然會造成非常糟糕的使用者體驗。我們不想將這個思考邏輯暴露給使用者！最簡單的解決方法是明確要求模型將面向使用者的回應輸出在特定的 XML 標籤中。我們先更新系統提示詞：

```python
system_prompt = """
You are a customer support chat bot for an online retailer called TechNova. 
Your job is to help users look up their account, orders, and cancel orders.
Be helpful and brief in your responses.
You have access to a set of tools, but only use them when needed.  
If you do not have enough information to use a tool correctly, ask a user follow up questions to get the required inputs.
Do not call any of the tools unless you have the required data from a user. 

In each conversational turn, you will begin by thinking about your response. 
Once you're done, you will write a user-facing response. 
It's important to place all user-facing conversational responses in <reply></reply> XML tags to make them easy to parse.
"""
```

看看對話輸出的範例：

![conversation8.png](images/conversation8.png)


Claude 現在用 `<reply>` 標籤包裹實際面向使用者的回應。我們現在只需要提取這些標籤之間的內容，並確保這是我們真正印給使用者看的唯一部分。以下是執行這個操作的更新版 `start_chat` 函式！

```python
import re

def extract_reply(text):
    pattern = r'<reply>(.*?)</reply>'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return None    
    
def simple_chat():
    system_prompt = """
    You are a customer support chat bot for an online retailer called TechNova. 
    Your job is to help users look up their account, orders, and cancel orders.
    Be helpful and brief in your responses.
    You have access to a set of tools, but only use them when needed.  
    If you do not have enough information to use a tool correctly, ask a user follow up questions to get the required inputs.
    Do not call any of the tools unless you have the required data from a user. 

    In each conversational turn, you will begin by thinking about your response. 
    Once you're done, you will write a user-facing response. 
    It's important to place all user-facing conversational responses in <reply></reply> XML tags to make them easy to parse.
    """
    user_message = input("\nUser: ")
    messages = [{"role": "user", "content": user_message}]
    while True:
        #如果最後一則訊息來自助理，請求使用者輸入下一則訊息
        if messages[-1].get("role") == "assistant":
            user_message = input("\nUser: ")
            messages.append({"role": "user", "content": user_message})

        #發送請求給 Claude
        response = client.messages.create(
            model=MODEL_NAME,
            system=system_prompt,
            max_tokens=4096,
            tools=tools,
            messages=messages
        )
        # 更新 messages 以包含 Claude 的回應
        messages.append(
            {"role": "assistant", "content": response.content}
        )

        #如果 Claude 停止是因為想要使用工具：
        if response.stop_reason == "tool_use":
            tool_use = response.content[-1] #簡單方式假設一次只呼叫 1 個工具
            tool_name = tool_use.name
            tool_input = tool_use.input
            print(f"======Claude wants to use the {tool_name} tool======")


            #實際在 db 上執行底層工具功能
            tool_result = process_tool_call(tool_name, tool_input)

            #加入我們的 tool_result 訊息：
            messages.append(
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": str(tool_result),
                        }
                    ],
                },
            )
        else: 
            #如果 Claude 不想使用工具，只需印出文字回應
            model_reply = extract_reply(response.content[0].text)
            print("\nTechNova Support: " + f"{model_reply}" )

# 開始聊天！！
# simple_chat()
```

以下截圖展示了上述變更的效果：

![conversation9.png](images/conversation9.png)

***

## 最終版本

以下是與這個腳本的一個較長對話截圖，該版本對輸出進行了彩色標記。

![conversation10.png](images/conversation10.png)

***

## 結語

這是一個為說明工具使用工作流程而製作的教育示範。這個腳本和提示詞**尚未準備好用於生產環境**。助理回應了「你可以在訂單確認電子郵件中找到訂單 ID」這類內容，但它其實並不知道這是否屬實。在現實世界中，我們需要為 Claude 提供大量關於我們公司的背景知識（至少要這樣）。我們也需要嚴格測試聊天機器人，確保它在所有情況下都能正常運作。另外，讓任何人都能輕易取消訂單可能是個壞主意！如果你擁有某人的電子郵件、使用者名稱或電話號碼，就很容易取消許多人的訂單。在現實世界中，我們可能需要某種形式的身份驗證。簡而言之：這只是一個示範，並非完整的聊天機器人實作！

***

## 練習

* 為我們的助理（以及底層的 `FakeDatabase` 類別）新增功能，讓使用者能夠更新他們的電子郵件和電話號碼。
* 定義一個名為 `get_user_info` 的新工具，結合了 `get_user` 和 `get_customer_orders` 的功能。這個工具應該接受使用者的電子郵件、電話或使用者名稱作為輸入，並一次返回使用者的資訊和他們的訂單歷史。
* 加入錯誤處理和輸入驗證！


#### 進階挑戰
* 更新聊天機器人，使用實際的資料庫來取代我們的 `FakeDatabase` 類別。
