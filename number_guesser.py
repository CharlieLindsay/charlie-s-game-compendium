def numberguesser():
    import os
    clear = lambda: os.system('clear')
    clear()
    LEADERBOARD_AMOUNT = 5
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
    mode = "name"  # Leaderboard uses to track whether currently checking for name or score
    print("Welcome to Number Gusser!")
    while valid is False:  # Keeps going until the user has chosen a valid input
        print("\np - play  l - leaderboard  q - quit")
        choice = input("What would you like to do? ").lower()
        if choice == "p" or choice == "play":
            valid = True
        elif choice == "l" or choice == "leaderboard":
            try:
                with open("number_guesser_leaderboard.txt") as f:  # (Attempts) opening the leaderboard data file
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
                        print("===LEADERBOARD===")
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
                        print(name_column)
                        print(first+first_gap+str(first_value))
                        print(second+second_gap+str(second_value))
                        print(third+third_gap+str(third_value))
                        print(fourth+fourth_gap+str(fourth_value))
                        print(fifth+fifth_gap+str(fifth_value))
            except FileNotFoundError:
                print("Sorry, there was an error loading the data!")  # Ensures the script doesn't crash when failing to access a file
        elif choice == "q" or choice == "quit":
            valid = True
        else:
            print("Sorry, I don't know that one!")
numberguesser()