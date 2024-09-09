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
            "I want my future to be you Chaemin. I don't want that to change at all.", "I love the way you love me and care for me.", "I can't get enough of you. I want to hold your hand forever.", "I always think you're so cute and lovely and I will give it my all for this relationship <3",
            "You're like my other half.", "I'm completely in love with you. You're so pretty.", "I can't wait to marry you.", "We should go to Korea together. First thing after we graduate hehe!", "I love hugging you really tightly.", "I love sending you good morning texts and having late night calls with you.",
            "You're beautiful, you know that?", "I can completely rely on you because I trust you the most.", "You are my favorite person :)", "You're so FUCKING PRETTYYYYYY", "I hope you're doing okay right now. I always do.", "I'm always so proud of everything that you do.",
            "You're a beauty. Prettiest girl that I have ever seen in my life.", "I can't help but go crazy whenever I see you. Because you are gorgeous.", "I care about you the most.", "I'll give you the strength to keep going, whenever you need it. :)", """dear chaemin,

            it’s almost national girlfriend’s day! i’m so happy that i’m your boyfriend and  that you are my girlfriend!! i still feel so lucky that i have someone to call as my love and my precious girlfriend. you always care for me so well and you always make me so so happy. i love these late night calls that i do with you because i’m able to talk with you after a long day. i love it

            i also love when we go on dates! i want to go on trips with you in the future and i want to see the world with you. i want to eat everything with you and i want to do everything with you. because you make me so so happy. i know i might get kind of goofy with you but i also love your goofy and silly side. it’s so cute

            i think you’re the cutest girl in the world. i said this like an infinite amount of times but that’s because it think you are infinitely cute. you are the prettiest and the cutest girl that i have ever seen and i just can’t help but fall in love with you. 

            i also really like how you draw. i really love all of your artworks which is why i always ask for them. i think they look beautiful and are genuinely wonderful. i can make a whole exhibition out of them. you’re artistic talent is so respectable and i wish i could have every single artwork of yours (like a copy). you’re like a beautiful artwork. 

            i love how you always take care of me and how you’re always so happy to see me. i love the way you love me and i’m so happy that i have someone who loves me just the way i love them. i think that i am eternally lucky for that. i really do. i want to love you forever and ever. i want to marry you

            we may have our ups and downs but no matter what, i am going to talk it out with you. i want to make this relationship work forever because you are the best girlfriend that i could ever ask for in this whole world. you are the best chaemin. you really are. don’t let anyone else tell you otherwise. 

            i’m so thankful to be your boyfriend. happy national girlfriends day my precious girl. 😊""", "Press this link! -> https://docs.google.com/document/d/1G3ETX4JxVgTgUlCVqzkCtwH5AWyvpWcKbczmLL3dA_U/edit", "Press this link! -> https://docs.google.com/document/d/1zzAh7oJm-GQAEJtmMjCopJJPfhOejZBNNrYFbCTzLs0/edit",
            "Press this link! -> https://docs.google.com/document/d/1ugWkqaKxeWFxjxktXC9i25aW1r7qx__gp4OU8DNGoeM/edit", "Press this link! -> https://docs.google.com/document/d/1b7GdDfcYctpz5Xk69xVYElzsWF_3EjDg3biuZp5NuXg/edit", "You were so pretty today, yesterday, and tomorrow.", "You got so much rizz girllll!", "I'll get you everything in the world. I just really want to make you happy :).",
            "I'll protect you from anything that harms you. I promise.", "SLAYYYYYYY YOU GO GIRLBOSS!!! POP OFF! YOU GO GIRL!", "I'm always proud of you. Remember that, okay?", "My lovely girlie girl.", "HI CHAE CHAE!", "You're so cute!", "채민아, 나는 너랑 있어서 행복해!", "고마워! 나를 사랑해줘서 :)", "너는 엄청 이쁘더라!", "너는 가장 사랑스럽고 아름다운 여자야. 내가 너의 남지친구이라는게 너무 좋아!", "갗이 한국 가자!!",
            "넌 나의 여자친구이고, 나는 너의 남자친구야 :) <3", "I want to try my best for this relationship. I promise.", "You are the prettiest in this world!!!", "Tis the season to be with you!", "You a drag queen cause you drag me in :D", "I've never stopped loving you. It's a fact", "You're so cute and adorable!",
            """dear chaemin,

            i love you with all of my heart. you are the cutest girl that I have ever ever met. i say this a lot but I love how you love me and i love that i love you. I am so happy to be with you and i genuinely can’t wait to marry you.

            i also can’t wait to see your gifts. i’m not a gift person but your gifts are always so thoughtful and lovely. i always love reading your cards and letters and all the small notes that you put on the gifts. i always feel bad with the gifts because i always feel like i don’t give enough compared to how much effort you put into yours. 

            chaemin, i am so happy that you are my girlfriend. despite my flaws, you still love me and treat me the best. i’m so happy that i continue to be your boyfriend throughout all this time. i love you so so much.

            i will never in my life regret the day that i asked you out on may 16, 2022, 2:40PM. i think that that is the best decision that i have made for my life. 

            you are perfect just the way you are. i feel so lucky that you chose me as your boyfriend. me. my first ever crush accepted my love! how lucky am i for that. i am so lucky that the girl that i love treats me the same way back. 

            thank you for accepting my love chaemin. i am eternally grateful for that. i always say that i feel lucky that you accepted my love and my confessions, but it’s true. i feel so so lucky. honestly, i also feel like it’s fate. i told you about the story of my friends back in wolfram asking if i think its fate, but i really do think its fate. i couldn’t answer no even though i was supposed to according to my stance in the debate LMAO

            i’m just so happy to be your boyfriend. i hope to be yours forever. 

            From, your eternal love""", """Dear Chaemin,

            Hi my love!! You are the best girlfriend that I could ever ask for. You are the prettiest, cutest, most wonderful girl to ever be with. I am so happy to be your boyfriend. Yesterday was wonderful and I am so thankful that I was able to meet you that day. I am grateful for everything that you do for me and I am so happy that I have someone that I can trust. 

            You know, I love every single part of you. No matter how much you say you don’t like your body, that will never change how much I love you. I love your smile, your nose, your sparkling eyes, your soft skin, your bright lips, your warm body. I love it all. I can never have enough of you. 

            You are beautiful you know that? I hope you really know that. I genuinely think that you are the most beautiful girl in the whole entire world. I feel so lucky that I am your boyfriend and I will be eternally grateful. I am so happy to be loved by you and to love you. I love you, my precious girl. I love you chaemin.""", "I won't raise my voice at you, even if we fight.", "I'll always help you with math.", 
            "You are the most beautiful girl I've seen.", "I love how you play the clarinet. I wish I could hear it again", "I love your body and your skin. It's so beautiful and hot.", "I love your love of cats. KITTTIESSSSS", "I'll get you scruffy and cornia and we'll start a cat family!!", "You're my best friend and my lover.", "I feel so lucky to be with you."]

