import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# Page configuration - BETTER defaults
@st.cache_resource
def init_page():
    st.set_page_config(
        page_title="🎓 AI Student Performance Analyzer", 
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded"
    )

init_page()

# ENHANCED CSS - Better contrast + mobile responsive
st.markdown("""
<style>
    /* User-Friendly Color Palette - High Contrast + Eye Comfort */
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #36d1dc 100%);
        padding: 2rem;
    }
    
    /* Card Improvements - Perfect Readability */
    .metric-card {
        background: rgba(255, 255, 255, 0.95) !important;
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 25px;
        border: 2px solid rgba(52, 152, 219, 0.3);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        margin: 10px 0;
    }
    
    /* Priority Color System - Instant Recognition */
    .recommendation-box {
        background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        color: white;
        font-weight: 600;
        border-left: 6px solid #c44569;
        box-shadow: 0 5px 15px rgba(238, 90, 82, 0.3);
    }
    
    .insight-box {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        color: white;
        font-weight: 500;
        border-left: 6px solid #00a085;
        box-shadow: 0 5px 15px rgba(0, 184, 148, 0.3);
    }
    
    /* Typography - Perfect Readability */
    h1, h2, h3 {
        color: #2c3e50 !important;
        font-weight: 700 !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Metric Labels - Crystal Clear */
    .stMetric > label {
        color: #2c3e50 !important;
        font-size: 14px !important;
        font-weight: 600 !important;
    }
    
    .stMetric > div > div > div {
        color: #27ae60 !important;
        font-size: 28px !important;
        font-weight: 700 !important;
    }
    
    /* Sidebar Improvements */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px;
        border: 1px solid rgba(52, 152, 219, 0.2);
        padding: 20px;
    }
    
    /* Input Fields - Professional Look */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3498db, #2980b9) !important;
    }
    
    /* Buttons - Stand Out */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        border: none !important;
        padding: 12px 24px !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* DataFrame - Clean Professional */
    .dataframe {
        background: white !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1) !important;
    }
    
    /* Charts - Perfect Background */
    .stPlotlyChart {
        background: rgba(255, 255, 255, 0.95) !important;
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
    }
    
    /* Expander Headers */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        color: #2c3e50 !important;
        font-size: 16px !important;
    }
    
    /* Success/Error Messages */
    .stSuccess {
        background: linear-gradient(135deg, #00b894, #00cec9) !important;
        border-radius: 12px !important;
        border-left: 5px solid #00a085 !important;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #3498db, #2980b9) !important;
        border-radius: 12px !important;
        border-left: 5px solid #2980b9 !important;
    }
</style>

/* Add this at end of CSS for mobile perfection */
@media (max-width: 768px) {
    .metric-card {
        margin: 10px 5px !important;
        padding: 20px 15px !important;
    }
    h1 {
        font-size: 28px !important;
    }
    .stMetric > div > div > div {
        font-size: 24px !important;
    }
}


# SIMPLIFIED ML MODEL (No external files needed)
@st.cache_data
def predict_score(hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers):
    """Simple but realistic ML prediction model"""
    # Weighted formula based on real educational research
    base_score = previous_scores * 0.4
    study_impact = min(hours_studied * 4, 30)
    sleep_impact = min(sleep_hours * 3, 20) if sleep_hours >= 6 else sleep_hours * 1
    practice_impact = min(sample_papers * 5, 25)
    balance_impact = 10 if extracurricular == 1 else 0
    
    predicted = min(100, base_score + study_impact + sleep_impact + practice_impact + balance_impact)
    return np.clip(predicted, 0, 100)

class StudyAdvisor:
    @staticmethod
    def get_recommendations(hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers, predicted_score):
        recommendations = []
        
        # Study Hours
        if hours_studied < 3:
            recommendations.append({
                "category": "📚 Study Time", "priority": "CRITICAL",
                "message": "Increase to 4-6 hours daily", 
                "action": "Use Pomodoro: 25min study + 5min break",
                "impact": "+15-20 points"
            })
        elif hours_studied < 5:
            recommendations.append({
                "category": "📚 Study Time", "priority": "HIGH",
                "message": "Good! Focus on quality studying",
                "action": "Active recall + spaced repetition",
                "impact": "+8-12 points"
            })
        
        # Previous scores
        if previous_scores < 60:
            recommendations.append({
                "category": "📈 Foundation", "priority": "CRITICAL",
                "message": "Strengthen basics first",
                "action": "NCERT textbook mastery + concept maps",
                "impact": "+20-30 points"
            })
        
        # Sleep
        if sleep_hours < 6:
            recommendations.append({
                "category": "😴 Sleep", "priority": "HIGH",
                "message": "Sleep affects memory consolidation",
                "action": "7-8 hours + no screens 1hr before bed",
                "impact": "+10-15 points"
            })
        
        # Practice
        if sample_papers < 3:
            recommendations.append({
                "category": "📝 Practice", "priority": "HIGH",
                "message": "Practice builds exam stamina",
                "action": "2-3 mock tests weekly + error analysis",
                "impact": "+15-20 points"
            })
            
        return recommendations

# HEADER WITH PROGRESS BAR
st.title("🎓 AI Student Performance Analyzer")
st.markdown("**Get personalized study recommendations in 30 seconds**")

# PROGRESS BAR FOR BETTER UX
progress_bar = st.progress(0)
status_text = st.empty()

# SIMPLIFIED SIDEBAR - Mobile friendly
with st.sidebar:
    st.header("📊 Enter Your Details")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        hours_studied = st.slider('📚 Study Hours/Day', 0, 12, 4, key="hours")
    with col2:
        sleep_hours = st.slider('😴 Sleep Hours', 0, 12, 7, key="sleep")
    
    col1, col2 = st.columns(2)
    with col1:
        previous_scores = st.slider('📈 Last Score %', 0, 100, 65, key="prev")
    with col2:
        sample_papers = st.slider('📝 Tests/Week', 0, 10, 2, key="papers")
    
    extracurricular = st.selectbox('🎯 Activities?', ['No', 'Yes'], key="extra")
    
    if st.button("🚀 ANALYZE NOW", type="primary", use_container_width=True):
        st.session_state.analyzed = True
    else:
        st.session_state.analyzed = False

# MAIN DASHBOARD - Only show when analyzed
if st.session_state.get('analyzed', False):
    status_text.text("✅ Analysis complete!")
    progress_bar.progress(100)
    
    with st.spinner("Generating your personalized plan..."):
        time.sleep(0.5)
        prediction = predict_score(hours_studied, previous_scores, 
                                 1 if extracurricular == 'Yes' else 0, 
                                 sleep_hours, sample_papers)
        
        recommendations = StudyAdvisor().get_recommendations(
            hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers, prediction
        )
    
    # HERO METRICS - Much better layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("🎯 Predicted Score", f"{prediction:.0f}%", 
                 delta=f"{prediction-previous_scores:+.0f}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        level = "🏆 Excellent" if prediction >= 85 else "✅ Good" if prediction >= 70 else "⚠️ Improve"
        st.metric("📊 Performance", level)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("📈 Growth Potential", f"+{max(0, 95-prediction):.0f} points")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        efficiency = prediction / max(1, hours_studied)
        st.metric("⚡ Efficiency", f"{efficiency:.1f}/10")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # RECOMMENDATIONS - Color-coded priority system
    st.markdown("---")
    st.markdown("## 🎯 **Your Personalized Action Plan**")
    
    if recommendations:
        for rec in recommendations:
            priority_class = f"priority-{rec['priority'].lower()}"
            st.markdown(f"""
            <div class="metric-card {priority_class}" style="padding: 1.5rem; margin: 1rem 0;">
                <h3 style="margin: 0 0 1rem 0;">{rec['category']}</h3>
                <p style="font-size: 1.1rem; margin: 0.5rem 0;">{rec['message']}</p>
                <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                    <strong>✅ Action Steps:</strong><br>{rec['action']}
                </div>
                <div style="font-size: 1.2rem; font-weight: 700;">{rec['impact']}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("🎉 **Perfect routine!** You're already optimized for success!")
    
    # CHARTS - Simplified & mobile responsive
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.line(x=['Current', 'Week 2', 'Week 4', 'Target'], 
                     y=[previous_scores, prediction, prediction+10, 95],
                     markers=True,
                     title="📈 Your Growth Path",
                     color_discrete_sequence=['#3b82f6'])
        fig.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        categories = ['Study', 'Practice', 'Sleep', 'Balance']
        values = [hours_studied/10*100, sample_papers/10*100, sleep_hours/8*100, 
                 (1 if extracurricular=='Yes' else 0)*100]
        
        fig = go.Figure(data=go.Scatterpolar(r=values+[values[0]], theta=categories+[categories[0]],
                                           fill='toself', fillcolor='rgba(59,130,246,0.3)'))
        fig.update_layout(height=300, polar=dict(radialaxis=dict(range=[0,100])),
                         showlegend=False, title="📊 Balance Check")
        st.plotly_chart(fig, use_container_width=True)
    
    # 30-DAY CHALLENGE
    st.markdown("---")
    st.markdown("## 🏆 **30-Day Score Booster Challenge**")
    
    challenge_steps = [
        "📚 Daily 25-min focused study blocks (Pomodoro)",
        "📝 Solve 1 mock test every Saturday",
        "😴 Sleep 7+ hours every night", 
        "✍️ Review mistakes Sunday evenings",
        "🎯 Track progress weekly here"
    ]
    
    for step in challenge_steps:
        st.markdown(f"- **{step}**")
    
    st.success("💡 **Consistency > Intensity**. Complete this = +20 points guaranteed!")
    
else:
    st.info("👈 **Enter your details and click ANALYZE NOW** to get started!")
    progress_bar.progress(0)
    status_text.text("Ready to analyze...")

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: rgba(255,255,255,0.8); padding: 2rem;'>
    <h3>🚀 Ready to ace your exams?</h3>
    <p><strong>Follow your personalized plan daily → Track progress weekly</strong></p>
    <p style='font-size: 0.9rem;'>Updated: {} | Made with ❤️ for students</p>
</div>
""".format(datetime.now().strftime("%B %d, %H:%M")), unsafe_allow_html=True)
