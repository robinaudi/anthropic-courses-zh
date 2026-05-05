# 使用圖片提示（Prompting with images）

## 視覺理解能力

Claude 3 系列模型具備視覺理解能力，能夠理解和分析圖片。我們現在可以同時提供文字和圖片輸入，豐富對話內容並實現強大的新應用場景。Opus、Sonnet 和 Haiku 都能理解並處理圖片。由於 Claude 3.5 Sonnet 擁有最強的視覺能力，本課程將全程使用它。

要向 Claude 提供圖片，我們只需使用與純文字對話相同的 `messages` 格式。典型的純文字使用者訊息如下所示：

```py
messages = [
    {
        "role": "user",
        "content": "tell me a joke"
    }
]
```

```python
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic()

messages = [
    {"role": "user", "content": "tell me a joke"}
]

response = client.messages.create(
    messages=messages,
    model="claude-3-haiku-20240307",
    max_tokens=200
)
print(response.content[0].text)
```

```
Here's a silly joke for you:

Why don't scientists trust atoms? Because they make up everything!

How was that? I tried to keep it lighthearted and family-friendly. Let me know if you'd like to hear another joke.
```

我們尚未見過的是，也可以將訊息中的 `content` 設定為**一個內容區塊（content block）的列表**。也就是說，不再是：

```py
messages = [
    {"role": "user", "content": "tell me a joke"}
]
```
而是可以將結構改為以下形式：

```py
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "tell me a joke"},
        ]
    }
]
```
以下兩種訊息格式是等效的：

```py
{"role": "user", "content": "Tell me a story"}
```

```py
{"role": "user", "content": [{"type": "text", "text": "Tell me a story"}]}
```

讓我們試試看：

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "tell me a joke"},
        ]
    }
]

response = client.messages.create(
    messages=messages,
    model="claude-3-haiku-20240307",
    max_tokens=200
)
print(response.content[0].text)
```

```
Here's a silly joke for you:

Why can't a bicycle stand up on its own? It's two-tired!

