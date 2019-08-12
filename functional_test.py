import unittest
from pencil_durability import Pencil, Paper

class pencil_durability_functional_tests(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()
        self.text_to_display='Hello'
        self.pencil.set_text_to_write(self.text_to_display)

    def tearDown(self):
        del self.pencil
        del self.paper

    #As a writer
    #I want to be able to use a pencil to write text on a sheet of paper
    #so that I can better remember my thoughts
    def test_pencil_writes_string_of_text_on_sheet_of_paper(self):
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.paper.text ,self.text_to_display)






    #As a pencil manufacturer
    #I want writing to cause a pencil point to go dull
    #so that I can sell more pencils
    def test_pencil_dulling_from_writing(self):
        before_writing_letter_until_dull = self.pencil.letters_until_dull
        self.pencil.write_on_paper(self.paper)
        after_writing_letter_until_dull = self.pencil.letters_until_dull
        self.assertTrue(before_writing_letter_until_dull > after_writing_letter_until_dull)

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
