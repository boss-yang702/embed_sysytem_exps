import RPi.GPIO as GPIO
import time
import threading 
import tkinter as tk



#定义GPIO引脚,数码管引脚
SCLK = 13
RCLK = 19
DIO = 26
LED_PINS = [13,19,26]
GPIO.setmode(GPIO.BCM) #设置引脚编号为BCM编号方式


#超声波模块引脚
TRIG=3
ECHO=4
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
for led_pin in LED_PINS: #将这些GPIO引脚设置为输出
    GPIO.setup(led_pin,GPIO.OUT)


LED_Library = [0xC0, 0xF9, 0xA4,0xB0,0x99,0x92,0x82,
               0xF8,0x80,0x90,0x8C,0xBF,0xC6,0xA1,0x86,0x8E,0xbf,0x02] #定义字模


'''
* 函数名称：Show(i_data)
* 功能：将i_data表示的数值，显示在4位数码管做上。
* 参数含义：
        i_data：要显示在数码管上的数值
'''
def Show(i_data):

    #提取i_data数值的每一位上的值
    flag=0
    if i_data<0:
        i_data=-i_data
        flag=1
    while i_data > 10000:
        i_data = i_data - 10000 #将数值限制在10000以下
    count=sum(str(int(i_data)))#整数部分的数量
    i_data=round(i_data,4-count)#限制在4位数
    num_list=list(str(i_data))

    if(i_data >= 1000):
        i_show1 = i_data//1000 #提取千位的值，存在i_show1中
        i_data = i_data - i_show1 * 1000 #减去千位
    else:
        i_show1 = 0
    if(i_data >= 100): #提取百位值，存在i_show2中
        i_show2 = i_data//100 #减去百位
        i_data -= 100 * i_show2
    else:
        i_show2 = 0
    if(i_data >= 10):
        i_show3 = i_data//10 #提取十位值，存在i_show3中
        i_data -= 10*i_show3 #减去十位
    else:
        i_show3 = 0
    i_show4 = i_data #提取个位值，存在i_show4中
    if flag:#如果是负数
        LED4_Display(16,0x08)
    else:
        LED4_Display(i_show1,0x08) #将千位值写入4位数码管模块的从左往右的第一位
    LED4_Display(i_show2,0x04) #将百位值写入4位数码管模块的从左往右的第二位
    LED4_Display(i_show3,0x02) #将十位值写入4位数码管模块的从左往右的第三位
    LED4_Display(i_show4,0x01) #将个位值写入4位数码管模块的从左往右的第四位

    

'''
* 函数名称：LED4_Display(i_index,hx_location)
* 功能：将i_index数字对应的数模，输入到4位数码管的hx_location个位置上显示出来。
* 参数含义：
        i_index：在该位要显示的数字
        hx_location: 表示4位数码管的某一位
'''
def LED4_Display(i_index,hx_location):
    LED_OUT(LED_Library[i_index]) #将要显示的字模型，输入到指定的4位数码管上
    LED_OUT(hx_location) #将位地址，输入到指定的4位数码管上
    GPIO.output(RCLK,GPIO.LOW) #字模和地址都通过DIO接口输出后，第一个4位数码管的接收时钟RCLK发出一个跳变信号，表示输出完成
    GPIO.output(RCLK,GPIO.HIGH) #即先低电平，再高电平


'''
* 函数名称：LED_OUT(X)
* 功能：将数据X输入到4位数码管模块上
* 参数含义：
        X: 一个字节的数据X，可以是字模数据，也可以是地址数据
''' 
def LED_OUT(X):
    for i in range(0,8): #一个字节是八位，循环8次将每一位数据通过DIO口输出到显示模块
        if(X&0x80): #如果X最高位是1
            GPIO.output(DIO,GPIO.HIGH) #则给高电平信号
        else:
            GPIO.output(DIO,GPIO.LOW) #低电平
        GPIO.output(SCLK,GPIO.LOW) #每一位数据输出后，都要给串行时钟一个跳变信号，（先低电平，后高电平）
        GPIO.output(SCLK,GPIO.HIGH)
        X<<=1 #X数据向左移一位，即准备读取下一位的数据


'''
* 函数名称：GPIO_init()
* 功能：初始化GPIO设置，如设置GPIO编号方式、设置引脚模式、注册中断事件、绑定中断响应函数
* 参数含义：
''' 
def GPIO_init():
    GPIO.setmode(GPIO.BCM) #设置GPIO编号方式
    #设置KEY1、2、3为输入模式、上拉模式
    GPIO.setup(KEY1, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(KEY2, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(KEY3, GPIO.IN, GPIO.PUD_UP)
    #给三个引脚注册中断事件，指定下降沿，读取信号延迟事件为200毫秒
    GPIO.add_event_detect(KEY1, GPIO.FALLING, bouncetime = 200)
    GPIO.add_event_detect(KEY2, GPIO.FALLING, bouncetime = 200)
    GPIO.add_event_detect(KEY3, GPIO.FALLING, bouncetime = 200)
    #给三个引脚绑定中断响应函数
    GPIO.add_event_callback(KEY1,callback = key_callback)
    GPIO.add_event_callback(KEY2,callback = key_callback)
    GPIO.add_event_callback(KEY3,callback = key_callback)

'''
    获取距离的函数
'''
def checkdist(): #检测距离的子函数
    GPIO.output(TRIG,GPIO.HIGH) #超声波模块的读取时序为给定一定时间的高电平，然后检测输出引脚的电平跳变并计时，根据时间计算距离
    time.sleep(0.000015) #15us高电平
    GPIO.output(TRIG,GPIO.LOW) 
    while not GPIO.input(3): #捕捉上升沿,开始计时
        pass 
    t1 = time.time() 
    while GPIO.input(3): #捕捉下降沿，结束计时
        pass 
    t2 = time.time() 
    return (t2-t1)*34000/2 #得到距离



if __name__ == "__main__":
    GPIO_init() #GPIO口初始化
    #设置五个线程：数码管显示、桌面tk窗口循环显示、三个按钮监听线程
    thread1 = threading.Thread(target = thread1_show,args = ())
    thread2 = threading.Thread(target = thread2_tk,args = ())
    thread3 = threading.Thread(target = thread3_readKey1,args = ())
    thread4 = threading.Thread(target = thread4_readKey2,args = ())
    thread5 = threading.Thread(target = thread5_readKey3,args = ())
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
