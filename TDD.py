from RCC import encrypt, decrypt

def tests():

    #Test 1 - empty string
    assert encrypt("", 2) == "", "Test 1 - empty string failed"

    #Test 2 - single letter
    assert encrypt("A", 1) == "B", f"Test 2 - single letter failed"

    print("All tests passed")

tests()