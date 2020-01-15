# Day1PyTorch历史与特点

### PyTorch历史

2002年发布Torch

2016年发布PyTorch 0.1

2018年12月发布1.0,基于CAFFE2

Tensorflow目前稳居第一，但PyTorch热度增长速度很快

### 动态图和静态图的区别

动态图：eg基于四个变量，做矩阵乘法加法运算，激活函数，计算图与代码同时进行

静态图：eg.tensorflow。一次成型，自建命名体系，用Python写的时候非常麻烦，tensorflow2.0能支持动态图优先

### 深度学习库能做什么

- GPU加速

- 自动求导：深度学习是导数编程
- 常用网络层API

Tensor运算

- Torch.add
- Torch.mul
- Torch.matmual矩阵乘法
- Torch.view展开
- Torch.expand扩展
- Torch.cat

神经网络

- Nn.Linear全连接层
- Nn.ReLU激活函数
- Nn.Conv2d二维的卷积操作
- Nn.Softmax
- Nn.Sigmoid
- Nn.CrossEntropyLoss