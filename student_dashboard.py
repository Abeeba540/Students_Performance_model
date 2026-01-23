import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="AI Student Performance Analyzer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# GLOBAL CSS – VISIBILITY & UX FIXED
# ==================================================
st.markdown("""
<style>

/* MAIN BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #312e81 0%, #1e1b4b 100%);
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #020617, #020617);
}

/* HEADINGS */
h1, h2, h3 {
    color: #ffffff !important;
    font-weight: 700;
}

/* NORMAL TEXT */
p, span, li {
    color: #e5e7eb;
    font-size: 15px;
}

/* METRICS */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 700;
}

[data-testid="stMetricLabel"] {
    color: #c7d2fe !important;
}

/* INSIGHT BOX */
.insight-box {
    background: rgba(14, 165, 233, 0.18);
    border-left: 4px solid #0ea5e9;
    border-radius: 12px;
    padding: 14px 18px;
    margin: 10px 0;
    color: #e0f2fe;
}

/* RECOMMENDATION BOX */
.recommendation-box {
    background: rgba(244, 114, 182, 0.18);
    border-left: 4px solid #f472b6;
    border-radius: 12px;
    padding: 14px 18px;
    color: #fce7f3;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LOAD MODEL
# ==================================================
@st.cache_resource
def load_model():
    with open("linear_regression_model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model()

# ==================================================
# HEADER (GLASSMORPHISM)
# ==================================================
st.markdown("""
<div style="
background: rgba(15,23,42,0.55);
backdrop-filter: blur(14px);
border-radius: 16px;
padding: 24px;
border: 1px solid rgba(255,255,255,0.08);
margin-bottom: 25px;
">
""", unsafe_allow_html=True)

st.markdown("## 🎓 AI-Powered Student Performance Analyzer")
st.markdown("### Personalized Learning Insights & Recommendations")

st.markdown("</div>", unsafe_allow_html=True)

# ==================================================
# SIDEBAR INPUTS
# ==================================================
with st.sidebar:
    st.header("📊 Input Your Data")
    st.markdown("---")

    hours_studied = st.slider("📚 Hours Studied (Daily)", 0, 10, 5)
    previous_scores = st.slider("📈 Previous Scores (%)", 0, 100, 70)
    extracurricular_activities = st.selectbox("🎨 Extracurricular Activities", ("Yes", "No"))
    sleep_hours = st.slider("😴 Sleep Hours (Daily)", 0, 12, 7)
    sample_papers = st.slider("📝 Sample Papers Practiced (Weekly)", 0, 10, 3)

    st.markdown("---")
    analyze_button = st.button("🚀 Analyze Performance", use_container_width=True)

# ==================================================
# PREDICTION
# ==================================================
extracurricular_encoded = 1 if extracurricular_activities == "Yes" else 0

input_df = pd.DataFrame([{
    "Hours Studied": hours_studied,
    "Previous Scores": previous_scores,
    "Extracurricular Activities": extracurricular_encoded,
    "Sleep Hours": sleep_hours,
    "Sample Question Papers Practiced": sample_papers
}])

numerical_cols = [
    "Hours Studied",
    "Previous Scores",
    "Sleep Hours",
    "Sample Question Papers Practiced"
]

input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])
prediction = model.predict(input_df)[0]

# ==================================================
# METRICS
# ==================================================
col1, col2, col3, col4 = st.columns(4)

col1.metric("🎯 Predicted Score", f"{prediction:.1f}%")
col2.metric("📊 Performance Level",
            "Excellent" if prediction >= 85 else
            "Good" if prediction >= 70 else
            "Average" if prediction >= 50 else
            "Needs Improvement")
col3.metric("📈 Growth Potential", f"+{max(0, 95 - prediction):.1f}%")
col4.metric("⚡ Study Efficiency", f"{(prediction / (hours_studied + 1)):.1f}/10")

st.markdown("---")

# ==================================================
# VISUALIZATIONS
# ==================================================
col1, col2 = st.columns(2)

with col1:
    categories = ['Study Hours', 'Previous Performance', 'Practice Tests', 'Sleep Quality', 'Life Balance']
    values = [
        (hours_studied / 10) * 100,
        previous_scores,
        (sample_papers / 10) * 100,
        (sleep_hours / 12) * 100,
        extracurricular_encoded * 100
    ]

    fig = go.Figure(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself'
    ))

    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(15,23,42,0.6)',
        font=dict(color='#e5e7eb'),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Performance Index", 'font': {'color': 'white'}},
        gauge={'axis': {'range': [0, 100]}}
    ))

    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(15,23,42,0.6)',
        font=dict(color='#e5e7eb'),
        height=400
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# FOOTER
# ==================================================
st.markdown("""
<div style="text-align:center; margin-top:40px; color:#e5e7eb;">
    <p>💡 <strong>Remember:</strong> Consistency beats intensity. Small daily improvements lead to remarkable results.</p>
    <p style="font-size:12px; opacity:0.7;">
        Last Updated: {}
    </p>
</div>
""".format(datetime.now().strftime("%B %d, %Y at %H:%M")), unsafe_allow_html=True)
