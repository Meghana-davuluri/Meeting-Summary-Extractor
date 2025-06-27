import os
import whisper

from transcripts_utils import clean_transcript
from llm_summary import generate_summary

# Add ffmpeg to PATH
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

model = whisper.load_model("base")
result = model.transcribe("Meeting.mp4", fp16=False)
transcript = result["text"]

#Save transcript to file for later use
with open("output/raw_transcript.txt", "w") as f:
    f.write(transcript)

#Read raw transcript from the file
transcript_text = open("output/raw_transcript.txt", "r").read()

#Cleanthe transcript
cleaned = clean_transcript(transcript_text)

# Generate Summary
summary = generate_summary(cleaned)

print(summary)
with open("output/summary_output.txt", "w") as f:
    f.write(summary)



