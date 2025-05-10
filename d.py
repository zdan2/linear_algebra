import numpy as np
import matplotlib.pyplot as plt
#31線形変換としての行列
m1=np.array([[1,2],[3,1]])

#回転
theta=np.pi/4
cos,sin=np.cos(theta),np.sin(theta)
R=np.array([
    [cos,-sin],
    [sin,cos]
])
print(f'回転: {theta}\n',m1@R)

#拡大
n=3
expansion=np.array([
    [n,0],
    [0,n]
])
print(f'拡大: {n}\n',m1@expansion)

#せん断
a=1
share=np.array([
    [1,a],
    [0,1]
])
print(f'せん断: {a}\n',m1@share)

#32回転行列とその合成
phi=np.pi/3
cos2,sin2=np.cos(phi),np.sin(phi)
R2=np.array([
    [cos2,-sin2],
    [sin2,cos2]
])
print(R@R2)
print(R2@R)

#33せん断行列
# Identity (元の基底)
'''
I = np.eye(2)

# Shear 行列（パラメータ a を好きな値に）
a = 1
shear2 = np.array([[1, 0],
                   [a, 1]])

# 元の基底ベクトル
e1 = I[:, 0]    # (1, 0)
e2 = I[:, 1]    # (0, 1)

# Shear 後のベクトル
v1 = shear2.dot(e1)   # -> (1, a)
v2 = shear2.dot(e2)   # -> (0, 1)

plt.figure()
# 元のベクトルを薄いグレーで
plt.quiver(0, 0, e1[0], e1[1],
           angles='xy', scale_units='xy', scale=1,
           color='gray', label='e1, e2 (元の基底)')
plt.quiver(0, 0, e2[0], e2[1],
           angles='xy', scale_units='xy', scale=1,
           color='gray')

# shear 後のベクトルを赤と青で
plt.quiver(0, 0, v1[0], v1[1],
           angles='xy', scale_units='xy', scale=1,
           color='r', label='shear2·e1')
plt.quiver(0, 0, v2[0], v2[1],
           angles='xy', scale_units='xy', scale=1,
           color='b', label='shear2·e2')

# 軸の範囲を shear の大きさに合わせて調整
margin = 0.5
all_x = [e1[0], e2[0], v1[0], v2[0]]
all_y = [e1[1], e2[1], v1[1], v2[1]]
plt.xlim(min(all_x)-margin, max(all_x)+margin)
plt.ylim(min(all_y)-margin, max(all_y)+margin)

plt.axhline(0, color='k', linewidth=0.5)
plt.axvline(0, color='k', linewidth=0.5)
plt.legend()
plt.gca().set_aspect('equal', 'box')
plt.title(f'Shear matrix: a = {a}')
plt.show()
'''

#34行列のランク
rank=np.linalg.matrix_rank(m1)
print(rank)
m2=np.array([
    [0,0,0],
    [1,1,1],
    [0,0,1]
])
rank2=np.linalg.matrix_rank(m2)
print(rank2)
m3=np.array([
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,0],
    [1,0,0,1]
])
rank3=np.linalg.matrix_rank(m3)
print(rank3)