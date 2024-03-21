import sys
from PIL import Image,ImageOps

def main():
    check_input()
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        exit("Input does not exist")
    shirtfile = Image.open("shirt.png")
    size = shirtfile.size
    image =ImageOps.fit(imagefile,size)
    image.paste(shirtfile,shirtfile)
    image.save(sys.argv[2])



def check_input():
    end = ["jpg", "jpeg","png" ]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        exit("Too many command-line arguments")
    a,x = (sys.argv[1]).split(".")
    b,y = (sys.argv[2]).split(".")
    if x.lower() not in end:
        exit("Invalid input")
    elif y.lower() not in end:
        exit("Invalid output")
    if x.lower() != y.lower():
        exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
