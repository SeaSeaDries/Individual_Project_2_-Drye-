from RCC import encrypt, decrypt

def tests():

    #Test 1 - empty string
    assert encrypt("", 2) == "", "Test 1 - empty string fail"

    print("All tests passed")

tests()