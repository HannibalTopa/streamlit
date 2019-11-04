#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np

st.title("Car Payment Plan App")

df1=pd.DataFrame({"a":[1,2],
                           "b":[3,4]})
my_slot1=st.empty()
my_slot2=st.empty()

if st.checkbox("Show Data"):
    my_slot2.line_chart(df1)
    my_slot1.text("This is the exact plot you want")

car=st.selectbox("Select a Car",["Audi Q3 40TFSI Quattro","Audi A4L 40TFSI","Calldilac XT4","BMW 325i"])
my_slot3=st.empty()
year=st.radio("Loan Term",key="n1",options=[1,2,3,4])
rate=st.radio("Interest Rate",options=[0.04,0.05])
dp_rate=st.slider("Select a Down Payment Ratio",min_value=20,max_value=100)
if car=="Audi Q3 40TFSI Quattro":
    price=281000
    my_slot3.error("The Price is: RMB "+str(price))
elif car=="Audi A4L 40TFSI":
    price=285000
    my_slot3.warning("The Price is: RMB "+str(price))
elif car=="Calldilac XT4":
    price=280000
    my_slot3.info("The Price is: RMB "+str(price))
elif car=="BMW 325i":
    price=300000
    my_slot3.success("The Price is: RMB "+str(price))
a=price*dp_rate/100
ins=10000
tax=price/1.16*0.1
c=pow(1+rate/12,year*12)
"Down Payment of Loan:",round(a,2)
"Full Initial Payment:",round(a+ins+tax,2)
"Monthly Payment:",round(((price-a)*(rate/12)*c)/(c-1),2)

