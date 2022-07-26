import random #random is used if you want random selection for different values
import time #time helps delay time between print lines

def gameFunc(): #function if you want to call other python files inside
    end = 0
    tie = 0
    win = 0
    loss = 0

    while end != -1: #while loop to keep the game going till user ends it

        rps = random.choice(["rock", "paper", "scissors"]) #array stores the bot information 
        userRPS = input("Please enter Rock, Paper, Scissors (type quit to leave): ")

        if userRPS == 'rock' or userRPS == 'Rock':  #If the user chooses rock, these are the outcomes
            if (userRPS == 'rock' or userRPS == 'Rock') and rps == 'rock':
                print("We tied with Rock!")
                tie = tie + 1
            elif (userRPS == 'rock' or userRPS == 'Rock') and rps == 'paper':
                print("You Lost! I chose Paper!")
                loss = tie + 1
            elif (userRPS == 'rock' or userRPS == 'Rock') and rps == 'scissors':
                print("You Won! I chose Scissors!")
                win = win + 1

        elif userRPS == 'paper' or userRPS == 'Paper': #If the user chooses paper, these are the outcomes
            if (userRPS == 'paper' or userRPS == 'Paper') and rps == 'rock':
                print("You Won! I chose Rock!")
                win = win + 1
            elif (userRPS == 'paper' or userRPS == 'Paper') and rps == 'paper':
                print("We tied with Paper!")
                tie = tie + 1
            elif (userRPS == 'paper' or userRPS == 'Paper') and rps == 'scissors':
                print("You Lost! I chose Scissors!")
                loss = tie + 1

        elif userRPS == 'scissors' or userRPS == 'Scissors': #If the user chooses scissors, these are the outcomes
            if (userRPS == 'scissors' or userRPS == 'Scissors') and rps == 'rock':
                print("You Lost! I chose Rock!")
                loss = tie + 1
            elif (userRPS == 'scissors' or userRPS == 'Scissors') and rps == 'paper':
                print("You Won! I chose Paper!")
                win = win + 1
            elif (userRPS == 'scissors' or userRPS == 'Scissors') and rps == 'scissors':
                print("We tied with Scissors!")
                tie = tie + 1
        elif userRPS == "quit" or userRPS == "Quit": #If the user wants to quit the function
            tie = str(tie)
            win = str(win)
            loss = str(loss)
            print()
            print("Game Over")
            time.sleep(1)
            print("You won " + win + " games")
            time.sleep(1)
            print("You loss " + loss + " games")
            time.sleep(1)
            print("You tied " + tie + " games")
            time.sleep(1)

            end = -1

        else:
            print("Please enter in a valid response: ") #If the user did not enter in any valid inputs
            time.sleep(1)
            
gameFunc()
