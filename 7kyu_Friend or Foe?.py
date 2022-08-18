#----------------------------------------------------------My Solution---------------------------------

import re
def friend(x):
    Frend_list = []
    pattern = r"^....$"
    for i in x:
        if re.findall(pattern,i):
            Frend_list.append(i)
    return Frend_list
  
#-------------------------------------------------------Test Client-------------------------------------

import codewars_test as test
from solution import friend

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Sample Test Cases')
    def sample_test_cases():
        test.assert_equals(friend(["Ryan", "Kieran", "Mark",]), ["Ryan", "Mark"])
        test.assert_equals(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
        test.assert_equals(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])
  
  
