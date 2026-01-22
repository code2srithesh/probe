import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load your API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("🔍 Searching for available models...")
try:
    for m in genai.list_models():
        # We only want models that can generate text (content)
        if 'generateContent' in m.supported_generation_methods:
            print(f" - {m.name}")
except Exception as e:
    print(f"❌ Error listing models: {e}")