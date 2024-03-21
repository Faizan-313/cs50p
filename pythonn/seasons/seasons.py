from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
     date_text = input("Date of Birth: ")
     validate(date_text)
     y,m,d = date_text.split("-")
     date_of_birth = date(int(y),  int(m), int(d))
     date_of_today = date.today()
     diff = date_of_today - date_of_birth
     total_min = diff.days * 24 * 60
     output = p.number_to_words(total_min, andword="")
     print(output.capitalize() + ' minutes')



def validate(date_txt):
        try:
            date.fromisoformat(date_txt)
        except ValueError:
            sys.exit(1)


if __name__ == "__main__":
    main()
