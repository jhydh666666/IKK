import numpy as np
import matplotlib.pyplot as plt

# 参数初始化
L1 = 100
L2 = 100
L3 = 100
th1 = np.deg2rad(35)  
th2 = np.deg2rad(45)  
th3 = np.deg2rad(40)  
Rz = th1 + th2 + th3

# 计算末端点 Px, Py
Px = L1 * np.cos(th1) + L2 * np.cos(th1 + th2) + L3 * np.cos(th1 + th2 + th3)
Py = L1 * np.sin(th1) + L2 * np.sin(th1 + th2) + L3 * np.sin(th1 + th2 + th3)

# 计算 Wx, Wy
Wx = Px - L3 * np.cos(th1 + th2 + th3)
Wy = Py - L3 * np.sin(th1 + th2 + th3)

# 计算 L4
L4 = np.sqrt(Wx**2 + Wy**2)

# 修正 th2 计算
th2_new = np.arccos((Wx**2 + Wy**2 - L1**2 - L2**2) / (2 * L1 * L2))

# 计算 fai
fai = np.arctan2(Wy, Wx)

# 修正 a 的计算
x = L2 * np.sin(th2_new)
a = np.arcsin(x / L4)

# 修正 th1 和 th3 的计算
th1_new = fai - a
th3_new = Rz - th2_new - th1_new

# 将弧度转换回角度显示
th1_deg = np.rad2deg(th1_new)
th2_deg = np.rad2deg(th2_new)
th3_deg = np.rad2deg(th3_new)

# 显示计算结果
print(f'th1_new = {th1_deg}')
print(f'th2_new = {th2_deg}')
print(f'th3_new = {th3_deg}')

# 绘制图像
plt.figure()

# 起点
x0, y0 = 0, 0

# 第一段
x1 = L1 * np.cos(th1)
y1 = L1 * np.sin(th1)

# 第二段
x2 = x1 + L2 * np.cos(th1 + th2)
y2 = y1 + L2 * np.sin(th1 + th2)

# 第三段
x3 = x2 + L3 * np.cos(th1 + th2 + th3)
y3 = y2 + L3 * np.sin(th1 + th2 + th3)

# 绘制每个连杆
plt.plot([x0, x1], [y0, y1], label=f'L1 = {L1}, θ1 = {np.rad2deg(th1):.2f}°')
plt.plot([x1, x2], [y1, y2], label=f'L2 = {L2}, θ2 = {np.rad2deg(th1 + th2):.2f}°')
plt.plot([x2, x3], [y2, y3], label=f'L3 = {L3}, θ3 = {np.rad2deg(th1 + th2 + th3):.2f}°')

# 设置图像属性
plt.scatter([x0, x1, x2, x3], [y0, y1, y2, y3], color='red')  # 绘制点
plt.title('机械臂的运动学表示')
plt.xlabel('X 坐标')
plt.ylabel('Y 坐标')
plt.axhline(0, color='gray', lw=0.5)
plt.axvline(0, color='gray', lw=0.5)
plt.grid(True)
plt.legend()
plt.axis('equal')

# 显示图像
plt.show()
