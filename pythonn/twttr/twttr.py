
#prompt for input
def main():
    s = input('Input: ')
    message = shorten(s)
    print('Output: '+ message)


#extracting vowels
def shorten(s):
    word_without_vowel = ""
    for c in s:
        if c not in ['a','A','e','E','I','i','O','o','u','U']:
            word_without_vowel += c
    return word_without_vowel

if __name__ == "__main__":
    main()
