from random import randint #import module
game_check=0 #game_check=0 keep going,game_check=1 stop running
game_tie=0 #calculate tie times
game_loss=0 #calculate loss times
print("Welcome to ROCK,PAPER,SCISSORS game!")
while(game_check==0):
    user=input("Enter your move:(r)ock (p)aper (s)cissors")
    print("ROCK versus...")
    choise=["ROCK","PAPER","SCISSORS"]  #construct a "ROCK","PAPER","SCISSORS" list
    ROCK=choise[randint(0,2)] #random to choose one
    print(ROCK)
    if(user=="r" and ROCK=="ROCK"): #tie game
        print("It is a tie!")
        game_tie += 1
    elif(user=="p" and ROCK=="PAPER"): #tie game
        print("It is a tie!")
        game_tie += 1
    elif (user=="s" and ROCK == "SCISSORS"): #tie game
        print("It is a tie!")
        game_tie += 1
    elif(user=="r" and ROCK=="PAPER"): #loss game
        print("You lose!")
        game_loss+=1
    elif user=="p" and ROCK=="SCISSORS": #loss game
        print("You lose!")
        game_loss += 1
    elif user=="s" and ROCK=="ROCK": #loss game
        print("You lose!")
        game_loss += 1
    elif(user=="r" and ROCK=="SCISSORS"): #win game
        print("You win!")
        game_check = 1 #already win,so we want code stop running
    elif user=="p" and ROCK=="ROCK": #win game
        print("You win!")
        game_check = 1
    elif user=="s" and ROCK=="PAPER": #win game
        print("You win!")
        game_check = 1
print("You have %d ties and %d losses before your first win"%(game_tie,game_loss))