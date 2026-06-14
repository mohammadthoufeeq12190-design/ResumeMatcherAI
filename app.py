import streamlit as st
import plotly.graph_objects as go

from modules.resume_parser import extract_text_from_pdf
from modules.matcher import extract_skills, calculate_match
from modules.gemini_ai import generate_feedback

st.set_page_config(page_title="ResumeMatcher AI")

st.title("📄 ResumeMatcher AI")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    value="""Python
SQL
Machine Learning
AWS
Docker
Git"""
)

if uploaded_file is not None:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.subheader("Resume Content")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=250
    )

    resume_skills = extract_skills(resume_text)

    st.subheader("Detected Resume Skills")

    for skill in resume_skills:
        st.write("✅", skill)

    jd_skills = extract_skills(job_description)

    score, matched, missing = calculate_match(
        resume_skills,
        jd_skills
    )

    st.subheader("Match Score")

    st.metric(
        "Resume Match %",
        f"{score}%"
    )

    # Gauge Chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text": "Resume Match Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"}
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Matched Skills")

    if len(matched) > 0:

        for skill in matched:
            st.write("✅", skill)

    else:
        st.write("No matched skills found.")

    st.subheader("Missing Skills")

    if len(missing) > 0:

        for skill in missing:
            st.write("❌", skill)

    else:
        st.write("No missing skills.")

    st.subheader("AI Resume Review")

    feedback = generate_feedback(
        resume_text,
        score,
        missing
    )

    st.write(feedback)

    st.download_button(
        label="📥 Download Report",
        data=feedback,
        file_name="resume_review.txt",
        mime="text/plain"
    )