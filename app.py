import streamlit as st
import pandas as pd
from sklearn import datasets
st.write("""
# find the product of two numbers
This app gives the product of two numbers taken as your input

""")

st.header("Input parameter")

input_1 = st.number_input("Enter first number")
input_2 = st.number_input("Enter second number")
l = [input_1, input_2]
ans = l[0]*l[1]
data = {"First Number": input_1,
        "Second Number": input_2
       }  
features = pd.DataFrame(data, index=[0])
features 
st.subheader("User input parameter")
data
st.subheader("The multiplication/product of the two inputs")
ans

