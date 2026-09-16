"""Tic Tac Toe Function Definition File."""
def tictactoe():
    import os
    clear = lambda: os.system('clear')
    clear()
    LEADERBOARD_AMOUNT = 5
    in_a_row = 0
    largest = 0
    first = ""
    first_value = 0
    second = ""
    second_value = 0
    third = ""
    third_value = 0
    fourth = ""
    fourth_value = 0
    fifth = ""
    fifth_value = 0
    valid = False
    names = []
    mode = "name"  # Leaderboard uses to track whether currently checking for name or score
    print("Welcome to Tic Tac Toe!")
    print("\nHow to play:\n")
    print("Tic Tac Toe (naughts and crosses) is a simple game played in a 3x3 format.\nEach player chooses a row and column to place one of their symbols ("
          "an X or O). The goal is to get 3 in a row before the other player.\nCan be diagonal, vertical, or horizontal in a row.\nHave fun!")
    with open("tic_tac_toe_leaderboard.txt") as f:  # (Attempts) opening the leaderboard data file
        leaderboard = f.readline()
        length_leaderboard = len(leaderboard)
        if length_leaderboard == 0:  # Checks if the leaderboard has no data yet
            print("No leaderboard data so far!")
        else:
            current = ""
            current_score = ""
            for i in range(length_leaderboard):
                if mode == "name":
                    if leaderboard[i] != "$":
                        current += leaderboard[i]
                    elif leaderboard[i] == "$":
                        mode = "wins"
                        names.append(current)
                elif mode == "wins":
                    if leaderboard[i] != "&":
                        current_score += str(leaderboard[i])  # Adds the current score to a string in case it is more than single digit
                    elif leaderboard[i] == "&":
                        mode = "name"
                        current_score = int(current_score)
                        if current_score > first_value:
                            fifth = fourth
                            fifth_value = fourth_value
                            fourth = third
                            fourth_value = third_value
                            third = second
                            third_value = second_value
                            second = first
                            second_value = first_value
                            first = current
                            first_value = current_score
                        elif current_score > second_value:
                            fifth = fourth
                            fifth_value = fourth_value
                            fourth = third
                            fourth_value = third_value
                            third = second
                            third_value = second_value
                            second = current
                            second_value = current_score
                        elif current_score > third_value:
                            fifth = fourth
                            fifth_value = fourth_value
                            fourth = third
                            fourth_value = third_value
                            third = current
                            third_value = current_score
                        elif current_score > fourth_value:
                            fifth = fourth
                            fifth_value = fourth_value
                            fourth = current
                            fourth_value = current_score
                        elif current_score > fifth_value:
                            fifth = current
                            fifth_value = current_score
                        current_score = ""
                        current = ""
            if len(first) > largest:
                largest = len(first)
            if len(second) > largest:
                largest = len(second)
            if len(third) > largest:
                largest = len(third)
            if len(fourth) > largest:
                largest = len(fourth)
            if len(fifth) > largest:
                largest = len(fifth)
            name_column = "Name"
            if largest > 4:
                for i in range(largest-3):
                    name_column += " "
                name_column += "Wins"
            first_gap = " "
            second_gap = " "
            third_gap = " "
            fourth_gap = " "
            fifth_gap = " "
            for i in range(largest-len(first)):
                first_gap += " "
            for i in range(largest-len(second)):
                second_gap += " "
            for i in range(largest-len(third)):
                third_gap += " "
            for i in range(largest-len(fourth)):
                fourth_gap += " "
            for i in range(largest-len(fifth)):
                fifth_gap += " "
    while valid is False:  # Keeps going until the user has chosen a valid input
        print("\np - play  l - leaderboard  q - quit")
        choice = input("What would you like to do? ").lower()
        if choice == "p" or choice == "play":
            valid = True
            row0 = [0,0,0]
            row1 = [0,0,0]
            row2 = [0,0,0]
            current_player = 2
            winner = False
            turns = 0
            tie = False
            turn = 0
            while winner is False:
                clear()
                row = ""
                for i in range(3):
                    if row0[i] == 0:
                        row += "."
                    elif row0[i] == 1:
                        row += "X"
                    elif row0[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(3):
                    if row1[i] == 0:
                        row += "."
                    elif row1[i] == 1:
                        row += "X"
                    elif row1[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(3):
                    if row2[i] == 0:
                        row += "."
                    elif row2[i] == 1:
                        row += "X"
                    elif row2[i] == 2:
                        row += "O"
                print(row)
                if turn >= 5:
                    response = input(f"Has {current_player} won (N/y)? ").lower()
                    if response == "y":
                        winner = True
                        winning_player = current_player
                if winner is False:
                    if turn > 8:
                        tie = True
                        winner = True
                    else:
                        valid_turn = False
                        """
                        turns += 1
                        if turns >= 8:
                            winner_announced = input(f"Has {current_player} got 4 in a row (N/y)? ").lower()
                            if winner_announced == "y":
                                winning_player = current_player
                                winner = True
                                valid_turn = True
                                """
                        if current_player == 2:
                            current_player = 1
                        else:
                            current_player = 2
                        valid_turn = False
                        while valid_turn is False:
                            if winner is False:
                                print(f"Player {current_player}'s Turn.")
                                taken = True
                                while taken is True:
                                    valid = False
                                    while valid is False:
                                        try:
                                            column = int(input("Choose a column (0-2): "))
                                            row = int(input("Choose a row (0-2): "))
                                            if column >= 0 and column <= 2 and row >= 0 and row <= 2:
                                                valid = True
                                            else:
                                                print("Please enter valid values.")
                                        except ValueError:
                                            print("Sorry, all values must be integers!")
                                    if row == 0:
                                        if row0[column] == 0:
                                            row0[column] = current_player
                                            taken = False
                                            valid_turn = True
                                        else:
                                            print("There is already a piece there!")
                                    elif row == 1:
                                        if row1[column] == 0:
                                            row1[column] = current_player
                                            taken = False
                                            valid_turn = True
                                        else:
                                            print("There is already a piece there!")
                                    else:
                                        if row2[column] == 0:
                                            row2[column] = current_player
                                            taken = False
                                            valid_turn = True
                                        else:
                                            print("There is already a piece there!")
                turn += 1
            if tie is True:
                print("It was a tie!")
            else:
                name_player = input(f"What is Player {winning_player}'s name? ")
                exists = False
                for i in range(len(names)):
                    if name_player == names[i]:
                        exists = True
                        amount = names.index(name_player)
                        times = 0
                        passed_names = 0
                        while passed_names < (amount+1):
                            if leaderboard[times] == "$":
                                passed_names += 1
                            times += 1
                        end = leaderboard.index("&", times)
                        new_score = int(leaderboard[times:end]) + 1
                        leaderboard = leaderboard[:times] + str(new_score) + leaderboard[end:]
                        with open("tic_tac_toe_leaderboard.txt", "w") as f:
                            f.write(leaderboard)
                        break
                    
                if exists == False:
                    with open("tic_tac_toe_leaderboard.txt", "a") as f:
                        f.write(name_player + "$" + str(1) + "&")

        elif choice == "l" or choice == "leaderboard":
            print("===LEADERBOARD===")
            print(name_column)
            print(first+first_gap+str(first_value))
            print(second+second_gap+str(second_value))
            print(third+third_gap+str(third_value))
            print(fourth+fourth_gap+str(fourth_value))
            print(fifth+fifth_gap+str(fifth_value))
        elif choice == "q" or choice == "quit":
            valid = True
        else:
            print("Sorry, I don't know that one!")
