# async 非同步
在處理一些耗時操作(IO操作、網路請求)，可以利用非同步的特性先讓程式先去處理其他任務

## 範例
```python=
import asyncio

async def task_1():
    print("任務1開始")
    await asyncio.sleep(1)
    print("任務1結束")

async def task_2():
    print("任務2開始")
    await asyncio.sleep(2)
    print("任務2結束")

async def main():
    # 同時執行兩個非同步任務
    await asyncio.gather(task_1(), task_2())
    

# 啟動事件迴圈
asyncio.run(main())
```
### 執行結果
```
任務1開始
任務2開始
任務1結束
任務2結束
```

# AsyncIOMotorClient

AsyncIOMotorClient 是 Motor 提供的一個用於與 MongoDB 進行非同步連線的客戶端，基於 asyncio 事件循環進行非同步操作。

## 特點與優勢
- 非同步處理: 相較於傳統的同步 pymongo，Motor 能夠避免因 I/O 等待而阻塞事件循環，適合高併發的場景。
- 與 FastAPI/Django 等框架整合: 在建置需要大量 I/O 操作的後端應用程式時，與非同步框架（例如 FastAPI）配合效果極佳。
- 與 async/await 相容: 使用 Python 原生的 async/await 語法來簡化非同步邏輯。

(以上by chatGPT)
可參考： [Motor (Async Driver)](https://www.mongodb.com/zh-cn/docs/drivers/motor/)

## 連上yee的database
```python=
from motor.motor_asyncio import AsyncIOMotorClient

dc_name = "你的dc名稱"
uri = "在dc上找找"
tlsCAFileName = "mongodb-bundle.pem"
client = AsyncIOMotorClient(uri, tlsCAFile=tlsCAFileName)
db = client[dc_name] #有這東西就能對資料庫做一些操作
```
接下來只要定義表的名稱就能做些資料庫操作
假設我要一個trick的表：
```python=
trick_collection = db["trick"]
```

## CRUD操作
參考: [MongoDB CRUD 操作](https://www.mongodb.com/zh-cn/docs/manual/crud/)

# beanie
[官方文件](https://beanie-odm.dev/)

為了方便開發，通常一個專案會有多個檔案
但這導致如果單純使用db得做些奇怪的操作才能讓各個路徑的api能存取db
或是每次存取都開關一次db(但這有點沒效率)

(剩下交給chatGPT)

Beanie 是一個基於 Motor 的高層封裝，專門用於 MongoDB 的非同步 ODM（Object Document Mapper）。它提供類似 ORM 的操作體驗，並支援 MongoDB 的 Schema 驗證與索引等功能，與 Pydantic 完美整合

## 基本架構與 Document 繼承
Beanie 的核心概念是 Document，透過從 Document 類別繼承來定義 MongoDB 集合的 Schema。

```python=
from beanie import Document, init_beanie
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import asyncio

class User(Document):
    name: str
    age: int
    email: Optional[str] = None
```

## init_beanie

```python=
async def init_db():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.test_database, document_models=[User])

```

## CRUD操作
建議參考官方文件

(1) 建立資料 (Create)
```python=
async def create_user():
    user = User(name="Alice", age=25, email="alice@example.com")
    await user.insert()  # 直接將物件插入 MongoDB
```
(2) 查詢資料 (Read)
```python=
async def get_user_by_name(name: str):
    user = await User.find_one(User.name == name)
    print(user)
```
(3) 更新資料 (Update)
```python=
async def update_user_email(name: str, new_email: str):
    user = await User.find_one(User.name == name)
    if user:
        user.email = new_email
        await user.save()  # 儲存更新後的資料
```
(4) 刪除資料 (Delete)
```python
async def delete_user(name: str):
    user = await User.find_one(User.name == name)
    if user:
        await user.delete()
```

# 環境變數
有時候，開源專案存在一些敏感資訊(這邊有dc名稱, uri, secret_key)
可以用環境變數的方法避免直接將這些資訊傳到github上
參考： [Day 10 環境變數](https://ithelp.ithome.com.tw/articles/10326207)

# lifespan
[Day 29 定時任務與健康狀態檢查](https://ithelp.ithome.com.tw/articles/10338847)有提到startup事件，但這東西已經被棄用，改為使用新的lifespan比較好

# 練習
與上一個完全相同，只是將招式儲存在資料庫