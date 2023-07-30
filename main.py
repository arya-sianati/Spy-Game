# Players Email
emails = [] 

# Number of spy/spies
spy_num = 1  














import smtplib
import random
from email.message import EmailMessage
import json
import time


with open('Games\SPY game\places.json', 'r', encoding="utf8") as f:
    data = json.load(f)

places = data["places"]
places_fa = data["places_fa"]


place = random.randint(0, len(places)-1)
spies = []

for i in range(spy_num):
    spy = emails[random.randint(0, len(emails)-1)]
    while spy in spies:
        spy = emails[random.randint(0, len(emails)-1)]
    
    spies.append(spy)


time = time.strftime("%H:%M:%S", time.localtime()) + " "

player_text = time + places[place] + " | " + places_fa[place]
spy_text = time + "You are spy | شما جاسوس هستید"


mail = "aryaspygame@gmail.com"
token = "xgkmguelbmlbizbs"


player_text = time + places[place] + " | " + places_fa[place]
def spy_text(x):
    if len(spies) > 1:
        text = time + "You are spy | شما جاسوس هستید \nYour teammate(S) | یار(ان) شما:"
        for i in spies:
                if x != i:
                    text += "\n" + i
    else:
        text = time + "You are spy | شما جاسوس هستید"

    return text


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(mail, token)

for i in emails:
    msg = EmailMessage()
    msg['Subject'] = 'Spy Game'
    msg['From'] = mail
    msg['To'] = i
    if i in spies:
        msg.set_content(spy_text(i))
    else:
        msg.set_content(player_text)


    s.send_message(msg)

s.quit()


print("Sent All")
