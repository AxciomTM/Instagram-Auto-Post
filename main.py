import time
from instabot import Bot
import requests
import os

def getLink():
    link = input("Image Link: ")
    r = requests.get(link)
    with open('00.jpeg', 'wb') as f:
        f.write(r.content)
def username():
    user = input("Username: ")
    return user
def password():
    password = input("Password: ")
    return password
def share(user,password):
    bot = Bot()
    bot.login(username=username,password=password)
    time.sleep(0.2)
    date=input("Date: ")
    artist_name=input("Artist: ")
    location=input("Location: ")
    tags = "#photo #sunset #moon"
    bot.upload_photo("00.jpeg",caption=date+" "+artist_name+"\n\n"+"Location: "+location+"\n"+"\n\n"+tags)
def delete():
    os.remove("00.jpeg.REMOVE_ME")

getLink()
username = username()
password= password()
share(username,password)
delete()
