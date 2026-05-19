# 🎥 YouTube Video Summarizer

An AI-powered YouTube Video Summarizer that extracts transcripts from YouTube videos, enhances the transcript using NLP techniques, and generates concise AI-powered summaries using Google Gemini AI.

The application also generates:
- 📌 Video Title
- 📝 Summary
- ❓ Comprehension Questions
- 📄 Downloadable PDF Summary

Built using Python, Streamlit, NLP, and Generative AI technologies.

---

# ✨ Features

- 🔗 YouTube video transcript extraction
- 🧠 AI-generated summaries using Gemini AI
- ✨ NLP-based transcript preprocessing
- 📌 Automatic title generation
- ❓ AI-generated comprehension questions
- 📄 Download summary as PDF
- 🎛️ Adjustable summary length
- 📚 View original and cleaned transcript
- 🖥️ Interactive Streamlit interface

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## AI / NLP
- Google Gemini API
- DeepMultilingualPunctuation
- NLP Text Processing

## Libraries Used

```txt
streamlit
google-generativeai
youtube-transcript-api
deepmultilingualpunctuation
contractions
fpdf
python-dotenv
re
```

---

# 📂 Project Structure

```bash
youtube-video-summarizer/
│
├── app.py
├── requirements.txt
├── .env
├── summary.pdf
└── README.md
```

---

# 🔄 Step-by-Step Working

## Step 1 — User Inputs YouTube URL

The user enters a YouTube video link into the Streamlit interface and selects the desired summary length.

---

## Step 2 — Transcript Extraction

The application extracts the transcript using:

- `youtube-transcript-api`

The raw transcript may contain:
- Missing punctuation
- Improper sentence structure
- Lowercase formatting

---

## Step 3 — NLP Preprocessing

The transcript undergoes preprocessing using NLP techniques:

### ✅ Contraction Expansion

Example:

```txt
don't → do not
can't → cannot
```

### ✅ Punctuation Restoration

Using:
- `deepmultilingualpunctuation`

Example:

Before:
```txt
hello everyone welcome to ai tutorial today we learn cnn
```

After:
```txt
Hello everyone, welcome to AI tutorial. Today we learn CNN.
```

### ✅ Sentence Capitalization

Regex-based sentence formatting and capitalization.

---

## Step 4 — Select Summary length

Select the summary length as per required as a count of words.

---

## Step 5 — AI Summary Generation

The cleaned transcript is sent to Google Gemini AI.

Gemini generates:
- 📌 Title
- 📝 Summary
- ❓ 5 Questions

---

## Step 6 — PDF Generation

The generated summary is converted into a downloadable PDF using:

- `FPDF`

---

# 🧠 NLP Techniques Used

## 1. Transcript Extraction
- Extracts subtitles/transcripts from YouTube videos

Library Used:
```txt
youtube-transcript-api
```

---

## 2. Contraction Expansion

Converts shortened words into complete forms.

Example:
```txt
I'm → I am
won't → will not
```

Library Used:
```txt
contractions
```

---

## 3. Punctuation Restoration

Adds proper punctuation to raw transcript text.

Example:
```txt
this is ai tutorial today we learn machine learning
```

Converted To:
```txt
This is AI tutorial. Today we learn machine learning.
```

Library Used:
```txt
deepmultilingualpunctuation
```

---

## 4. Sentence Formatting

Uses Regular Expressions (`re`) for:
- Sentence splitting
- Capitalization
- Formatting

---

# ▶️ How to Run Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/youtube-video-summarizer.git
cd youtube-video-summarizer
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

Get API Key from:

https://aistudio.google.com/

---

## 5️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📬 Contact

**Shreyansh Patel**

## 🔗 GitHub
https://github.com/ShreyanshPatel17


## 🔗 LinkedIn
https://linkedin.com/in/shreyanshpatel17
