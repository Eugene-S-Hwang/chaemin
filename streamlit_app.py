import streamlit as st
import send_email
import email_address

receiver = email_address.receiver()

sender = email_address.sender()
st.title("For Chaemin")
if(st.button("Press for a surprise!", type="primary")):
    send_email.send_email(receiver, sender)
    st.write("sent!")
if(st.button("Press for a new surprise!", type="primary")):
    send_email.send_new_email(receiver, sender)
    st.write("sent!")