#-----------------------------------------------------My Solution---------------------------
def is_pangram(s):
    output = True
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in s.lower(): 
            return False
    return output
#----------------------------------------------------Testfile-----------------------------
from solution import is_pangram
import codewars_test as test

@test.describe("sample tests")
def sample_tests():
    
    @test.it("Should return true for a pangram")
    
