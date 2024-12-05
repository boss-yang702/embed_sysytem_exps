### 通过ssh连接开启I2C服务

执行如下命令进行树莓派配置

```bash
sudo raspi-config
```

![image-20231014232413915](C:\Users\Ankhron\AppData\Roaming\Typora\typora-user-images\image-20231014232413915.png)

选择第3个 Interface Options 

![image-20231014232502846](C:\Users\Ankhron\AppData\Roaming\Typora\typora-user-images\image-20231014232502846.png)

开启I2C服务

![image-20231014232531756](C:\Users\Ankhron\AppData\Roaming\Typora\typora-user-images\image-20231014232531756.png)

I2C-tool查询I2C设备

```bash
i2cdetect -y 1
```

![image-20231014232715644](C:\Users\Ankhron\AppData\Roaming\Typora\typora-user-images\image-20231014232715644.png)