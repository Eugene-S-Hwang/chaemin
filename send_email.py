import yagmail
import random

receiver = "rubysophia0716@gmail.com"

yag = yagmail.SMTP('eugene2chaemin@gmail.com', oauth2_file='~/Work/oauth2.json')

def send_email():

    body = ["I love you so much!", "You are doing great. Keep going, I am right next to you.", "You are so so pretty :D", "You're the best and you make me feel so happy. I feel so loved when I'm with you",
            "If I'm not with you, I miss you.", "I can trust you with my life, my love. I can trust you with everything."]

    yag.send(
        to=receiver,
        subject="test",
        contents=body[random.randint(0, len(body) - 1)]
    )