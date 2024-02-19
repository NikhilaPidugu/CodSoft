import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("Your Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of your password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer")
    password = generate_password(length)
    print(f"\nYour password is : {password}")

if __name__ == "__main__":
    main()
