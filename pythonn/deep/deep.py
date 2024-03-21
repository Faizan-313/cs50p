#prompt user for answer
question = input('What is the answer to the Great Question of Life, the Universe and Everything? ')

#correct the users input
question = question.lower().strip()

#equating the users input
if question == "42" or question == "forty-two" or question == "forty two":
    print("Yes")
else:
    print("no")