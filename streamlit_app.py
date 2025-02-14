import streamlit as st
import send_email
import email_address

receiver = email_address.receiver()

sender = email_address.sender()

st.markdown("""
    <style>
        button {
            padding-top: 50px !important;
            padding-bottom: 50px !important;
        }
    </style>
""", unsafe_allow_html=True)

def yes():
    st.session_state["stage"] = 0

def no():
    if(st.session_state.stage == 1):
        st.session_state["stage"] = 2
    else:
        st.session_state["stage"] = 1

if("stage" not in st.session_state):
    st.session_state["stage"] = 1

if(st.session_state["stage"] >= 1):
    st.image("images/cat.jpg")
    st.header("Chaemin, would you like to be my valentine this year?")

if(st.session_state["stage"] == 1):
    col1, col2 = st.columns(2)
    with col1:
        st.button("\n\nYES!!!!!!\n\n", type="primary", on_click=yes, use_container_width=True)
    with col2:
        st.button("\n\nno\n\n", type="primary", on_click=no, use_container_width=True)

if(st.session_state["stage"] == 2):
    col1, col2 = st.columns(2)
    with col1:
        st.button("\n\nno\n\n", type="primary", on_click=no, use_container_width=True)
    with col2:
        st.button("\n\nYES!!!!!!\n\n", type="primary", on_click=yes, use_container_width=True)

if(st.session_state["stage"] == 0):
    st.image("images/yay!.jpg")
    st.header("YAYAYAYYAYYAYYAYYYYAY!")
    st.subheader("Click below for a message!")

    # st.title("For Chaemin")
    if(st.button("Press for a surprise!", type="primary")):
        send_email.send_email(receiver, sender)
        st.write("sent!")
    if(st.button("Press for a new surprise!", type="primary")):
        send_email.send_new_email(receiver, sender)
        st.write("sent!")