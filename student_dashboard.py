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

# Custom CSS for high-tech look
st.markdown("""
<style>
 [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #1f2937, #111827);
}

h1, h2, h3 {
    color: white !important;
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
        color: white;
        font-weight: 500;
    }
    .insight-box {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        color: white;
    }
    h1, h2, h3 {
        color: white !important;
    }
    .stMetric label {
        color: white !important;
    }
    .stMetric .css-1xarl3l {
        color: white !important;
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

# Header
st.markdown("""
<div style="
background: rgba(255,255,255,0.12);
backdrop-filter: blur(12px);
border-radius: 16px;
padding: 20px;
">
""", unsafe_allow_html=True)

st.markdown("## 🎓 AI-Powered Student Performance Analyzer")
st.markdown("### Personalized Learning Insights & Recommendations")

st.markdown("</div>", unsafe_allow_html=True)

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
    
    # Main dashboard
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
        
        st.markdown("---")
        
        # Visualization section
        col1, col2 = st.columns(2)
        
        with col1:
            # Radar chart for skill analysis
            categories = ['Study Hours', 'Previous Performance', 'Practice Tests', 'Sleep Quality', 'Life Balance']
            values = [
                (hours_studied / 10) * 100,
                previous_scores,
                (sample_papers / 10) * 100,
                (sleep_hours / 12) * 100,
                extracurricular_encoded * 100
            ]
            
            fig = go.Figure(data=go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                fillcolor='rgba(99, 110, 250, 0.5)',
                line=dict(color='rgb(99, 110, 250)', width=2)
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100], showticklabels=True, ticks=''),
                    bgcolor='rgba(255, 255, 255, 0.1)'
                ),
                showlegend=False,
                title="Your Performance Profile",
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white', size=12),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Score comparison gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=prediction,
                delta={'reference': previous_scores, 'increasing': {'color': "green"}},
                title={'text': "Performance Index", 'font': {'color': 'white', 'size': 20}},
                gauge={
                    'axis': {'range': [None, 100], 'tickcolor': 'white'},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 50], 'color': 'rgba(255, 99, 71, 0.3)'},
                        {'range': [50, 70], 'color': 'rgba(255, 215, 0, 0.3)'},
                        {'range': [70, 85], 'color': 'rgba(50, 205, 50, 0.3)'},
                        {'range': [85, 100], 'color': 'rgba(0, 128, 0, 0.3)'}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 85
                    }
                }
            ))
            
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font={'color': "white", 'family': "Arial"},
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # AI Recommendations Section
        st.markdown("---")
        st.markdown("## 🤖 AI-Powered Recommendations")
        
        recommendations, insights, mentoring_plan = StudyAdvisor.get_study_recommendations(
            hours_studied, previous_scores, extracurricular_encoded, 
            sleep_hours, sample_papers, prediction
        )
        
        # Display insights
        if insights:
            st.markdown("### 💡 Key Insights")
            for insight in insights:
                st.markdown(f'<div class="insight-box">{insight}</div>', unsafe_allow_html=True)
        
        # Display recommendations
        if recommendations:
            st.markdown("### 🎯 Personalized Action Plan")
            
            # Sort by priority
            priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
            recommendations.sort(key=lambda x: priority_order.get(x['priority'], 4))
            
            for rec in recommendations:
                priority_color = {
                    "CRITICAL": "🔴",
                    "HIGH": "🟠", 
                    "MEDIUM": "🟡",
                    "LOW": "🟢"
                }
                
                with st.expander(f"{priority_color.get(rec['priority'], '⚪')} {rec['category']} - {rec['message']}", expanded=True):
                    st.markdown(f"**Priority Level:** {rec['priority']}")
                    st.markdown(f"**Action Steps:**")
                    st.info(rec['action'])
                    st.success(f"**Expected Impact:** {rec['impact']}")
        
        # Mentoring Plan
        st.markdown("---")
        st.markdown("### 👨‍🏫 Personalized Mentoring Plan")
        
        if mentoring_plan:
            for i, plan in enumerate(mentoring_plan, 1):
                st.markdown(f"{i}. {plan}")
        else:
            st.info("Continue your excellent self-directed learning approach!")
        
        # Study Techniques
        st.markdown("---")
        st.markdown("### 🧠 Proven Study Techniques")
        
        techniques = StudyAdvisor.get_study_techniques()
        
        cols = st.columns(2)
        for idx, (technique, description) in enumerate(techniques.items()):
            with cols[idx % 2]:
                st.markdown(f"**{technique}**")
                st.caption(description)
        
        # Progress Tracking
        st.markdown("---")
        st.markdown("### 📅 30-Day Improvement Roadmap")
        
        weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
        projected_scores = [
            prediction,
            min(100, prediction + 5),
            min(100, prediction + 12),
            min(100, prediction + 20)
        ]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=weeks, y=projected_scores,
            mode='lines+markers',
            name='Projected Progress',
            line=dict(color='#00f2fe', width=4),
            marker=dict(size=12, color='#4facfe')
        ))
        
        fig.add_trace(go.Scatter(
            x=weeks, y=[85]*4,
            mode='lines',
            name='Excellence Target',
            line=dict(color='green', width=2, dash='dash')
        ))
        
        fig.update_layout(
            title="Your Growth Trajectory",
            xaxis_title="Timeline",
            yaxis_title="Performance Score",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(255,255,255,0.1)',
            font=dict(color='white'),
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: white; padding: 20px;'>
            <p>💡 <strong>Remember:</strong> Consistency beats intensity. Small daily improvements lead to remarkable results!</p>
            <p style='font-size: 12px; opacity: 0.7;'>Last Updated: {}</p>
        </div>
        """.format(datetime.now().strftime("%B %d, %Y at %H:%M")), unsafe_allow_html=True)

else:
    st.error("Unable to load the model. Please check if model files exist in the directory.")
    st.info("Required files: linear_regression_model.pkl, scaler.pkl")



