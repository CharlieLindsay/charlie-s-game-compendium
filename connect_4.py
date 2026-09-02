def connectfour():
    valid = False
    while valid is False:
        print("Welcome to Connect 4!\np - play  l - leaderboard")
        choice = input("What would you like to do? ")
        if choice == "p" or choice == "play":
            valid = True
            print("Playing Connect 4")
        elif choice == "l" or choice == "leaderboard":
            print("Opening Leaderboard")
        else:
            print("Sorry, I don't know that one!")