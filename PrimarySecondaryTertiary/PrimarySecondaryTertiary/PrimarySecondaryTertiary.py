import random

#Lap 3 Group project- creative use of random function and elif statements
#By Heather Whittlesey

print(
"""
        ~~  COLOR JUMBLE  ~~


Choose a color.
Remember: primary > secondary > tertiary > primary

Choice of colors are: red, blue, yellow, green, orange, purple, magenta, teal, and chartreuse
     
      """
      )
comp_wins = 0
player_wins = 0
#tied_games = 0
#error_bool = False

def User_Option():

    user = input("You can enter the full word or first letter: ")
    if user in ["Red", "red", "r", "R"]:
        user = "red"
    elif user in ["Yellow", "yellow", "y", "Y"]:
        user = "yellow"
    elif user in ["Blue", "blue", "b", "B"]:
        user = "blue"
    elif user in ["Orange", "orange", "o", "O"]:
        user = "green"
    elif user in ["Green", "green", "g", "G"]:
        user = "green"
    elif user in ["Purple", "purple", "p", "P"]:
        user = "purple"
    elif user in ["Magenta", "magenta", "m", "M"]:
        user = "magenta"
    elif user in ["Teal", "teal", "t", "T"]:
        user = "teal"
    elif user in ["chartreuse", "chartreuse", "c", "C"]:
         user = "chartreuse"
    else:
        print("Please try again.")
        User_Option()
    return user



def Computer_Option():
    comp = random.randint(1, 10)
    if comp == 1:
        comp = "red"
    elif comp == 2:
        comp = "yellow"
    elif comp == 3:
        comp = "blue"
    elif comp == 4:
        comp = "green"
    elif comp == 5:
        comp = "orange"
    elif comp == 6:
        comp = "purple"
    elif comp == 7:
        comp = "teal"
    elif comp == 8:
        comp = "chartreuse"
    else:
        comp = "magenta"
    return comp



while True:
    print("")
    
    user = User_Option()
    comp = Computer_Option()

    print("")

 #red
    
    if user == "red":
        if comp == "red":
            print("You tied.")
            #tied_game += 1
        
        elif comp == "yellow":
            print(comp + " and " + user +" are both primary")
            print("You tied.")
            #tied_game += 1
            
        elif comp == "blue":
            print(comp + "and " + user +" are both primary")
            print("You tied.")

        elif comp == "green":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "orange":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "magenta":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

        elif comp == "teal":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

        elif comp == "chartreuse":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1
           
#yellow

    elif user == "yellow":
        if comp == "yellow":
            print("You tied.")
            #tied_game += 1
        
        elif comp == "red":
            print(comp + " and " + user +" are both primary.")         
            #tied_game += 1

        elif comp == "blue":
            print(comp + " and " + user +" are both primary.")           

        elif comp == "green":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "orange":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1            

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "magenta":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

        elif comp == "teal":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

        elif comp == "chartreuse":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

#blue

    elif user == "blue":
        if comp == "blue":
            print("You tied.")
            #tied_game += 1
        
        elif comp == "red":
            print(comp + " and " + user +" are both primary. You tied.")         
            #tied_game += 1
            
        elif comp == "yellow":
            print(comp + " and " + user +" are both primary.")

        elif comp == "green":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "orange":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1            

        elif comp == "magenta":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

        elif comp == "teal":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

        elif comp == "chartreuse":
            print("The computer chose " + comp +", a tertiary color, you lose.")
            comp_wins += 1

#green

    elif user == "green":
        if comp == "green":
            print("You tied.")
            #tied_game += 1
        
        elif comp == "red":
            print("The computer chose " + comp +", a primary color, you lose.")
            comp_wins += 1

        elif comp == "blue":
            print("The computer chose " + comp +", a primary color, you lose.")
            comp_wins += 1
            
        elif comp == "yellow":
            print("The computer chose " + comp +", a primary color, you lose.")
            comp_wins += 1

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you win.")
            player_wins += 1

        elif comp == "orange":
            print(comp + " and " + user +" are both secondary.")
            player_wins += 1

        elif comp == "magenta":
            print("The computer chose " + comp +", a tertiary color, you win.")
            player_wins += 1

        elif comp == "teal":
            print("The computer chose " + comp +", a tertiary color, you win.")
            player_wins += 1

        elif comp == "chartreuse":
            print("The computer chose " + comp +", a tertiary color, you win.")
            player_wins += 1


#purple

    elif user == "purple":
        if comp == "purple":
            print("You tied.")
            #tied_game += 1
        
        elif comp == "red":
            print("The computer chose " + comp +", a primary color, you lose.")
            comp_wins += 1

        elif comp == "blue":
            print("The computer chose " + comp +", a primary color, you lose.")
            comp_wins += 1
            
        elif comp == "yellow":
            print("The computer chose " + comp +", a primary color, you lose.")
            comp_wins += 1

        elif comp == "green":
            print(comp + " and " + user +" are both secondary.")
            

        elif comp == "orange":
            print(comp + " and " + user +" are both secondary.")
            

        elif comp == "magenta":
            print("The computer chose " + comp +", a tertiary color, you win.")
            player_wins += 1

        elif comp == "teal":
            print("The computer chose " + comp +", a tertiary color, you win.")
            player_wins += 1

        elif comp == "chartreuse":
            print("The computer chose " + comp +", a tertiary color, you win.")
            player_wins += 1

#magenta

    elif user == "magenta":
        if comp == "magenta":
            print("You tied.")
            #tied_game += 1

        elif comp == "red":
                print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.")
                player_wins += 1
        
        elif comp == "yellow":
            print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "blue":
            print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "green":
            print("The computer chose " + comp +", a secondary color, you chose a tertiary color, you win.")

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "teal":
            print(comp + " and " + user +" are both tertiary.")
            

        elif comp == "chartreuse":
            print(comp + " and " + user +" are both tertiary.")

#teal

    elif user == "teal":
        if comp == "teal":
            print("You tied.")
            #tied_game += 1

        elif comp == "red":
                print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.")
                player_wins += 1
        
        elif comp == "yellow":
            print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "blue":
            print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "green":
            print("The computer chose " + comp +", a secondary color, you chose a tertiary color, you win.")

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "magenta":
            print(comp + " and " + user +" are both tertiary.")
            

        elif comp == "chartreuse":
            print(comp + " and " + user +" are both tertiary.")
            
#chartreuse

    elif user == "chartreuse":
        if comp == "chartreuse":
            print("You tied.")
            #tied_game += 1

        elif comp == "red":
                print("The computer chose " + comp +", a primary color, you chose a tertiary color, you winm.")
                player_wins += 1
        
        elif comp == "yellow":
            print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.m")
            player_wins += 1

        elif comp == "blue":
            print("The computer chose " + comp +", a primary color, you chose a tertiary color, you win.m")
            player_wins += 1

        elif comp == "green":
            print("The computer chose " + comp +", a secondary color, you chose a tertiary color, you win.")

        elif comp == "purple":
            print("The computer chose " + comp +", a secondary color, you chose a tertiary color, you win.")
            player_wins += 1

        elif comp == "teal":
            print(comp + " and " + user +" are both tertiary.")
            
        elif comp == "magenta":
            print(comp + " and " + user +" are both tertiary.")        
                         

    print("")
    print("Player wins: " + str(player_wins))
    print("Computer wins: " + str(comp_wins))
    #print("Tied games: " + str(tied_games))
    print("")
    
    user = input("Do you want to play again? (y/n)")
    if user in ["Y", "y", "yes", "Yes"]:
        pass
    elif user in ["N", "n", "no", "No"]:
        break
    else:
        break
           
