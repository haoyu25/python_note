#安装Numpy
#setting-python interpreter--- +
import numpy as np

#使用python原生代码创造函数
def python_sum(n):
    a=[i**2 for i in range(n)] #创建列表
    b=[i**3 for i in range(n)]
    ab_sum=[]
    for i in range (n):
        ab_sum.append(a[i]+b[i])
    return ab_sum

print(python_sum(10))

#使用numpy实现代码
def numpy_sum(n):
    a=np.arange(n)**2
    b=np.arange(n)**3
    return a+b

print(numpy_sum(10))

#一维数组索引
ar1=np.arange(10)
ar2=ar1[2:7:2] #start:stop:step
print(ar1)
print(ar2)
ar3=ar1[2]#第三个元素
ar4=ar1[2:]#从第三个元素开始到最后
ar5=ar1[:2] #到第三个元素前

#二维数组索引
ar4_5=np.arange(20).reshape(4,5)
print(ar4_5)
print('----切片----')
print(ar4_5[2])
print(ar4_5[2][2])
print(ar4_5[2:])
print('使用省略号，将包含第n列/行中所有行/列元素')
print(ar4_5[...,1])
print(ar4_5[1,...])

#ar4_5[1,2]==ar4_5[1][2]
#ar4_5[...,2]!=ar4_5[...][2] #都取的行

print("--------")
#数组索引
b=np.array([[1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12]])

a=b[[0,0,3,3],[0,2,0,2]] #取四个角上的数
print(a)

c=b[1:3,1:3] #1-3不包含，1-3，等于b[[1,2],[1,2]]

#创建国际象棋棋盘矩阵
z=np.zeros((8,8),dtype=int)
print(z)
z[1::2,::2]=1
z[::2,1::2]=1
print(z)

#布尔数组索引
x=np.array([[0,1,2],
           [3,4,5],
           [6,7,8],
           [9,10,11]])

print(x[x>6]) #提取出所有满足条件的数组

print(x[x%2==1]) #提取出所有满足条件的数组

#索引后修改
x[x%2==1]=-1
print(x)

print('--------统计-------')
ml=np.arange(20).reshape(4,5)
#平均数
print(ml.mean())
print(np.mean(ml))
print(ml.mean(axis=0))#从上往下计算
print(ml.mean(axis=1))#从左往右计算
#中位数
ar1=np.array([1,3,5,6,7])
print(np.median(ar1))
#标准差
print(np.std(ar1))
#方差
print(np.var(ar1))
#最大最小
print(ml.max())
print(ml.min(axis=0))
#求和
print(ml.sum())
print(ml.sum(axis=1))
#加权平均数
xiaoming=np.array([80,90,95])
xiaogang=np.array([95,90,80])
weights=np.array([0.2,0.3,0.5])
print(np.average(xiaoming,weights=weights))
print(np.average(xiaogang,weights=weights))

#自定义数据类型
teacher=np.dtype([('teacher',np.str_,2),('age',"i1"),('salary','f4')])
b=np.array([('wl',32,8734.50),
           ('lh',28,3456.80)
           ],dtype=teacher)
print(b)