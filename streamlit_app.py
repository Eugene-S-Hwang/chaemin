import streamlit as st
import send_email


receiver = "rubysophia0716@gmail.com"

sender = "eugene2chaemin@gmail.com"
st.title("For Chaemin")
if(st.button("Press for a surprise!", type="primary")):
    send_email.send_email(receiver, sender)
    st.write("sent!")