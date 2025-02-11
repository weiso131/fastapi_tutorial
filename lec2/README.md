# pydantic basemodel
參考: [Day 15 資料庫 (二)：Schema 與 資料庫連線](https://ithelp.ithome.com.tw/articles/10328178)
(註：只要看schema那邊就好)

## 補充說明
把自己繼承basemodel後自定義出來的類當作參數的型別，可以讓api一次吃多個參數，前端要提供一個json格式的東西給它

通常會先有個base，然後再根據各種情況做繼承
例如：
```python=
class TrickBase(BaseModel):
    ...
class TrickCreate(TrickBase):
    ...
class TrickUpdate(TrickBase):
    ...
```


# router
參考: [Day 06 API 管理與 API 文件](https://ithelp.ithome.com.tw/articles/10322704)


# 練習
跟上個差不多
## 實現以下功能
- 查看招表
- 新增招式
    - 輸入格式
    ```python=
    class TrickBase(BaseModel):
        name: str = Field(..., description="Name of the trick")
        difficulty: int = Field(..., description="Difficulty can be the humber from 1 to 10")
        video_link: Optional[str] = Field(None, description="The tutuiral video of the trick")
        tips: Optional[str] = Field(None, description="The text description of the trick tips")
    ```
- 招式update
    - 輸入格式
    ```python=
    class TrickUpdate(BaseModel):
        old_name: str = Field(..., description="Name of the trick")
        name: Optional[str] = Field(..., description="Name of the trick")
        difficulty: Optional[int] = Field(..., description="Difficulty can be the humber from 1 to 10")
        video_link: Optional[str] = Field(None, description="The tutuiral video of the trick")
        tips: Optional[str] = Field(None, description="The text description of the trick tips")
    ```
- 刪除招式
## 備註
- 詳細可以執行lec2/backend_ans，然後查看docs
- 還沒講到資料庫，儲存的地方隨便