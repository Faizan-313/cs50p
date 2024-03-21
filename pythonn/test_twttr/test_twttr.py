from twttr import shorten

def main():
    test_str()
    test_numbers()

def test_str():
    assert shorten("hello world") == "hll wrld"
    assert shorten("VOWEL") == "VWL"

def test_numbers():
    assert shorten("1234") == "1234"

def test_pun():
    assert shorten(".,?!") == ".,?!"
    
if __name__ == "__main__":
    main()
