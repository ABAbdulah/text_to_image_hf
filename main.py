import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HF_TOKEN = os.getenv("HF_API_KEY")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_image(prompt: str, output_path="output.png"):
    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": prompt}
    )

    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved to '{output_path}'")
    else:
        print("❌ Error generating image:")
        print(response.status_code, response.text)

if __name__ == "__main__":
    prompt = input("📝 Enter your prompt: ")
    generate_image(prompt)
