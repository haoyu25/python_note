#保留字--严格区分大小写
#查看保留字
import keyword #导入关键字
print(keyword.kwlist) #保留字的列表

#标识符---字母、下划线、数字（数字不能第一个）
#严格区分大小写
my_name_1="快跑" #my_name_1 是一个标识符
#定义类--一般首字母大写，用下划线连接
class MyClass:
    class _InnerClass:
        pass
#定义函数
def fun():
    pass
#定义常量--一般用大写
PI=3.14

#变量
luck_number=7 #创建一个整型变量luck_number，并为其赋值为8
my_name="跑跑" #字符串
print(my_name,"的幸运数字为：",luck_number)
#数据类型
print("luck_number的数据类型是：", type(luck_number)) #查看类型
luck_number="北京欢迎你" #通过赋值直接修改数据类型
print("luck_number的数据类型是：", type(luck_number))

#允许多个变量指向同一个值
no=number=1024 #no, number 两个变量
print(no,number)
#查看内存位置
print(id(no))
print(id(number))

#数据类型
#整数
num=987 #默认十进制表示整数
num2=0b110101 #0b或0B开头 使用二进制表示整数
num3=0o765 #0o或0O开头 使用八进制表示整数
num4=0x87ABF #0x或0X开头 使用十六进制表示整数
print(num,num2,num3,num4)

#浮点数
height=187.0 #必须有小数部分
print(type(height))
#浮点数不确定的尾数问题（因为计算机是使用二进制计算的）
print(0.1+0.2) #0.30000000000000004
print(round(0.1+0.2,1)) # 保留一位小数

#复数
x=123+456j #j 是虚数部分的单位
print("实数部分：", x.real)
print("叙述部分：", x.imag)

#字符串
city="北京" #单行字符串
info='''地址：北京市
收件人：跑跑
手机号：152
''' #多行字符串---三个
print(city)
print(info)
print("北京\n欢迎你") #转义字符 \n 表示换行
print("老师说：\'你好!\'") #转义单双引号
print(r"北京\n欢迎你") #字符前加上r或R， 转义失效
#字符串索引
s="HELLOWORLD"
print(s[0],s[-10]) #递增递减，表示同一个
print("北京欢迎你"[4])
print(s[1:4]) #正向递增序列
print(s[-8:-3]) #反向递减序列
print(s[:5]) #默认从0开始，到结尾
#字符串操作
y='2022年'
z='北京冬奥会'
print(y+z) #拼接字符串
print(10*y) #输出十次
print('北京' in y) #输出False/True，是否是子字符串
print('北京' in z)

#布尔类型
x=True
print(x)
print(type(x))
print(True+10) #11
print(False+10) #10
print(bool(0)) #测试布尔值
#布尔值为假：False,None,0,空字符串

s=('3.14')
print(s,type(s))
x=eval(s) #输入字符串，去掉双引号
print(x,type(x))

#eval()经常和input()一起使用， 用来获取用户输入的数值型
age=eval(input('请输入您的年龄：')) #将字符串类型转换成数值类型，相当于int()
print(age,type(age))



