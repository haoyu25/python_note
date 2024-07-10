print("-----if语句----")
#比较表达式
number=eval(input('请输入您的6位中奖号码：'))
if number == 98324 :
    print('恭喜您，中奖了！')
if number != 98324 :
    print('谢谢参与')

#条件表达式
n=98
if n%2: #余数为0，0的布尔值为False,非0为True
    print(n,'为奇数')
if not n%2:
    print(n,'为偶数')

print('----判断一个字符串是否空字符串----')

x=input("请输入一个字符串：")
if x: #空字符串的布尔值是False
    print("x是一个非空字符串")
if not x:
    print("x是一个空字符串")

print('-----if-else语句-----')
number=eval(input('请输入您的6位中奖号码：'))
if number == 98324:
    print('恭喜您，中奖了！')
else:
    print('谢谢参与')

print('----条件表达式简化-----')
number = eval(input('请输入您的6位中奖号码：'))
result = '恭喜您，中奖了！' if number == 98324 else '谢谢参与'
print(result)
#print('恭喜您，中奖了！' if number == 98324 else '谢谢参与')

print('-----多重if-----')
print('----if-elif-else-----')

score=eval(input('请输入您的成绩：'))
#判断成绩是否有问题
if score<0 or score>100:
    print("成绩有误")
elif 0<=score<60:
    print("E")
elif score<80:
    print("C")
else:
    print("A")

print("-----if嵌套----")

answer=input("喝酒了吗？y/n")
if answer=='y':
    proof=eval(input('请输入酒精含量：'))
    if proof<20:
        print("不构成酒驾")
    elif proof<80:
        print("酒驾")
    else:
        print("醉驾")
else:
    print("没喝酒")