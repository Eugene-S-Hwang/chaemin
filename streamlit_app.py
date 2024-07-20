import streamlit as st
# import os
# from twilio.rest import Client

# account_sid = os.environ["TWILIO_SID"]
# auth_token = os.environ["TWILIO_TOKEN"]
# client = Client(account_sid, auth_token)

st.title("For Chaemin")
if(st.button("Press for a surprise!", type="primary")):
    # message = client.messages.create(
    #     body="Testing Testing",
    #     from_=os.environ["TWILIO_CH_NUM"],
    #     to=os.environ["CH_NUM"],
    # )
    st.write("works")
