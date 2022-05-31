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
 #print("CPU chose", CPU)
    
 if player in list:
     if player == CPU:
        print("CPU chose:",CPU)
        print("Its a Tie!")

 if player == "R":  
    if CPU == "P":
         print("Player(Rock) : CPU(Paper)")
         print("Oops.. CPU Wins!","Paper","beats","Rock")
    elif CPU == "S":
         print("Player(Rock) : CPU(Scissors)")
         print("You Win!","Rock","beats","Scissors" )
 elif player =="P":
     if CPU == "S":
         print("Player(Paper) : CPU(Scissors)")
         print("Oops..CPU Wins!","Scissors","beats","Paper")
     elif CPU=="R":
         print("Player(Paper) : CPU(Rock)")
         print("You win!","Paper","beats","Rock" )
 elif player =="S":
     if CPU =="R":
        print("Player(Scisors) : CPU(Rock)")
        print("Oops..CPU Wins","Rock","beats","Scissors")
     elif CPU == "P":
            print("Player(Scissors) : CPU(Paper)")
            print("You Win!","Scissors","beats","Paper" )
 else:
    print("Error! Input another choice")