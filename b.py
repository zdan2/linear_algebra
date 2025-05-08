import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
v0=np.array([2,2,2])
v1=np.array([1,2,3])
v2=np.array([4,5,6])

#11 コサイン類似度の計算
def cosine_simirality(v1,v2):
    dot_product=np.dot(v1,v2) 
    norm_v1=np.linalg.norm(v1)
    norm_v2=np.linalg.norm(v2)

    if norm_v1==0 or norm_v2==0:
        return 0
    
    return dot_product/(norm_v1*norm_v2)

sim=cosine_simirality(v1,v2)
print(f'cosine simirality:{sim}')


#12　ベクトルの外積
cross_v=np.cross(v1,v2)
print(f'cross vector:{cross_v}')


#13 投影ベクトルの計算
def projection_v(va,vb):
    dot_product=np.dot(va,vb)
    norm_v2=np.linalg.norm(vb)
    proj=dot_product/norm_v2**2*vb

    return proj

print(projection_v(v1,v2))

#14 2Dベクトルの回転
def rot(v,theta):
    v=np.array([v]).T
    cos,sin=np.cos(theta),np.sin(theta)

    R=np.array([
        [cos,-sin],
        [sin,cos]
    ])
    return R.dot(v)

v3=np.array([2,1])
theta=3.14/3
print(rot(v3,theta))

v4=np.array([3,4])

#15 ベクトルの可視化
fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax1.quiver(0, 0, v3[0], v3[1], angles='xy', scale_units='xy', scale=1, color='r')
ax1.quiver(0, 0, v4[0], v4[1], angles='xy', scale_units='xy', scale=1, color='b')
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 4)
ax1.set_aspect('equal')
ax1.grid(True)
ax1.set_title("2D Vectors")


#16 ベクトルの可視化２
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='g')
ax2.set_xlim([0, 3])
ax2.set_ylim([0, 3])
ax2.set_zlim([0, 3])
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_title("3D Vector")

plt.tight_layout()
plt.show()

#17and18and19 ベクトルの線形独立の判定
def is_linear_independence(*args):
    v=[*args]
    A=np.stack(v,axis=1)
    rank=np.linalg.matrix_rank(A)
    print(f'rank:{rank}')
    if rank==A.shape[1]:
        return True
    return False

print(is_linear_independence(v1,v2))

#20基底の概念 
# Step 1: 新しい基底 e1, e2 を定義
e1 = np.array([2, 1]) 
e2 = np.array([1, 2]) 

# Step 2: この基底におけるベクトル v の座標（座標系Bでの表現）
v_coords_in_B = np.array([3, 1]) 

# Step 3: 新しい基底を行列として持つ（列ベクトルとして並べる）
B = np.column_stack((e1, e2)) 

# Step 4: 標準基底での v を求める（元の空間での v を再構成）
v_standard = B @ v_coords_in_B

print("新しい基底 e1, e2:\n", B)
print("基底Bにおける座標:", v_coords_in_B)
print("標準基底における v:", v_standard)
