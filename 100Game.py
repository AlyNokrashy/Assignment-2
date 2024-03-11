#File: CS112_A1_T2_1_20230239.py
#Purpose: The two players start with 0 and each player adds a number between 1-10 alternatively and whoever reaches 100 first wins
#Author: Ali Ahmed Fathy Mosaad Elnokrashy
#ID: 20230239


#set the starting number
#initializing the current player to player 1 to start the game
sum = 0
CurrentPlayer = 1
#welcome msg
print("Welcome to The 100 GAME \nThis is a 2 player game where both players take turns choosing a number between \
(1-10) \nThe first player to reach 100 wins.\n")

#game keeps working until user types exit
while True:
    UserInput = input("Enter 'start' to play, to quit enter 'exit' : ")
    if UserInput.lower() == "exit": 
        print("Exited program")
        break
    elif UserInput.lower() == "start":
        while sum < 100:
            print(f"Current score: {sum}")
            if sum < 91:
            #check for invalid input
                try:
                    turn = int(input(f"Player {CurrentPlayer}: Please choose a number from 1-10 : "))
                    if not (1 <= turn <= 10):
                        raise ValueError
                
                #if the user enters any value other than 1-10 keep prompting till they enter the right input
                except ValueError:
                    print("Wrong input! Please the number must be between 1 and 10")
                    continue
            
            #when the total is 91 or more the player must enter a number that doesn't exceed 100
            else :
                try:
                    turn = int(input(f"Player {CurrentPlayer}: Please choose a number from 1 - {100 - sum} : "))
                    if not (1 <= turn <= (100 - sum)):
                        raise ValueError
                except ValueError:
                    print(f"Wrong input! Please the number must be between 1 and {100 - sum}: ")
                    continue
            
            #calculating the score
            sum += turn
            
            #result
            if sum == 100:
                print(f"Player {CurrentPlayer} wins!")
                sum = 0
                break
           
            #switching players for the next turn
            if CurrentPlayer == 2:
                CurrentPlayer = 1
            else:
                CurrentPlayer = 2
    
    #if the user types anything other than 'start' or 'exit' keep prompting till they enter the right input
    else:
        print("Worng Input! Enter 'start' or 'exit'\n")
        continue