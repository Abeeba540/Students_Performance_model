import streamlit as st
import pickle
import numpy as np

st.title('Student Performance Prediction App')

# Load the trained model and scaler
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.sidebar.header('User Input Features')

def user_input_features():
    hours_studied = st.sidebar.slider('Hours Studied', 0, 10, 5)
    previous_scores = st.sidebar.slider('Previous Scores', 0, 100, 70)
    extracurricular_activities = st.sidebar.selectbox('Extracurricular Activities', ('Yes', 'No'))
    sleep_hours = st.sidebar.slider('Sleep Hours', 0, 12, 7)
    sample_papers = st.sidebar.slider('Sample Question Papers Practiced', 0, 10, 3)

    # Convert Extracurricular Activities to numerical
    extracurricular_activities_encoded = 1 if extracurricular_activities == 'Yes' else 0

    data = {
        'Hours Studied': hours_studied,
        'Previous Scores': previous_scores,
        'Extracurricular Activities': extracurricular_activities_encoded,
        'Sleep Hours': sleep_hours,
        'Sample Question Papers Practiced': sample_papers
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('User Input:')
st.write(input_df)

# Preprocess the input data
numerical_cols = ['Hours Studied', 'Previous Scores', 'Sleep Hours', 'Sample Question Papers Practiced']
input_df[numerical_cols] = scaler.transform(input_df[numerical_cols])

# Make prediction
prediction = model.predict(input_df)

st.subheader('Predicted Performance Index:')
st.write(f'Your predicted performance index is: {prediction[0]:.2f}')
