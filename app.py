import streamlit as st

st.header('Calculator App')
st.write('This is a calculator application developed using Streamlit')
btn=st.button('Click Me')
if btn:
    st.balloons()

num1=st.number_input('Enter the first number',value=0)
option=st.selectbox('Select the operation',("+","-","/","*"))
num2=st.number_input("Enter the second number",value=0)
button1=st.button('Calculate')
if button1:
    if option=='+':
        st.subheader(f'added result is {num1+num2}')
    elif option=='-':
        st.subheader(f'substract a result is {num1-num2}')  
    elif option=='*':
        st.subheader(f'multiplied result is {num1*num2}')
    elif option=='/':
        st.subheader(f'devide a result is {num1/num2}')