import re
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="AI Resume Analyzer & Screener", page_icon="📄", layout="wide"
)

def extract_text_from_pdf(uploaded_file):
    """Extract text from uploaded PDF file."""
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def clean_text(text):
    """Clean extra spaces and newlines."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_match_score(resume_text, job_desc):
    """Calculate semantic similarity match percentage using TF-IDF and Cosine Similarity."""
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_desc])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100
    return round(score, 2)


def extract_keywords(text):
    """Extract top important terms from text."""
    vectorizer = TfidfVectorizer(stop_words="english", max_features=12)
    try:
        vectorizer.fit([text])
        return list(vectorizer.get_feature_names_out())
    except:
        return []


# --- UI Layout ---
st.title("📄 AI-Powered Resume Analyzer & Screener")
st.write(
    "Upload candidate resumes and paste job descriptions to evaluate alignment instantly."
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Job Description")
    job_description = st.text_area(
        "Paste the job description requirements here...", height=220
    )

with col2:
    st.subheader("2. Upload Resume")
    uploaded_file = st.file_uploader("Upload candidate resume", type=["pdf"])

# Analysis trigger
if st.button("Run Analysis", type="primary"):
    if not job_description or not uploaded_file:
        st.error("Please provide both a job description and upload a resume PDF.")
    else:
        with st.spinner("Analyzing resume content..."):
            # Process texts
            resume_text = extract_text_from_pdf(uploaded_file)
            cleaned_resume = clean_text(resume_text)
            cleaned_jd = clean_text(job_description)

            # Calculate match score
            score = calculate_match_score(cleaned_resume, cleaned_jd)

            # Extract keywords for comparison
            resume_keywords = set(extract_keywords(cleaned_resume))
            jd_keywords = set(extract_keywords(cleaned_jd))
            missing_keywords = jd_keywords - resume_keywords

            # Results Section
            st.markdown("---")
            st.subheader("📊 Screening Results")

            res_col1, res_col2 = st.columns(2)

            with res_col1:
                st.metric(label="Overall Match Score", value=f"{score}%")
                st.progress(min(score / 100.0, 1.0))

            with res_col2:
                st.write("**Top Key Terms Found in Resume:**")
                st.write(
                    ", ".join(resume_keywords)
                    if resume_keywords
                    else "No keywords found"
                )

            st.markdown("---")
            st.subheader("💡 Recommendations & Insights")

            if score > 70:
                st.success(
                    "✨ **Strong Match:** This candidate's background matches the core requirements of the job description."
                )
            elif score > 40:
                st.info(
                    "ℹ️ **Moderate Match:** The resume aligns partially, but missing key terminology or specific technical skills could impact ranking."
                )
            else:
                st.warning(
                    "⚠️ **Low Match:** Significant divergence between resume skills and job description criteria."
                )

            if missing_keywords:
                st.write(
                    "**Potential Missing Keywords / Skills:**",
                    ", ".join(missing_keywords),
                )

            with st.expander("View Raw Extracted Resume Text"):
                st.write(resume_text)