import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    exit("Too many command-line arguments")
x = (sys.argv[1]).endswith(".py")       #x = .py
if x == False:                        #if x contains .py
    exit("Not a Python file")
line_count = 0
try:
    with open(sys.argv[1],"r") as file:
        for line in file:
            if line.strip().startswith("#") or line.isspace():      #for blank line and comments
                continue
            line_count += 1
except FileNotFoundError:
    exit("File does not exist")
print(line_count)
