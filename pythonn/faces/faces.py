#ask uder for input
def main():
    x = input('Input: ')
    x = convert(x)
    print(x)


#defining convert function
def convert(to):
     to = to.replace(':)','🙂')
     to = to.replace(':(','🙁')
     return to

main()