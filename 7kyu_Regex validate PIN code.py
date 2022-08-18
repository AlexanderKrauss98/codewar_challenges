#------------------------------------------------------------------------My Solution----------------------------------------

import re

def validate_pin(pin):
    #init
    result = True
    #return pin in list for to check conditions
    list = [x for x in pin]
    #check lengh
    if len(list) < 4 or len(list) == 5 or len(list) > 6:
        #if lengh not correct -> False
        result = False
    else:
        #for every character of pin...
        for i in list:
            #if character is an digit...
            if re.search("\d",i):
                pass
            else:
                # if is not -> result = False
                result = False
    return result
                
#------------------------------------------------------------------Test Client-----------------------------------------------

import codewars_test as test
from solution import validate_pin

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("should return False for pins with length other than 4 or 6")
    def basic_test_cases():    
        test.assert_equals(validate_pin("1"),False, "Wrong output for '1'")
        test.assert_equals(validate_pin("12"),False, "Wrong output for '12'")
        test.assert_equals(validate_pin("123"),False, "Wrong output for '123'")
        test.assert_equals(validate_pin("12345"),False, "Wrong output for '12345'")
        test.assert_equals(validate_pin("1234567"),False, "Wrong output for '1234567'")
        test.assert_equals(validate_pin("-1234"),False, "Wrong output for '-1234'")
        test.assert_equals(validate_pin("-12345"),False, "Wrong output for '-12345'")
        test.assert_equals(validate_pin("1.234"),False, "Wrong output for '1.234'")
        test.assert_equals(validate_pin("00000000"),False, "Wrong output for '00000000'")
