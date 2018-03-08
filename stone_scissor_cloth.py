#石头剪刀布游戏 人机大战
import random
computer=random.randint(1,3)
#判断玩家赢了的状态
def test(player,computer):
    if (player == 1 and computer == 2) or (player == 2 and computer ==3) or (player == 2 and computer == 3):
        print("哈哈，你太厉害了")
    #判断平局
    elif player == computer:
        print("平局")
    #判断玩家输了的状态
    else:
        print("运气不太好啊，要不要再来一次")    
true_false=int(input("是否开始游戏(开始请按1,退出请0)："))
while true_false:
    player = int(input("请出拳(石头是1,剪刀是2,布是3): "))
    test(player,computer)
    true_false=int(input("是否继续游戏(继续请按1,退出请0)："))
    
