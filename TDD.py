from RCC import encrypt, decrypt

def tests():

    # Test 1 - empty string
    assert encrypt("", 2) == "", "Test 1 - empty string - failed"

    # Test 2 - single letter
    assert encrypt("A", 1) == "B", "Test 2 - single letter - failed"

    # Test 3 - multiple letters
    assert encrypt("AA", 1) == "BC", "Test 3 - multiple letters - failed"

    # Test 4 - non-alphabetic character
    assert encrypt("A A", 1) == "B C", "Test 4 - non-alphabetic characters - failed"

    # Test 5 - Case sensitive
    assert encrypt("Aa", 1) == "Bc", "Test 5 - case sensitice letters - failed"

    # Test 6 - Alphabet wrapping 
    assert encrypt("Z", 1) == "A", "Test 6 - alphabet wrapping - failed"

    # Test 7 - Decryption 
    assert decrypt("CE", 2) == "AA", "Test 7 - decrypt - failed"

    print("All tests passed")

tests()