import random
options=("rock","paper","scissors")
playing=True
while playing :
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("enter your choice(rock,paper,scissors):")

    print(f"player :{player}")
    print(f"computer:{computer}")
    if (player==computer):
        print("the game is tie")
    elif(player=="rock" and computer=="scissors"):
        print("you win")
    elif(player=="paper" and computer=="rock"):
        print("you win")
    elif(player=="scissors" and computer=="paper"):
        print("you win")
    else:
        print("you lose")
    play_again=input(" do you want to Play again ? (y/n):").lower()
    if not play_again=="y":
        playing=False
print("Thank you for playing !")