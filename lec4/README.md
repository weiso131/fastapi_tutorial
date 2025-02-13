# bcrypt
bcrypt 是一種密碼雜湊（hashing）函式，常用於安全地存儲用戶密碼。它具有以下特點：

1. 基於 Blowfish 加密演算法：bcrypt 由 Blowfish 加密演算法演變而來，專為密碼存儲設計。
2. 內建鹽值（Salt）機制：每次雜湊時會自動生成一個隨機的鹽值，防止相同密碼生成相同的哈希值，提高安全性。
3. 可調整成本參數（Cost Factor）：bcrypt 允許設定計算成本（例如 12、14），增加計算時間，使暴力破解變得更困難。
4. 抗彩虹表攻擊：由於內建隨機鹽值，即使攻擊者擁有預計算好的哈希值表，也無法直接匹配。
5. 適合存儲密碼：因為計算較慢，相比 SHA-256 等快速哈希函式，bcrypt 能有效降低暴力破解速度。

```python=
import bcrypt

# 生成雜湊密碼
password = "my_secure_password".encode()
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

# 驗證密碼
if bcrypt.checkpw(password, hashed):
    print("密碼正確")
else:
    print("密碼錯誤")
```

以上by chatGPT

## 關於密碼儲存
1. 在實作使用者密碼儲存時，不太會直接儲存明碼（原本的樣子），會存hash過後的字串
2. 儲存字串的時候可以先把它decode成utf-8，這樣就會是```str```型別，忘記是在encode jwt還是存進資料庫時
如果是原本```crypt.hashpw(password, salt)```的樣子會炸開，因為它是```bytes```型別

# jwt身份驗證

## 介紹
### JWT 由三個部分組成，每個部分用 . 分隔：

- Header（標頭）：包含 JWT 的類型（typ: JWT）和簽名演算法（alg，如 HMAC、RSA）。
- Payload（負載）：存放使用者資訊或其他聲明（claims），例如 user_id、exp（過期時間）。
- Signature（簽名）：用來驗證 JWT 是否被竄改，通常由 Header 指定的演算法加密 Header 和 Payload。

### JWT 如何運作？
#### 登入時產生 JWT
使用者登入後，伺服器根據其資訊產生 JWT，並返回給使用者。
#### 使用 JWT 進行請求
使用者每次請求時，把 JWT 放到 Authorization Header，如：
```
Authorization: Bearer <JWT>
```
#### 伺服器驗證 JWT
伺服器收到請求後，檢查 JWT 是否有效（是否被篡改、是否過期）。
#### 驗證成功則允許訪問
若 JWT 有效，伺服器允許請求，否則拒絕存取。
### 優缺點
#### 優點：

- 無狀態：伺服器不需要存使用者 session（適合分散式系統）。
- 跨平台：JSON 格式適用於各種語言和框架。
- 可攜帶自定義資訊：可在 Payload 裡存放用戶角色等資訊。
#### 缺點：

- 無法撤銷：JWT 一旦發出，除非設置短期有效期，否則無法強制登出特定使用者。
- 佔用空間較大：相比 session ID，JWT 會變長，影響請求效能。
- 安全性風險：若私鑰洩漏，攻擊者可偽造 JWT。
### 常見應用場景
- API 驗證：使用 JWT 確保 API 只被授權用戶存取。
- 單點登入（SSO）：多個應用程式之間共享身份驗證信息。
- 無狀態身份驗證：讓伺服器不需要保存使用者 session。

以上by chatGPT

## 程式碼
```python=
def generate_tokens(payload):
    """
    生成訪問與刷新 Token
    :param user_id: int, 用戶 ID
    :param username: str, 用戶名
    :return: dict, 包含訪問與刷新 Token
    """
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)
    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {
        "access_token": access_token,
    }

def verify_jwt(token):
    """
    驗證 JWT Token
    :param token: str, JWT Token
    :return: dict, 解碼後的 Payload
    :raises: jwt.ExpiredSignatureError, jwt.InvalidTokenError
    """
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise TOKEN_EXPIRED
    except jwt.InvalidTokenError:
        raise TOKEN_INVALID
```

# Depend
參考： [Day13 架構優化： Depends 萬用刀 & 常見錯誤](https://ithelp.ithome.com.tw/articles/10329960)

## 搭配jwt驗證
這東西是看[yee的code](https://github.com/gdsc-ncku/Tricking-Practice-1/blob/main/backend/routes/auth.py)學來的


```python=
from fastapi import Depends, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECURITY = HTTPBearer(
    scheme_name="JWT",
    description="JWT which get from /auth/login."
)

def verify_jwt(token: HTTPAuthorizationCredentials = Security(SECURITY)):
    以下略
UserDepend = Depends(verify_jwt)

```

在任何需要jwt身份驗證的地方

```python=
@router.get('/api')
def api(payload=UserDepend):
    做一些事情
```

這樣能吃到前端放在```Authorization: Bearer```的東西


# 練習
延續上次的練習
1. 加入register和login，回傳都是jwt token
2. 利用jwt token，限制以下api需要已登入者才能存取
    - 新增招式
    - 招式update
    - 刪除招式