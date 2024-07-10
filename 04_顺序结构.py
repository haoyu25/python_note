#赋值运算符的执行顺序，从右到左
name='张三'
age=20

a=b=c=d=100 #链式赋值
print(a,b,c,d)
name1,age1='李四' #系列解包赋值
print(name1,age1)
name2,age2='李四',22 #元组分解赋值
print(name2,age2)
[name3,age3]=['王五',30] #列表分解赋值
print(name3,age3)
a,b,c,d="room" #字符串分解赋值
print(a)
print(b)

#扩展的字符串解包赋值
a,*b="room"
print(a) #r
print(b) #['o', 'o', 'm'] 列表