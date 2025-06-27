import openai
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_summary(transcript_text):
    prompt = f"""
You are a meeting summarizer.
Given the following transcript, return:
1. A bullet-point summary of the key points discussed
2. A list of clear, actionable next steps (action items), including names if mentioned.

Transcript:
{transcript_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    summary = response.choices[0].message.content
    return summary
