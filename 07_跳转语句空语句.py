print('-----跳转语句break-----')

#累加和大于22
s=0
i=1
while i <11:
    s+=i
    if s>20:
        print('累加和大于20的当前数',i)
        break #终止循环，直接退出循环
    i+=1

print("-----使用for循环----")
s=0
i=1
for i in range(11):
    s+=i
    if s>20:
        print('累加和大于20的当前数',i)
        break #终止循环，直接退出循环
    i+=1

for i in 'hello':
    if i=='e':
        break #当i==e为True，直接结束循环
    print(i)

print('------continue----')

#1-100之间的偶数
s=0
i=1
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print("1-100之间的偶数和：",s)

print('----使用for循环----')
s=0
i=1
for i in range(1,101):
    if i%2==1:
        continue
    s+=i
print("1-100之间的偶数和：",s)

print("----空语句pass-----")
if True:
    pass

while True:
    pass

for i in range(10):
    pass
