#prompt user for input
x = input("File Name: ").strip().lower()

#print file format  according to users input
if x.endswith(".gif"):
    print('image/gif')
elif x.endswith(".jpg"):
    print('image/jpeg')
elif x.endswith(".jpeg"):
    print('image/jpeg')
elif x.endswith(".pdf"):
    print('application/pdf')
elif x.endswith(".zip"):
    print('application/zip')
elif x.endswith(".txt"):
    print('text/plain')
else:
    print('application/octet-stream')


