from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

#variable aanmaken voor de pins op de Raspberry PI
button1=16
button2=12
button3=22
button4=18
button5=36
button6=32
servo1=7
servo2=11
servo3=13

#Variable binden aan pinnen op de Raspberry PI
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button6,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
GPIO.setup(servo3,GPIO.OUT)

#frequentie voor de servo's instellen pwm staat voor pulse-width-modulation
pwm1=GPIO.PWM(servo1,50)
pwm2=GPIO.PWM(servo2,50)
pwm3=GPIO.PWM(servo3,50)

#begin positie van servo's instellen
pwm1.start(7.5)
pwm2.start(7.5)
pwm3.start(7.5)

#varable aanmaken 
place1=7.5
place2=7.5
place3=7.5

#als knop ingedrukt is verplaats de arm als minimum is bereikt stopt de arm met bewegen
while(1):
        if GPIO.input(button1)==0:
                print "Button 1 was Pressed"
                place1=place1-0.25
                if place1<2.5:
                        place1=2.5
                        print "minimum"
                pwm1.ChangeDutyCycle(place1)
                sleep(0.1)
                print "Your place is",place1
        if GPIO.input(button2)==0:
                print "Button 2 was Pressed"
                place1=place1+0.25
                if place1>12.5:
                        place1=12.5
                        print "maximum"
                pwm1.ChangeDutyCycle(place1)
                sleep(0.1)
                print "Your place is",place1
		if GPIO.input(button3)==0:
                print "Button 3 was Pressed"
                place2=place2-0.25
                if place2<2.5:
                        place2=2.5
                        print "minimum"
                pwm2.ChangeDutyCycle(place2)
                sleep(0.1)
                print "Your place is",place2
        if GPIO.input(button4)==0:
                print "Button 4 was Pressed"
                place2=place2+0.25
                if place2>12.5:
                        place2=12.5
                        print "maximum"
                pwm2.ChangeDutyCycle(place2)
                sleep(0.1)
                print "Your place is",place2
		if GPIO.input(button5)==0:
                print "Button 5 was Pressed"
                place3=place3-0.25
                if place3<2.5:
                        place3=2.5
                        print "minimum"
                pwm3.ChangeDutyCycle(place3)
                sleep(0.1)
                print "Your place is",place3
        if GPIO.input(button6)==0:
                print "Button 6 was Pressed"
                place3=place3+0.25
                if place3>12.5:
                        place3=12.5
                        print "maximum"
                pwm3.ChangeDutyCycle(place3)
                sleep(0.1)
                print "Your place is",place3

