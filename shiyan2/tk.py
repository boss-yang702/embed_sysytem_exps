import tkinter as tk

# # 创建一个400x400像素的窗口
# window = tk.Tk()
# window.geometry("400x400")

# # 创建3个标签并将它们放置在窗口中央
# label1 = tk.Label(window, text="Value 1: <value from Raspberry Pi>")
# label1.place(relx=0.5, rely=0.33, anchor="center")
# label2 = tk.Label(window, text="Value 2: <value from Raspberry Pi>")
# label2.place(relx=0.5, rely=0.5, anchor="center")
# label3 = tk.Label(window, text="Value 3: <value from Raspberry Pi>")
# label3.place(relx=0.5, rely=0.67, anchor="center")
# label1.config(font=16)
# label1.config(text=4577)
# # 运行窗口
# window.mainloop()
top = ttk.Window(themename='superhero')
top.title('实验四超声波测距')  # 设置界面标题
top.geometry('400x80+400+200')  # 设置界面大小与位置
label1 = ttk.Label(top, text="distance：", bootstyle="warning")
text1 = ttk.Text(top, width=10, height=1)
label1.place(x=65, y=22)
text1.place(x=140, y=16)
def updatedata():
    text1.delete(1.0, "end")
    text1.insert("insert", distance)
    top.after(100, updatedata)  # 在给定时间后调用函数一次
    top.update()
top.after(100, updatedata)  # 0.1s更新一次数据
# 进入消息循环
top.mainloop()