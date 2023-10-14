# !/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_List=[14,15,18,23,24,25,8,7]
GPIO.setup(LED_List,GPIO.OUT,initial=GPIO.HIGH)
tt=0.1
print("start of blinking.......")
try:
    while True:
        #从左往右依次点亮
        for va in LED_List:
            GPIO.output(va,GPIO.LOW)
            time.sleep(tt)
        #从左往右依次熄灭
        for va in LED_List:
            GPIO.output(va,GPIO.HIGH)
            time.sleep(tt)
        #从右往左依次点亮
        for va in reversed(LED_List):
            GPIO.output(va,GPIO.LOW)
            time.sleep(tt)
        #从右往左依次熄灭
        for va in reversed(LED_List):
            GPIO.output(va,GPIO.HIGH)
            time.sleep(tt)
        half_len=len(LED_List)//2
        length=len(LED_List)

        #两边向中间点亮
        for it in range(half_len):
            GPIO.output(LED_List[it],GPIO.LOW)
            GPIO.output(LED_List[length-it-1],GPIO.LOW)
            time.sleep(tt)
        #两边向中间熄灭
        for it in range(half_len):
            GPIO.output(LED_List[it],GPIO.HIGH)
            GPIO.output(LED_List[length-it-1],GPIO.HIGH)
            time.sleep(tt)

        #两边向中间点亮
        for it in reversed(range(half_len)):
            GPIO.output(LED_List[it],GPIO.LOW)
            GPIO.output(LED_List[length-it-1],GPIO.LOW)
            time.sleep(tt)
        #两边向中间熄灭
        for it in reversed(range(half_len)):
            GPIO.output(LED_List[it],GPIO.HIGH)
            GPIO.output(LED_List[length-it-1],GPIO.HIGH)
            time.sleep(tt)
except:
    print("except")
GPIO.cleanup()
print("END of blinking")