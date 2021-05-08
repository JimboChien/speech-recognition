# -*- coding: utf-8 -*-
import Ex_1
import time
import jieba
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def main():
    target = Ex_1.main()
    words = jieba.lcut(target,cut_all=False)
    for word in words:
        print(word)
        if(word == u'開燈'):
            GPIO.output(7,1)
            time.sleep(1)
        if(word == u'關燈'):
            GPIO.output(7,0)
            time.sleep(1)
        if(word == u'閃爍'):
            GPIO.output(7,0)
            time.sleep(0.3)
            GPIO.output(7,1)
            time.sleep(0.3)
            GPIO.output(7,0)
            time.sleep(0.3)
            GPIO.output(7,1)
            time.sleep(0.3)
            GPIO.output(7,0)
            time.sleep(0.3)
            GPIO.output(7,1)

if __name__ == '__main__':
    main()

