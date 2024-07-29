import yagmail
import streamlit as st
import random
import os

body = ["I love you so much!", "You are doing great. Keep going, I am right next to you.", "You are so so pretty :D", "You're the best and you make me feel so happy. I feel so loved when I'm with you",
            "If I'm not with you, I miss you.", "I can trust you with my life, my love. I can trust you with everything.", "the way you go up and down while tugging my sleeves when you see something cute is my favorite weird habit of yours.", 
            "I love your nose and your body. I know you're insecure about them but I love them", "Before you came into my life, I didn't know I needed your sweetness and the love that you give me.", "Your beauty caught me off guard the moment I first saw you.",
            "사랑해! 사랑해요! 사랑합니다!", "I can never forget the moment you told you liked me.", "I admire your determination and how you always try to improve yourself", 
            "YOURE SO PRETYTYTYTY AND CUTEEEETKLESJLKJES!!!", "I love your pouts so much!", "You're making me better at time management. Well, I think you are. But you definitely help me!", "I love answering your questions. You can never ever ask too much to the point I say stop. I love it so much!",
            "I love that I'm stuck with you. Sometimes I daydream about us in our home in a couch or bed just cuddling while watching a movie.", "I'm always going to be by my girlfriend's side and I'm always going to help you and support you!", 
            "You are my cute precious girl.", "I sometimes think I'm so lucky that my first crush loves me back.", "I love pinching your cheeks and playing around with them. They're so cuteeee!", "The way you treat me is so different from everyone. It just pulled me in to you so much faster than I expected.",
            "Press this link :) --> https://docs.google.com/document/d/1SoDOTAQRlWuL9NBBWDMRc2cXvHtoqW3SPRZ8wDURG8Q/edit", "It's also the first time I've ever been attached to someone. And I want to keep it as the only time. My first and only lover.",
            "I fall more in love with you every day.", "Chaemin, I promise that I'll always tell you all the stories in the world and that I'll always be falling for you.", 
            "I want my future to be you Chaemin. I don't want that to change at all.", "I love the way you love me and care for me.", "I can't get enough of you. I want to hold your hand forever."]

def send_email(receiver, sender):

    yag = yagmail.SMTP(sender, oauth2_file='oauth2.json')
    yag.send(
        to=receiver,
        subject="test",
        contents=body[random.randint(0, len(body) - 1)]
    )