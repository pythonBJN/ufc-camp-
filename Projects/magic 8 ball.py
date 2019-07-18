# guessing game

#beckett Nikitas

from gpiozero import Button
from time import sleep
l=Button(4)
r=Button(17)


print(" say your question aloud and click a button")
while True:     
    if r.is_pressed:
        print("the outcome looks good")
        break
    if l.is_pressed:
        print("the outcome looks bad")
        break
sleep(2)
print(" say your question aloud and click a button")
while True:
    if  l.is_pressed:
        print(" yes")
        break
    if r.is_pressed:
        print(" no")
        break
sleep(2)
print(" say your question aloud and click a button")
while True:
    if r. is_pressed:
        print(" it is not likely")
        break
    if l.is_pressed:
        print(" it is likely")
        break
sleep(2)
print(" say your question aloud and click a button")
while True:
    if l.is_pressed:
        print("no Way!")
        break
        if r.is_pressed:
            print(" yessssssssssss!")
            break
sleep(2)
print(" say your question aloud and click a button")
while True:
    if r.is_pressed:
        print("it will happen!")
        break
    if l.is_pressed:
        print("it will not happen")
        break
slepp(2)
print(" say your question aloud and click a button")
while True:
    if r.is_pressed:
        print("im sorry what did you say!")
        break
    if l.is_pressed:
        print("please say that again please")
        break
              
wait(5)
              
print("thank you for asking THE BEST THE GLORIUS MAGIC 8888888 BALLLLLL!!!!!!!!! please ask again sooooon!")