from validator_collection import validators, checkers, errors

def main():
    email = input("What is your email: ")
    try:
        email_is_valid = validators.email(email)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
