#python 支持链式赋值
a=b=c=100
print(a,b,c)

#python支持系列解包赋值
a,b=10,20
print(a,b)

#python支持直接交换赋值
a,b=b,a
print(a,b)

#位运算
#位与 & --- 二进制位数都是1才输出1
print(12&8)
#位或 | --- 二进制位数都是0才输出0
print(12|8)
#位异或 ^ --- 不同为1，相同为0
print(12^8)
#位取反 ~ --- 10取反
print(~12)
#左移位 << 相当于乘以2的N次幂
print('左移位：',2<<3) #将2向左移动3位
#右移位 >> 除以2的N次幂
print('右移位：', 24>>3)

#练习
num=eval(input("请输入一个四位整数："))
sd=num%10
tens=num//10%10
hundred=num//100%10
thousands=num//1000
print('个位上的数字：',sd)
print('十位上的数字：',tens)
print('百位上的数字：',hundred)
print('千位上的数字：',thousands)

