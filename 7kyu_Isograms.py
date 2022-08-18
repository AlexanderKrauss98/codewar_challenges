#-----------------------------------------------------------------------------My Solution-------------------------------------------------

def is_isogram(string):
    a = True
    #return True if string is empty
    if len(string) == 0:
        return a  
    # if not empty...
    else:
        # bring all character in lower letter
        lower = string.lower()
        #split into list
        lower = lower.split()
        lower_splitted = []    
        for i in lower[0]:
            lower_splitted.append(i)
        #check if they are multiple character
        for i in  lower_splitted: 
            if lower_splitted.count(i) >= 2:
                a = False
        return a 

#----------------------------------------------------------------------Test Client--------------------------------------------

import codewars_test as test
from solution import is_isogram

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():      
        test.assert_equals(is_isogram("Dermatoglyphics"), True )
        test.assert_equals(is_isogram("isogram"), True )
        test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
        test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
        test.assert_equals(is_isogram("isIsogram"), False )
        test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )
