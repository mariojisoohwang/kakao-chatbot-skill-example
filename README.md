# Kakao Chatbot Skill Example
[카카오 챗봇빌더](https://chatbot.kakao.com/)에 연결할 스킬 서버를 쉽게 개발할 수 있도록 참고할 수 있는 예제입니다.

## Skill
아래는 간단한 스킬서버 예제입니다. 카카오 챗봇빌더 서버의 [HTTP POST 요청](https://chatbot.kakao.com/docs/skill-response-format#skillpayload)을 받아서, 원하는 [응답](https://chatbot.kakao.com/docs/skill-response-format#skillresponse)을 만들 수 있습니다.


```python

app = FastAPI()

@app.post("/skill/hello")
async def skill(req: ChatbotRequest):

    response_json = {

        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕하세요!"
                    }
                }
            ]
        }
    }

    return response_json

```



## 콜백
일반적인 스킬은 타임아웃이 5초로 설정되어 있습니다. 5초 이상의 처리 시간이 필요한 경우에는 콜백을 이용하여 구현할 수 있습니다.  아래는 콜백이 동작하는 방식입니다.  스킬 요청을 받아서 (1) 콜백 활성화 (2) 응답 메시지 전송, 이렇게 두 단계로 사용자에게 응답을 보낼 수 있습니다.

```
     ┌─────┐          ┌────────────┐     
     │Kakao│          │Skill Server│     
     └──┬──┘          └─────┬──────┘     
        │     Request       │            
        │──────────────────>│            
        │                   │            
        │ Enable Callback   │            
        │<──────────────────│            
        │                   │            
        │         ╔═════════╧═══════════╗
        │         ║Time consuming task ░║
        │         ╚═════════╤═══════════╝
        │     Callback      │            
        │<──────────────────│   
```


1. 콜백 활성화
    ```json
    {
            "version" : "2.0",
            "useCallback" : true
    }
    ```

2. 응답 메시지 전송
(1)에서 요청에 포함된 ```userRequest.callbackUrl```로 HTTP POST 요청을 보냅니다.



## 배포하기 

### Fly.io 사용 예시 
*  참고 : https://fly.io/docs/languages-and-frameworks/python/ 

1. flyctl 설치  (https://fly.io/docs/hands-on/install-flyctl/)

```
brew install flyctl
```


2. Lauch

```
cd <project home>;
fly launch
```

