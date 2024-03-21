import inflect

p = inflect.engine()
#create list to keep the track of names
name = []

while True:
    try:
        #get users input and add it to list
        x = input("Name: ")
        name.append(x)

        #create new line and stop the loop
    except EOFError:
        print()
        break

#printing using inflect pmodule
output = p.join(name)
print("Adieu, adieu, to "+output)


