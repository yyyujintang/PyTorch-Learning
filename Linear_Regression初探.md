# Linear Regression初探

eg loss=x^2*sin(x)

高中求极值：求导数，找导数为0 点，判断是否为极大值或极小值

梯度下降法：X'=X-δX（Y在X处的导数） 每一步迭代

### Linear Regression实现

learning rate学习速率X'=X-lr*δX(lr is short for learning rate)

### 求解Linear Regression

#### comput_error

![comput_error](comput_error.PNG)

#### step_gradient

![step_gradient](step_gradient.PNG)

#### gradient_descent_runner

![gradient_descent_runner](gradient_descent_runner.PNG)

#### run

![run](run.PNG)

#### 输出

![LR_output](LR_output.PNG)