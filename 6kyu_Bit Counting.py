#---------------------------------------My Solution-------------------------------

def count_bits(n):   
    temp = format(n, "b")   #create "b"incode     
    x = [int(a) for a in str(temp)]   #bring bin code into a list    
    return (x.count(1))   #counting 1 from list
  
#-------------------------------------Testfile Client----------------------

import codewars_test as test
from solution import count_bits

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(count_bits(0), 0)
        test.assert_equals(count_bits(4), 1)
        test.assert_equals(count_bits(7), 3)
        test.assert_equals(count_bits(9), 2)
        test.assert_equals(count_bits(10), 2)
