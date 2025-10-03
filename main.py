import os
from dotenv import load_dotenv
from cerebras.cloud.sdk import Cerebras

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("CEREBRAS_API_KEY")

if not API_KEY:
    raise ValueError("⚠️ Please set your CEREBRAS_API_KEY in a .env file")

# Initialize Cerebras client
client = Cerebras(api_key=API_KEY)

def generate_code(prompt: str) -> str:
    """Send coding request to Cerebras LLM and return generated code."""
    response = client.chat.completions.create(
        model="llama3.1-8b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content  # ✅ FIXED

def main():
    print("🚀 AI Code Assistant (powered by Cerebras)\n")
    user_prompt = input("Enter your coding request: ")

    code = generate_code(user_prompt)

    print("\n✨ Generated Code:\n")
    print(code)

    # Save code to file
    with open("generated_code.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("\n✅ Code saved to generated_code.py")

if __name__ == "__main__":
    main()
