import streamlit as st
import pickle
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Student Performance Analyzer",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - BLACK TEXT FOR PERFECT VISIBILITY
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stApp {
        background: transparent;
    }
    .metric-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    .recommendation-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        color: black !important;
        font-weight: 500;
    }
    .insight-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        color: black !important;
    }
    h1, h2, h3 {
        color: black !important;
    }
    .stMetric label {
        color: black !important;
    }
    .stMetric .css-1xarl3l {
        color: black !important;
    }
    .stMetric .stMetricValue {
        color: black !important;
    }
    /* Fix ALL text elements */
    .stMarkdown, .stText, p, div, span, li {
        color: black !important;
    }
    /* Sidebar text */
    .css-1d391kg {
        color: black !important;
    }
    /* Button text */
    .stButton > button {
        color: black !important;
        background: rgba(255,255,255,0.9) !important;
    }
    /* Slider labels */
    .stSlider label {
        color: black !important;
    }
    /* Expander text */
    .streamlit-expanderHeader {
        color: black !important;
    }
    /* Dataframe headers */
    .dataframe thead th {
        color: black !important;
        background-color: rgba(255,255,255,0.8) !important;
    }
    /* Dataframe cells */
    .dataframe tbody td {
        color: black !important;
        background-color: rgba(255,255,255,0.7) !important;
    }
