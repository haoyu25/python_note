print('Hello World')
print("hello world") #单引号双引号都可以
print("""hello world""") #多个引号会忽略
print(20)

a=100
b=200
print(a+b)
print(a*b)

#输出多个结果
print(a,b,"hello")

#输出ASCII表示的字符--美国信息交换标准码
#使用内置函数chr()
print('b') # 输出字符b
print(chr(98)) #输出字符b
#中文Unicode编码
print(ord("北")) # 北 这个字的编码（数字）是21271
print(ord("京"))
#计算器--程序员--输入数字--HEX获得十六进制
#北--21271--5317
#使用\u分隔
print("\u5317\u4eac")

#使用print将内容输出到文件
fp=open("note.txt","w") #打开文件 w-->write
print("北京欢迎你", file=fp) #输出到文件中
fp.close() #关闭文件

#Ctrl+点击函数-->了解详情
#print()
#def print(self, *args, sep=' ', end='\n', file=None)
#默认end=“\n" 换行， 多个self间用空格连接

#多条print()输出到一行显示
#修改换行
print("北京", end="--->")
print("欢迎你") #只需要run这行
#修改空格连接
print(1314) #直接输出整数
print(3.14) #直接输出浮点数
print(1,3,1,4) #使用逗号链接要输出的数字，中间使用空格链接
print(192,168,1,1,sep=".") #改成.连接
#print("北京"+2022) #默认加法计算，字符类型错误
print("北京"+"2022") #改成直接连接

#输入函数input()
name=input("请输入您的姓名：") #要求键盘输入姓名
print("我的姓名是："+name)

num=int(input("请输入您的幸运数字：")) #需要通过int()将字符串转换成整数
print("我的幸运数字是：", num) #字符串+整数 不能用+连接， 输出两个变量

#单行注释
# coding:utf-8 中文注释