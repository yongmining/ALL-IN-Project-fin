import openai

# OpenAI API 키 설정
openai.api_key = "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"

# 대화 데이터를 API에 보내기 위한 함수
def create_openai_chat(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message["content"]

# 대화 시작
messages = [
    {"role": "user", "content": "안녕, 오늘 날씨 어때?"},
    {"role": "system", "content": "You are a helpful assistant."},
]

while True:
    user_input = input("사용자: ")
    messages.append({"role": "user", "content": user_input})

    # 대화를 OpenAI에 보내고 답변 받기
    assistant_response = create_openai_chat(messages)
    print("AI 답변:", assistant_response)

    # 대화 메시지에 AI 답변 추가
    messages.append({"role": "assistant", "content": assistant_response})