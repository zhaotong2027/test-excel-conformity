import numpy as np
import time
import matplotlib.pyplot as plt

"""
01、演示两种线性
"""
# w1 = -0.93
# w2 = -0.77
# b = 0.12

# x = np.linspace(-6, 7, 20)
# y = -w1/w2 * x - b/w2  # 高纬映射？ X
# plt.plot(x, y)
# plt.axis((-6, 6, -6, 6))
# plt.xticks(np.arange(-6, 7))
# plt.show()

# x = np.linspace(-10, 10, 100)
# y = 1 / (1 + np.exp(-x))
# plt.plot(x, y)
# plt.show()

# 梯度下降
# 导数求导图解：导数的链式法则
# 结果线性回归和逻辑回归不调包，自己实现


"""
02、线性效率演示
"""
# a = np.random.rand(100000)
# b = np.random.rand(100000)

# c = 0
# start = time.time()
# for i in range(100000):
#     c += a[i]*b[i]
# end = time.time()
# print("计算所用时间%s" %str(1000*(end - start)) + "ms")

# start = time.time()
# c = np.dot(a, b)
# end = time.time()
# print("计算所用时间%s" % str(1000 * (end - start)) + "ms")


"""
03、激活函数演示
"""

# max((1, 0))

# def relu(x):
#     return max(x, 0)

# x = np.linspace(-10, 10, 100)
# # y = relu(x)
# plt.plot(x, [relu(i) for i in x])
# plt.show()

# sigmoid一般做为分类任务最后一层（即输出层的激活函数）
# 一般不做隐层的激活函数，因为容易梯度消失或梯度爆炸
# tanh 双曲正切函数
# 特殊函数会用到，比如循环神经网络

# def tanh(x):
#     return (np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x))
#
# x = np.linspace(-10, 10, 100)
# plt.plot(x, [tanh(i) for i in x])
# plt.show()

# softplus 
def softplus(x):
    return np.log(np.exp(x) + 1)

x = np.linspace(-10, 10, 100)
plt.plot(x, [softplus(i) for i in x])
plt.show()


# 超参数
# 学习速率 a
# 迭代次数 N
# 隐藏层的层数 L
# 每一层的神经元个数 n[1]、n[2]
# 激活函数 g(z) 的选择

# 反向传播
# 正向传播
