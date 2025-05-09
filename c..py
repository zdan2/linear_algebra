from random import randint
import numpy as np
import matplotlib.pyplot as plt

#21行列の定義と生成22行列の足し算引き算23行列とスカラー演算
def rnd_matrix(n):
    return np.array([[randint(1,10) for _ in range(n)] for _ in range(n) ])

m1=rnd_matrix(2)
m2=rnd_matrix(2)
print(f'{m1} + {m2}')
print(m1+m2)

t1=rnd_matrix(3)
t2=rnd_matrix(3)
print(f'{t1} - {t2}')
print(t1-t2)

print(f'4*{m1} = {4*m1}')
print(f'{m1}/4 = {m1/4}')

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(A)
A[1][1]=0
print(A)
A[1][1]=5

#25単位行列の作成
I2=np.eye(2,dtype=int)
I3=np.eye(3,dtype=int)
print(I2)
print(I3)

#26零行列の作成
Z=np.zeros([3,3])
print(Z)

#27行列の転置
tA=A.T
print(A)
print(tA)

#28行列の積
print(m1@m2)
print(t1@t2)

#29行列の積
v1=np.array([2,3,2])
tv1=v1.T
print(tv1@A)

#30行列の可視化
plt.imshow(A,cmap='plasma',interpolation='none',origin='lower')
plt.show()