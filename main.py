import smtplib
import random
from email.message import EmailMessage


places = ["Airplane", "Bank", "Beach", "Broadway Theater", "Casino", "Cathedral", "Circus Tent", "Corporate Party", "Navy Army", "Day Spa", "Embassy", "Hospital", "Hotel", "Military Base", "Movie Studio", "Ocean Liner", "Passenger Train", "Pirate Ship", "Polar Station", "Police Station", "Restaurant", "School", "Service Station", "Space Station", "Submarine", "Supermarket", "University", "Amusement Park", "Art Museum", "Candy Factory", "Cemetery", "Coal Mine", "Construction Site", "Game Center", "Gas Station", "Harbor Docks", "Ice Hockey Stadium", "Jail", "Library", "Office", "Race Track", "Retirement Home", "Rock Concert", "Sightseeing Bus", "Subway", "The U.N.", "Vineyard", "Wedding", "Zoo", "Jungle"]
places_fa = ["هواپیما", "بانک", "ساحل", "تئاتر شهر", "کازینو", "مسجد", "چادر سیرک", "مهمانی شرکت", "ارتش دریایی", "سالن ماساژ", "سفارت", "بیمارستان", "هتل", "پایگاه نظامی", "استودیو فیلمبرداری", "کشتی باربری", "قطار مسافرتی", "کشتی دزدان دریایی", "ایسنگاه قطبی", "ایستگاه پلیس", "رستوران", "مدرسه", "تعمیرگاه", "ایستگاه فضایی", "زیر دریایی", "سوپرمارکت", "دانشگاه", "شهر بازی", "موزه ی هنر", "کارخونه ی شکلات سازی", "قبرستون", "معدن ذغال سنگ", "محوطه ی ساخت و ساز", "گیم نت", "پمپ بنزین", "اسکله", "استادیوم هاکی روی یخ", "زندان", "کتابخونه", "دفتر کار", "پیست مسابقه", "خانه ی سالمندان", "کنسرت راک", "اتوبوس گشت و گذار", "مترو", "سازمان ملل متحد", "باغ انگور", "عروسی", "باغ وحش", "جنگل"]

# Players Email
emails = []

mail = "aryaspygamemail@gmail.com"
token = "hrgxmjsaqunuqxfk"


spy = emails[random.randint(1, len(emails)-1)]
place = random.randint(0,48)

player_text = places[place] + " | " + places_fa[place]
spy_text = "You are spy | شما جاسوس هستید"


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(mail, token)

for i in emails:
    msg = EmailMessage()
    msg['Subject'] = 'Spy Game'
    msg['From'] = mail
    msg['To'] = i
    if i == spy:
        msg.set_content(spy_text)
    else:
        msg.set_content(player_text)

    s.send_message(msg)

s.quit()


print("Sent")
