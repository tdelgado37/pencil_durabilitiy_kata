import unittest
from pencil_durability import Pencil, Paper

class pencil_durability_functional_tests(unittest.TestCase):
    def setUp(self):
        self.pencil = Pencil()
        self.paper = Paper()

    def tearDown(self):
        del self.pencil
        del self.paper

    def test_pencil_is_created(self):
        self.assertIsInstance(self.pencil, Pencil)

    def test_paper_is_created(self):
        self.assertIsInstance(self.paper, Paper)

    def test_pencil_set_text_to_write(self):
        self.pencil.set_text_to_write('hello world')
        self.assertEqual(self.pencil.text_to_write, 'hello world')


    def test_white_space_does_not_dull_pencil(self):
        pencil_letters_until_dull_before = self.pencil.letters_until_dull
        self.pencil.set_text_to_write(' ')
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.pencil.letters_until_dull, pencil_letters_until_dull_before)

    def test_writing_after_pencil_is_dull_will_write_white_space(self):
        self.pencil.set_text_to_write('hello world!')
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.paper.text, 'hello world ')

    def test_newline_does_not_dull_pencil(self):
        pencil_letters_until_dull_before = self.pencil.letters_until_dull
        self.pencil.set_text_to_write('\n')
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.pencil.letters_until_dull, pencil_letters_until_dull_before)

    def test_writing_upper_case_letter_takes_two_points_off_dull(self):
        pencil_letters_until_dull_before = self.pencil.letters_until_dull
        self.pencil.set_text_to_write('H')
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.pencil.letters_until_dull, pencil_letters_until_dull_before - 2)

    def test_pencil_sharpener_sharpens_to_inital_sharpen_value(self):
        inital_sharpen_value = self.pencil.letters_until_dull
        self.pencil.letters_until_dull = 0
        self.pencil.sharpen()
        self.assertEqual(inital_sharpen_value, self.pencil.letters_until_dull)

    def test_pencil_only_erases_str_provided(self):
        self.pencil.set_text_to_write('Hi hi')
        self.pencil.write_on_paper(self.paper)
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.paper.text, 'Hi   ')

    def test_pencil_erases_one_str_match(self):
        self.pencil.set_text_to_write('hi hi')
        self.pencil.write_on_paper(self.paper)
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(len(self.paper.text.split()), 1)

    def test_pencil_erases_str_in_reverse_order(self):
        self.pencil.set_text_to_write('hi hi')
        self.pencil.write_on_paper(self.paper)
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.paper.text, 'hi   ')

    def test_pencil_erase_str_when_str_is_in_word(self):
        self.pencil.set_text_to_write('hi hill')
        self.pencil.write_on_paper(self.paper)
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.paper.text, 'hi   ll')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
