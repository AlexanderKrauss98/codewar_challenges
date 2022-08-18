#---------------------------------------------------------Solution-------------------------------------

def count(string):
    result = {}        #we want an set is ordered
    if len(string) == 0:  #if string is empty  
        return result
    else:        
        splitted = list(string)   #split string into a list       
        for i in splitted:  #for every character in the list...            
            if i not in result:   # if the character not already in result                
                result[i] = splitted.count(i) #add the character as a Key with the count of Character in the list as item
            else:              
                pass  #is the caharacter already in the list, pass
    return result

#-----------------------------------------------------Testfile from Taskgiver------------------------

test.assert_equals(count('aba'), {'a': 2, 'b': 1})
test.assert_equals(count(''), {})
