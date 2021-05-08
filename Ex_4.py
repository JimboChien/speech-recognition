# -*- coding: utf-8 -*-
import Ex_1,Ex_2
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
def main():
    target = Ex_1.main()
    if(target == u'開燈'):
        GPIO.output(7,1)
    if(target == u'關燈'):
        GPIO.output(7,0)

if __name__ == '__main__':
    main()

