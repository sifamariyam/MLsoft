import pandas as pd
import streamlit as st
from PIL import Image
import pickle
from sklearn.preprocessing import LabelEncoder

#load
model=pickle.load(open('diabetes_model.save','rb'))
scaler=pickle.load(open('diabetes_scaler.save','rb'))
encod=pickle.load(open('diabetics_encoder.save','rb'))
encod1=pickle.load(open('diabetics_encoder1.save','rb'))

# Define a function to navigate to the selected page

def navigate_to(page):
    st.session_state.current_page = page

# Initialize session state for the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Home'

with st.sidebar:
    st.title('Navigation')
    if st.button("Home"):
        navigate_to("Home")

    if st.button("Symptoms"):
        navigate_to("Symptoms")

    if st.button("Complications"):
        navigate_to("Complications")

    if st.button("Management and Treatment"):
        navigate_to("Management and Treatment")

    if st.button("Prevention"):
        navigate_to("Prevention")

    if st.button('Check Diabetics'):
        navigate_to(('Check Diabetics'))

# Display the selected page
if st.session_state.current_page == "Home":
    st.title('DIABETES PREDICTION')
    img = Image.open('Diabetes.jpg')
    st.image(img, width=500)
    st.write()
    st.write(':point_right: Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high.')
    st.write(':point_right: Glucose is your body\'s main source of energy. Your body can make glucose, but it also comes from the food you eat.')
    st.write(':point_right: Insulin is a hormone made by the pancreas that helps glucose get into your cells to be used for energy.')
    st.write(':point_right: When your body does not make enough insulin or cannot use it properly, glucose stays in your blood and does not reach your cells.')
    st.write(':point_right: Diabetes raises the risk of damage to the eyes, kidneys, nerves, and heart. It can also increase the risk of other serious health conditions over time.')

elif st.session_state.current_page == "Symptoms":
    st.title('Symptoms of Diabetes')
    st.write("1. Increased thirst and hunger")
    st.write("2. Frequent urination")
    st.write("3. Unexplained weight loss")
    st.write("4. Fatigue")
    st.write("5. Blurred vision")
    st.write("6. Slow-healing sores")
    st.write("7. Frequent infections")

elif st.session_state.current_page == "Complications":
    st.title('Complications of Diabetes')
    st.write("If poorly managed, diabetes can lead to complications.such as:")
    st.write("1. Cardiovascular disease (heart attack, stroke)")
    st.write("2. Neuropathy (nerve damage)")
    st.write("3. Nephropathy (kidney damage)")
    st.write("4. Retinopathy (eye damage leading to blindness)")
    st.write("5. Foot problems (infections, ulcers)")

elif st.session_state.current_page == "Management and Treatment":
    st.title('Management and Treatment')
    st.write(":point_right: Diet and Exercise: A balanced diet and regular physical activity are crucial in managing diabetes and maintaining healthy blood sugar levels.")
    st.write(":point_right: Medications: Depending on the type of diabetes, medications may include insulin, metformin, or other drugs to help control blood glucose levels.")
    st.write(":point_right: Blood Sugar Monitoring: Regular monitoring of blood glucose levels helps in managing diabetes effectively and preventing complications.")
    st.write(":point_right: Education and Support: Education on diabetes management and support from healthcare providers, family, and community play a key role in effective treatment.")

elif st.session_state.current_page == "Prevention":
    st.title('Prevention of Diabetes')
    st.write("1. Maintain a healthy weight.")
    st.write("2. Follow a balanced diet rich in fruits, vegetables, whole grains, and lean proteins.")
    st.write("3. Exercise regularly.")
    st.write("4. Avoid tobacco use.")
    st.write("5. Limit alcohol consumption.")
    st.write("Early detection and proper management are key to preventing complications associated with diabetes.")

elif st.session_state.current_page == "Check Diabetics":
    st.title('Diabetics Prediction')
    #input features
    Gender=st.radio('gender',['Female', 'Male'])
    gen=encod.transform([Gender])[0]
    age=st.text_input('Age','')
    hypertension=st.radio('hypertension',['Yes','No'])

    if hypertension == 'Yes':
        hypertension=1
    else:
        hypertension=0

    heart_disease=st.radio('heart_disease',['Yes', 'No'])
    if heart_disease == 'Yes':
        heart_disease=1
    else:
        heart_disease=0

    smoking_history=st.selectbox('smoking_history',['not current', 'former', 'No Info', 'current', 'never', 'ever'])
    smoke_enco=encod1.transform([smoking_history])[0]

    bmi=st.text_input('BMI','')
    HbA1c_level=st.text_input('HbA1c_level','')
    bgl=st.text_input('blood glucose level','')

    features=[gen,age, hypertension,heart_disease, smoke_enco,bmi,HbA1c_level,bgl]
    
    predict=st.button('Click')
    if predict:
        pred=model.predict(scaler.transform([features]))
        if pred == 1:
            st.header('Indicating the presence of Diabetes')
        else:
            st.header('No Diabetes')