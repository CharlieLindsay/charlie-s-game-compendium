"""Connect Four Function Definition File."""
def connectfour():
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
    print("Welcome to Connect 4!")
    while valid is False:  # Keeps going until the user has chosen a valid input
        print("\np - play  l - leaderboard  q - quit")
        choice = input("What would you like to do? ").lower()
        if choice == "p" or choice == "play":
            valid = True
        elif choice == "l" or choice == "leaderboard":
            try:
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
                            elif mode == "wins":
                                if leaderboard[i] != "&":
                                    current_score += str(leaderboard[i])  # Adds the current score to a string in case it is more than single digit
                                elif leaderboard[i] == "&":
                                    mode = "name"
                                    current_score = int(current_score)
                                    if current_score > fifth_value:
                                        fifth = current
                                        fifth_value = current_score
                                    if current_score > fourth_value:
                                        fifth_value = fourth_value
                                        fifth = fourth
                                        fourth = current
                                        fourth = current_score
                                    if current_score > third_value:
                                        fifth = fourth
                                        fifth_value = fourth_value
                                        fourth_value = third_value
                                        fourth = third
                                        third = current
                                        third_value = current_score
                                    if current_score > second_value:
                                        fifth = fourth
                                        fifth_value = fourth_value
                                        fourth_value = third_value
                                        fourth = third
                                        third = second
                                        third_value = second_value
                                        second = current
                                        second_value = current_score
                                    if current_score > first_value:  # If the current checking score is higher than the current best, all the leaderboard moves down
                                        fifth = fourth
                                        fifth_value = fourth_value
                                        fourth_value = third_value
                                        fourth = third
                                        third = second
                                        third_value = second_value
                                        second = first
                                        second_value = first_value
                                        first = current
                                        first_value = current_score
                                    current_score = ""
                                    current = ""
                        print(first)        
            except FileNotFoundError:
                print("Sorry, there was an error loading the data!")  # Ensures the script doesn't crash when failing to access a file
        elif choice == "q" or choice == "quit":
            valid = True
        else:
            print("Sorry, I don't know that one!")
connectfour()