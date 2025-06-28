import streamlit as st
import whisper
from transcripts_utils import clean_transcript
from llm_summary import generate_summary

st.title("📝 Meeting Summary Extractor")

uploaded_file = st.file_uploader("Upload meeting audio or video file", type=["mp3", "mp4", "m4a", "wav"])

if uploaded_file:
    st.info("Transcribing audio...")

    # Save uploaded file
    with open("temp_input.mp4", "wb") as f:
        f.write(uploaded_file.read())

    # Transcribe using Whisper
    model = whisper.load_model("base")
    result = model.transcribe("temp_input.mp4", fp16=False)
    transcript = result["text"]

    # Clean and summarize
    cleaned = clean_transcript(transcript)
    st.success("Generating summary... (this may take a few seconds)")
