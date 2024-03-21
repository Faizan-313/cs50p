def main():
    fraction = input('Fraction: ')
    frac_converted = convert(fraction)
    output = guage(frac_converted)
    print(output)


def convert(fraction):
   #loop for continues prompts
    while True:
        try:
            #prompt and split x and y and check if not x is > y
            x , y = fraction.split('/')
            x = int(x)
            y = int(y)
            f = x / y
            #if condition is true than do the math ouside loop
            if f <= 1:
                p = int(f*100)
                return p
            else:
                fraction = input("fraction: ")
                pass

        #if these errors occur than prompt the user again until the user prompts right values
        except (ValueError,ZeroDivisionError):
            raise

def guage(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
