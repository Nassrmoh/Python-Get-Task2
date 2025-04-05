# checker.py

def check_name():
    name = input("Write your name: ")
    try:
        if not name.isalpha():
            raise ValueError("Invalid name")
        print(f"Welcome {name}")
        return name
    except ValueError as e:
        print(e)
        return check_name()  # Retry if the name is invalid

def check_email():
    while True:
        email = input("Enter your email: ")
        try:
            username, domain = email.split("@")
            x, y = domain.split(".")
            if not username or not domain or not x or not y:
                raise ValueError("Invalid email structure")
            break
        except ValueError:
            print("Invalid email, please enter a valid email")
    return email