import streamlit as st
import pickle

st.title("Credit Prediction")
limit_balance=st.number_input("Insert the LimitBalance")
pay0= st.number_input("Insert the pay0")
pay2= st.number_input("Insert the pay2")
pay3= st.number_input("Insert the pay3")
billatm1=st.number_input("Insert the BillATM1")
billatm2=st.number_input("Insert the BillATM2")
billatm3=st.number_input("Insert the BillATM3")
payatm1=st.number_input("Insert the payatm1")
payatm2=st.number_input("Insert the payatm2")
payatm3=st.number_input("Insert the payatm3")

submit = st.button("predict")
if submit:
    with open(r"model_pickle.pickle","rb") as f:
        mp=pickle.load(f)
        
    output=mp.predict([[limit_balance,pay0,pay2,pay3,billatm1,billatm2,billatm3,payatm1,payatm2,payatm3]])
    st.success( " output ==> " + str(output[0]))
    







