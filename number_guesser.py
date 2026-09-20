def numberguesser():
    import os
    import random

    leaderboardfile = "number_guesser_leaderboard.txt"
    if not os.path.exists(leaderboardfile):
        open(leaderboardfile, "w").close()
    clear = lambda: os.system('clear')  # Allows me to quickly clear the terminal
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
    names = []
    mode = "name"  # Leaderboard uses to track whether currently checking for name or score


    with open("number_guesser_leaderboard.txt") as f:  # (Attempts) opening the leaderboard data file
        leaderboard = f.readline()
        length_leaderboard = len(leaderboard)
        if length_leaderboard == 0:  # Checks if the leaderboard has no data yet
            print("No leaderboard data so far!")
            name_column = "Name"
            first = second = third = fourth = fifth = ""
            first_value = second_value = third_value = fourth_value = fifth_value = 0
            first_gap = second_gap = third_gap = fourth_gap = fifth_gap = ""
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
                name_column += "High Score"
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
    
    print("Welcome to Number Guesser!")
    print("Number Guesser is a simple game where you first choose 2 numbers to guess between (at least 100 apart).\n"
          "You then guess the number which will be randomly generated. Once you get it correct, your score is 20-guesses (lowest score is 1).\n"
          "Have fun!")
    while valid is False:  # Keeps going until the user has chosen a valid input
        print("\np - play  l - leaderboard  q - quit")
        choice = input("What would you like to do? ").lower()
        if choice == "p" or choice == "play":
            score = 20
            clear()
            valid = False
            while valid is False:
                try:
                    lowest = int(input("Enter the lowest possible number: "))
                    valid = True
                except ValueError:
                    print("Must be an integer!")
            highest = lowest
            valid = False
            while valid is False:
                try:
                    highest = int(input("\nEnter the highest possible number: "))
                    if highest < (lowest + 100):
                        print("Must be at least 100 higher than the lowest!")
                    else:
                        valid = True
                except ValueError:
                    print("Must be an integer!")
            number = random.randint(lowest, highest)
            guessed = False
            closest_high = highest
            closest_low = lowest
            while guessed is False:
                clear()
                print(f"You know it is between {closest_low} and {closest_high}.")
                valid = False
                while valid is False:
                    try:
                        guess = int(input("Guess the number: "))
                        valid = True
                    except ValueError:
                        print("Must be an integer!")
                if guess < closest_high and guess > closest_low:
                    if guess > number:
                        if closest_high > guess:
                            closest_high = guess
                        print("That was too high!")
                        if score > 1:
                            score -= 1
                    elif guess < number:
                        if closest_low < guess:
                            closest_low = guess
                        print("That was too low!")
                        if score > 1:
                            score -= 1
                    else:
                        guessed = True
                        print("That is correct!")
                        if score > 1:
                            score -= 1
                else:
                    print("Guess between your known range!")
                if guessed is False:
                    input("Press any key to continue")
            name_player = input(f"What is your name? ")
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
                    old_score = int(leaderboard[times:end])
                    if score > old_score:
                        print("Congratulations beating your previous high score!")
                        leaderboard = leaderboard[:times] + str(score) + leaderboard[end:]
                        with open("number_guesser_leaderboard.txt", "w") as f:
                            f.write(leaderboard)
                    break
            if exists == False:
                with open("number_guesser_leaderboard.txt", "a") as f:
                    f.write(name_player + "$" + str(score) + "&")
        elif choice == "l" or choice == "leaderboard":
            print("===LEADERBOARD===")
            entries = [(first, first_value, first_gap), (second, second_value, second_gap), (third, third_value, third_gap), (fourth, fourth_value, fourth_gap), (fifth, fifth_value, fifth_gap)]
            num_entries = min(LEADERBOARD_AMOUNT, len(names))
            if num_entries == 0:
                print("No leaderboard data so far!")
            else:
                print(name_column)
                for i in range(num_entries):
                    print(entries[i][0]+entries[i][2]+str(entries[i][1]))
        elif choice == "q" or choice == "quit":
            valid = True
        else:
            print("Sorry, I don't know that one!")

#numberguesser()