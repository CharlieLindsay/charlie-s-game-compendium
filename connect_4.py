def connectfour():
    valid = False
    print("Welcome to Connect 4!")
    while valid is False:
        print("\np - play  l - leaderboard  q - quit")
        choice = input("What would you like to do? ").lower()
        if choice == "p" or choice == "play":
            valid = True
        elif choice == "l" or choice == "leaderboard":
            try:
                f = open("user_data.txt")
                f.readline()
                leaderboard = f.readline()
                length_leaderboard = len(leaderboard)
                print(length_leaderboard)
                if length_leaderboard == 0:
                    print("No leaderboard data so far!")
            except FileNotFoundError:
                print("Sorry, there was an error loading the data!")
        elif choice == "q" or choice == "quit":
            valid = True
        else:
            print("Sorry, I don't know that one!")
connectfour()