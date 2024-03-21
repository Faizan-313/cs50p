import re
import sys


def main():
     print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>",s):
        matches = re.search(r"(https?:\/\/(www\.)?youtube\.com\/embed\/)([a-zA-Z_0-9]+)",s)
        if matches:
            url_split = matches.groups()
            return "https://youtu.be/" + url_split[2]


if __name__ == "__main__":
    main()
