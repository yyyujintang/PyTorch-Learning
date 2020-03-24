#  PyTorch 练习题 002

ID:小隐隐于野

11. 将一个4x4的张量resize成一个一维张量
    ```python
    import torch
    a = torch.rand(4, 4).view(16)
    a.size()
    ```
    
    运行结果
    
    ```python
    torch.Size([16])
    ```
    
    
    
12. 将一个4x4的张量resize成一个2x8的张量
    ```python
    a = torch.rand(4, 4).view((2,-1))
    a.size()
    ```
    
    运行结果
    
    ```python
    torch.Size([2, 8])
    ```
    
    
    
13. 从张量中取出数字
    ```python
    a = torch.rand(1)
    a.item()
    ```
    
    运行结果
    
    ```python
    0.2103900909423828
    ```
    
    
    
14. 将张量装换成numpy数组
    ```python
    a = torch.rand(4, 4)
    a = a.numpy()
    a
    ```
    
    运行结果
    
    ```python
    array([[0.8020465 , 0.6433286 , 0.8768645 , 0.11901444],
           [0.7810658 , 0.9912449 , 0.16681737, 0.16454577],
           [0.19409567, 0.08386511, 0.2835585 , 0.6073738 ],
           [0.7847471 , 0.30840635, 0.20832407, 0.18062735]], dtype=float32)
    ```
    
    
    
15. 将张量+1，并观察上题中numpy数组的变化
    ```python
    a = a + 1
    a
    ```
    
    运行结果
    
    ```python
    array([[1.8020465, 1.6433287, 1.8768644, 1.1190145],
           [1.7810658, 1.9912449, 1.1668174, 1.1645458],
           [1.1940956, 1.0838652, 1.2835585, 1.6073737],
           [1.7847471, 1.3084064, 1.2083241, 1.1806273]], dtype=float32)
    ```
    
    
    
16. 从numpy数组创建张量
    ```python
    import numpy as np
    a = np.ones([4, 4])
    b = torch.tensor(a)
    b
    ```
    
    运行结果
    
    ```python
    tensor([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]], dtype=torch.float64)
    ```
    
    
    
17. 将numpy数组+1并观察上题中张量的变化
    ```python
    a += 1
    print(a)
    print(b)
    ```
    
    运行结果
    
    ```python
    [[2. 2. 2. 2.]
     [2. 2. 2. 2.]
     [2. 2. 2. 2.]
     [2. 2. 2. 2.]]
    tensor([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]], dtype=torch.float64)
    ```
    
    
    
18. 新建一个张量，并设置requires_grad=True
    ```python
    x = torch.rand(4, 4, requires_grad=True)
    x
    ```
    
    运行结果
    
    ```python
    tensor([[0.9211, 0.6011, 0.3496, 0.5043],
            [0.0785, 0.2188, 0.9145, 0.3624],
            [0.2995, 0.6557, 0.7666, 0.6992],
            [0.9952, 0.6867, 0.9104, 0.0115]], requires_grad=True)
    ```
    
    
    
19. 对张量进行任意操作（y = x + 2）
    ```python
    y = x + 2
    y
    ```
    
    运行结果
    
    ```python
    tensor([[2.9211, 2.6011, 2.3496, 2.5043],
            [2.0785, 2.2188, 2.9145, 2.3624],
            [2.2995, 2.6557, 2.7666, 2.6992],
            [2.9952, 2.6867, 2.9104, 2.0115]], grad_fn=<AddBackward0>)
    ```
    
    
    
20. 再对y进行任意操作
    ```python
    out = y * 2
    ```
    
21. 对out进行反向传播
    ```python
    out.backward(torch.ones_like(out))
    ```
    
22. 打印梯度d(out)/dx
    ```python
    x.grad
    ```
    
    运行结果
    
    ```python
    tensor([[5., 5., 5., 5.],
            [5., 5., 5., 5.],
            [5., 5., 5., 5.],
            [5., 5., 5., 5.]])
    ```
    
    
    
23. 创建一个结果为矢量的计算过程（y=x*2^n）
    ```python
    x = torch.rand(3, requires_grad=True)
    n = 10
    y = x * 2 ** n
    y
    ```
    
    运行结果
    
    ```python
    tensor([492.7599, 348.5622, 485.4855], grad_fn=<MulBackward0>)
    ```
    
    
    
24. 计算v = [0.1, 1.0, 0.0001]处的梯度
    ```python
    v = torch.tensor([0.1, 1.0, 0.0001])
    y.backward(v)
    print(x.grad)
    ```
    
    运行结果
    
    ```python
    tensor([1.0240e+02, 1.0240e+03, 1.0240e-01])
    ```
    
    
    
25. 关闭梯度的功能
    ```python
    x = torch.rand([1], requires_grad=True)
    with torch.no_grad():
        y = x * 2
    y.requires_grad
    ```
    
    运行结果
    
    ```python
    False
    ```
    
    

