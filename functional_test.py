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
        self.pencil.write_on_paper(self.paper, 'hi')
        self.assertEqual(self.paper.text ,'hi')


    #As a pencil manufacturer
    #I want writing to cause a pencil point to go dull
    #so that I can sell more pencils
    def test_pencil_dulling_from_writing(self):
        before_writing_letter_until_dull = self.pencil.letters_until_dull
        self.pencil.write_on_paper(self.paper, 'hello')
        after_writing_letter_until_dull = self.pencil.letters_until_dull
        self.assertTrue(before_writing_letter_until_dull > after_writing_letter_until_dull)

    #As a writer
    #I want to be able to sharpen my pencil
    #so that I can continue to write with it after it goes pencil_durability_functional_tests
    def test_pencil_sharpener(self):
        self.pencil.letters_until_dull = 0
        self.pencil.sharpen()
        self.assertTrue(self.pencil.letters_until_dull > 0)


    #As a writer
    #I want to be able to erase previouly written text
    #so that I can remove my mistakes
    def test_pencil_eraser(self):
        self.pencil.write_on_paper(self.paper, 'Hello')
        self.pencil.erase(self.paper, 'Hello')
        self.assertEqual(self.paper.text, '     ')

    #As a pencil manufacturer
    #I want a pencil eraser to eventually wear out
    #so that I can sell more pencils
    def test_pencil_eraser_degradation(self):
        eraser_status_before_erase = self.pencil.eraser_status
        self.pencil.write_on_paper(self.paper, 'Hello')
        self.pencil.erase(self.paper, 'Hello')
        self.assertTrue(eraser_status_before_erase > self.pencil.eraser_status)

    #As a writer
    #I want to be able to edit previously written text
    #so that I can change my writing without starting over
    def test_editing(self):
        self.pencil.write_on_paper(self.paper, 'hello hi')
        self.pencil.erase(self.paper, 'hello')
        self.pencil.edit_text(self.paper, 'gosh')
        self.assertEqual(self.paper.text, 'gosh  hi')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
