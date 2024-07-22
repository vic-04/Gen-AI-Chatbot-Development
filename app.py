import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
from dotenv import load_dotenv
import base64
from utils import get_answer, text_to_speech, autoplay_audio, speech_to_text, get_conversation_chain, create_vector_store #get_text_input
from IPython.display import HTML, display

float_init()
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hi! How may I assist you today?"}
        ]
    if "audio_initialized" not in st.session_state:
        st.session_state.audio_initialized = False

initialize_session_state()

def main():
    # Chat display
    st.subheader("GreeneDesk Chatbot")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


        # Text input
    #user_text = get_text_input()
    user_text = st.text_input("Enter your question or message:")

        # Create buttons side by side
    cols = st.columns(3)

        # Text-to-Text (Send button)
    if cols[0].button("Send"):
        if user_text:
            messages = [{"role": "user", "content": user_text}]
            response = get_answer(messages)
            st.session_state.messages.append({"role": "user", "content": user_text})
            st.session_state.messages.append({"role": "assistant", "content": response})

        # Text-to-Speech (Speak button)
    if cols[1].button("Speak"):
        if user_text:
            final_response = get_answer([{"role": "user", "content": user_text}])
            with st.spinner("Generating audio response..."):
                audio_file = text_to_speech(final_response)
                autoplay_audio(audio_file)
                os.remove(audio_file)
    else:
        # Speech-to-Text (Microphone button)
        audio_bytes = audio_recorder()
        #if cols[2].audio_bytes:
        if audio_bytes:
            with st.spinner("Transcribing..."):
                webm_file_path = "temp_audio.mp3"
                with open(webm_file_path, "wb") as f:
                    f.write(audio_bytes)
                transcript = speech_to_text(webm_file_path)
            if transcript:
                st.session_state.messages.append({"role": "user", "content": transcript})
                with st.spinner("Thinking🤔..."):
                    final_response = get_answer(st.session_state.messages)
                st.session_state.messages.append({"role": "assistant", "content": final_response})
                with st.chat_message("assistant"):
                    st.write(final_response)

 #main_container.float("bottom: 0rem;")
if __name__ == '__main__':
    main()
