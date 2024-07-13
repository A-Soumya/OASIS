import random
import string

def generate_password(length,use_let,use_num,use_sym):
    characters=""
    if use_let:
        characters+=string.ascii_letters
    if use_num:
        characters+=string.digits
    if use_sym:
        characters+=string.punctuation
    if not characters:
        return "No character types selected. Please try again."
    password=""
    for _ in range(length):
        password+=random.choice(characters)
    return password
def main():
    print("Welcome to the Password Generator")

    length=int(input("Enter the desired length of the password:"))
    use_let=input("Include letters (y/n)?").lower()=='y'
    use_num=input("Include numbers (y/n)?").lower()=='y'
    use_sym=input("Include symbols (y/n)?").lower()=='y'

    password = generate_password(length,use_let,use_num,use_sym)
    print("Generated Pasword",password)

if __name__=="__main__":
    main()
