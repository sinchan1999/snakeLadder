""" Project Title --> Snake&Ladder Game
    Creation Date --> 16/01/2021
    Devloped By   --> SINCHAN PANDA
    Devloped on   --> Jupyter notebook & VsCode.(python v3.8)
    Compatible with-->python v3.7 or higher"""


# Importing random module for generating random numbers
import random

print("\t\t\t\t*** Welcome to Snake & Ladder Game ***")
player_1 = input("Please enter your name Player_1 : ")

player_2 = input("Please enter your name Player_2 : ")

# A quick view of the Game rules & Modes for a New player.
New_player = input(
    "\nNew to this Game? Need help?\n(***RECOMMENDED :First time users are requested to read the rules by Pressing'Y')\nPress 'Y' for YES or Press any key to skip:")
if (New_player == 'Y' or New_player == 'y'):
    print("\n\t\t\t###---- RULES & MODES ----###\n1: The first player who reaches the 100th position WINS the Game."
          "\n2: Try to avoid getting eaten by Snakes.Ladders are boon for you to reach the glory!\n"
          "3: You can play this game in either of the two modes\n"
          "   AUTO MODE  -> In this mode you need to enter 'roll' each time then the dice will be thrown to get a lucky number !!!\n"
          "   MANUAL MODE-> Here you need to choose your desired number directly between 1 to 20\n"
          "4: Once you select a mode it can't be changed in between the Game\n"
          "5: After both the players play their moves score will appear on SCOREBOARD at right-side\n"
          "6: Anytime you want to Quit the game Press 'Q' or type 'exit'.\n"
          "   If you quit the game in between the other player will win automatically"
          )

Game_mode = input("\nSelect your Game mode AUTO or MANUAL : ")
z = 0

# This Auto_mode() is use to generate a random dice no and executes the complete game in AUTO MODE.


def Auto_mode(name_1, name_2):
    i = 0
    player = [name_1, name_2]
    score = [0, 0]
    sum1 = 0
    sum2 = 0
    error = 2
    k = 0
    while i < 2:
        if (k == 0):

            Play = input(player[i] + " Play your turn : ")

           # IF any player wants to exit the game in between.
            if (Play == 'Q' or Play == 'q' or Play == 'exit' or Play == 'EXIT'):
                error = 0
                q = input(player[i] + " Are u sure to quit this Game??? Your opponent will WIN if you do so!!\n"
                                      "Type 'YES' to quit or 'RESUME' to continue the Game : ")

                # CONFIRMING if the player really wants to exit the game.
                if (q == 'YES' or q == 'yes' or q == 'Yes'):
                    print("\n" + player[i] + " EXITS the game ")

                # IF one player leaves the other player wins automaticallY!
                    if (i == 0):
                        print("\t\t\t\t\t" + player[i + 1] + " You WON!!!")
                    elif (i == 1):
                        print("\t\t\t\t\t" + player[i - 1] + " You WON!!!")
                    break

                # RESUMES the game if the player changes his/her mind from exiting to playing!
                elif (q == 'RESUME' or q == 'resume' or q == 'Resume'):
                    error = 2
                    continue

                # CHECKING the relevant input for playing each turn
            if (Play == 'roll' or Play == 'ROLL' or Play == 'Roll' or Play == 'R' or Play == 'r'):
                error = 0
                # To generate random numbers.
                x = random.randint(1, 6)
                if (i == 0 and error == 0):

                    # CALLING the Snake_Ladder() and passing the previous score.
                    y = Snake_Ladder((x + sum1))
                    score[i] = y
                    if (x == score[i]):
                        sum1 = sum1 + score[i]
                    elif (x != score[i]):
                        sum1 = score[i]

                    # WINNING message!!!
                    if sum1 == 100:
                        print("\t\t\t\t BRAVO!!! " +
                              player[i] + " WINS THE GAME!!!")
                        k = k + 1
                        break

                    # CANCELLS the move if the player's score exceeds 100.
                    elif sum1 > 100:
                        print(
                            player[i] + " your move exceeds 100.So, this move is not counted!")
                        sum1 = sum1 - x
                elif (i == 1 and error == 0):
                    y = Snake_Ladder((x + sum2))
                    score[i] = y

                    if (x == score[i]):
                        sum2 = sum2 + score[i]

                    elif (x != score[i]):
                        sum2 = score[i]

                    if sum2 == 100:
                        print("\t\t\t\t BRAVO!!! " +
                              player[i] + " WINS THIS GAME!!!")
                        k = k + 1
                        break
                    elif sum2 > 100:
                        print(
                            player[i] + " you can't exceed 100. So, this move is not counted!")
                        sum2 = sum2 - x

                    # FINAL display of scores in scoreboard.
                    print("\t\t\t\t\t\t\t\t\t" +
                          str(sum1) + "\t\t\t\t" + str(sum2))
                    i = i - 2

            # INVALID message pops up for every irrelevant user input.
            else:
                print("\nINVALID INPUT!!! Please try to make a valid input.\nValid Input---> ROLL or R.\n"
                      "TRY AGAIN!!! ")
                i = i - 1
            i = i + 1

# This Manual_mode() is use to take relevant input between 1-20 and executes the complete game in Manual_mode.
# Similar blocks of code as of the Auto_mode is present here,so only changes are commented.


