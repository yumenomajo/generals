import numpy as np
import matplotlib.pyplot as plt

# 初始种群大小
N0 = 100
# 增长率
r = 0.1
# 时间步长
dt = 0.1
# 总时间
T = 10

# 时间点
t = np.arange(0, T, dt)
# 种群大小
N = np.zeros(len(t))
N[0] = N0

for i in range(1, len(t)):
    dN = r * N[i-1] * dt
    N[i] = N[i-1] + dN

plt.plot(t, N)
plt.xlabel('时间')
plt.ylabel('种群大小')
plt.title('生物增长模型')
plt.show()
