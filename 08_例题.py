#猜数游戏
#产生随机数

import random
rand=random.randint(1,100)
count=1
while count<=10:
    number=eval(input("请猜1-100："))
    if number==rand:
        print("猜对了！")
        break
    elif number>rand:
        print("大了")
    else:
        print("小了")
    count+=1

#判断次数
if count<=3:
    print("真聪明，一共猜了",count,"次")