def Manual_mode(name_1, name_2):
    i = 0
    player = [name_1, name_2]
    score = [0, 0]
    sum1 = 0
    sum2 = 0
    k = 0
    error = 1

    while i < 2:
        if (k == 0):
            m = input(player[i] + " enter your number :")

        if (m == 'Q' or m == 'q' or m == 'exit' or m == 'EXIT'):
            error = 0
            q = input(player[i] + " Are u sure to quit this Game??? Your opponent will WIN if you do so!!\n"
                                  "Type 'YES' to quit or 'RESUME' to continue the Game : ")
            if (q == 'YES' or q == 'yes' or q == 'Yes'):
                print("\n" + player[i] + " EXITS the game ")
                if (i == 0):
                    print("\t\t\t\t\t" + player[i + 1] + " You WON!!!")
                elif (i == 1):
                    print("\t\t\t\t\t" + player[i - 1] + " You WON!!!")
                break
            elif (q == 'RESUME' or q == 'resume' or q == 'Resume'):
                error = 1
                continue

        # CONVERTS the String no. input to Integer formate.
        if (m.isdigit()):
            g = m
            x = int(g)
            if (1 <= x <= 20):
                error = 0

                if (i == 0 and error == 0):
                    y = Snake_Ladder((x + sum1))
                    score[i] = y
                    if (x == score[i]):
                        sum1 = sum1 + score[i]
                    elif (x != score[i]):
                        sum1 = score[i]
                    if sum1 == 100:
                        print("\t\t\t\t BRAVO!!! " +
                              player[i] + " WINS THE GAME!!!")
                        k = k + 1
                        break
                    elif sum1 > 100:
                        print(
                            player[i] + " you can't exceed 100.So, this move is not counted!")
                        sum1 = sum1 - x
                elif (i == 1 and error == 0):
                    y = Snake_Ladder((x + sum2))
                    score[i] = y
                    if (x == score[i]):
                        sum2 = sum2 + score[i]
                    elif (x != score[i]):
                        sum2 = score[i]
                    if sum2 == 100:
                        print("\t\t\t\t BRAVO!!! " +
                              player[i] + " WINS THIS GAME!!!")
                        k = k + 1
                        break
                    elif sum2 > 100:
                        print(
                            player[i] + " you can't exceed 100.So, this move is not counted!")
                        sum2 = sum2 - x
                    print("\t\t\t\t\t\t\t\t\t" +
                          str(sum1) + "\t\t\t\t" + str(sum2))
                    i = i - 2
            else:
                print("\nINVALID INPUT!!! Please try to make a valid input.\nValid Input---> Number between 1 to 20.\n"
                      "TRY AGAIN!!! ")
                i = i - 1

        # POPS up if user accidentally gives a alphabet or special character.
        elif (error >= 1):
            print("\n NO ALPHABETS OR SPECIAL CHARC. INPUT!!!\n"
                  " Please enter any number between 1 to 20.\n"
                  " TRY AGAIN!!! ")
            i = i - 1
        error = error + 1
        i = i + 1

# Snake_Ladder() always returns the updated score everytime it is called.


def Snake_Ladder(num):
    Current_pos = 0
    Current_pos = Current_pos + num

    # POSITIONS of Snake & Ladders in game.
    Snake_pos = {17: 7, 54: 34, 62: 19, 98: 79}
    Ladder_pos = {3: 38, 24: 33, 42: 93, 72: 84}

    key = Current_pos
    if key in Snake_pos:
        Final_pos = Snake_pos[key]
        print("-->OOPs!!! Snake took u down")
    elif key in Ladder_pos:
        Final_pos = Ladder_pos[key]
        print("-->Wohoo!!! you got a ladder")
    else:
        Final_pos = Current_pos

    return Final_pos


# MODE activation and calling of respective function.
if ((Game_mode == "AUTO") or (Game_mode == "auto") or (Game_mode == "Auto")):
    z = 1
    print("\n\t\t\t ###---- Let the battle begin ----###")
    print("\t\t\t\t  " + player_1 + " VS " + player_2)
    print("\n\t\t\t  <<<---AUTO MODE activated--->>>")
    print("***NOTE : Type 'roll' or Press 'R' to play your turn ")
    print("\t\t\t\t\t\t\t\t" + "\t  <<<==SCOREBOARD==>>>")
    print("\t\t\t\t\t\t\t\t" + player_1 + "\t\t\t\t" + player_2)
    Auto_mode(player_1, player_2)

# MODE activation and calling of respective function.
if ((Game_mode == "MANUAL") or (Game_mode == "manual") or (Game_mode == "Manual")):
    z = 1
    print("\n\t\t\t ###---- Let the battle begin ----###")
    print("\t\t\t\t  " + player_1 + " VS " + player_2)
    print("\n\t\t\t  <<<---MANUAL MODE activated--->>>")
    print("***NOTE :Players are requested to enter any number between 1 to 20.")
    print("\t\t\t\t\t\t\t\t" + "\t  <<<==SCOREBOARD==>>>")
    print("\t\t\t\t\t\t\t\t" + player_1 + "\t\t\t\t" + player_2)
    Manual_mode(player_1, player_2)

# POPs up if player gives irrelevant/wrong input while seleting mode.
elif(z == 0):
    print("\n\t\t\t WRONG MODE!!! \tGame terminated!! \n\t\t\t\t Restart game!")
# End-message to the player.
if(z != 0):
    print(" \n\t\t\t\t\t***----GAME OVER----***")
    print("\t\t\t--Thanks for playing!!! Hope you have enjoyed the Game.--")
