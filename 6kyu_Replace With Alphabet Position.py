#----------------------------------------------------------My Solution----------------------------------

import re

def alphabet_position(text):
    #init
    tick = 1 
    dic = {}
    
    #-----------------------------Create Dictionary------------------------------
    #non-upper
    def range_char(start, stop):
        return (chr(n) for n in range(ord(start), ord(stop) + 1))
    for character in range_char("a", "z"):
        dic[character] = tick
        tick += 1
    tick = 1
    #upper 
    def range_char(start, stop):
        return (chr(n) for n in range(ord(start), ord(stop) + 1))
    for character in range_char("A", "Z"):
        dic[character] = tick
        tick += 1
    #-----------------------------------------------------------------------------
    
    #create an list of potion_letter
    list_char = []
    
    #for every letter...
    for i in text:
        #if the letter is in dictionary
        if i in dic:
            #give the position in the list
            list_char.append(dic[i])
            
    #bring all into an string 
    answer = ' '.join(map(str, list_char))
    return answer
  
#---------------------------------------------------------------------Testfile from Taskgiver---------------------------------

from random import randint
test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

number_test = ""
for item in range(10):
    number_test += str(randint(1, 9))
test.assert_equals(alphabet_position(number_test), "")
