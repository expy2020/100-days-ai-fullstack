import secrets
import string

SYMBOLS = "!#$%&()*+"


def generate_password(num_letters: int, num_symbols: int, num_numbers: int) -> str:
    if num_letters < 0 or num_symbols < 0 or num_numbers < 0:
        raise ValueError("Character counts cannot be negative.")

    if num_letters + num_symbols + num_numbers < 8:
        raise ValueError("Total password length must be at least 8 characters.")

    password_chars: list[str] = []

    for _ in range(num_letters):
        password_chars.append(secrets.choice(string.ascii_letters))

    for _ in range(num_numbers):
        password_chars.append(secrets.choice(string.digits))

    for _ in range(num_symbols):
        password_chars.append(secrets.choice(SYMBOLS))

    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


try:
    letters_count = int(input("Number of letters: ").strip())
    numbers_count = int(input("Number of numbers: ").strip())
    symbols_count = int(input("Number of symbols: ").strip())

    generated = generate_password(
        num_letters=letters_count,
        num_symbols=symbols_count,
        num_numbers=numbers_count,
    )
    print(f"Your Password: {generated}")
except ValueError as e:
    print(f"Error: {e}")































# import string
# import secrets

# symbols = "!#$%&()*+"  
# def generate_password(num_letters: int, num_symbols: int, num_numbers: int) -> str:
#     if num_letters < 0 or num_symbols < 0 or num_numbers < 0:
#         raise ValueError("Character counts cannot be negative.")
    
#     total_length = num_letters + num_symbols + num_numbers

#     if total_length < 8:
#         raise ValueError("Error: total password length must be at least 8 character")

#     letters = string.ascii_letters
#     numbers = string.digits
      


#     password_char = []

#     for _ in range(num_letters):
#         random_char = secrets.choice(letters)
#         password_char.append(random_char)

#     for _ in range(num_numbers):
#         random_char = secrets.choice(numbers)
#         password_char.append(random_char)

#     for _ in range(num_symbols):
#         random_char = secrets.choice(symbols)
#         password_char.append(random_char)    

#     secrets.SystemRandom().shuffle(password_char)

#     final_password = "".join(password_char) 

#     return final_password


 

# try:
#     letters_count = int(input("enter the number of letters you want in your password: ").strip())
#     numbers_count = int(input("enter the number of numbers you want in your password: ").strip())
#     symbols_count = int(input("enter the number of symbols you want in your password: ").strip())  


#      generated = generate_password(
#          num_letters=letters_count,
#           num_symbols=symbols_count,
#           num_numbers=numbers_count,
#           )
#     print(f"Your Password: {generated}")
# except ValueError as e:
#     print(f"Error: {e}")     