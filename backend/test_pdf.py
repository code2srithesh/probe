from app.services.parser import extract_skills_from_resume
import os

# Create a dummy PDF for testing if you don't have one handy, 
# OR just change the path below to a real PDF on your desktop.
pdf_path = "test_resume.pdf" 

if not os.path.exists(pdf_path):
    print(f"❌ Please put a PDF file named '{pdf_path}' in the backend folder to test.")
else:
    print("🧪 Testing Parser...")
    skills = extract_skills_from_resume(pdf_path)
    print(f"🎉 Result: {skills}")