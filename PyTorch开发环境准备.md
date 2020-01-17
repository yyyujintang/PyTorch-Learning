# PyTorch开发环境准备

### 开发环境

- Python3.7+Anaconda 5.3.1
- CUDA 10.0 只能运行在NVIDIA显卡上
- Pycharm Community

### 安装NVIDIA显卡驱动

Nvidia强制默认安装在C盘（即使更改解压目录也没用）在C:/Program Files/NVIDIA GPU Computing Toolkit文件夹下

nvcc.exe 

将C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin添加到环境变量

在cmd中输入nvcc -V查看版本信息

### 安装PyTorch

在PyTorch官网选择对应的版本

![](/img/PyTorch_download.PNG)

在Anaconda Prompt中使用对应命令进行安装

### 测试是否安装成功

在Pycharm中import torch

输出torch版本和是否可以使用GPU

![](/img/test.PNG)

