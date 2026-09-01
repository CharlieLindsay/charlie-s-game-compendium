def name_exists():
    try:
        f = open("user_data.txt")
        name = f.readline()
        return True, name
    except FileNotFoundError:
        return False, ""