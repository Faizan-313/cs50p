def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #checks if it does not starts with  two letters and if no. of elements is < 2 and > 6
    #and if any special symbols and spaces are present
    if  len(s) < 2 or len(s) > 6 or s[0:2].isalpha() == False  or s.isalnum() == False:
        return False

    #checks if first number is 0
    #checks if any number is in between the letters
    c = 0
    for i in range(len(s) - 1):
        if s[i].isalpha() == False:
            if s[i] == '0' or s[i+1].isalpha() == True:
                c += 1
    if c > 0:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
