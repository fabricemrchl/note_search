## Public Lib
import streamlit as st
import pandas as pd
import numpy as np

## Project lib
import marqo_helper
import llm_helper


## Set web page settings
st.set_page_config(
    page_title="Note what ? 🔍",
    page_icon=":mag:",
    layout="centered",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

## Set page title
st.title('Note what ?')

temperature = st.sidebar.slider('Set temperature', 0.0, 1.0, 0.2, 0.1)
marqo_helper.create_index()

## Upload notes file
uploaded_files = st.file_uploader('Your notes in TXT format (UTF-8), multiple files accepted', type=['txt'], accept_multiple_files=True)
marqo_helper.import_data(uploaded_files)

# Create a text element and let the reader know the data is loading.
data_load_state = st.empty
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.


# Delete loading text
data_load_state.empty()

# Set search field
question = st.text_input("Text Search")

# research input text in marqo Database
results = marqo_helper.mq_search(question)

# Display marqo result
st.subheader('Raw data')
st.write(results)


# Display LLM Result
st.subheader('LLM answer')
if question == "":
    text_space = st.write("Text Search needed")
else:
    text_space = st.write("Brainstorming in progress...")
    llm = llm_helper.ask_llm(results, question, temperature)
    text_space = st.write(llm.content)



