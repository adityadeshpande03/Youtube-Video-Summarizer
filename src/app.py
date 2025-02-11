from configure.config import generate_gemini_content
from tools.transcription import extract_transcript
from input.prompts import prompt
import streamlit as st

st.title('Youtube Video Summarizer')
youtube_video_url = st.text_input('Enter the Youtube video URL:')

st.sidebar.title("📌 Instructions")
st.sidebar.write("1️⃣ Enter the Youtube Video URL.")
st.sidebar.write("x")
st.sidebar.write("3️⃣ Review the generated summary.")

if youtube_video_url:
    video_id = youtube_video_url.split('=')[1]
    print(video_id)

if st.button('Get Detailed Summary'):
    transcript_text = extract_transcript(youtube_video_url)

    if transcript_text:
        summary = generate_gemini_content(transcript_text+prompt)
        st.markdown('**Detailed Summary:**')
        st.write(summary)