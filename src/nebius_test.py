import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NEBIUS_API_KEY = os.getenv("NEBIUS_API_KEY")
NEBIUS_MODEL = os.getenv(
    "NEBIUS_MODEL",
    "meta-llama/Llama-3.3-70B-Instruct"
)

if not NEBIUS_API_KEY:
    raise ValueError(
        "NEBIUS_API_KEY is missing. Add it to your .env file before running this script."
    )

client = OpenAI(
    base_url="https://api.tokenfactory.nebius.com/v1/",
    api_key=NEBIUS_API_KEY,
)


def run_nebius_smoke_test():
    response = client.chat.completions.create(
        model=NEBIUS_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a concise AI assistant."
            },
            {
                "role": "user",
                "content": "Reply with exactly this sentence: Nebius Token Factory model call worked."
            }
        ],
        temperature=0,
        max_tokens=80,
    )

    message = response.choices[0].message
    content = message.content

    print("\nNebius Token Factory smoke test completed.")
    print(f"Model used: {NEBIUS_MODEL}\n")

    if content:
        print(content)
    else:
        print("The request succeeded, but the model returned no text content.")
        print("Raw response:")
        print(response)


if __name__ == "__main__":
    run_nebius_smoke_test()