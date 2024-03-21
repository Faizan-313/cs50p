#loop for continues prompts
while True:
    try:
        #prompt and split x and y and check if not x is > y
        x , y = (input('Fraction: ')).split('/')
        x , y = int(x),int(y)

        #if condition is true than do the math ouside loop
        if x <= y:
            r_o = round((x/y)*100)
            break
            
    #if these errors occur than prompt the user again until the user prompts right values
    except (ValueError,ZeroDivisionError):
        pass
#print fuel percentage accordingly
if r_o <= 1:
    print('E')
elif r_o >= 99:
    print('F')
else:
    print(f'{r_o}%')

