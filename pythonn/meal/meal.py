def main():
    formats = input('What is time format(12 or 24 hr)')
    if formats == '24':
        time = input('What time is it? ')
        t = convert(time)
        if 7 <= t <=8:
            print('Breskfast time')
        elif 12 <= t <= 13:
            print('lunch time')
        elif 18 <= t <= 19:
            print('dinner time')
    else:
        time = input('What time is it? ')
        t ,f = convert_tw(time)
        if f == 'a.m':
            if  7 <= t <=8:
                print('Breskfast time')
        else:
            if 12 <= t < 13 or t == 1:
                print('lunch time')
            elif 6 <= t <= 7:
                print('dinner time')


def convert(t):
        h,m = t.split(':')
        t = float(h) + (float(m)/60)
        return t


def convert_tw(t):
     h,f = t.split(':')
     m,f = f.split(' ')
     t = float(h)+float(m)/60
     return t , f


main()