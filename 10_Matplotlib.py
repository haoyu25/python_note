
import numpy as np
from matplotlib import pyplot as plt

x=np.arange(-50,50)
y=x**2
#设置图标名称
plt.title('y=x^2')
plt.plot(x,y)
plt.show()
#设置中文字体
plt.rcParams['font.sans-serif']=['SimHei']#默认字体设置改为中文黑体
plt.rcParams['axes.unicode_minus']=False #中文不识别符号
plt.title('y等于x的平方')
plt.plot(x,y)
plt.show()

#先设置，再画图
plt.xlabel('x轴')#设置X轴Y轴名称
plt.ylabel('y轴',fontsize=10)
plt.title('y等于x的平方')
plt.plot(x,y,linewidth=5) #设置线条
plt.show()

#多线条
x=np.arange(-10,10)
y1=x**2
y2=x
plt.title("y=x^2",fontsize=16)
plt.xlabel('x轴',fontsize=12)
plt.ylabel("y轴")
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()

#添加图例
plt.title("y=x^2",fontsize=16)
plt.xlabel('x轴',fontsize=12)
plt.ylabel("y轴")
plt.plot(x,y1,label='y1=x^2')
plt.plot(x,y2,label='y2=x')
plt.legend() #默认位置是loc=best
for x,y in zip(x,y1):
    plt.text(x,y,y) #点的位置和值
plt.show()

#显示网格
plt.title("y=x^2",fontsize=16)
plt.xlabel('x轴',fontsize=12)
plt.ylabel("y轴")
plt.plot(x,y1,label='y1=x^2')
plt.plot(x,y2,label='y2=x')
plt.legend() #默认位置是loc=best
for x,y in zip(x,y1):
    plt.text(x,y,y) #点的位置和值
plt.grid(True
         #, linestyle='--',color='gray',linewidth='0.5',axis='both'
         )
plt.show()