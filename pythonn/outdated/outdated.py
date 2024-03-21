month = ["January",
    "February", "March","April","May","June",
    "July","August","September","October",
    "November","December"]

while True:
    date = input('Date: ').capitalize()
    #if the user inputs the date  as 9/8/1636
    try:
        #split  wrt /
        m,d,y = date.split('/')

        #convert string to integer
        m,d,y = int(m),int(d),int(y)

        #check condition for total no. of months and days in a month(31)
        if m <= 12 and d <= 31:

            #print with index 0 for single digits
            print(f'{y:02}-{m:02}-{d:02}')
            break

    #if the user inputs the date as july 2, 1636
    except ValueError:

        #split wrt space
        if ',' in date:
            date = date.replace(',','')
            m,d,y = date.split(' ')
        else:
            continue

        #check if month is right
        if m in month:

            #change month to its equivalent no.
            m = month.index(m) + 1
            d,y = int(d),int(y)
        else:
            continue

        if d <= 31:
            #print the date
            print(f'{y:02}-{m:02}-{d:02}')
            break
