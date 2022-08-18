#-------------------------------------------------------------------My Solution----------------------------------------

#import re
def solution(string, ending):
    if string.endswith(ending):  #alternativ if re.search('(.*)'+ ending,string):
        return True 
    else:
        return False
      
#------------------------------------------------------------------Testfile Client------------------------------------

test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)
