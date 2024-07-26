import yagmail
import random
import os

receiver = os.environ["CH_EMAIL"]

yag = yagmail.SMTP(os.environ["CH2EMAIL"], oauth2_file='~/Work/oauth2.json')

def send_email():

    body = ["I love you so much!", "You are doing great. Keep going, I am right next to you.", "You are so so pretty :D", "You're the best and you make me feel so happy. I feel so loved when I'm with you",
            "If I'm not with you, I miss you.", "I can trust you with my life, my love. I can trust you with everything."]

    yag.send(
        to=receiver,
        subject="test",
        contents=body[random.randint(0, len(body) - 1)]
    )