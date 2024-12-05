import tkinter as tk

def update_values():
    # 这个函数用于更新显示的分压值
    thermal_resistor = thermal_resistor_scale.get()
    light_resistor = light_resistor_scale.get()
    variable_resistor = variable_resistor_scale.get()
    
    # 在Label上更新分压值
    thermal_resistor_label.config(text=f"热敏电阻：{thermal_resistor}")
    light_resistor_label.config(text=f"光敏电阻：{light_resistor}")
    variable_resistor_label.config(text=f"可变电阻：{variable_resistor}")

# 创建主窗口
window = tk.Tk()
window.title("传感器数据监测")

# 创建热敏电阻滑块
thermal_resistor_label = tk.Label(window, text="热敏电阻：")
thermal_resistor_label.pack()
thermal_resistor_scale = tk.Scale(window, from_=0, to=100, orient="horizontal")
thermal_resistor_scale.pack()

# 创建光敏电阻滑块
light_resistor_label = tk.Label(window, text="光敏电阻：")
light_resistor_label.pack()
light_resistor_scale = tk.Scale(window, from_=0, to=100, orient="horizontal")
light_resistor_scale.pack()

# 创建可变电阻滑块
variable_resistor_label = tk.Label(window, text="可变电阻：")
variable_resistor_label.pack()
variable_resistor_scale = tk.Scale(window, from_=0, to=100, orient="horizontal")
variable_resistor_scale.pack()

# 创建一个更新按钮
update_button = tk.Button(window, text="更新数值", command=update_values)
update_button.pack()

# 运行Tkinter主循环
window.mainloop()