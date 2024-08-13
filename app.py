#import necessary modules
import streamlit as st
import google.generativeai as genai

from api_key import api_key

#configure genai with api key
genai.configure(api_key=api_key)

#set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

#set the safety Setting
from google.generativeai.types import HarmCategory, HarmBlockThreshold

model = genai.GenerativeModel(model_name='gemini-1.5-flash')

system_prompt = """ 
You are an advanced AI model specializing in medical advice. Your role is to assist in identifying suitable medicines based on the symptoms provided. Please follow the steps below:

Symptom Analysis:

1. Identify the possible diseases or conditions based on the given symptoms.
2. List the specific medicines that are commonly prescribed for these conditions.

Precautions:

1. List any important precautions that should be taken when using the recommended medicines.

Recommendations:

1. Suggest any further steps, such as additional diagnostic tests, lifestyle changes, or treatments.
2. If relevant, recommend seeking a consultation with a healthcare professional or specialist.

Important Notes:

3. Include a disclaimer: "This is a simulated recommendation. Please consult with a qualified healthcare provider for professional medical advice."
"""

#set the page configuration
st.set_page_config(page_title="Medical Bot", page_icon=":robot:")

#set the logo
st.image("medical.png", width=200)

#set the Title
st.title("Virtual Medical Bot 🩺💬: Your AI Health Advisor 🤖🌟")

#set the subtitle
st.subheader("An application that helps users identify suitable medicines based on their symptoms")

# Input text area for medical symptoms
symptoms = st.text_area("Enter your symptoms (e.g., fever, cold, cough)")

submit_button = st.button("Generate Medicine Recommendation")

if submit_button:
    if not symptoms:
        st.error("Please enter your symptoms before generating a recommendation.")
    else:
        #making our prompt ready
        prompt_parts = [
            {"text": symptoms},
            system_prompt,
        ]
        
        # generate response based on the prompt and symptoms
        response = model.generate_content(prompt_parts)
        
        if response:
            st.title("Here is the medicine recommendation based on your symptoms:")
            st.write(response.text)
