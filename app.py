# type: ignore
import os
from typing import TextIO
import pandas as pd
import streamlit as st
import openai
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI

#openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_answer_csv(file: TextIO, query: str) -> str:
    """
    Returns the answer to the given query by querying a CSV file.

    Args:
    - file (str): the file path to the CSV file to query.
    - query (str): the question to ask the agent.

    Returns:
    - answer (str): the answer to the query from the CSV file.
    """
    # Create an agent using OpenAI and the CSV file
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)

    # Run the agent on the given query and return the answer
    answer = agent.run(query)
    return answer

st.header("Chat with any CSV")
uploaded_file = st.file_uploader("Upload a csv file", type=["csv"])

if uploaded_file is not None:
    query = st.text_area("Ask any question related to the document")
    button = st.button("Submit")
    if button:
        st.write(get_answer_csv(uploaded_file, query))
