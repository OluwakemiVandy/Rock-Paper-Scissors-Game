import random
while True:
 print ("Rock-Paper-Scissors Game:", "CPU vs Player")
 print ("R for Rock")
 print("P for Paper")
 print ("S for Scissors")
 
 player= input("Choose R, P or S: ")
 player=player.upper()
 list=["R","P","S"]
 CPU = random.choice(list)
 print("CPU chose", CPU)
    
 if player in list:
     if player == CPU:
        print("Its a Tie!")
 if player == "R":
    if CPU == "P":
         print("Oops.. CPU Wins!","Paper","beats","Rock")
    elif CPU == "S":
         print("You Win!")
 elif player =="P":
     if CPU == "S":
         print("Oops..CPU Wins!","Scissors","beats","Paper")
     elif CPU=="R":
         print("You win!")
 elif player =="S":
     if CPU =="R":
        print("Oops..CPU Wins","Scissors","beats","Rock")
     elif CPU == "P":
            print("You Win!")
 else:
    print("Error! Input another choice")