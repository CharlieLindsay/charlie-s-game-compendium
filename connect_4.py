"""Connect Four Function Definition File."""
def connectfour():
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
    print("Welcome to Connect 4!")
    with open("connect_four_leaderboard.txt") as f:  # (Attempts) opening the leaderboard data file
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
            row0 = [0,0,0,0,0,0,0]
            row1 = [0,0,0,0,0,0,0]
            row2 = [0,0,0,0,0,0,0]
            row3 = [0,0,0,0,0,0,0]
            row4 = [0,0,0,0,0,0,0]
            row5 = [0,0,0,0,0,0,0]
            current_player = 2
            winner = False
            turns = 0
            while winner is False:
                clear()
                row = ""
                for i in range(7):
                    if row0[i] == 0:
                        row += "."
                    elif row0[i] == 1:
                        row += "X"
                    elif row0[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(7):
                    if row1[i] == 0:
                        row += "."
                    elif row1[i] == 1:
                        row += "X"
                    elif row1[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(7):
                    if row2[i] == 0:
                        row += "."
                    elif row2[i] == 1:
                        row += "X"
                    elif row2[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(7):
                    if row3[i] == 0:
                        row += "."
                    elif row3[i] == 1:
                        row += "X"
                    elif row3[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(7):
                    if row4[i] == 0:
                        row += "."
                    elif row4[i] == 1:
                        row += "X"
                    elif row4[i] == 2:
                        row += "O"
                print(row)
                row = ""
                for i in range(7):
                    if row5[i] == 0:
                        row += "."
                    elif row5[i] == 1:
                        row += "X"
                    elif row5[i] == 2:
                        row += "O"
                print(row)
                valid_turn = False
                turns += 1
                if turns >= 8:
                    winner_announced = input(f"Has {current_player} got 4 in a row (N/y)? ").lower()
                    if winner_announced == "y":
                        winning_player = current_player
                        winner = True
                        valid_turn = True
                if current_player == 2:
                    current_player = 1
                else:
                    current_player = 2
                while valid_turn is False:

                    if winner != True:
                        print(f"Player {current_player}'s Turn.")
                        column = (int(input("Choose a column: "))-1)
                        if row5[column] == 0:
                            if current_player == 1:
                                row5[column] = 1
                            else:
                                row5[column] = 2
                            valid_turn = True
                        elif row4[column] == 0:
                            if current_player == 1:
                                row4[column] = 1
                            else:
                                row4[column] = 2
                            valid_turn = True
                        elif row3[column] == 0:
                            if current_player == 1:
                                row3[column] = 1
                            else:
                                row3[column] = 2
                            valid_turn = True
                        elif row2[column] == 0:
                            if current_player == 1:
                                row2[column] = 1
                            else:
                                row2[column] = 2
                            valid_turn = True
                        elif row1[column] == 0:
                            if current_player == 1:
                                row1[column] = 1
                            else:
                                row1[column] = 2
                            valid_turn = True
                        elif row0[column] == 0:
                            if current_player == 1:
                                row0[column] = 1
                            else:
                                row0[column] = 2
                            valid_turn = True
                        else:
                            print("Sorry, there is no space on that column!")
                        """
                        in_a_row = 0
                        for i in range(7):
                            
                            if row0[i] == 1:
                                try:
                                    if row1[i-1] != 1 and row1[i+1] != 1:
                                        in_a_row += 2
                                except IndexError:
                                    try:
                                        if row1[i-1] == 1:
                                            in_a_row += 2
                                    except IndexError:
                                        try:
                                            if row == 1:
                                                in_a_row += 2
                                        except:
                                            in_a_row += 1
                        """
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
                    with open("connect_four_leaderboard.txt", "w") as f:
                        f.write(leaderboard)
                    break
                
            if exists == False:
                with open("connect_four_leaderboard.txt", "a") as f:
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
