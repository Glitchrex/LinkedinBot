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

def generate_post(prompt, context):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": context}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

def main():
    base = f"user"
    prompt = read_file(f"{base}/prompt.txt")
    context = read_file(f"{base}/context.txt")

    post = generate_post(prompt, context)

    posts_dir = f"{base}/posts"
    os.makedirs(posts_dir, exist_ok=True)

    # Compute content hash at generation time and include it in the filename
    post_hash = hashlib.sha256(post.encode("utf-8")).hexdigest()
    filename = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}-{post_hash}.txt"
    path = f"{posts_dir}/{filename}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(post)

    print(f"✅ Post generated : {path} (hash: {post_hash})")

if __name__ == "__main__":
    main()
