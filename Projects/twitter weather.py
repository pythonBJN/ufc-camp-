 twitter weather poster

# Beckett Nikitas
from gpiozero import Button
from time import sleep
from twython import Twython

consumer_key = 'VD9uUIdeYYaAfhiEVFL1185DZ'
consumer_secret = 'kofk91vXJkFlsqbNLh3s7GUbuTOzqd1JpNpFA9qX2mDQTR6rhG'
access_token = '1141880993487495173-g1WOpZ4yrC8dco40AhLGnouj4fqNjW'
access_token_secret = 'tyuG1Nm3VNCQrJYv3HsmslYBIysZ0ibJCNTPqYsJsuoA1'


twitter = Twython(consumer_key,consumer_secret,access_token,access_token_secret)

l = Button(4)
m = Button(22)
r = Button(17)
 

message = ""

print(" were are you? Chicago left button,Michigan middle button,california right button")
while True:
    if l.is_pressed:
        message += "In Chicago illinois, "
        break
    if m.is_pressed:
        message =+ "In Michigan,"
        break
    if r.is_pressed:
        message += " In California,"
        break
sleep(3)
print(" what season is it? left button  is summer, fall and spring is the middle button, and winter is the right button") 
while True:
    if r.is_pressed:
        message += " it is winter"
        break
    if l.is_pressed:
        message += " it is summer"
        break
    if m.is_pressed:
        message += " it is spring/fall"
sleep(3)
print("What is the temperature like? left button is hot, right button is cold, and middle button is when it is inbeetween around 40-90 degrees farenhight.")
while True,
    if r.is_pressed:
        message += " and the weather is cold"
        break
    if m.is_pressed:
        message += " and the weather is moderate"
        break
    if l.is_pressed:
      message += " and the weather is hot"
      break
sleep(3)
print("is their snow,hail,rain? right button is if their is snow,hail, or rain, and left button is if their is not any snow hail or rain, the middle button is incase their is ice on roads")
 while True:
    if r.is_pressed:
        print("left button is for hail,middle button is for rain, and right button is for snow")
        if r.is_pressed:
            print("left button is for light snow, middle button is for medium snow, and right button is for heavy snow")
            if r.is_pressed:
                message += " with heavy snow."
                break
            if m.is_pressed:
                message += " with moderate snow."
                break
            if l.is_pressed:
                message += " with light snow."
                break
        if m.is_pressed:
            print("left button is for light rain, middle button is for moderate rain, and right button is for heavy/thunderstorms")
            if l.is_pressed:
                  message += " with light rain."
                  break
            if m.is_pressed:
                  message += " with moderate rain."
                  break
            if r.is_pressed:
                  print("left button is for heavy rain, and right button is for thunder storms.")
                  if l.is_pressed:
                      message += " with heavy rain."
                      break
                  if r.is_pressed
                      message += " with thunder storms."
                      break
        if l.is_pressed:
            print(" left button is for light hail,middle  utton is for moderate hail, and right button is for heavy hail")
            if l.is_pressed:
                message += " with light hail."
                break
            if m.is_pressed:
                message += " with moderate hail."
                break
            if r.is_pressed:
                message += " with heavy hail."
                break
    if m.is_pressed:
        message += " with some ice on the roads so be careful."
        break
    if l.is_pressed:
        message "."
        break
sleep(3)
print("what is the cloud cover like? left button is for blue skys/ light cloud cover,middle button is for partly cloudy, and right button is for heavy cloud cover")
while True:
    if r.is_pressed:
        message " Also their is heavy cloud cover"
        break
    if m.is_pressed:
        message " Also the sky is partly cloudy"
        break
    if l.is_pressed:
        message " Also the sky is clear"
sleep(3)
print("what is the wind like? left button is for light wind, the middle button is for moderate wind speeds , right button is for high wind speeds")

        








twitter.update_status(status=message)
print("tweeted: %s" % message)
