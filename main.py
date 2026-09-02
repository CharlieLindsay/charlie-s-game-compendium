"""Charlie's Game Compendium."""
import menu
import user_management
import connect_4
import number_guesser
import tic_tac_toe
thing = False
running = True
exists, name = user_management.name_exists()
if exists == True:
    print(f"Welcome back, {name}")
else:
    name = menu.new()
    f = open("user_data.txt", "x")
    f.write(name)
    print(f"Hi, {name}!")
while running is True:
    print("\nThere are three games to choose from:\n1. Connect 4"
        "\n2. Number Guesser\n3. Tic Tac Toe\n")
    game = input("What game do you choose? ('q' to quit): ").lower()
    if game == "1" or game == "connect 4":
        connect_4.connectfour()
    elif game == "2" or game == "number guesser":
        number_guesser.numberguesser()
    elif game == "3" or game == "tic tac toe":
        tic_tac_toe.tictactoe()
    elif game == "q":
        running = False
    else:
        print("I don't know that one!")
print(f"Thanks for playing, {name}!")