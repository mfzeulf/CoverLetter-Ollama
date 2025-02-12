import streamlit as st
import os
from cover_letter import CoverLetter_Ollama  

st.set_page_config(page_title="Cover Letter Generator", layout="centered")
st.markdown("""<h1 style='text-align: center;'>Cover Letter Generator</h1>
            <h5 style='text-align: center;'>Automatically create cover letter from your resume locally with LLM</h5>""", unsafe_allow_html=True)
st.session_state.generating = False
# Upload Resume
st.subheader("Upload your ATS resume.")
st.write("Upload a **.docx** or **.pdf** file of your ATS resume.")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    temp_file_path = f"temp_{uploaded_file.name}"
    with open(temp_file_path, "wb") as temp_file:
        temp_file.write(uploaded_file.read())
    # Input company data
    st.subheader("Company name and position")
    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("Enter the Company name here", placeholder="Example: Lipsum Intl", key="companyname")
    with col2:
        job_position = st.text_input("Enter the job role/position here", placeholder="Example: AI Engineer", key="positionname")
    #Input some descriptions
    st.subheader("Describe the company")
    company_description = st.text_area("Briefly describe the company description. You can copy paste the company description here", placeholder="Example: An automotive company specializing in car manufacturing and distribution. Has won many awards such as the best auto manufacturer of 2024.", height=100)
    st.subheader("Describe the position")
    job_description = st.text_area("You can copy paste the job description here", height=300)  

    # Start generating
    if st.button("Generate!"):
        st.session_state.generating = True
        process_resume = CoverLetter_Ollama(model="mistral")  # Menggunakan Ollama secara lokal
        process_resume.read_input(temp_file_path, job_description, company_name, job_position, company_description)  
        st.write("Processing... Your cover letter will appear below once it's finished.")
        st.text_area("Here's the generated cover letter.", process_resume.generate_cover_letter(), height=300)
        st.write("You can copy and paste this to your favorite document processor.")
        st.session_state.generating = False
    os.remove(temp_file_path)

# Footer with Credits
st.markdown(
    """
    <div class="footer">
        <p>Inspired from <a href="https://towardsdatascience.com/from-resume-to-cover-letter-using-ai-and-llm-with-python-and-streamlit/" target="_blank">This Article</a> By Piero Paialunga | Check him out!</p>
    </div>
    """,
    unsafe_allow_html=True
)