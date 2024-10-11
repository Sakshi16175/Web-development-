import streamlit as st
import PyPDF2
import openai


# App title
st.title("PDF Chatbot")
st.write("Upload a PDF file and ask questions.")

# Set API Key from environment variable
openai.api_key = "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" # Make sure to set this in your environment

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""  # Handle pages with no text
        return text
    

# Function to generate a response using the language model
def generate_response(user_question, pdf_text):
    messages = [
        {"role": "system", "content": "You are an AI assistant tasked with answering questions based on a provided document."},
        {"role": "user", "content": user_question},
        {"role": "system", "content": f"Document: {pdf_text}"}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=300,
            temperature=0.6,
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Error communicating with OpenAI: {e}")
        return "Sorry, I couldn't generate a response."

# File uploader for PDF
pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

if pdf_file is not None:
    pdf_text = extract_text_from_pdf(pdf_file)
    if pdf_text:  # Only proceed if text extraction was successful
        st.write("PDF uploaded successfully.")

        # Create a form 
        with st.form(key='question_form'):
            user_input = st.text_input("Ask a question about the PDF")
            submit_button = st.form_submit_button(label='Submit')

            if submit_button and user_input:
                response = generate_response(user_input, pdf_text)
                st.write("Chatbot response:")
                st.write(response)
