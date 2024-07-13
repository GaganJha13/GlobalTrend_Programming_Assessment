import random
import string

def generate_random_password(length=12):
    # Define characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices (Python 3.6+)
    password = ''.join(random.choices(characters, k=length))

    return password

# Example usage
random_password = generate_random_password()
print("Random Password:", random_password)
