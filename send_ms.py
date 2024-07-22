# import os
# from twilio.rest import Client

# # def send_msg():
# account_sid = os.environ["TWILIO_SID"]
# auth_token = os.environ["TWILIO_TOKEN"]
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     body="Testing Testing",
#     from_=os.environ["TWILIO_CH_NUM"],
#     # to=os.environ["CH_NUM"],
#     to="+12019129586"
# )

# print(message.body)