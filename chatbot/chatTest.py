from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
import openai

app = FastAPI()

# OpenAI API 키 설정
openai.api_key = "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"

# 요청 데이터를 처리하기 위한 Pydantic 모델 정의
class ChatRequest(BaseModel):
    userNickname: str   
    userType: str
    userNo: int  
    userMessage: str

# FastAPI 엔드포인트 정의
@app.post("/chat")
async def chat_with_openai(request: ChatRequest = Body(...)):
    user_nickname = request.userNickname
    user_type = request.userType 
    user_no = request.userNo  
    user_message = request.userMessage
    try:
        # 사용자가 보낸 메시지를 OpenAI에 보내고 답변 받기
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": request.userMessage},
            {"role": "assistant", "content": "You are a helpful assistant."},
        ]
    )


        # 대화 메시지에 AI 답변 추출
        bot_message = response.choices[0].message["content"]
        print("Received data:", request)
        return {"botMessage": bot_message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
