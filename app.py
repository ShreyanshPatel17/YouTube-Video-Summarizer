# Import all neccessary Libraries

import streamlit as st  
import google.generativeai as genai
from dotenv import load_dotenv 
from youtube_transcript_api import YouTubeTranscriptApi 
from fpdf import FPDF 

# NLP & Text Enhancement
from deepmultilingualpunctuation import PunctuationModel
import contractions
import re
import os

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Load punctuation model
punct_model = PunctuationModel()

# --- Text Enhancement Functions ---
def expand_contractions(text):
    return contractions.fix(text)

def punctuate_and_format(text):
    return punct_model.restore_punctuation(text)

def capitalize_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    capitalized = [s.strip().capitalize() for s in sentences if s]
    return ' '.join(capitalized)

def preprocess_text(text):
    expanded = expand_contractions(text)
    punctuated = punctuate_and_format(expanded)
    final = capitalize_sentences(punctuated)
    return final

# --- Transcript Extraction ---
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        original_transcript = " ".join([i["text"] for i in transcript_data])
        cleaned_transcript = preprocess_text(original_transcript)
        return original_transcript, cleaned_transcript
    except Exception as e:
        st.error("Error fetching transcript: " + str(e))
        return None, None

# --- Generate Summary ---
def generate_gemini_content(transcript_text, word_limit):
    prompt = f"""You are a YouTube video summarizer. 
    Summarize the video transcript in **{word_limit} words**. 
    Focus on key points and provide a clear, structured summary.
    And also generate a Title of that summary as per the transcript.
    Based on the following YouTube video summary, generate 5 thoughtful and relevant questions.
    The questions should test understanding of the key concepts, ideas, or facts presented in the video.
    Put questions at the end of the generated summary.

    Transcript: 
    {transcript_text}
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text

# --- PDF Generator ---
def clean_for_pdf(text):
    return text.encode('ascii', 'ignore').decode('ascii')

def create_pdf(summary):
    summary = clean_for_pdf(summary)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10,"Youtube Video Summary", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf_output_path = "summary.pdf"
    pdf.output(pdf_output_path)
    return pdf_output_path

# --- Streamlit UI ---
st.title("YouTube Video Summarizer")
youtube_link = st.text_input("Enter YouTube Video Link:")
word_limit = st.slider("Select Summary Length (Words)", min_value=50, max_value=500, step=50, value=250)

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Summary"):
    original_transcript, cleaned_transcript = extract_transcript_details(youtube_link)

    if cleaned_transcript:
        with st.expander("🔍 View Original Transcript"):
            st.write(original_transcript)

        with st.expander("🧹 View Preprocessed Transcript"):
            st.write(cleaned_transcript)

        with st.spinner("Generating summary..."):
            summary = generate_gemini_content(cleaned_transcript, word_limit)

        st.subheader("📃 Summary")
        st.write(summary)

        pdf_path = create_pdf(summary)

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(label="📄 Download Summary as PDF",
                               data=pdf_file,
                               file_name="YouTube_Summary.pdf",
                               mime="application/pdf")
