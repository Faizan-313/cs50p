grocery = {}

while True:
    try:
        item = input().upper()

        #check if item is already in the dict , if true than increment the value
        if item in grocery:
            grocery[item] += 1

        #if not than add it with value 1
        else:
            grocery[item] = 1
    except EOFError:
        break

 #print the list in sorted and values first order
for item in sorted(grocery.keys()):
    print(grocery[item],item)


