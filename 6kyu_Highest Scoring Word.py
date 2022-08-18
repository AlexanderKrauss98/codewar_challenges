#---------------------------------------------------------------------------Solution---------------------------------------------------------

def high(sentence):    
    #-----------------------------Create Dictionary----{Char : Position}----------------
    tick = 1 
    dic = {}
    def range_char(start, stop):
        return (chr(n) for n in range(ord(start), ord(stop) + 1))
    for character in range_char("a", "z"):
        dic[character] = tick
        tick += 1
    #-----------------------------Count----------------------------------------
    words = sentence.split() #split sentence into words
    
    bigest_count = 0
    bigest_word = None
    
    for word in words: #for every word...
        temp_count = 0 #reset counter        
        temp_list_char = [] #create list of Char for every Word         
        for c in word: 
            temp_list_char.append(c)            
        for c in temp_list_char:  # add count of position in dic to reset counter 
            temp_count += dic.get(c)             
        if temp_count > bigest_count: # Create new Leader if the count is the biggest jet
            bigest_word = word
            bigest_count = temp_count
    
    return bigest_word
  
#------------------------------------------------------------------Testfile Taskgiver----------------------------------------------------

import codewars_test as test
from solution import high

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
        test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
        test.assert_equals(high('take me to semynak'), 'semynak')
        test.assert_equals(high('aa b'), 'aa')
        test.assert_equals(high('b aa'), 'b')
        test.assert_equals(high('bb d'), 'bb')
        test.assert_equals(high('d bb'), 'd')
        test.assert_equals(high("aaa b"), "aaa")
