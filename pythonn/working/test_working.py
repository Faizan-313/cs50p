from working import convert

def main():
    test_valid_time()
    test_correct_hour()
    test_new_format()

def test_valid_time():
    assert convert('9:60 AM to 5:60 PM') == ValueError
    assert convert('9 AM - 5 PM') == ValueError\
    assert convert('09:00 AM - 17:00 PM') == ValueError

def test_correct_hour():
    assert convert('13:00 AM to 04:00 PM') == ValueError
    assert convert('09:00 AM to 20:00 PM') == ValueError

def test_new_format():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'


if __name__ == "__main__":
    main()
