import requests                                 # for api call
import datetime  
from bs4 import BeautifulSoup,SoupStrainer      # for web scrapping
import smtplib                                  # for email
from email.message import EmailMessage          # for formatting email
import random


def getHadith(hadiths):
    hadith = random.choice(hadiths)
    hadith = hadith.text
    if not hadith.startswith("same as above Hadith"):
        return hadith
    else:
        getHadith(hadiths)


today = datetime.date.today()
date_in_str = str(today)
formatted_date = datetime.datetime.strptime(date_in_str, '%Y-%m-%d').strftime('%d-%m-%Y')

# api call for timings
api_url = f'https://api.aladhan.com/v1/timingsByCity/{formatted_date}?city=karachi&country=pakistan&method=1&school=1'
response = requests.get(api_url)
response = response.json()
prayer_names = {"Fajr":0,"Sunrise":0,"Dhuhr":0,"Asr":0,"Maghrib":0,"Isha":0}

for prayer in prayer_names:
    prayer_names[prayer] = response["data"]["timings"][prayer]

timings = f"PRAYER TIMINGS FOR {today}:\nFajr: {prayer_names['Fajr']}\nDhuhr: {prayer_names['Dhuhr']}\nAsr: {prayer_names['Asr']}\nMaghrib: {prayer_names['Maghrib']}\nIsha: {prayer_names['Isha']}"


# web scrapping 

# Making a GET request
hadith_from_web = requests.get('https://sahih-bukhari.com/Pages/Bukhari_1_03.php')

# Parsing the HTML
hadith_from_web = BeautifulSoup(hadith_from_web.content, 'html.parser')
multiple_hadiths = hadith_from_web.find_all("blockquote")


todays_hadith = getHadith(multiple_hadiths)

if todays_hadith != None: 
    mail_content = f"{timings}\n\nToday's Hadith:\n{todays_hadith} "
else:
    mail_content = f"{timings}"

# Email setup

# Create a message object
msg = EmailMessage()

# Set the content of the message
msg.set_content(mail_content)

# Set the subject, from, and to headers
msg["Subject"] = "Todays prayer time"
msg["From"] = "sender's email"
msg["To"] = "receiver's email"

# Connect to the SMTP server and send the message
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("sender's email", "app password")
server.send_message(msg)
server.quit()
print("mail sent")
