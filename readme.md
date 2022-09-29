适用操作系统 win10 64位
### Python 版本
python 3.6兼容多个版本
### 摄像头配置
[DEFAULT]
config.py文件进行录像机海康SDK路径设置
    #海康sdk的库文件在工程lib目录下
    SDKPath = 'F:/hk/pyhikvision-master/lib/win64/'
    # SDKPath = 'D:/java/HKCamera/'
    User = 'admin'
    Password = 'jxlgust123'
    Port = 8000
    IP = '172.26.20.51'
    Plat = '1'  # 0-Linux，1-windows
    Suffix = '.dll'

### example启动方式
使用pycharm打开工程
需安装opencv
运行example下instant_preview.py


### 维护及联系：

1. QQ群（52185025）可指导使用



