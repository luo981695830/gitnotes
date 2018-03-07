# 这是一个猜数字的游戏
import random
print("======================================")
print("========欢迎您进入猜数字游戏==========")
print("===        请选择关卡难度：        ===")
print("             1.简单                   ")
print("             2.普通                   ")
print("             3.中等                   ")
print("             4.困难                   ")
print("======================================")
flag = 0
while True:
    level = int(input("请输入关卡难度数字: "))
    if level==1:
        print("简单")
    elif level==2:
        print("普通")
    elif level==3:
        print("中等")
    elif level==4:
        print("困难")
    else:
        print("您输入不对，请重新输入")
                                                    
    secretNumber =random.randint(1,10**level)
    if flag:
        print("关卡难度升级，请小心!!!")
    for guessTaken in range(5):
        guessNumber = int(input("请输入你猜的数字: "))
        if guessNumber < secretNumber:
            print("你猜的这个数太小了"      )
        elif guessNumber >secretNumber:
            print("你猜的这个数字太大了")
        else:
            break
    if guessNumber == secretNumber:
        print('恭喜你，猜对了'+str(guessNumber))
    else:
        print('你猜了'+str(guessTaken)+'次都没猜对，真够笨的')
    if True:
        judge=int(input("请问是否继续: （是请按1，否请按0）"))
        if judge == 1:
            flag=1
            continue
        elif judge == 0:
            break
    
