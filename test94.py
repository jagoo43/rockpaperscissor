import random
options=["rock","paper","scissors"]
userchoice=input("chose rock paper or scissor")
computerchoice=random.choice(options)
print(computerchoice)
if userchoice==computerchoice:
    print("its a tie")
elif userchoice=="rock" and computerchoice=="scissors":
    print("you win")
elif userchoice=="paper" and computerchoice=="rock":
    print("you win")
elif userchoice=="scissors" and computerchoice=="paper":
    print("you win")
else:
    print("you lose")