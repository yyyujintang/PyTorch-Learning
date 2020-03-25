#  PyTorch100题_Day3

ID:小隐隐于野

### chapter 1 Exercises

1. Start Python to get an interactive prompt.

   - What Python version are you using: 2.x or 3.x?

   ```python
   !python -V
   ```

   运行结果

   ```python
   Python 3.7.4
   ```

   

   - Can you import torch? What version of PyTorch do you get?

   ```python
   import torch
   torch.__version__
   ```

   运行结果

   ```python
   '1.4.0'
   ```

   

   - What is the result of `torch.cuda.is_available()`? Does it match your expectation based on the hardware you’re using?

   ```python
   torch.cuda.is_available()
   ```

   运行结果

   ```python
   True
   ```

2. Start the Jupyter Notebook server.

   - What version of Python is Jupyter using?

   ```python
   import sys
   sys.version
   ```

   运行结果

   ```python
   '3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]'
   ```

   

   - Is the location of the torch library used by Jupyter the same as the one you imported from the interactive prompt?

   ```python
   torch.__config__
   ```

   运行结果

   ```python
   <module 'torch.__config__' from 'D:\\Anaconda3\\lib\\site-packages\\torch\\__config__.py'>
   ```

### chapter 2 Exercises

1. Create a tensor a from `list(range(9))`. Predict then check what the size, offset, and strides are.

   ```python
   a = list(range(9))
   a = torch.Tensor(a)
   print(a)
   print(a.size())
   print(a.storage_offset())
   print(a.stride())
   ```

   运行结果

   ```python
   tensor([0., 1., 2., 3., 4., 5., 6., 7., 8.])
   torch.Size([9])
   0
   (1,)
   ```

   

2. Create a tensor `b = a.view(3, 3)`. What is the value of `b[1,1]`?

   ```python
   b = a.view(3, 3)
   b[1, 1]
   ```

   运行结果

   ```python
   tensor(4.)
   ```

   

3. Create a tensor `c = b[1:,1:]`. Predict then check what the size, offset, and strides are.

   ```python
   c = b[1:, 1:]
   print(c)
   print(c.size())
   print(c.storage_offset())
   print(c.stride())
   ```

   运行结果

   ```python
   tensor([[4., 5.],
           [7., 8.]])
   torch.Size([2, 2])
   4
   (3, 1)
   ```

   

4. Pick a mathematical operation like cosine or square root. Can you find a corresponding function in the torch library?

   ```python
   import math
   math.sin(1)
   ```

   运行结果

   ```python
   0.8414709848078965
   ```

   ```python
   a = torch.Tensor([1])
   a.sin()
   ```

   运行结果

   ```python
   tensor([0.8415])
   ```

   

5. Is there a version of your function that operates in-place?

```python
a.sin_()
a
```

运行结果

```python
tensor([0.8415])
```

