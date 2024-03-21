from seasons import validate

def main():
    test_check_birthdate()
    test_bad()

def test_check_birthdate():
    assert validate('2021-08-12') == 'Five hundred twenty-five thousand, six hundred minutes'
    assert validate('2020-08-12') == 'One million, fifty-one thousand, two hundred minutes'

def test_bad():
    with pytest.raises(SystemExit):
        validate('2020-8-12')

if __name__ == "__main__":
    main()



