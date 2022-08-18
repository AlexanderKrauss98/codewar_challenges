#-------------------------------------------------------My Solution-----------------------------------

import gc
def sum_dig_pow(a, b):
    #initial
    range_list = []
    result = []
    #create list of Ranges
    for i in range(a,b+1):
        range_list.append(i)
    #for every integer in range...
    for i in range_list:
        #create temporary list with digits of every range
        string_curent = [int(digit) for digit in str(i)]
        #initial
        summe = 0
        exponent = 1
        #for every digit...
        for b in string_curent:
            summe += b ** exponent
            exponent += 1 
        if summe == i:
            result.append(i)
            
        #hold savespace. without this you would use to many ram
        del summe
        del exponent
        del string_curent
                
    return result

    #hold savespace. without this you would use to many ram
    del range_list
    gc.collect()
 
#------------------------------------------------------------------------------Testfile from Taskgiver--------------------------------------

from solution import sum_dig_pow
import codewars_test as test

@test.describe("Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!")
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals( sum_dig_pow(1, 10), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        test.assert_equals(sum_dig_pow(1, 100), [1, 2, 3, 4, 5, 6, 7, 8, 9, 89])
        test.assert_equals(sum_dig_pow(10, 89),  [89])
        test.assert_equals(sum_dig_pow(10, 100),  [89])
        test.assert_equals(sum_dig_pow(90, 100), [])
