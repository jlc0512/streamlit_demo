
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title('Incorporating a Model Prediction')

@st.cache
def load_model(file):
    model_file = open(file, 'rb')
    loaded_model = joblib.load(model_file)
    model_file.close()
    return loaded_model

penguin_model = load_model('penguin_dt.pkl')
st.sidebar.title('Form for Input')
form1 = st.sidebar.form(key='Inputs')
form1.header('Features to input:')
form1.subheader('Bill Length & Depth:')
bill_length = form1.number_input('Enter bill length (mm)', min_value=0.0)
bill_depth = form1.number_input('Enter bill depth (mm)', min_value=0.0)
form1.subheader('Flipper Length:')
flip_length = form1.number_input('Enter flipper length (mm)', min_value=0.0)
form1.subheader('Body Mass:')
body_mass = form1.number_input('Enter body mass (g)', min_value=0.0)
form1.subheader('Sex:')
sex = form1.number_input('Enter sex', help='Please enter 0 for Male or 1 for Female', min_value=0, max_value=1)
form1.subheader('Island:')
island_string = form1.selectbox('Select the Island', options=['Torgersen', 'Biscoe', 'Dream'])
form_button = form1.form_submit_button('Submit Features')

st.header('New Penguin Stats')
new_input = np.array([island_string, bill_length, bill_depth, flip_length, body_mass, sex]).reshape(1,-1)
predict_in = pd.DataFrame(new_input, columns=penguin_model.feature_names_in_)
expander_df = st.expander('Show new penguin stats')
expander_df.table(predict_in.loc[0])

predict_button = st.button('Predict the species of Penguin')
if predict_button:
    if float(predict_in['bill_length_mm'][0]) == 0.0:
        st.write('These are not valid stats')
    else:
        prediction = penguin_model.predict(predict_in)
        st.write('According to our model the species of this model is {prediction[0]}')
