print("This is a test python file!")
print("I hope you enjoy!")
readyness = False
while readyness is False:
    answer = input("ARE YOU READY?! ")
    if answer == "yes" or answer == "ye" or answer == "yup" or answer == "true" or answer == "indeed":
        readyness = True
    else:
        print("Okay... then. Let's pause for a minute.\nHow about now?\nAre you ready?\nArE YoU ReAdY?!\n")
name = input("Sweet, in that case let me tell you a story. First off, what is your name? ")
print(f"That's great, {name}! Thanks for listening to my story!")
valid = False
while valid is False:
    age = input("What is your age: ")
    try:
        age = int(age)
        if age < 0 or age > 150:
            print("That can't be right! ;)")
        else:
            valid = True
    except ValueError:
        print("Sorry, that isn't right!")
if age < 13:
    print("Well, young one, welcome to my tale of being Tech Crew at Murrays Bay Primary Production today.")
elif age < 20:
    print("Well, teen, welcome to my tale of being Tech Crew at Murrays Bay Primary Production today.")
else:
    print("Welcome to my tale of being Tech Crew at Murrays Bay Primary Production today.")
print(f"You see, {name}, this is a diabolical situation for a 16 year old such as myself to get into, but I was running the SOUND for a whole production!")
print(f"Even at {age}, I'm sure you can understand just how tiring this is for me, and how it is weird that I am just writing it all out like this...")
experience = input(f"In a few words, what would you, {name}, describe the craziest thing that has happened to you? ")
print(f"You {experience}?! That's epicness maxmimus! You rock!")
hobby = input("What is your favourite thing to do? ")
print("Thank you very much for all that information, now I will be sharing it on the dark web and will be using it for malicious reasons why would you give a random terminal script all your details?")
print("Nah, I'm probably just kidding, first...")
input("Could you tell me your birthdate?")
