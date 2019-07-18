# quiz
# author: Beckett Nikitas

from gpiozero import Button

from time import sleep


l = Button(4)
r= Button(17)


print("right Button is true left is false")
sleep(5)
print("do platypuses have a third eye")
while True:
    if r.is_pressed:
        print(" what you think that this is true you fell for ramir's joke, shame on you shame on you:(((((((((((((((((((((((((")
        break
    if l.is_pressed:
        print(" correct I am glad you didnt fall for ramir's joke :)))))")
        break

sleep(5)
print("are the nostrils are missing from the painting of ‘The Mona Lisa’?") 

while True:
    if r.is_pressed:
        print("you are incorrect, the mona lisa is not missing nostrils however the ears are debated:(")
        break
    if l.is_pressed:
        print("you are correct, the mona lisa is not missing nostrils however the ears are debated:)")
        break
sleep(5)
print("	does A golf ball has a fixed amount of dimples?") #false
 
while True:
    
    if r.is_pressed:
        print(" you are incorrect there is not a fixed number of dimples on a golf ball :(")
        break

    if l.is_pressed:
        print(" you are correct there is not a fixed number of dimples on a golf ball:)")
        break
sleep(5)
print(" Liver is offal?") #true

while True:
   
    if r.is_pressed:
        print("you are correct the liver is offal:)")
        break
    if l.is_pressed:
        print("you are incorrect the liver is offal:(")
        break
sleep(5)
print("	is Nicole Scherzinger  a member of 'Destiny's Child'?") #false: Nicole Scherzinger is a member of The Pussycat Dolls

while True:
    if r.is_pressed:
        print(" you are incorrect Nicole Scherzinger is a member of The Pussycat Dolls not Destinys child:(")
        break
    if l.is_pressed:
        print("you are correct Nicole Scherzinger is a member of The Pussycat Dolls not Destinys child:)")
        break
sleep(5)
print("	does USB stands for Universal Serial Bus?")

while True:
    if r.is_pressed:
        print(" you are correct usb stands for universal serial bus:)")
        break
    if l.is_pressed:
        print("you are incorrect USB does stand for universal serial bus:(")
        break
sleep(5)
print("True or false question: Diet Coke promises 'maximum taste, zero calories'?")
while True:
    if r.is_pressed:
        print(" False: The tagline belongs to Pepsi Max :(")
        break
    if l.is_pressed:
        print("you are correct is is False: The tagline belongs to Pepsi Max :)")
        break
sleep(5)
print("True or false question: There are 11 different types of chocolates in a box of Quality Street?")
while True:
    if r.is_pressed:
        print("sorry you are not correct the answer is False: There are twelve varieties :( ")
        
True or false question: There are 32 black squares on a chessboard?

True or false question: The second largest state in America is Texas?

True or false question: On a graph, the x-axis is vertical?

True or false question: There are 6 zeros are in a billion?

True or false question: The 8th official planet in our solar system (furthest from the Sun) is Neptune?

sleep(5)
print("thank you for playing:)")

#true: It's an abbreviation for Universal Serial Bus

