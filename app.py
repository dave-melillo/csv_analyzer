# Load libraries
import pandas as pd
from pandas.io.json import json_normalize 
import numpy as np
import requests
import urllib.request
import json
from datetime import datetime
import datetime as dt
import streamlit as st
import openai
from bs4 import BeautifulSoup
import json
    

finaldf = pd.DataFrame()
st.title("OpenAI CSV Analyzer")
st.markdown('###### This is a simple app that allows you to perform conversational analysis on any CSV file. Providing quality inputs will result in quality answers.')

st.markdown('---')

st.title("Upload CSV")

uploaded_file = st.file_uploader("Upload Here")
if uploaded_file is not None:
#process and format csv 
    df = pd.read_csv (uploaded_file)
    x = df.to_json()
    x = x[:1000]

st.markdown('---')

st.title("Inputs")

st.markdown('#### :rotating_light: you must put in your own API KEY for this app to work :rotating_light:')
openai_key = st.text_input('Enter your OpenAI API Key Here')
context = st.text_area('Provide some context about the file.')
#st.markdown('###### hint: The more context you give about the file, the better your answers will be. Describe columns, values and overall subject of the file.')

questions = st.text_area('Ask the questions you want answered.')
#st.markdown('###### hint: Are there any statistical anomalies? Is there anything else interesting about the file that a human would not see? ')

st.markdown('---')

st.title("Analyze the file with OpenAI")

with st.form("step_3"):
   # Every form must have a submit button.
   submitted = st.form_submit_button("Analyze")
   if submitted:
        #build prompt
    prompt = f"""
    This is the content of the file: "{x}"

    This is the context of the file: "{context}"

    Answer the following questions about the contents of the file: "{questions}"
    """
    #authenticate openai
    openai.api_key = openai_key
    # Set up the model
    model_engine = "text-davinci-003"
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024, 
        n=1,
        stop=None,
        temperature=0.5,
    )
    #access response text
    response = completion.choices[0].text


    st.write(response)
