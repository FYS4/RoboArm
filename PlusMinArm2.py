from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
button1=16
button2=12
button3=22
button4=18
servo1=7
servo2=11
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(button4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)
pwm1=GPIO.PWM(servo1,50)
pwm2=GPIO.PWM(servo2,50)
pwm1.start(7.5)
pwm2.start(7.5)
place=7.5
place2=7.5
while(1):
        if GPIO.input(button1)==0:
                print "Button 1 was Pressed"
                place=place-0.25
                if place<2.5:
                        place=2.5
                        print "minimum"
                pwm1.ChangeDutyCycle(place)
                sleep(0.1)
                print "Je plaats is",place
        if GPIO.input(button2)==0:
                print "Button 2 was Pressed"
                place=place+0.25
                if place>12.5:
                        place=12.5
                        print "maximum"
                pwm1.ChangeDutyCycle(place)
                sleep(0.1)
                print "Je plaats is",place
	if GPIO.input(button3)==0:
                print "Button 3 was Pressed"
                place2=place2-0.25
                if place2<2.5:
                        place2=2.5
                        print "minimum"
                pwm2.ChangeDutyCycle(place2)
                sleep(0.1)
                print "Je plaats is",place2
        if GPIO.input(button4)==0:
                print "Button 4 was Pressed"
                place2=place2+0.25
                if place2>12.5:
                        place2=12.5
                        print "maximum"
                pwm2.ChangeDutyCycle(place2)
                sleep(0.1)
                print "Je plaats is",place2

