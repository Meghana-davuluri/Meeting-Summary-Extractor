import os
import whisper

# Add ffmpeg to PATH
os.environ["PATH"] += os.pathsep + "/opt/homebrew/bin"

model = whisper.load_model("base")
result = model.transcribe("Meeting.mp4", fp16=False)
print(result["text"])

