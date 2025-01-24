#to run the file: streamlit run calculator.py
import streamlit as st

st.title('calculator')
st.markdown("this is a simple calculator")

c1,c2 = st.columns(2)
fnum =c1.number_input("enter first number", value=0)
snum=c2.number_input('enter second number',value=0)

options= ["Addition","Subtraction","Multipication","Division"]
choice =st.radio("Select Operation",options)

button =st.button("Calculate")

if button:
    if choice =="Addition":
        result = fnum + snum
    if choice == "Subtraction":
        result = fnum - snum
    if choice == "Multipication":
        result = fnum * snum
    if choice =="Division":
        result = fnum/ snum


st.success(f"Result is {result}")