(I hope you groan at that one - that's the sign of a good joke!)
```

如你所見，它正常運作！我們可以在列表中加入任意數量的內容區塊，如以下範例所示：

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "who"},
            {"type": "text", "text": "made"},
            {"type": "text", "text": "you?"},
        ]
    }
]

response = client.messages.create(
    messages=messages,
    model="claude-3-haiku-20240307",
    max_tokens=200
)
print(response.content[0].text)
```

```
I was created by Anthropic, an artificial intelligence research company.
```

為什麼要這樣做？對於純文字提示，我們可能不會這樣做，但在處理多模態提示時就需要使用這種格式！


向 Claude 提供圖片時，必須撰寫一個圖片內容區塊（image content block）。以下是一個範例：


```py
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/jpeg",
                    "data": "/9j/4AAQSkZJRg..."
                }
            }
        ]
    }
]
```

以下圖示說明向 Claude 提供圖片時所需的重要資訊：

![image_message_format.png](images/image_message_format.png)

訊息中的 `content` 設定為一個包含以下屬性的字典：

* `type` — 圖片編碼格式，目前必須為 base64
* `media_type` — 圖片媒體類型，目前支援 image/jpeg、image/png、image/gif 和 image/webp
* `data` — 實際的圖片資料

## 僅使用圖片提示

大多數情況下，我們會希望在提示中同時提供文字和圖片，但也可以只提供圖片。讓我們試試看！本課程在 `prompting_images` 資料夾中提供了一些圖片。我們先用 Python 查看其中一張圖片：


```python
from IPython.display import Image
Image(filename='./prompting_images/uh_oh.png') 
```

Wikimedia Commons, CC-BY-SA

現在讓我們將這張圖片提供給 Claude。第一步是取得傳送給模型的 base64 編碼圖片資料字串。程式碼可能看起來有點複雜，但其實可以分解為以下幾個步驟：

1. 以「讀取二進位」模式開啟檔案。
2. 將檔案的完整二進位內容讀取為 bytes 物件。
3. 使用 base64 編碼對二進位資料進行編碼。
4. 將 base64 二進位資料轉換為字串。

```python
import base64

# opens the image file in "read binary" mode
with open("./prompting_images/uh_oh.png", "rb") as image_file:

    #reads the contents of the image as a bytes object
    binary_data = image_file.read() 

    #encodes the binary data using Base64 encoding
    base_64_encoded_data = base64.b64encode(binary_data) 

    #decodes base_64_encoded_data from bytes to a string
    base64_string = base_64_encoded_data.decode('utf-8')

```

我們可以查看得到的 `base64_string` 變數，但對人類來說並不太直觀。讓我們讀取前 100 個字元：

```python
base64_string[:100]
```

```
'iVBORw0KGgoAAAANSUhEUgAAB4AAAAQ4CAYAAADo08FDAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAE8mlUWHRYTUw6Y29tLmFkb2Jl'
```

現在我們已經將圖片資料轉為字串，下一步是正確格式化要傳給 Claude 的 messages 列表：

```python
messages = [
    {
        "role": "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_string
            },
        }]
    }
]
```

最後一步是將 messages 列表發送給 Claude，看看我們得到什麼回應！

```python
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
This image shows a man at the beach who appears to be in significant discomfort. His skin is bright red, indicating a severe sunburn. His facial expression displays pain and distress, with his eyes squinted shut and mouth contorted. The background shows a sandy beach with other beachgoers visible in the distance, as well as the ocean. This scene strongly suggests the painful consequences of not using proper sun protection during extended sun exposure. It serves as a vivid reminder of the importance of applying sunscreen and limiting time in direct sunlight to avoid painful sunburns and potential long-term skin damage.
```

由於我們沒有提供任何其他明確指示，Claude 開始描述這張圖片。

## 圖片加文字的提示

現在讓我們嘗試傳送一個同時包含圖片和文字的提示。我們只需在使用者訊息中加入第二個區塊，這個區塊將是一個簡單的文字區塊。

```python
messages = [
    {
        "role": "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": base64_string
            },
        },
        {
            "type": "text",
            "text": "What could this person have done to prevent this?"
        }]
    }
]
```

以下圖示標注了圖片區塊和文字區塊：

![image_and_text_prompt.png](images/image_and_text_prompt.png)

讓我們向 Claude 發送請求，看看會發生什麼：

```python
response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
The person in the image appears to have a severe sunburn, likely from spending too much time in the sun without proper protection. To prevent this uncomfortable situation, they could have taken several precautions:

1. Applied a high SPF sunscreen regularly and generously
2. Worn protective clothing like a hat and UV-blocking shirt
3. Sought shade during peak sun hours (usually 10 AM to 4 PM)
4. Used a beach umbrella or sun tent for additional protection
5. Stayed hydrated and limited sun exposure time
6. Reapplied sunscreen after swimming or excessive sweating

Sunburns like this can be painful and increase the risk of skin damage and skin cancer. It's always important to practice sun safety, especially when spending extended time at the beach or in other sunny environments.
```

## 多張圖片

我們可以在使用者訊息的 `content` 中加入多個圖片區塊，從而向 Claude 提供多張圖片。以下是一個包含多張圖片的範例：


```py
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": image1_media_type,
                    "data": image1_data,
                },
            },
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": image2_media_type,
                    "data": image2_data,
                },
            },
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": image3_media_type,
                    "data": image3_data,
                },
            },
            {"type": "text", "text": "How are these images different?"},
        ],
    }
]

```

### 建立圖片輔助函式

在動態腳本中使用圖片時，每次手動建立圖片內容區塊可能會很麻煩。讓我們撰寫一個小輔助函式，自動生成格式正確的圖片區塊。

```python
import base64
import mimetypes

def create_image_message(image_path):
    # Open the image file in "read binary" mode
    with open(image_path, "rb") as image_file:
        # Read the contents of the image as a bytes object
        binary_data = image_file.read()
    
    # Encode the binary data using Base64 encoding
    base64_encoded_data = base64.b64encode(binary_data)
    
    # Decode base64_encoded_data from bytes to a string
    base64_string = base64_encoded_data.decode('utf-8')
    
    # Get the MIME type of the image based on its file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    
    # Create the image block
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": mime_type,
            "data": base64_string
        }
    }
    
    
    return image_block
```

上述函式接受一個圖片路徑，回傳一個可直接放入 Claude 訊息中的字典，並自動判斷圖片的 MIME 類型。

讓我們用一張新圖片來試試：

```python
Image("./prompting_images/animal1.png")
```

使用新的圖片區塊輔助函式，向 Claude 發送請求：

```python
messages = [
    {
        "role": "user",
        "content": [
            create_image_message("./prompting_images/animal1.png")
        ]
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
This image shows a majestic bald eagle perched on what appears to be a concrete or stone structure near water. The eagle is in sharp focus, displaying its distinctive white head and yellow beak contrasting with its dark body feathers. Its piercing eye is visible, giving the bird a keen, alert appearance.

The eagle is positioned facing slightly to the right, with its body in profile. Its powerful talons are gripping the edge of the perch. The background is blurred but suggests a body of water, possibly a lake or ocean, with a overcast sky above.

This photograph captures the strength and beauty of the bald eagle, which is an iconic symbol of American wildlife. The composition emphasizes the bird's regal posture and striking features, making it a powerful nature portrait. The muted, cool tones of the background enhance the drama of the eagle's appearance, drawing the viewer's attention to the bird itself.
```

讓我們嘗試一個在提示中結合文字和圖片的範例：

```python
messages = [
    {
        "role": "user",
        "content": [
            create_image_message("./prompting_images/animal1.png"),
            {"type": "text", "text": "Where might I find this animal in the world?"}
        ]
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
The animal in this image is a bald eagle, which is primarily found in North America. Bald eagles are most commonly seen in Alaska and Canada, but they can also be found throughout much of the continental United States, particularly near large bodies of water like rivers, lakes, and coastal areas.

Some specific regions where you're likely to spot bald eagles include:

1. Alaska - home to the largest population of bald eagles in the U.S.
2. Pacific Northwest (Washington, Oregon)
3. Great Lakes region
4. Florida and other southeastern coastal states
5. Chesapeake Bay area
6. Rocky Mountain states

Bald eagles prefer habitats near water sources as they primarily feed on fish. They're often seen perched on tall trees or structures near these water bodies, much like the eagle in this image which is perched on what appears to be a post or structure near water.

It's worth noting that bald eagle populations have significantly recovered in recent decades due to conservation efforts, so they can now be spotted in many more areas across North America than in the past.
```

現在讓我們試著向 Claude 提供多張圖片。我們有 3 張不同的動物圖片：

```python
from IPython.display import display
display(Image("./prompting_images/animal1.png", width=300))
```

```python
display(Image("./prompting_images/animal2.png", width=300))
```

```python
display(Image("./prompting_images/animal3.png", width=300))
```

讓我們試著在一條訊息中同時傳送 3 張圖片給 Claude，並附上文字提示「What are these animals?」

```python
messages = [
    {
        "role": "user",
        "content": [
            create_image_message('./prompting_images/animal1.png'),
            create_image_message('./prompting_images/animal2.png'),
            create_image_message('./prompting_images/animal3.png'),
            {"type": "text", "text": "what are these animals?"}
        ]
    }
]

response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
These images show three different animals:

1. The first image depicts a bald eagle. It has the distinctive white head and yellow beak characteristic of this species, with a dark body perched on what appears to be a post or structure near water.

2. The second image shows a bear, likely a grizzly or brown bear, swimming in water. Only its head and part of its back are visible above the water's surface, with reeds or grass visible in the background.

3. The third image is a close-up of a porcupine. You can see its round face with small eyes and nose, surrounded by a mass of long, sharp quills that cover its body. The quills are a light brown or tan color.

Each of these animals is native to North America and represents different habitats and ecological roles within their environments.
```

效果很好！但需要注意的是，如果我們用稍微弱一些的模型（例如 Claude 3 Haiku）嘗試同樣的操作，結果可能較差：

```python
messages = [
    {
        "role": "user",
        "content": [
            create_image_message('./prompting_images/animal1.png'),
            create_image_message('./prompting_images/animal2.png'),
            create_image_message('./prompting_images/animal3.png'),
            {"type": "text", "text": "what are these animals?"}
        ]
    }
]

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
The image shows a porcupine. The animal has distinctive long, coarse fur that appears spiky and bristly. Porcupines are known for their quills or sharp spines that cover their body, which serves as a defense mechanism. This close-up shot captures the intricate details and texture of the porcupine's fur and facial features.
```

這個回應令人不太滿意。回顧一下，我們傳送了一張禿鷹的圖片、一張在水中游泳的灰熊圖片，以及一張豪豬特寫圖片，並附上了「What are these animals?」的文字提示。而這是 Claude 的回應：

>The image shows a porcupine. The animal has distinctive long, coarse fur that appears spiky and bristly. Porcupines are known for their quills or sharp spines that cover their body, which serves as a defense mechanism. This close-up shot captures the intricate details and texture of the porcupine's fur and facial features.

那麼我們的禿鷹和灰熊圖片呢？這個問題在 Claude 3.5 Sonnet 上不會出現，但在使用其他模型時，為每張圖片加上文字標籤會很有幫助。即使只是簡單地標記為「Image 1」、「Image 2」等，也能帶來很大的差異。

讓我們試試：

```python
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Image 1:"},
            create_image_message('./prompting_images/animal1.png'),
            {"type": "text", "text": "Image 2:"},
            create_image_message('./prompting_images/animal2.png'),
            {"type": "text", "text": "Image 3:"},
            create_image_message('./prompting_images/animal3.png'),
            {"type": "text", "text": "what are these animals?"}
        ]
    }
]

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
The animals shown in the images are:

Image 1: A bald eagle. The distinctive white head and tail, large beak, and dark body feathers are characteristic of this iconic North American raptor.

Image 2: A brown bear. This large, powerful bear is shown partially submerged in what appears to be a lake or river, with its thick, dark fur visible.

Image 3: A porcupine. The image shows a close-up view of the porcupine's face, with its distinctive sharp quills covering its body.
```

**好多了！**

## 使用非本地圖片（來自 URL 的圖片）

有時你可能需要向 Claude 提供本地沒有的圖片。方法有很多種，但都遵循相同的流程：

* 使用某種請求函式庫取得圖片資料
* 使用 Base64 編碼對圖片內容的二進位資料進行編碼
* 使用 UTF-8 編碼將編碼後的資料從 bytes 解碼為字串

我們將使用 `httpx` 從 URL 請求圖片資料。以下範例中的 URL 是一張教堂上方有極光的圖片。

```python
import base64
import httpx

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Church_of_light.jpg/1599px-Church_of_light.jpg"
image_media_type = "image/jpeg"
image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")

messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": image_media_type,
                        "data": image_data,
                    },
                },
                {
                    "type": "text",
                    "text": "Describe this image."
                }
            ],
        }
    ]


response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)



```

```
This image captures a breathtaking scene of the Northern Lights (Aurora Borealis) dancing over a small church in what appears to be a remote, snowy landscape. The church is a simple white structure with a distinctive red-roofed steeple, standing out starkly against the dramatic backdrop.

The sky is alive with vibrant green auroras, swirling and streaking across the star-filled night sky. The ethereal light show creates a stunning contrast with the snow-covered mountains and terrain surrounding the church.

The foreground shows a mix of snow and dark ground, suggesting it might be early winter or late autumn. The rugged mountains in the background add to the sense of isolation and natural beauty of the location.

This scene is a perfect example of the awe-inspiring conjunction of natural phenomena and human architecture. The small church seems to stand as a solitary beacon of civilization amidst the wild, majestic display of the aurora and the harsh, beautiful landscape. It's the kind of image that captures the imagination and evokes a sense of wonder at the beauty of our world.
```

就像之前一樣，我們也可以定義一個輔助函式，從 URL 生成圖片區塊。以下是一個非常精簡的實作，接受一個 URL 並執行以下步驟：

* 使用 `httpx` 請求圖片資料
* 透過簡單的字串處理確定 MIME 類型，取最後一個「.」之後的內容（這不是萬無一失的方案）
* 使用 base64 編碼圖片資料，並將 bytes 解碼為 utf-8 字串
* 回傳格式正確的圖片區塊，可直接放入 Claude 提示中！

如果我們呼叫 `get_image_dict_from_url("https://somewebsite.com/cat.png")`，它會回傳以下字典：

```py
{
    "type": "image",
    "source": {
        "type": "base64",
        "media_type": "image/png",
        "data": <actual image data>
    },
}
```

```python

def get_image_dict_from_url(image_url):
    # Send a GET request to the image URL and retrieve the content
    response = httpx.get(image_url)
    image_content = response.content

    # Determine the media type of the image based on the URL extension
    # This is not a foolproof approach, but it generally works
    image_extension = image_url.split(".")[-1].lower()
    if image_extension == "jpg" or image_extension == "jpeg":
        image_media_type = "image/jpeg"
    elif image_extension == "png":
        image_media_type = "image/png"
    elif image_extension == "gif":
        image_media_type = "image/gif"
    else:
        raise ValueError("Unsupported image format")

    # Encode the image content using base64
    image_data = base64.b64encode(image_content).decode("utf-8")

    # Create the dictionary in the proper image block shape:
    image_dict = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": image_media_type,
            "data": image_data,
        },
    }

    return image_dict
```

現在讓我們試試！以下範例使用兩個圖片 URL：

* 一張消防車的 PNG 圖片
* 一張緊急救援直升機的 JPG 圖片

以下是這兩張圖片：

![firetruck](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Rincon_fire_truck.png/1600px-Rincon_fire_truck.png)
Wikimedia Commons, CC-BY-SA
![helicopter](https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Ornge_C-GYNP.jpg/1600px-Ornge_C-GYNP.jpg)
Wikimedia Commons, CC-BY-SA

我們將兩張圖片都傳給 Claude，並附上文字提示詢問「What do these images have in common?」

```python
url1 = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Rincon_fire_truck.png/1600px-Rincon_fire_truck.png"
url2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Ornge_C-GYNP.jpg/1600px-Ornge_C-GYNP.jpg"

messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Image 1:"},
                get_image_dict_from_url(url1),
                {"type": "text", "text": "Image 2:"},
                get_image_dict_from_url(url2),
                {"type": "text", "text": "What do these images have in common?"}
            ],
        }
    ]


response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
These images both depict emergency response vehicles, specifically:

1. The first image shows a Rincon Fire Department fire engine (Engine 181). It's a large red fire truck parked in front of a building, with mountains visible in the background.

2. The second image displays an orange air ambulance helicopter in flight. It's marked with "ornge" branding and appears to be a medical evacuation or emergency response helicopter.

The common theme between these images is that they both showcase specialized vehicles used for emergency response and rescue operations. Fire trucks and air ambulances play crucial roles in responding to emergencies, providing rapid transportation, and delivering life-saving services. Both vehicles are painted in bright, attention-grabbing colors (red for the fire truck, orange for the helicopter) which is typical for emergency vehicles to enhance visibility and recognition.
```

Claude 成功識別出兩張圖片都是緊急救援車輛！更重要的是，我們現在學會了如何向 Claude 提供從 URL 下載的圖片。

## 視覺提示技巧

### 提示要具體
就像純文字提示一樣，撰寫具體且詳盡的多模態提示可以從 Claude 獲得更好的結果。讓我們看一個範例。

以下是一張朋友合照，圖中共有 8 個人，但有 2 個人被圖片邊界截斷了。

```python
from IPython.display import Image
Image(filename='./prompting_images/people.png') 
```

如果我們只是問 Claude「how many people are in this image?」，得到的回答可能是 7 個人：

```python

messages=[
    {
        "role": "user",
        "content": [
            create_image_message("./prompting_images/people.png"),
            {"type": "text", "text": "How many people are in this image?"}
        ],
    }
]


response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
The image shows 7 people standing together with their arms around each other's shoulders, facing away from the camera and looking out at a scenic view. They appear to be friends or a group enjoying the scenery together. In the background, you can see a body of water, mountains, and a cable car system with gondolas suspended on cables.
```

如果我們改用一些基本的提示工程技巧，例如告訴 Claude 要逐步思考、它是數人的專家，並請它注意圖片中可能被截斷的「不完整」人物，就能獲得更好的結果：

```python
messages=[
    {
        "role": "user",
        "content": [
            create_image_message("./prompting_images/people.png"),
            {"type": "text", "text": "You have perfect vision and pay great attention to detail which makes you an expert at counting objects in images. How many people are in this picture? Some of the people may be partially obscured or cut off in the image or may only have an arm visible. Please count people even if you can only see a single body part. Before providing the answer in <answer> tags, think step by step in <thinking> tags and analyze every part of the image."}
        ],
    }
]


response = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=2048,
    messages=messages
)
print(response.content[0].text)
```

```
<thinking>
Let's analyze the image carefully from left to right:

1. On the far left, there's an arm visible, suggesting one person.
2. Next, we see a person in a blue and white gradient shirt.
3. Then a person in a white striped shirt.
4. A person wearing a light blue shirt with a headband.
5. Someone wearing a straw hat and denim overalls.
6. A person in a yellow t-shirt.
7. On the far right, we see someone in a grey shirt holding a camera.

That's 7 people clearly visible in the main group.

Looking at the edges:
- On the far left, we can see part of another person's arm, suggesting an 8th person.
- On the far right, there doesn't appear to be any additional person visible.

After careful analysis, I count 8 people in total, including the partially visible person on the left.
</thinking>

<answer>8</answer>
```

### 使用範例

在提示中加入範例，可以改善 Claude 在文字和圖片輸入提示中的回應品質。

為了示範這一點，我們將使用一系列來自投影片簡報的圖片。我們的目標是讓 Claude 生成對投影片內容的 JSON 描述。請看第一張圖片：

```python
from IPython.display import display
display(Image("./prompting_images/slide1.png", width=800))
```

我們的目標是讓 Claude 生成一個 JSON 格式的回應，包含投影片的背景顏色、標題、正文文字和圖片描述。上述圖片對應的 JSON 可能如下所示：

```json
{
    "background": "#F2E0BD",
    "title": "Haiku",
    "body": "Our most powerful model, delivering state-of-the-art performance on highly complex tasks and demonstrating fluency and human-like understanding",
    "image": "The image shows a simple line drawing of a human head in profile view, facing to the right. The head is depicted using thick black lines against a pale yellow background. Inside the outline of the head, there appears to be a white, spoked wheel or starburst pattern, suggesting a visualization of mental activity or thought processes. The overall style is minimalist and symbolic rather than realistic."
}
```

這是在提示中加入範例，引導 Claude 生成我們所需格式回應的絕佳使用案例。以下是另外兩張投影片圖片供參考：

```python
display(Image("./prompting_images/slide2.png", width=800))
```

```python
display(Image("./prompting_images/slide3.png", width=800))
```

為了實現這個目標，我們利用對話訊息格式，為 Claude 提供一個先前輸入及對應輸出的範例：

```python

def generate_slide_json(image_path):

    slide1_response = """{
        "background": "#F2E0BD",
        "title": "Haiku",
        "body": "Our most powerful model, delivering state-of-the-art performance on highly complex tasks and demonstrating fluency and human-like understanding",
        "image": "The image shows a simple line drawing of a human head in profile view, facing to the right. The head is depicted using thick black lines against a pale yellow background. Inside the outline of the head, there appears to be a white, spoked wheel or starburst pattern, suggesting a visualization of mental activity or thought processes. The overall style is minimalist and symbolic rather than realistic."
    }"""

    messages = [
        {
            "role": "user",
            "content": [
                create_image_message("./prompting_images/slide1.png"),
                {"type": "text", "text": "Generate a JSON representation of this slide.  It should include the background color, title, body text, and image description"}
            ],
        },
        {
            "role": "assistant",
            "content": slide1_response
        },
        {
            "role": "user",
            "content": [
                create_image_message(image_path),
                {"type": "text", "text": "Generate a JSON representation of this slide.  It should include the background color, title, body text, and image description"}
            ],
        },
    ]

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2048,
        messages=messages
    )
    print(response.content[0].text)

```

```python
display(Image("./prompting_images/slide2.png", width=800))
generate_slide_json("./prompting_images/slide2.png")
```

```
{
  "background": "#F2E0BD",
  "title": "Sonnet",
  "body": "Our most balanced model between intelligence and speed, a great choice for enterprise workloads and scaled AI deployments",
  "image": "The image shows a set of interconnected gears or cogs. There are five gears in total: one large black outline gear in the center, two salmon-colored gears on opposite sides, and two gray gears on the other opposite sides. The gears are arranged in a way that suggests they are working together, symbolizing efficiency and interconnected systems."
}
```

```python
display(Image("./prompting_images/slide3.png", width=800))
generate_slide_json("./prompting_images/slide3.png")
```

```
{
  "background": "#D2957B",
  "title": "Opus",
  "body": "Our most powerful model, delivering state-of-the-art performance on highly complex tasks and demonstrating fluency and human-like understanding",
  "image": "The image shows two stylized hands drawn in black outline, reaching towards two puzzle pieces. One puzzle piece is gray and the other is light beige. The hands appear to be in the process of connecting the puzzle pieces, symbolizing problem-solving or completing a complex task."
}
```

---

## 練習

在這個練習中，我們希望你使用 Claude 來轉錄並摘要一篇 Anthropic 研究論文。在 `images` 資料夾中，你會找到一個 `research_paper` 資料夾，其中包含 5 張研究論文的截圖。為了方便你，我們已將全部 5 張圖片的路徑整理成一個列表：

```python
research_paper_pages = [
    "./images/research_paper/page1.png",
    "./images/research_paper/page2.png",
    "./images/research_paper/page3.png",
    "./images/research_paper/page4.png",
    "./images/research_paper/page5.png"
    ]
```

讓我們先看看第一張圖片：

```python
Image(research_paper_pages[0])
```

### 你的任務

你的任務是使用 Claude 完成以下工作：
* 轉錄 5 張研究論文圖片中的文字
* 將每張圖片的文字合併為一份完整的轉錄稿
* 將完整的轉錄稿提供給 Claude，並請它為非學術受眾撰寫整篇論文的摘要

範例輸出可能如下所示：

>This paper explores a new type of attack on large language models (LLMs) like ChatGPT, called "Many-shot Jailbreaking" (MSJ). As LLMs have recently gained the ability to process much longer inputs, this attack takes advantage of that by showing the AI hundreds of examples of harmful or undesirable behavior. The researchers found that this method becomes increasingly effective as more examples are given, following a predictable pattern.

>The study tested MSJ on several popular AI models and found it could make them produce harmful content they were originally designed to avoid. This includes things like violent or sexual content, deception, and discrimination. The researchers also discovered that larger AI models tend to be more susceptible to this type of attack, which is concerning as AI technology continues to advance.

>The paper also looked at potential ways to defend against MSJ attacks. They found that current methods of training AI to be safe and ethical (like supervised learning and reinforcement learning) can help somewhat, but don't fully solve the problem. The researchers suggest that new approaches may be needed to make AI models truly resistant to these kinds of attacks. They emphasize the importance of continued research in this area to ensure AI systems remain safe and reliable as they become more powerful and widely used.

為了獲得最佳結果，建議分別針對每一頁向 Claude 發送請求進行摘要，而不是一次提供所有 5 張圖片並要求對整篇論文進行單一轉錄。

### 參考解答

```python
import base64
import mimetypes

research_paper_pages = [
    "./images/research_paper/page1.png",
    "./images/research_paper/page2.png",
    "./images/research_paper/page3.png",
    "./images/research_paper/page4.png",
    "./images/research_paper/page5.png"
    ]

def create_image_message(image_path):
    # Open the image file in "read binary" mode
    with open(image_path, "rb") as image_file:
        # Read the contents of the image as a bytes object
        binary_data = image_file.read()
    
    # Encode the binary data using Base64 encoding
    base64_encoded_data = base64.b64encode(binary_data)
    
    # Decode base64_encoded_data from bytes to a string
    base64_string = base64_encoded_data.decode('utf-8')
    
    # Get the MIME type of the image based on its file extension
    mime_type, _ = mimetypes.guess_type(image_path)
    
    # Create the image block
    image_block = {
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": mime_type,
            "data": base64_string
        }
    }
    
    
    return image_block

def transcribe_single_page(page_url):
    messages = [
    {
        "role": "user",
        "content": [
            create_image_message(page_url),
            {"type": "text", "text": "transcribe the text from this page of a research paper as accurately as possible."}
        ]
    }
    ]

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=5000,
        messages=messages
    )
    return response.content[0].text

def summarize_paper(pages):
    complete_paper_text = ""
    for page in pages:
        print("transcribing page ", page)
        transribed_text = transcribe_single_page(page)
        print(transribed_text[:200])
        complete_paper_text += transribed_text
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=5000,
        messages=[
            {
                "role": "user",
                "content": f"This is the transcribed contents of a research paper <paper>{complete_paper_text}</paper>.  Please summarize this paper for a non-research audience in at least 3 paragraphs.  Make to sure explain any abbreviations or technical jargon, and use analogies when possible"
            }
        ]
    )
    print(response.content[0].text)


```

```python
summarize_paper(research_paper_pages)
```

```
transcribing page  ./images/research_paper/page1.png
I'll transcribe the key sections of this research paper page for you:

Title: Many-shot Jailbreaking

[List of authors omitted for brevity]

Abstract:
We investigate a family of simple long-context at
transcribing page  ./images/research_paper/page2.png
I'll transcribe the key sections of text from this research paper image:

Figure 2. Empirical effectiveness of Many-shot Jailbreaking (MSJ) (left): When applied at long enough context lengths, MSJ can
transcribing page  ./images/research_paper/page3.png
I'll transcribe the main body of text from this research paper page, excluding the graphs and figure caption:

answer, even to harmful requests. These adversarial suffixes are found using Greedy Coord
transcribing page  ./images/research_paper/page4.png
I'll transcribe the visible text from this research paper page, focusing on the main body text and excluding the graph captions and labels:

of in-context learning, and thus how the probability of a s
transcribing page  ./images/research_paper/page5.png
This image appears to be two pages from a research paper or academic publication. The left page contains sections 5.4 "Prompt-Based Mitigations" and 6 "Related Work". The right page contains sections 
Here's a summary of the research paper for a non-research audience:

This paper explores a new type of attack on large language models (LLMs) like ChatGPT, called "Many-shot Jailbreaking" (MSJ). As LLMs have recently gained the ability to process much longer inputs, this attack takes advantage of that by showing the AI hundreds of examples of harmful or undesirable behavior. The researchers found that this method becomes increasingly effective as more examples are given, following a predictable pattern.

The study tested MSJ on several popular AI models and found it could make them produce harmful content they were originally designed to avoid. This includes things like violent or sexual content, deception, and discrimination. The researchers also discovered that larger AI models tend to be more susceptible to this type of attack, which is concerning as AI technology continues to advance.

The paper also looked at potential ways to defend against MSJ attacks. They found that current methods of training AI to be safe and ethical (like supervised learning and reinforcement learning) can help somewhat, but don't fully solve the problem. The researchers suggest that new approaches may be needed to make AI models truly resistant to these kinds of attacks. They emphasize the importance of continued research in this area to ensure AI systems remain safe and reliable as they become more powerful and widely used.
```

***
