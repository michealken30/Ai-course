import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic(
    base_url=os.getenv("ANTHROPIC_BASE_URL"),
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    timeout=300.0,
)

response = client.messages.create(
    model=os.getenv("MODEL", "qwen3:4b"),
    max_tokens=512,
    messages=[
        {
            "role": "user",
            "content": "/no_think\nSay hello in one short sentence."
        }
    ],
)

for block in response.content:
    if block.type == "text":
        answer = block.text

        # Remove reasoning text if present
        if "</think>" in answer:
            answer = answer.split("</think>")[-1]

        print("AI Answer:", answer.strip())