newbody = ["I want to try my best for this relationship. I promise.", "You are the prettiest in this world!!!", "Tis the season to be with you!", "You a drag queen cause you drag me in :D", "I've never stopped loving you. It's a fact", "You're so cute and adorable!",
           """dear chaemin,

i love you with all of my heart. you are the cutest girl that I have ever ever met. i say this a lot but I love how you love me and i love that i love you. I am so happy to be with you and i genuinely can’t wait to marry you.

i also can’t wait to see your gifts. i’m not a gift person but your gifts are always so thoughtful and lovely. i always love reading your cards and letters and all the small notes that you put on the gifts. i always feel bad with the gifts because i always feel like i don’t give enough compared to how much effort you put into yours. 

chaemin, i am so happy that you are my girlfriend. despite my flaws, you still love me and treat me the best. i’m so happy that i continue to be your boyfriend throughout all this time. i love you so so much.

i will never in my life regret the day that i asked you out on may 16, 2022, 2:40PM. i think that that is the best decision that i have made for my life. 

you are perfect just the way you are. i feel so lucky that you chose me as your boyfriend. me. my first ever crush accepted my love! how lucky am i for that. i am so lucky that the girl that i love treats me the same way back. 

thank you for accepting my love chaemin. i am eternally grateful for that. i always say that i feel lucky that you accepted my love and my confessions, but it’s true. i feel so so lucky. honestly, i also feel like it’s fate. i told you about the story of my friends back in wolfram asking if i think its fate, but i really do think its fate. i couldn’t answer no even though i was supposed to according to my stance in the debate LMAO

i’m just so happy to be your boyfriend. i hope to be yours forever. 

From, your eternal love""", """Dear Chaemin,

Hi my love!! You are the best girlfriend that I could ever ask for. You are the prettiest, cutest, most wonderful girl to ever be with. I am so happy to be your boyfriend. Yesterday was wonderful and I am so thankful that I was able to meet you that day. I am grateful for everything that you do for me and I am so happy that I have someone that I can trust. 

You know, I love every single part of you. No matter how much you say you don’t like your body, that will never change how much I love you. I love your smile, your nose, your sparkling eyes, your soft skin, your bright lips, your warm body. I love it all. I can never have enough of you. 

You are beautiful you know that? I hope you really know that. I genuinely think that you are the most beautiful girl in the whole entire world. I feel so lucky that I am your boyfriend and I will be eternally grateful. I am so happy to be loved by you and to love you. I love you, my precious girl. I love you chaemin.""", "I won't raise my voice at you, even if we fight.", "I'll always help you with math.", 
"You are the most beautiful girl I've seen.", "I love how you play the clarinet. I wish I could hear it again", "I love your body and your skin. It's so beautiful and hot.", "I love your love of cats. KITTTIESSSSS", "I'll get you scruffy and cornia and we'll start a cat family!!", "You're my best friend and my lover.", "I feel so lucky to be with you."]


def send_email(receiver, sender):

    yag = yagmail.SMTP(sender, oauth2_file='oauth2.json')
    msg = body[random.randint(0, len(body) - 1)]
    yag.send(
        to=receiver,
        subject="YOU GOT A MESSAGE",
        contents=msg
    )

def send_new_email(receiver, sender):
    yag = yagmail.SMTP(sender, oauth2_file='oauth2.json')
    msg = newbody[random.randint(0, len(newbody) - 1)]
    yag.send(
        to=receiver,
        subject="YOU GOT A MESSAGE",
        contents=msg
    )

# send_email("rubysophia0716@gmail.com", "euge ne2chaemin@gmail.com")