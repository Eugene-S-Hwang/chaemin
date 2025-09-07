import yagmail
import streamlit as st
import random
from messages import messages
# import os

# og_indxs = []
class emails:
    def send_email(receiver, sender):
        body = messages.body()
        yag = yagmail.SMTP(sender, oauth2_file='oauth2.json')
        indx = random.randint(0, len(body) - 1)
        # while(indx in og_indxs):
        #     indx = random.randint(0, len(body) - 1)
        msg = body[indx]
        # og_indxs.append(indx)
        # if len(og_indxs) == len(body):
        #     og_indxs.clear()
        yag.send(
            to=receiver,
            subject="YOU GOT A MESSAGE",
            contents=msg
        )

    # new_indxs = []
    def send_new_email(receiver, sender):
        newbody = messages.new_body()
        yag = yagmail.SMTP(sender, oauth2_file='oauth2.json')
        indx = random.randint(0, len(newbody) - 1)
        # while(indx in new_indxs):
        #     indx = random.randint(0, len(newbody) - 1)
        msg = newbody[indx]
        # new_indxs.append(indx)
        # if len(new_indxs) == len(newbody):
        #     new_indxs.clear()
        yag.send(
            to=receiver,
            subject="YOU GOT A MESSAGE",
            contents=msg
        )

    def send_new_long_email(receiver, sender):
        long_body = messages.long_body()
        yag = yagmail.SMTP(sender, oauth2_file='oauth2.json')
        indx = random.randint(0, len(long_body) - 1)
        msg = long_body[indx]
        yag.send(
            to=receiver,
            subject="YOU GOT A MESSAGE",
            contents=msg
        )

# send_email("rubysophia0716@gmail.com", "eugene2chaemin@gmail.com")