import os

# Red - \u001b[31m
# Blue - \u001b[34m
# White - \u001b[37m
# Cyan -\u001b[36m
# Cyan is easier to read than Blue - may add a colour picker later

#The grid has 6 rows and 7 columns
#| | | | | | | |
#| | | | | | | |
#| |0| | | | | |
#| |0| | | |0| |
#| |0| |0| |0| |
#|0|0|0|0| |0|0|
#|1|2|3|4|5|6|7|

os.system("cls||clear")

# red_token = "\u001b[31m0\u001b[37m"
# blue_token = "\u001b[36m0\u001b[37m"
row1 = [" ", " ", " ", " ", " ", " ", " ",]
row2 = [" ", " ", " ", " ", " ", " ", " ",]
row3 = [" ", " ", " ", " ", " ", " ", " ",]
row4 = [" ", " ", " ", " ", " ", " ", " ",]
row5 = [" ", " ", " ", " ", " ", " ", " ",]
row6 = [" ", " ", " ", " ", " ", " ", " ",]
grid_rows = [row1, row2, row3, row4, row5, row6,]
turn_counter = 0
win = 0

def show_grid():
    # Prints the grid with whatever tokens are in it
    print("|{}|{}|{}|{}|{}|{}|{}|".format(row6[0], row6[1], row6[2], row6[3], row6[4], row6[5], row6[6]))
    print("|{}|{}|{}|{}|{}|{}|{}|".format(row5[0], row5[1], row5[2], row5[3], row5[4], row5[5], row5[6]))
    print("|{}|{}|{}|{}|{}|{}|{}|".format(row4[0], row4[1], row4[2], row4[3], row4[4], row4[5], row4[6]))
    print("|{}|{}|{}|{}|{}|{}|{}|".format(row3[0], row3[1], row3[2], row3[3], row3[4], row3[5], row3[6]))
    print("|{}|{}|{}|{}|{}|{}|{}|".format(row2[0], row2[1], row2[2], row2[3], row2[4], row2[5], row2[6]))
    print("|{}|{}|{}|{}|{}|{}|{}|".format(row1[0], row1[1], row1[2], row1[3], row1[4], row1[5], row1[6]))
    print("|1|2|3|4|5|6|7|")

def column_choice():
    c_choice = 0
    while c_choice == 0:
        c_choice = input("\u001b[3{}mPlayer {}\u001b[37m please choose a column: ".format(str(1 + (player_turn * 5)), str(player_turn + 1)))
        if c_choice.isnumeric() == False:
            print("Please write your choice as a number")
            print()
            c_choice = 0
        elif int(c_choice) < 1 or int(c_choice) > 7:
            print("That's not a valid column")
            print()
            c_choice = 0
        else:
            c_choice = int(c_choice)
            if row6[c_choice - 1] == " ":
                token_placed = 0
                for i in grid_rows:
                    if i[c_choice - 1] == " " and token_placed == 0:
                        i[c_choice - 1] = "\u001b[3{}m0\u001b[37m".format(str(1 + (player_turn * 5)))
                        token_placed = 1
            else:
                print("That column is full")
                print()
                c_choice = 0


print()
print("Let's Play \u001b[36mConnect\u001b[31m 4\u001b[37m")
print()
show_grid()
print()
input("Press <ENTER> to Continue")

while turn_counter < 42 and win == 0:
    player_turn = turn_counter % 2
    turn_counter = turn_counter + 1
    os.system("cls||clear")
    print()
    print("Turn {} \u001b[3{}mPlayer {}\u001b[37m's Move".format(turn_counter, str(1 + (player_turn * 5)), str(player_turn + 1)))
    print()
    show_grid()
    print()
    column_choice()
    os.system("cls||clear")
    print()
    print("Turn {} \u001b[3{}mPlayer {}\u001b[37m's Move".format(turn_counter, str(1 + (player_turn * 5)), str(player_turn + 1)))
    print()
    show_grid()
    print()
    win_check = input("Did you win? ")
    if win_check.lower() == "yes":
        win = 1