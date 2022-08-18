#--------------------------------------------------------------My Solution-----------------------------------------------------

import re

def solution(s):
    return re.sub( '(?=[A-Z])',' ', s )

#------------------------------------------------------------Testfile from Taskgiver------------------------------------------

test.assert_equals(solution("helloWorld"), "hello World")
test.assert_equals(solution("camelCase"), "camel Case")
test.assert_equals(solution("breakCamelCase"), "break Camel Case")
