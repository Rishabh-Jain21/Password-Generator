import random
import string


def password_generator():
    try:
        n = int(input("Enter password length minimum(8): "))
        if n < 8:
            print("Invalid length")
            password_generator()
        else:
            password = random.choices(
                string.ascii_letters+string.digits+string.punctuation+string.punctuation, k=n)
            print("".join(password))
    except:
        print("Invalid input")
        password_generator()


password_generator()
