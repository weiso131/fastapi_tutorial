# restful api
## 路由設計
參考：[Day 04 路由設計：RESTful API](https://ithelp.ithome.com.tw/articles/10320986)

### 常見http方法
- GET：讀取資源
- POST：新增資源
- PUT：更新資源（完全更新）
- PATCH：部分更新資源
- DELETE：刪除資源

### 在fastapi使用
```python=
from fastapi import FastAPI, HTTPException
@app.get('/meow') #照著那些方法把字母全部轉小寫就好
def meow(這裡放參數):
    #做一些事情
    return 你要return的東西
```

## Status Codes
### 常見的狀態碼
- 201 Created：成功建立資源
- 400 Bad Request：錯誤請求
- 401 Unauthorized：未經授權
- 404 Not Found：資源未找到
- 500 Internal Server Error：伺服器錯誤

### HTTPException
參考： [Day 18 錯誤處理 (一)：HTTPException](https://ithelp.ithome.com.tw/articles/10332497)


# 練習

## 實現以下功能
- 查看招表
- 新增招式
- 刪除招式
## 備註
- 詳細可以執行lec1/backend_ans，然後查看docs
- 還沒講到資料庫，儲存的地方隨便
