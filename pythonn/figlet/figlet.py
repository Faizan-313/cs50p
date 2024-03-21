import sys
import random
from pyfiglet import Figlet

if(len(sys.argv) == 1):
    fontIsRandom = True
elif(len(sys.argv) == 3):
    fontIsRandom = False
else:
    sys.exit("command line argument not expected")

figlet = Figlet()

availableFont = figlet.getFonts()

if fontIsRandom == False:
     if(sys.argv[1] not in ["-f" ,"--Font"]):
        sys.exit("second command line argument incorrect")
     try:
        font = figlet.setFont(font=sys.argv[2])
     except:
        sys.exit("font does not exist")
else:
    font = random.choice(availableFont)

txt = input("Input: ")

print(figlet.renderText(txt))
