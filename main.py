"""Charlie's Game Compendium."""
import menu
import user_management
thing = False
exists, name = user_management.name_exists()
if exists == True:
    print(f"Welcome back, {name}")
else:
    name = menu.new()
    f = open("user_data.txt", "x")
    f.write(name)
    print(f"Hi, {name}!")