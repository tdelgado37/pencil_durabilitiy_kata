import unittest
from pencil_durability import Pencil, Paper

class pencil_durability_functional_tests(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()

    def tearDown(self):
        del self.pencil
        del self.paper

    #As a writer
    #I want to be able to use a pencil to write text on a sheet of paper
    #so that I can better remember my thoughts
    def test_pencil_writes_string_of_text_on_sheet_of_paper(self):
        text_to_display='Hello world!'
        self.pencil.set_text_to_write(text_to_display)
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.paper.text ,text_to_display)






#As a pencil manufacturer
#I want writing t ocause a pencil point to go dull
#so that I can sell more pencils

#As a writer
#I want to be able to sharpen my pencil
#so that I can continue to write with it after it goes pencil_durability_functional_tests

#As a writer
#I want to be able to erase previouly written text
#so that I can remove my mistakes

#As a pencil manufacturer
#I want a pencil eraser to eventually wear out
#so that I can sell more pencils


if __name__ == '__main__':
    unittest.main(warnings='ignore')
