# !/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import smbus
import threading
GPIO.setmode(GPIO.BCM)

SCLK1=1
RCLK1=4
DIO1=17

SCLK2=1
RCLK2=4
DIO2=17

LED1_PINS =[1,4,17]
LED2_PINS =[1,4,17]
GPIO.setwarnings(False)
GPIO.setup(LED1_PINS,LED2_PINS ,GPIO.OUT)

LED_Library=[0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xf8,0x80,0x90,
             0xBF,0xC6,0xA1,0x86,0x8E,0xbf]

def Show(i_data,LED):
    i_show4=i_data % 10
    i_data=i_data // 10
    i_show3=i_data % 10
    i_data=i_data // 10
    i_show2=i_data % 10
    i_data=i_data // 10
    i_show1=i_data % 10
    i_data=i_data // 10
    LED4_Display(i_show1,0x08)
    LED4_Display(i_show2,0x04)
    LED4_Display(i_show3,0x02)
    LED4_Display(i_show4,0x01)

def LED4_Display(i_index,hx_location):
    LED_OUT(LED_Library[i_index])
    LED_OUT(hx_location)
    GPIO.output(RCLK,GPIO.LOW)
    GPIO.output(RCLK,GPIO.HIGH)


def LED_OUT(X):
    for i in range(0,8):
        if(X&0x80):
            GPIO.output(DIO,GPIO.HIGH)
        else:
            GPIO.output(DIO,GPIO.LOW)
        GPIO.output(SCLK,GPIO.LOW)
        GPIO.output(SCLK,GPIO.HIGH)
        X <<=1


address = 0x48
A0=0x40
A1=0x41
A2=0x42
A3=0x43
        
bus=smbus.SMBus(1)
value1=0
value2=0
value3=0
def Read_data():
    global value1,value2,value3
    while True:
        bus.write_byte(address,A1)
        value1=bus.read_byte(address)
        bus.write_byte(address,A2)
        value2=bus.read_byte(address)
        bus.write_byte(address,A2)
        value3=bus.read_byte(address)

def Display_data():
  while True:
    for i in range(1000):
        Show(value1,LED1)
        Show(value2,LED2)