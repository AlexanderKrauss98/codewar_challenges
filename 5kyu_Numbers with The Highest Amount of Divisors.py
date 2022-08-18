#NOTE: This code pass all Test but the Runtime is limited on the Side on 12000MS. Normaly its complete if no timelimit would exist. I i would enjoy for Tipps.

#-----------------------------------------------------------------------My Solution-----------------------------------------------------------
def proc_arrInt(listNum):

    Task_1 = len(listNum) #Task 1 
    
    temp_Task_2 = [] #Task 2
    for k in listNum:                         
        if k > 1:                           # ---------------------------------------------
            for i in range(2, int(k/2)+1):  # ---------------------------------------------
                 if (k % i) == 0:           # ------------clasic prime algorithm-----------
                    break                   # ---------------------------------------------
            else:                           # ---------------------------------------------
                temp_Task_2.append(k)       # ---- if its prime. put it into temp list-----
                
    Task_2 = len(temp_Task_2) #count elements of primes 
      
    a = 0 #count of bigest divisor
    b = [] #num with bigest count of divisor 
    for i in listNum: 
        temp_count = 0      
        for d in range (1,i+1): # for 1 - i (range doesnt work exactly for i, so i+1)
            if i%d == 0: 
                temp_count += 1 # temp_count +1 if its divisible               
        if temp_count == a: # add to b if it has the same count of divisor
            b.append(i) 
        elif temp_count > a: # set new leader if temp_count is bigger then the actually a 
            a = temp_count  
            b = [i]
    b.sort()
    
    return [Task_1, Task_2, [a, b]]
  
#---------------------------------------------------------------Testcase client------------------------------------------------------------------
  
test.describe("Example Tests")
arr1 = [66, 36, 49, 40, 73, 12, 77, 78, 76, 8, 50, 20, 85, 22, 24, 68, 26, 59, 92, 93, 30] 
test.assert_equals(proc_arrInt(arr1), [21, 2, [9, [36]]])
arr2 = [267, 273, 271, 145, 275, 150, 487, 169, 428, 50, 314, 444, 445, 67, 458, 211, 58, 95, 357, 486, 359, 491, 108, 493, 247, 379] 
test.assert_equals(proc_arrInt(arr2),[26, 7, [12, [108, 150, 444, 486]]])
