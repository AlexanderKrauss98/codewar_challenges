#----------------------------------------------------------------------------My Solution---------------------------------------

def xo(s):
    x_ticker = 0
    o_ticker = 0
    
    if len(s) == 0:   #if s is empty      
        a = True      #return True
        
    else:    
        for i in s: # count xX
            if i == "x" or i =="X":
                x_ticker += 1
            elif i == "o" or i == "O": # count oO
                o_ticker += 1
        a = True if x_ticker == o_ticker else False #vergleicht xO and oO
    return a #return vergleich
  
#----------------------------------------------------------------------------Testfile Client---------------------------------------
  
test.expect(xo('xo'), 'True expected')
test.expect(xo('xo0'), 'True expected')
test.expect(not xo('xxxoo'), 'False expected')
