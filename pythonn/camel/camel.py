#prompt user for camel case
c = input('camelcase: ')

#transform it into snake case and print snake case
print('snake_case: ',end='')
for s in c:
    if s in s.upper():
        print('_',end="")
        print(s.lower(),end="")
    else:
        print(s,end='')
print()
