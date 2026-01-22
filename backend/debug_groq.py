import os
from dotenv import load_dotenv

print("----------- GROQ DIAGNOSTIC TOOL -----------")

# 1. Test Environment Variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ CRITICAL ERROR: GROQ_API_KEY is missing!")
    print("   Make sure you created a file named .env in the backend/ folder.")
    print("   It should look like this: GROQ_API_KEY=gsk_1234...")
    exit()
else:
    # Cleanup whitespace just in case
    api_key = api_key.strip()
    print(f"✅ API Key found: {api_key[:5]}...{api_key[-4:]}")

# 2. Test Import
try:
    from groq import Groq
    print("✅ Groq library installed.")
except ImportError:
    print("❌ CRITICAL ERROR: 'groq' library not installed.")
    print("   Run: pip install groq")
    exit()

# 3. Test Connection
print("\n🔍 Testing Connection to Groq Cloud...")
try:
    client = Groq(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "Reply with one word: Success"}],
        # UPDATED MODEL NAME (The old one was decommissioned)
        model="llama-3.3-70b-versatile",
    )
    print(f"🎉 RESULT: {chat_completion.choices[0].message.content}")
    print("\n✅ CONNECTION SUCCESSFUL!")
    print("   If your app still fails, check if app/services/generator.py is loading .env correctly.")

except Exception as e:
    print(f"\n❌ CONNECTION FAILED: {e}")
    if "401" in str(e):
        print("   -> 401 means your API Key is invalid. Copy it again from console.groq.com")
    if "model_decommissioned" in str(e):
        print("   -> ERROR: You are using an old model name. Switch to 'llama-3.3-70b-versatile'.")
    if "429" in str(e):
        print("   -> 429 means you hit a rate limit.")