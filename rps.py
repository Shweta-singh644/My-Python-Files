from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
     player = input("Rock, PAper,Scissors?")
     if player == computer:
         print("Tie!")
     elif player =="Rock":
         if computer =="Paper":
            print("You lose!", computer,"covers", player)
         else:
            print("You win!",player, "smashes", computer)
     elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player )
            else:
                print("You win!", player,"cut", computer)
     else:
            print("That's not a valid play. Check your spelling!")
     player = False
     computer = t[randint(0,2)]