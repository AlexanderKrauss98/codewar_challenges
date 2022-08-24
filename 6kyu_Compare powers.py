#--------------------------------------------My Solution---------------------------------------
def compare_powers(n1,n2):
    return(-1 if n1[0]**n1[1] > n2[0]**n2[1] else 0 if n1[0]**n1[1] == n2[0]**n2[1] else 1)
    # this Code works well with the normal Test but not with the randoms because the exponent goes then over 1000000 and its an limited time for to run the code. 
#------------------------------------------Testfile--------------------------------------------
test.describe("Sample tests")
test.it("Smaller numbers")
test.assert_equals(compare_powers([2,10],[2,15]),1)
test.assert_equals(compare_powers([2,10],[3,10]),1)
test.assert_equals(compare_powers([2,10],[2,10]),0)
test.assert_equals(compare_powers([3,9],[5,6]),-1)
test.assert_equals(compare_powers([7,7],[5,8]),-1)
