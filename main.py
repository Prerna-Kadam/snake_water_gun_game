'''
1 for Snake
-1 for Water
0 for Gun

'''
import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice (s/w/g) : ")
youDict = {"s" : 1, "w" : -1, "g" : 0}
reversed_Dict = {1 : "Snake", -1 : "Water", 0 : "Gun"}

if youstr not in youDict:
    print("Invalid Choice! Please enter only s, w or g.")
else:
    you = youDict[youstr]

print(f"you chose {reversed_Dict[you]}\ncomputer chose {reversed_Dict[computer]}")

if computer == you:
    print("Its a Draw")
else:
    if (computer == -1 and you == 1):  #water  snake
        print("You win!")
    elif(computer == -1 and you == 0):  #water drowns gun ye true hai
        print("You Lose!")
    elif(computer == 1 and you == -1):  #Snake drinks Water ye true hai
        print("You Lose!")
    elif(computer == 1 and you == 0):   #Snake gun
        print("You Win!")
    elif(computer == 0 and you == -1):  #gun Water
        print("You Win!")
    elif(computer == 0 and you == 1):   #gun shoots Snake ye true hai
        print("You Lose!")
    else:
        print("Something went wrong!")


