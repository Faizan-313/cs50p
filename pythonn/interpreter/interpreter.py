#prompt the user for expression
exp = input('Expression: ')

x,y,z = exp.split(' ')
x,z= float(x),float(z)
match y:
    case '+':
        print(x+z)
    case '-':
        print(x-z)
    case '*':
        print(x*z)
    case '/':
        print(x/z)
    case _:
        print('invalid expression')