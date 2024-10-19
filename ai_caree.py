import streamlit as st
import pickle
import numpy as np

# Load the models and LabelEncoders
with open('model1.pkl', 'rb') as file:
    model1 = pickle.load(file)

with open('model2.pkl', 'rb') as file:
    model2 = pickle.load(file)

with open('model3.pkl', 'rb') as file:
    model3 = pickle.load(file)

with open('label_encoders.pkl', 'rb') as file:
    label_encoders = pickle.load(file)

le_education = label_encoders['le_education']
le_skills = label_encoders['le_skills']
le_career_goal = label_encoders['le_career_goal']
le_career_path = label_encoders['le_career_path']
le_missing_skills = label_encoders['le_missing_skills']
le_learning_path = label_encoders['le_learning_path']

# Set page title and background style
st.title("AI Career Counseling Platform")
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #6a11cb, #2575fc); /* New gradient background */
        color: white;
    }
    /* Change button style */
    .stButton > button {
        background-color: #007bff; /* New button background color (blue) */
        color: white; /* Button text color */
        border: none; /* No border */
        border-radius: 10px; /* Rounded corners */
        padding: 10px 20px; /* Padding */
        font-size: 16px; /* Font size */
        cursor: pointer; /* Pointer on hover */
    }
    /* Change button hover effect */
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# Input from user
education = st.selectbox('Select Education', le_education.classes_)
skills = st.selectbox('Select Skills', le_skills.classes_)
career_goal = st.selectbox('Select Career Goal', le_career_goal.classes_)

# Predict button
if st.button('Predict'):
    # Encode user input
    input_data = np.array([[le_education.transform([education])[0], 
                            le_skills.transform([skills])[0], 
                            le_career_goal.transform([career_goal])[0]]])

    # Predictions
    predicted_career_path = le_career_path.inverse_transform([model1.predict(input_data)[0]])
    predicted_missing_skill = le_missing_skills.inverse_transform([model2.predict(input_data)[0]])
    predicted_learning_path = le_learning_path.inverse_transform([model3.predict(input_data)[0]])

    # Display predictions
    st.write(f'Recommended Career Path: {predicted_career_path[0]}')
    st.write(f'Missing Skill: {predicted_missing_skill[0]}')
    st.write(f'Suggested Learning Path: {predicted_learning_path[0]}')
