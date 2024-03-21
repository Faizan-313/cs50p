from plates import is_valid

def main():
    test_letter_count()
    test_starting_letters()
    test_middle_letters()
    test_firstno_used()
    test_special_symbols()

def test_letter_count():
    assert is_valid("AA") == True
    assert is_valid("abs") == True
    assert is_valid("abcdefg") == False
    assert is_valid("S") == False

def test_starting_letters():
    assert is_valid("a1") == False
    assert is_valid("4s") == False
    assert is_valid("56") == False
    assert is_valid("ER") == True

def test_middle_letters():
    assert is_valid("asdf2") == True
    assert is_valid("SAH34f") == False
    assert is_valid("ssd4f") == False

def test_firstno_used():
    assert is_valid("sad01") == False
    assert is_valid("ASF10") == True

def test_special_symbols():
    assert is_valid("sad f") == False
    assert is_valid("HF!.") == False

if __name__ == "__main__":
    main()
