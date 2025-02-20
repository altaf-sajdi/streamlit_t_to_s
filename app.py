import streamlit as st
from gtts import gTTS
import os
import shutil

"""
Developer: Altaf Hussain Sajidi
--------------------------------
Contact: 03003976568
--------------------------------
"""

# App Title
st.title("🎤 Text-to-Speech App with Multiple Voices")

# User Input with increased max characters
text = st.text_area("Enter your text:", max_chars=12000)

# Display character count
char_count = len(text)
st.write(f"Character Count: {char_count}/12000")

# Language Selection
available_languages = {
    "English": "en",
    "Urdu": "ur",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Hindi": "hi",
    "Chinese": "zh",
    "Japanese": "ja",
    "Russian": "ru",
    "Arabic": "ar",
    "Bengali": "bn",
    "Turkish": "tr",
    "Korean": "ko"
}
language = st.selectbox("Select Language:", list(available_languages.keys()))

# Voice Selection (Expanded with more options)
available_voices = {
    "Male": "com", 
    "Female": "f", 
    "UK Male": "co.uk",
    "UK Female": "co.uk_f",
    "US Male": "com",
    "US Female": "com_f",
    "Australian Male": "com.au",
    "Australian Female": "com.au_f",
    "Indian Male": "co.in",
    "Indian Female": "co.in_f",
    "Canadian Male": "ca",
    "Canadian Female": "ca_f"
}
voice_gender = st.selectbox("Select Voice:", list(available_voices.keys()))

if st.button("🔊 Listen"):
    if text.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Convert text to speech using gTTS
        tts = gTTS(text=text, lang=available_languages[language], slow=False, tld=available_voices[voice_gender])
        tts.save("speech.mp3")
        st.audio("speech.mp3", format="audio/mp3")
        
        # Save audio file in gallery directory
        gallery_path = "gallery"
        if not os.path.exists(gallery_path):
            os.makedirs(gallery_path)
        audio_path = os.path.join(gallery_path, "speech.mp3")
        shutil.copy("speech.mp3", audio_path)
        
        with open("speech.mp3", "rb") as file:
            st.download_button("📥 Download Audio", file, file_name="speech.mp3", mime="audio/mp3")

# To run the application, use the following command:
# streamlit run script.py
# To download the audio file:
# 1. Click the "Listen" button to generate audio
# 2. Use the "Download Audio" button that appears below
