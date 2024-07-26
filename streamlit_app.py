import streamlit as st
import send_email

st.title("For Chaemin")
if(st.button("Press for a surprise!", type="primary")):
    send_email.send_email()
    st.write("sent!")
