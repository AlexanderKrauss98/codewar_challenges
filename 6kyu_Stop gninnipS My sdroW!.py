#-------------------------------------------------------------------------Task-------------------------------------------------------------------
#Write a function that takes in a string of one or more words, and returns the same string, 
#but with all five or more letter words reversed (Just like the name of this Kata). 
#Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

#Examples:

#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#spinWords( "This is a test") => returns "This is a test" 
#spinWords( "This is another test" )=> returns "This is rehtona test"

#--------------------------------------------------------------------------------My Solition--------------------------------------------------------------

def spin_words(sentence):
    splitted_words = sentence.split()
    output = []
    for i in splitted_words:
        character = list(i)
        if len(character) >= 5:
            character.reverse()
        output.append(''.join(character))
    return ' ' .join(output)
  
#---------------------------------------------------------------------------Testfile from Creator----------------------------------------------------------------

import codewars_test as test
from solution import spin_words

@test.describe("Stop gninnipS My sdroW!")
def fixed_tests():
    @test.it("Single word")
    def _():
        test.assert_equals(spin_words("Welcome"), "emocleW")
        test.assert_equals(spin_words("to"), "to")
        test.assert_equals(spin_words("CodeWars"), "sraWedoC")

    @test.it("Multiple words")
    def _():
        test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
