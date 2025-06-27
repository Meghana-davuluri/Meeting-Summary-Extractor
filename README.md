Meeting Summary Extractor

Overview:
Transcribe Zoom/MP4 meeting recordings into clean, concise bullet-point summaries with action items — using Whisper + GPT.
Built as a modular project with a real-world goal: **"No one revisits meeting recordings — this tool makes them instantly useful."**

## 🧠 Day 1: Audio Transcription (Whisper)

- 🎯 Goal: Convert meeting recordings into raw text
- ✅ Implemented using OpenAI Whisper (local)
- 🔁 Supports `.mp4`, `.mp3`, `.wav`, etc.
- 📦 Output: `output/raw_transcript.txt`

**Tech used**:
- Python
- `whisper`
- `ffmpeg` (for audio extraction if needed)

## 💡 Day 2: LLM Summarization

- 🎯 Goal: Take the transcript and return:
  - Bullet-point summary
  - Action items with names/dates
- ✅ Built using GPT-4 via OpenAI SDK (v1)
- 🧼 Transcript is cleaned before prompt is sent
- 📦 Output: `output/summary_output.txt`

**Tech used**:
- `openai` SDK (v1.x)
- `dotenv` for key management


