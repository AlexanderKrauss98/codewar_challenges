#--------------------------------------------------------------My Solution--------------------------------

def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
          
#-------------------------------------------------------------Test Client---------------------------------

import codewars_test as test
from solution import stray

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(stray([1, 1, 1, 1, 1, 1, 2]), 2)
        test.assert_equals(stray([2, 3, 2, 2, 2]), 3)
        test.assert_equals(stray([3, 2, 2, 2, 2]), 3)
