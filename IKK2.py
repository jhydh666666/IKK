import numpy as np  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

L1 = 100 
L2 = 100
L3 = 100
def calculate(Rz, Px, Py):
    Wx = Px - L3 * np.cos(Rz)
    Wy = Py - L3 * np.sin(Rz) 
    L4 = np.sqrt(Wx**2 + Wy**2)
    th2_new = np.arccos((Wx**2 + Wy**2 - L1**2 - L2**2) / (2 * L1 * L2))
    fai = np.arctan2(Wy, Wx)
    x = L2 * np.cos(th2_new)
    a = np.arcsin(x / L4)
    th1_new = fai - a
    th3_new = Rz - th2_new - th1_new  

    th1_deg = np.rad2deg(th1_new)
    th2_deg = np.rad2deg(th2_new)
    th3_deg = np.rad2deg(th3_new) 

    return th1_deg, th2_deg, th3_deg

def plot(L1, L2, L3, th1_deg, th2_deg, th3_deg):
    th1 = np.deg2rad(th1_deg)
    th2 = np.deg2rad(th2_deg)
    th3 = np.deg2rad(th3_deg)

    plt.figure()
    x0, y0 = 0, 0

    x1 = L1 * np.cos(th1)
    y1 = L1 * np.sin(th1)

    x2 = x1 + L2 * np.cos(th1 + th2)
    y2 = y1 + L2 * np.sin(th1 + th2)

    x3 = x2 + L3 * np.cos(th1 + th2 + th3)
    y3 = y2 + L3 * np.sin(th1 + th2 + th3)

    plt.plot([x0, x1], [y0, y1], label=f'L1 = {L1}, θ1 = {np.rad2deg(th1):.2f}°')
    plt.plot([x1, x2], [y1, y2], label=f'L2 = {L2}, θ2 = {np.rad2deg(th1 + th2):.2f}°')
    plt.plot([x2, x3], [y2, y3], label=f'L3 = {L3}, θ3 = {np.rad2deg(th1 + th2 + th3):.2f}°')

    plt.scatter([x0, x1, x2, x3], [y0, y1, y2, y3], color='red')  # 绘制点
    plt.title('机械臂的运动学表示')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='gray', lw=0.1)
    plt.axvline(0, color='gray', lw=0.1)
    plt.grid(True)
    plt.legend()
    plt.axis('equal')
    # 显示图像
    plt.show()

Rz_deg =100
Rz = np.deg2rad(Rz_deg)
Px = 120
Py = 100

th1_deg, th2_deg, th3_deg = calculate(Rz, Px, Py)

print(f'th1 = {th1_deg:.2f}°')
print(f'th2 = {th2_deg:.2f}°')
print(f'th3 = {th3_deg:.2f}°')

plot(L1, L2, L3, th1_deg, th2_deg, th3_deg)


