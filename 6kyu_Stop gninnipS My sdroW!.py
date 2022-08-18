#--------------------------------------------------------------------------------My Solition--------------------------------------------------------------

def spin_words(sentence):
    splitted_words = sentence.split() #Create list of every Word in sentence
    output = []  
    for i in splitted_words: #for every Word in sentence
        character = list(i) #create list of character
        if len(character) >= 5: #if the word has more then 5 character...
            character.reverse() #reverse it 
        output.append(''.join(character)) #anyway give it back to output 
    return ' ' .join(output) #return sentence 
  
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
