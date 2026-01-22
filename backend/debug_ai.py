import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Force load the .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("----------- AI DIAGNOSTIC TOOL -----------")

if not api_key:
    print("❌ CRITICAL ERROR: GEMINI_API_KEY is missing!")
    print("   Make sure you have a .env file with GEMINI_API_KEY=...")
    exit()
else:
    print(f"✅ API Key found: {api_key[:5]}...{api_key[-4:]}")

# 2. Configure
try:
    genai.configure(api_key=api_key)
except Exception as e:
    print(f"❌ Configuration Failed: {e}")
    exit()

# 3. Test Connection & List Models
print("\n🔍 Testing Connection to Google...")
try:
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
            print(f"   - Found: {m.name}")
    
    if not available_models:
        print("❌ No text generation models found! Your key might be invalid.")
        exit()
        
except Exception as e:
    print(f"❌ Connection Failed: {e}")
    print("   (This usually means your Internet is blocking Google or the Key is banned)")
    exit()

# 4. Try the safest model
# Force test the one we want to use
test_model = 'models/gemini-flash-latest'
if test_model not in available_models:
    test_model = available_models[0] # Pick the first available one

print(f"\n🧪 Attempting generation with: {test_model}")

try:
    model = genai.GenerativeModel(test_model)
    response = model.generate_content("Reply with only the word: Success")
    print(f"🎉 RESULT: {response.text}")
    print(f"\n✅ FIX: Open generator.py and parser.py and use this model name: '{test_model}'")
except Exception as e:
    print(f"❌ Generation Failed: {e}")
    if "429" in str(e):
        print("⚠️ RATE LIMIT HIT: You have used all your free credits. Wait 1 hour or use a new Google Account.")