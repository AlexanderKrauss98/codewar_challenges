#---------------------------------------------------------------------My Solution--------------------------------------------

import re
def to_camel_case(text):
    callback = lambda pat: pat.group(1).upper()
    big = re.sub(r'((-|_)[a-z]){1}', callback, text)
    return re.sub(r"(-|_)" , "" , big)

#-----------------------------------------------------------------Teestfile from Taskgiver----------------------------------

test.describe("Testing function to_camel_case")
test.it("Basic tests")
test.assert_equals(to_camel_case(''), '', "An empty string was provided but not returned")
test.assert_equals(to_camel_case("the_stealth_warrior"), "theStealthWarrior", "to_camel_case('the_stealth_warrior') did not return correct value")
test.assert_equals(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior", "to_camel_case('The-Stealth-Warrior') did not return correct value")
test.assert_equals(to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value")
