from RCC import encrypt, decrypt

def tests():

    #Test 1 - empty string
    assert encrypt("", 2) == "", "Test 1 - empty string - failed"

    #Test 2 - single letter
    assert encrypt("A", 1) == "B", f"Test 2 - single letter - failed"

    # Test 3 - multiple letters
    assert encrypt("AA", 1) == "BC", f"Test 3 - multiple letters - failed"

    # Test 4 - non-alphabetic character
    assert encrypt("A A", 1) == "B C", f"Test 4 - non-alphabetic characters - failed"

    print("All tests passed")

tests()