</style>
""", unsafe_allow_html=True)

# Load model and scaler
@st.cache_resource
def load_model():
    try:
        with open('linear_regression_model.pkl', 'rb') as file:
            model = pickle.load(file)
        with open('scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        return model, scaler
    except:
        st.error("⚠️ Model files not found. Please ensure 'linear_regression_model.pkl' and 'scaler.pkl' are in the directory.")
        return None, None

model, scaler = load_model()

# [REST OF YOUR CODE REMAINS EXACTLY THE SAME - NO CHANGES NEEDED]
# AI-Powered Recommendation Engine
class StudyAdvisor:
    @staticmethod
    def get_study_recommendations(hours_studied, previous_scores, extracurricular, sleep_hours, sample_papers, predicted_score):
        recommendations = []
        insights = []
        mentoring_plan = []
        
        # Study Hours Analysis
        if hours_studied < 3:
            recommendations.append({
                "category": "📚 Study Time",
                "priority": "HIGH",
                "message": "Increase study hours to 4-6 hours daily",
                "action": "Create a structured study schedule with 25-min focused sessions (Pomodoro Technique)",
                "impact": "+15-20 points potential"
            })
            mentoring_plan.append("Weekly check-ins to monitor study schedule adherence")
        elif hours_studied < 5:
            recommendations.append({
                "category": "📚 Study Time",
                "priority": "MEDIUM",
                "message": "Good study habits! Optimize for quality over quantity",
                "action": "Focus on active recall and spaced repetition techniques",
                "impact": "+10-15 points potential"
            })
        else:
            insights.append("✅ Excellent study time commitment! Maintain this consistency.")
        
        # Previous Scores Analysis
        if previous_scores < 50:
            recommendations.append({
                "category": "📈 Foundation Building",
                "priority": "CRITICAL",
                "message": "Focus on strengthening fundamental concepts",
                "action": "1. Daily concept review sessions\n2. One-on-one tutoring\n3. Start with easier topics to build confidence",
                "impact": "+20-30 points potential"
            })
            mentoring_plan.append("Bi-weekly personalized tutoring sessions focusing on weak areas")
            mentoring_plan.append("Monthly progress assessments with detailed feedback")
        elif previous_scores < 75:
            recommendations.append({
                "category": "📈 Performance Boost",
                "priority": "MEDIUM",
                "message": "You're on the right track! Let's optimize your approach",
                "action": "1. Practice advanced problem-solving\n2. Join study groups\n3. Teach concepts to others (Feynman Technique)",
                "impact": "+15-20 points potential"
            })
            mentoring_plan.append("Weekly peer study group facilitation")
        else:
            insights.append("🌟 Outstanding previous performance! Focus on maintaining excellence.")
        
        # Sleep Analysis
        if sleep_hours < 6:
            recommendations.append({
                "category": "😴 Sleep & Wellness",
                "priority": "HIGH",
                "message": "Insufficient sleep significantly impacts learning and memory",
                "action": "1. Aim for 7-8 hours of sleep\n2. Establish a bedtime routine\n3. Avoid screens 1 hour before bed",
                "impact": "+10-15 points potential"
            })
            insights.append("⚠️ Sleep deprivation reduces cognitive function by up to 40%")
        elif sleep_hours > 9:
            recommendations.append({
                "category": "😴 Sleep Optimization",
                "priority": "LOW",
                "message": "Consider optimizing sleep duration",
                "action": "7-8 hours is optimal for most students. Extra sleep may indicate other issues.",
                "impact": "+5 points potential"
            })
        else:
            insights.append("✅ Perfect sleep schedule for optimal learning!")
        
        # Sample Papers Analysis
        if sample_papers < 3:
            recommendations.append({
                "category": "📝 Practice & Testing",
                "priority": "HIGH",
                "message": "Increase practice with sample papers and mock tests",
                "action": "1. Solve 2-3 sample papers weekly\n2. Analyze mistakes thoroughly\n3. Time yourself to build exam stamina",
                "impact": "+15-20 points potential"
            })
            mentoring_plan.append("Weekly mock test sessions with detailed performance analysis")
        elif sample_papers < 6:
            recommendations.append({
                "category": "📝 Practice Enhancement",
                "priority": "MEDIUM",
                "message": "Good practice! Let's make it more strategic",
                "action": "Focus on previous year papers and challenging questions",
                "impact": "+10 points potential"
            })
        else:
            insights.append("🎯 Excellent practice routine! You're exam-ready!")
        
        # Extracurricular Balance
        if extracurricular == 0:
            recommendations.append({
                "category": "⚖️ Life Balance",
                "priority": "MEDIUM",
                "message": "Consider adding extracurricular activities",
                "action": "1. Join 1-2 activities you enjoy\n2. Improves stress management\n3. Enhances overall cognitive function",
                "impact": "+5-10 points potential"
            })
        else:
            insights.append("🎨 Great balance between academics and activities!")
        
        # Predicted Score Based Recommendations
        if predicted_score < 50:
            recommendations.append({
                "category": "🎯 Intensive Improvement Plan",
                "priority": "CRITICAL",
                "message": "Comprehensive support needed",
                "action": "1. Daily structured study plan\n2. Professional tutoring 3x/week\n3. Weekly progress monitoring\n4. Identify and address learning gaps",
                "impact": "+25-35 points potential"
            })
            mentoring_plan.append("Daily check-ins via messaging app")
            mentoring_plan.append("Parent-teacher meetings every 2 weeks")
        elif predicted_score < 70:
            recommendations.append({
                "category": "🎯 Strategic Improvement",
                "priority": "HIGH",
                "message": "Focus on targeted improvements",
                "action": "1. Identify top 3 weak areas\n2. Dedicated practice sessions\n3. Regular self-assessment",
                "impact": "+15-25 points potential"
            })
            mentoring_plan.append("Bi-weekly mentoring sessions")
        elif predicted_score < 85:
            insights.append("💪 Strong performance! Fine-tune your strategies for excellence.")
            mentoring_plan.append("Monthly strategy optimization sessions")
        else:
            insights.append("🏆 Outstanding prediction! You're on track for exceptional results!")
            mentoring_plan.append("Quarterly advanced learning sessions")
        
        return recommendations, insights, mentoring_plan
    
    @staticmethod
    def get_study_techniques():
        return {
            "Active Recall": "Test yourself frequently instead of passive re-reading",
            "Spaced Repetition": "Review material at increasing intervals over time",
            "Feynman Technique": "Explain concepts in simple terms to identify gaps",
            "Pomodoro Method": "25-min focused study + 5-min break cycles",
            "Mind Mapping": "Visual organization of concepts and relationships",
            "Interleaving": "Mix different subjects/topics in study sessions",
            "Practice Testing": "Regular mock exams under timed conditions",
            "Elaborative Interrogation": "Ask 'why' and 'how' for deeper understanding"
        }

# [INCLUDE ALL THE REST OF YOUR ORIGINAL CODE EXACTLY AS-IS FROM HERE...]
# Header through Footer - no changes needed since CSS fixes visibility

# Header
st.title("🎓 AI-Powered Student Performance Analyzer")
st.markdown("### Personalized Learning Insights & Recommendations")

# Sidebar for inputs
with st.sidebar:
    st.header("📊 Input Your Data")
    st.markdown("---")
    
    hours_studied = st.slider('📚 Hours Studied (Daily)', 0, 10, 5, 
                              help="Average hours you study per day")
    
    previous_scores = st.slider('📈 Previous Scores (%)', 0, 100, 70,
                                help="Your recent exam scores")
    
    extracurricular_activities = st.selectbox('🎨 Extracurricular Activities', 
                                              ('Yes', 'No'),
                                              help="Do you participate in sports, arts, or clubs?")
    
    sleep_hours = st.slider('😴 Sleep Hours (Daily)', 0, 12, 7,
                           help="Average sleep duration per night")
    
    sample_papers = st.slider('📝 Sample Papers Practiced (Weekly)', 0, 10, 3,
                             help="Number of practice tests you complete weekly")
    
    st.markdown("---")
    analyze_button = st.button("🚀 Analyze Performance", type="primary", use_container_width=True)

if model and scaler:
    # Prepare input data
    extracurricular_encoded = 1 if extracurricular_activities == 'Yes' else 0
    
    input_data = {
        'Hours Studied': hours_studied,
        'Previous Scores': previous_scores,
        'Extracurricular Activities': extracurricular_encoded,
        'Sleep Hours': sleep_hours,
        'Sample Question Papers Practiced': sample_papers
    }
    
    input_df = pd.DataFrame(input_data, index=[0])
    
    # Scale numerical features
    numerical_cols = ['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']
    input_scaled = input_df.copy()
    input_scaled[numerical_cols] = scaler.transform(input_df[numerical_cols])
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    
    # Main dashboard [CONTINUE WITH ALL YOUR ORIGINAL DASHBOARD CODE...]
    if analyze_button or True:  # Auto-analyze on load
        # Top metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("🎯 Predicted Score", f"{prediction:.1f}%", 
                     delta=f"{prediction - previous_scores:.1f}",
                     help="AI-predicted performance index")
        
        with col2:
            performance_level = "Excellent" if prediction >= 85 else "Good" if prediction >= 70 else "Average" if prediction >= 50 else "Needs Improvement"
            st.metric("📊 Performance Level", performance_level)
        
        with col3:
            potential_improvement = max(0, 95 - prediction)
            st.metric("📈 Growth Potential", f"+{potential_improvement:.1f}%",
                     help="Maximum achievable improvement")
        
        with col4:
            study_efficiency = (prediction / (hours_studied + 1)) * 10
            st.metric("⚡ Study Efficiency", f"{study_efficiency:.1f}/10",
                     help="Output per hour of study")
        
        # [CONTINUE WITH ALL YOUR VISUALIZATIONS, RECOMMENDATIONS, AND FOOTER EXACTLY AS ORIGINAL]
        # ... rest of your code remains IDENTICAL ...

else:
    st.error("Unable to load the model. Please check if model files exist in the directory.")
    st.info("Required files: linear_regression_model.pkl, scaler.pkl")
