# !/usr/bin/python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
import smbus
import threading
GPIO.setmode(GPIO.BCM)

#定义引脚
SCLK1=25
RCLK1=8
DIO1=7

SCLK2=5
RCLK2=4
DIO2=17


GPIO.setwarnings(False)#不报警告
GPIO.setup([SCLK1,SCLK2,RCLK1,RCLK2,DIO1,DIO2] ,GPIO.OUT)#设置模式

#数码管显示数字定义
LED_Library=[0xC0,0xF9,0xA4,0xB0,0x99,0x92,0x82,0xf8,0x80,0x90,
             0xBF,0xC6,0xA1,0x86,0x8E,0xbf]


#输入显示的数据和显示数字的led引脚列表
def Show(i_data,RCLK,SCLK,DIO):
    i_show4=i_data % 10
    i_data=i_data // 10
    i_show3=i_data % 10
    i_data=i_data // 10
    i_show2=i_data % 10
    i_data=i_data // 10
    i_show1=i_data % 10
    i_data=i_data // 10
    LED4_Display(i_show1,0x08,RCLK,SCLK,DIO)#显示第一位
    LED4_Display(i_show2,0x04,RCLK,SCLK,DIO)#显示第二位
    LED4_Display(i_show3,0x02,RCLK,SCLK,DIO)#显示第三位
    LED4_Display(i_show4,0x01,RCLK,SCLK,DIO)#显示第四位

# 显示一个数字在其中一个数码管上，以及显示的位置
def LED4_Display(i_index,hx_location,RCLK,SCLK,DIO):
    LED_OUT(LED_Library[i_index],SCLK,DIO)#输入显示的数码位
    LED_OUT(hx_location,SCLK,DIO)
    GPIO.output(RCLK,GPIO.LOW)#先低再高脉冲
    GPIO.output(RCLK,GPIO.HIGH)

# 字模和位地址都从DIO口输入，然后通过SCLK和RCLK对数据进行锁存
def LED_OUT(X,SCLK,DIO):
    for i in range(0,8):
        if(X&0x80):#从高到底依次检查位数高输出1，低输出0
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
        #读取3个模拟值
        bus.write_byte(address,A1)
        value1=bus.read_byte(address)
        bus.write_byte(address,A2)
        value2=bus.read_byte(address)
        bus.write_byte(address,A3)
        value3=bus.read_byte(address)

def Display_data():
  while True:
    disp1=value2
    disp2=value3
    for i in range(1000):
        #显示模拟值
        Show(disp1,RCLK1,SCLK1,DIO1)
        Show(disp2,RCLK2,SCLK2,DIO2)
    label1.config(text=value1)
    label2.config(text=value2)
    label3.config(text=value3)


import tkinter as tk
import threading
# 创建一个400x400像素的窗口
window = tk.Tk()
window.geometry("400x400")

#创建3个标签并将它们放置在窗口中央
label1 = tk.Label(window, text="0",font=("Arial",16))
label1.place(relx=0.5, rely=0.33, anchor="center")

label2 = tk.Label(window, text="0",font=("Arial",16))
label2.place(relx=0.5, rely=0.5, anchor="center")

label3 = tk.Label(window, text="0",font=("Arial",16))
label3.place(relx=0.5, rely=0.67, anchor="center")

threadd1=threading.Thread(target=Read_data,args=())
threadd1.start()
threadd2=threading.Thread(target=Display_data,args=())
threadd2.start()
# 运行窗口
window.mainloop()
RPi.GPIO.cleanup()
