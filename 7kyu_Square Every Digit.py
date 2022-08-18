#--------------------------------------------------------------------------My Solution-------------------------------------------

def square_digits(num):
    
    #brings input into a list
    x = [int(a) for a in str(num)] 
    
    #concatenate the elements of the list
    tick = 0
    for i in x:
        x[tick] = i**2
        tick += 1
    
    #convert elements back to normal integer    
    def convert(list):
        s = [str(i) for i in list]
        res = int("".join(s))
        return(res)
    return(convert(x))

#----------------------------------------------------------------------------Testfile Client-------------------------------------

import codewars_test as test
from solution import square_digits

@test.describe("Premade tests: ")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(square_digits(9119), 811181)
        test.assert_equals(square_digits(0), 0)
