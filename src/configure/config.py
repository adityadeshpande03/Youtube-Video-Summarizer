import os
from dotenv import load_dotenv
import google.generativeai as genai
from input.prompts import prompt

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def generate_gemini_content(transcript_text):
    model=genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt+transcript_text)
    return response.text
