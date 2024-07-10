print('-----遍历循环for-in----')

#遍历字符串
for i in "hello":
    print(i)

#range()函数, 产生一个[n,m)的整数序列
for i in range(1,11):
    #print(i)
    if i%2:
        print(i,"是奇数")
    if i%2==0:
        print(i,"是偶数")

#计算累加
s=0 #用于存储累加
for i in range(1,11):
    s+=i
print('1-10之间的累加和为：',s)

print("-----100-999之间的水仙花数----")
for i in range(100,1000):
    sd=i%10
    tens=i//10%10
    hundred=i//100
    if sd**3+tens**3+hundred**3==i:
        print(i)

#一般结合 break 或 continue 使用else
s=0 #用于存储累加
for i in range(1,11):
    s+=i
else:
    print('1-10之间的累加和为：',s)

print("-----无限循环while----")
#一般结合 break 或 continue
#通过条件语句控制执行语句
answer=input("今天要上课吗?y/n") #1.初始化变量
while answer=='y': #2.条件判断
    print("好好学习") #3.语句块
    answer=input("今天要上课吗?y/n") #4.改变变量

# 1-100之间的累加和
i=1
s=0
while i<=100:
    s+=i
    i+=1
print("1-100之间的累加和：",s)

#while--else
i=1
s=0
while i<=100:
    s+=i
    i+=1
else:
    print("1-100之间的累加和：",s)

print('------嵌套循环-----')
#三行四列
for i in range(1,4):
    for j in range(1,5):
        print('x', end='')
    #换行
    print()

#直角三角形
for i in range(1,5):
    for j in range(1,i+1):
        print('x', end='')
    print()

#等腰三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1, i*2):
        print('x', end="")
    print()

#菱形
row=eval(input("请输入菱形的行数"))
top_row=(row+1)//2 #上增部分的行数
#上半部分
for i in range(1,top_row+1):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1, i*2):
        print('x', end="")
    print()
#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1, 2*(bottom_row-i+1)):
        print('x', end="")
    print()

#空心菱形
#菱形
row=eval(input("请输入菱形的行数"))
top_row=(row+1)//2 #上增部分的行数
#上半部分
for i in range(1,top_row+1):
    for j in range(1,6-i):
        print(' ',end='')
    for k in range(1, i*2):
        if k==1 or k==i*2-1:
            print("x",end="")
        else:
            print(' ', end="")
    print()
#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(' ',end='')
    for k in range(1, 2*(bottom_row-i+1)):
        if k==1 or k==2*(bottom_row-i)+1:
            print('x', end='')
        else:
            print(' ', end="")
    print()