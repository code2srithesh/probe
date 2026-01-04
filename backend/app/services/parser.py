import pdfplumber
import os
import json
from groq import Groq
from dotenv import load_dotenv

# 1. Load Environment Variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def extract_skills_from_resume(pdf_path: str):
    text = ""
    print(f"📄 Reading PDF: {pdf_path}")
    
    # 2. Extract Text from PDF
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        print(f"✅ PDF Read Success. Length: {len(text)} chars")
    except Exception as e:
        print(f"❌ PDF Error: {e}")
        return ["Resume Read Error"]

    print("⚡ Sending text to Groq (Llama 3.3)...")
    
    # 3. Ask Groq to extract skills
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # <--- THE WORKING MODEL
            messages=[
                {
                    "role": "system", 
                    "content": "You are a JSON extractor. Output ONLY valid JSON."
                },
                {
                    "role": "user",
                    "content": f"""
                    Extract TECHNICAL skills from this text as a JSON list of strings.
                    Ignore soft skills.
                    Text: {text[:6000]}
                    Output strictly: ["Skill1", "Skill2"]
                    """
                }
            ],
            temperature=0,
        )
        
        json_text = completion.choices[0].message.content
        # Clean up Markdown (sometimes Groq adds ```json)
        json_text = json_text.replace("```json", "").replace("```", "").strip()
        
        skills = json.loads(json_text)
        print(f"✅ Found Skills: {skills}")
        return skills
        
    except Exception as e:
        print(f"⚠️ Groq Parser Failed: {e}. Using Mock Skills.")
        return ["Java", "Python", "SQL", "Groq-Failed"]