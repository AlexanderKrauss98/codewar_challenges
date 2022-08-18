#------------------------------------------------------------My Solution-----------------------------------------

def spin_words(sentence):
    splitted_words = sentence.split()
    output = []
    for i in splitted_words:
        character = list(i)
        if len(character) >= 5:
            character.reverse()
        output.append(''.join(character))
    return ' ' .join(output)
  
#-----------------------------------------------------------Testcase Client-----------------------------
  
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
