import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,0,1])
you=(input("Enter Input From User for Game: "))
game={"s":1,"w":-1, "g":0}
reverse={1:"Snake",-1:"water",0:"Gun"}
# s for snake, w for water, g for gun
user=game[you]
print(f"You choose {reverse[user]}, and computer choose {reverse[computer]}")

if computer==user:
    print("Draw")
else:
    if user==1 and computer ==-1:
        print("You Win")
    elif user==-1 and computer==1:
        print("You Lose")
    elif user==1 and computer==0:
        print("You Lose")
    elif user==0 and computer==1:
        print("You win")
    elif user==0 and computer==-1:
        print("You win")
    elif user==-1 and computer==0:
        print("You Lose")
    else:
        print("Wrong Input")