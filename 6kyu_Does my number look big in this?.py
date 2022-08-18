#--------------------------------------------------My Solution---------------------------

def narcissistic(value):  
    x = [int(a) for a in str(value)]  #split integer in List        
    laenge = len(x) #count elements in List
    
    #sum elements**elementscounts
    Summe = 0 
    for i in x:
        Summe += i**laenge
        
    #Output
    if Summe == value: #sum == Value?
        return True 
    else:
        return False
      
#----------------------------------------------Testfile Taskgiver------------------------

test.assert_equals(narcissistic(7), True, '7 is narcissistic');
test.assert_equals(narcissistic(371), True, '371 is narcissistic');
test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')
