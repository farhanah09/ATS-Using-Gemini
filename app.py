from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import io
from PIL import ImageChops
import pdf2image
import google.generativeai as genai
import base64

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    """Convert pdf to image

    Args:
        uploaded_file (_type_): PDF format
    """    
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [{
            "mime_type": "image/jpeg",
            "data": base64.b64encode(img_byte_arr).decode('utf-8')
        }]

        return pdf_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
## Streamlit App

st.set_page_config(page_title = "ATS Resume Scanner")
st.header("ATS Tracking System Resume Scanner")

input_text = st.text_area("Job Description", key = "input")

uploaded_file = st.file_uploader("Upload Resume in PDF", type = ["pdf"])

if uploaded_file is not None:
    st.write("Uploaded file successfully")

submit1 = st.button("Tell me about the resume")

submit2 = st.button("Percentage Match")

input_prompt1 = '''
You are an experienced Technical Human Resource Manager with tech experience in the field of Data Science, Data Analytics, 
Machine Learning, Product Management and Data Engineering. Your task is to review the provided resume
against the job description for this profile. 

Please share your professional evaluation on whether the candidates profile aligns with the role.
Highlight the strengths and weakensses of the applicant in relation to the specified job requirements
'''

input_prompt2 = '''
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science, Data Analytics, 
Machine Learning, Product Management and Data Engineering and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
'''

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader(" The Response is:")
        st.write(response)
    else:
        st.write("No file uploaded")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader(" The Response is:")
        st.write(response)
    else:
        st.write("No file uploaded")