# day1_hello.py
from openai import OpenAI

client = OpenAI(
    api_key="xxxx",
    base_url="https://api.deepseek.com"  # 指向DeepSeek
)

messages = [
    {"role": "system", "content": "你是一个Go语言专家，回答简洁，给出代码示例"}
]

stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "详细解释一下Go的GMP调度模型"}
    ],
    stream=True  # 开启流式输出
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()  # 换行
