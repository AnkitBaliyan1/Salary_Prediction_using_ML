import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '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'

st.title('OpenAI GPT-3 Streamlit Demo')
st.subheader('Demo chatbot')

user_input = st.text_area("Enter some text:", height=150)

if st.button('Submit'):
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        temperature=0.5,
        max_tokens=100
    )
    st.write(response.choices[0].text.strip())
