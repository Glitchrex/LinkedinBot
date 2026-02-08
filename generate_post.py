import os
import sys
import hashlib
from datetime import datetime
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GITHUB_TOKEN"),
    base_url="https://models.inference.ai.azure.com"
)

MODEL = "gpt-4o-mini"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def generate_post(system_prompt, user_message):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def main():
    base = "user"
    
    context_guidelines = read_file(f"{base}/context.txt")
    user_input = read_file(f"{base}/prompt.txt")
    system_prompt = f"{context_guidelines}"
    
    post = generate_post(system_prompt, user_input)

    posts_dir = f"{base}/posts"
    os.makedirs(posts_dir, exist_ok=True)

    post_hash = hashlib.sha256(post.encode("utf-8")).hexdigest()
    filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-{post_hash}.txt"
    path = f"{posts_dir}/{filename}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(post)

    print(f"✅ Post generated: {path} (hash: {post_hash})")

if __name__ == "__main__":
    main()
