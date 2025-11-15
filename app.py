import streamlit as st
st.title('CALCULATE YOUR BMI')
Weight = st.number_input('Enter your weight in KGs:')
Height = st.number_input('Enter your heght in CMs')
if Height==0:
    BMI = 0
else:
    BMI = Weight / Height**2
print("BMI =", BMI)
st.success(f'Your BMI is {BMI} KG/cm^2')

