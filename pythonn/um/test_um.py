from um import count

def main():
    test_befor_um()
    test_after_um()
    test_upper_lower_case()

def test_befor_um():
    assert count('...um hello') == 1
    assert count('hellum') == 0

def test_after_um():
    assert count('um, hello how are you um...') == 2
    assert count('umhasr , i am the um') == 1

def test_upper_lower_um():
    assert count('Um, thanks for the album. ') == 1
    assert count('UM, how are doing. uM, um') == 3

if __name__ == "__main__":
    main()

