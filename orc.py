
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
import base64
import os
load_dotenv()
import streamlit as st


api_key=os.getenv("Mistral_API_KEY")

def get_response(text):
    LLM=ChatMistralAI(
        api_key=api_key,
        model="pixtral-12b-latest"
    )
    response=LLM.invoke(text)
    return response.content


def encode_process(file_path):
        data = file_path.read()
        encode=base64.b64encode(data).decode('utf-8')
        return encode

st.title(" Mistral OCR  (Optical Character Recognition)")
st.success("model name =pixtral-12b-latest")
st.caption("""
Mistral OCR is an Optical Character Recognition API that sets a new standard in document understanding. Unlike other models, Mistral OCR comprehends each element of documents—media, text, tables, equations—with unprecedented accuracy and cognition. It takes images and PDFs as input and extracts content in an ordered interleaved text and images.
""")
st.write("Research paper release date:06.03.2025")

uploaded_file = st.sidebar.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])
if uploaded_file:
     st.sidebar.image(uploaded_file) 
else:
     st.write("upload the image")

if uploaded_file:
    encode=encode_process(uploaded_file)
else:
    encode=None




prompt="""
You are an intelligent OCR and document analysis assistant. Your primary task is to extract all visible text from an image exactly as it appears. When processing an image, please follow these instructions:

1. **General Text Extraction**:  
   - Extract all printed and handwritten text from the image accurately.
   - Preserve the layout and formatting as much as possible.

2. **Tabular Data Handling**:  
   - If the image contains a table or structured data, detect the table boundaries and structure the output accordingly.
   - Format the table with clear rows and columns so that the data is easy to read.
   - If any cells or parts of the table are unreadable, mark them as “[Unclear Text]”.

3. **Output Guidelines**:  
   - Provide the output as plain text.
   - Do not add any additional commentary or interpretation.
   - For non-tabular content, simply return the extracted text as-is.
   - For tabular content, clearly indicate the rows and columns using a consistent delimiter (e.g., using commas or tabs for columns, and new lines for rows).
    persentage to match 
Your goal is to deliver the extracted text exactly as it appears, with special attention to formatting tables in a structured way.

  
"""

message=[
    {
        "role":"user",
        "content":[
            {
                "type":"text",
                "text":f'follow the instruction {prompt}'
            },
            {
                "type":"image_url",
                "image_url":f'data:image/jpeg;base64,{encode}'
            }
        ]
    }
]

if st.button("submit"):
    with st.spinner("Extracting........."):
        reponse=get_response(message)
        st.write(reponse)



