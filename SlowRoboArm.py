import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

p = GPIO.PWM(7,46)
p.start(2.5)

try:
        while True:
                p.ChangeDutyCycle(2.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(3.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(3.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(4.0)
                time.sleep(0.1)
		p.ChangeDutyCycle(4.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(5.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(5.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(6.0)
                time.sleep(0.1)
		p.ChangeDutyCycle(6.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(7.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(7.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(8.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(8.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(9.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(9.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(10.0)
                time.sleep(0.1)
		p.ChangeDutyCycle(10.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(11.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(11.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(12.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(12.5)
                time.sleep(0.1)
#		p.ChangeDutyCycle(13.0)
#               time.sleep(0.1)
#               p.ChangeDutyCycle(12.5)
#               time.sleep(0.1)
                p.ChangeDutyCycle(12.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(11.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(11.0)
                time.sleep(0.1)
		p.ChangeDutyCycle(10.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(10.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(9.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(9.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(8.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(8.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(7.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(7.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(6.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(6.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(5.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(5.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(4.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(4.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(3.5)
                time.sleep(0.1)
                p.ChangeDutyCycle(3.0)
                time.sleep(0.1)
                p.ChangeDutyCycle(2.5)
                time.sleep(0.1)



except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

