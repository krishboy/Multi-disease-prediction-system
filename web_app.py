import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Your Fav Health Assistant",
                   layout="wide",
                   page_icon="👨‍⚕️")
diabetes_model = pickle.load(open('trained_model1.sav', 'rb'))
parkinsons_model = pickle.load(open('trained_model2.sav', 'rb'))
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System by Krishna',

                           ['Female Diabetes Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity','person'],
                           default_index=0)
if selected == 'Female Diabetes Prediction':
    st.title('Female Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    diabetes_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diabetes_prediction = diabetes_model.predict([user_input])
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The person is diabetic'
        else:
            diabetes_diagnosis = 'The person is not diabetic'
    st.success(diabetes_diagnosis)

#parkinsons
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.text_input('MDVP : Fo(Hz)')
    with col2:
        flo = st.text_input('MDVP : Flo(Hz)')
    with col3:
        Shimmer = st.text_input('MDVP : Shimmer')
    with col1:
        APQ = st.text_input('MDVP : APQ')
    with col2:
        HNR = st.text_input('HNR')
    with col3:
        spread1 = st.text_input('spread 1')
    with col1:
        spread2 = st.text_input('spread 2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, flo, Shimmer, APQ, HNR, spread1, spread2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have the Parkinson's disease"
    st.success(parkinsons_diagnosis)
