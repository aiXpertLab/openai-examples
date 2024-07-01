"""
    Module Name: Chat with Vector-PostgreSQL
    Version: 1.0

    Description: Vector-PostgreSQL entrance page.

    Initialize:
    - message
    - uri
    - unique_id
    - ui to run()
"""
import streamlit as st
from app.utils import streamlit_components, streamlit_docs

streamlit_components.streamlit_ui('🌤️ Chroma 🦣 PostgreSQL')
streamlit_docs.chroma_postgre_intro()
# -----------------------------------------------------------------------------------------------------------
from app import (
    chat_ui,
    db_vector_handler,
    llm_vector_handler
)

with st.spinner('loading'):
    if __name__ == "__main__":

        # initialization
        db_vector_handler = db_vector_handler.DBVectorHandler()   # init: session_state add uri, with save() get unique_id.
        llm_vector_handler = llm_vector_handler.LLMVectorHandler()  # LLM handler with the OpenAI API key

        # Create an instance of the Streamlit UI and pass the handlers to it
        app = chat_ui.ChatUI(db_vector_handler, llm_vector_handler)

        app.run()       # Run the Streamlit application
