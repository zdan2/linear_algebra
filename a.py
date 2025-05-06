import numpy as np

#1 ベクトルの定義と生成
a=np.array([1,2])
b=np.array([3,5])
c=np.array([3,4,5])

#2ベクトルの足し算
d=a+b
print(d)

#3ベクトルの引き算
e=a-b
f=b-a
print(e)
print(f)

#4スカラー倍
print(e,e*2)
print(f,f*3.14)

#5ベクトル要素へのアクセス
print(c)
c[1]=0
print(c)

#6ゼロベクトルの生成
z=np.zeros(3,int)
print(z)

#7単位ベクトルの生成
g=np.eye(3,dtype=int)
print(g)
print(g[0])

#8ベクトルの長さ
ud=np.linalg.norm(a,ord=2)
print(ud)
r=sum(e**2 for e in a)**0.5
print(r)

#9ベクトルの正規化
na=a/ud
print(a,na)

#10内積の計算
print(sum(a*b))