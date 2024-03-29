import unittest
from pencil_durability import Pencil, Paper

class pencil_durability_unit_tests(unittest.TestCase):
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

    def test_white_space_does_not_dull_pencil(self):
        pencil_letters_until_dull_before = self.pencil.letters_until_dull
        self.pencil.write_on_paper(self.paper, ' ')
        self.assertEqual(self.pencil.letters_until_dull, pencil_letters_until_dull_before)

    def test_writing_after_pencil_is_dull_will_write_white_space(self):
        self.pencil.write_on_paper(self.paper, 'hello world!')
        self.assertEqual(self.paper.text, 'hello world ')

    def test_newline_does_not_dull_pencil(self):
        pencil_letters_until_dull_before = self.pencil.letters_until_dull
        self.pencil.write_on_paper(self.paper, '\n')
        self.assertEqual(self.pencil.letters_until_dull, pencil_letters_until_dull_before)

    def test_writing_upper_case_letter_takes_two_points_off_dull(self):
        pencil_letters_until_dull_before = self.pencil.letters_until_dull
        self.pencil.write_on_paper(self.paper, 'H')
        self.assertEqual(self.pencil.letters_until_dull, pencil_letters_until_dull_before - 2)

    def test_pencil_sharpener_sharpens_to_inital_sharpen_value(self):
        inital_sharpen_value = self.pencil.letters_until_dull
        self.pencil.letters_until_dull = 0
        self.pencil.sharpen()
        self.assertEqual(inital_sharpen_value, self.pencil.letters_until_dull)

    def test_pencil_only_erases_str_provided(self):
        self.pencil.write_on_paper(self.paper, 'Hi hi')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.paper.text, 'Hi   ')

    def test_pencil_erases_one_str_match(self):
        self.pencil.write_on_paper(self.paper, 'hi hi')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(len(self.paper.text.split()), 1)

    def test_pencil_erases_str_in_reverse_order(self):
        self.pencil.write_on_paper(self.paper, 'hi hi')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.paper.text, 'hi   ')

    def test_pencil_erase_str_when_str_is_in_word(self):
        self.pencil.write_on_paper(self.paper, 'hi hill')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.paper.text, 'hi   ll')

    def test_pencil_eraser_when_eraser_status_is_zero(self):
        self.pencil.eraser_status = 3
        self.pencil.write_on_paper(self.paper, 'Bill')
        self.pencil.erase(self.paper,'Bill')
        self.assertEqual(self.paper.text, 'B   ')

    def test_erased_position(self):
        self.pencil.write_on_paper(self.paper, 'hi hi')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.pencil.erased_position, 3)

    def test_erased_position_erase_first_word(self):
        self.pencil.write_on_paper(self.paper, 'hi hello')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.pencil.erased_position, 0)

    def test_pencil_erased_position_erase_middle_word(self):
        self.pencil.write_on_paper(self.paper, 'a hi hello')
        self.pencil.erase(self.paper,'hi')
        self.assertEqual(self.pencil.erased_position, 2)

    def test_erased_position_partial_word_erased(self):
        self.pencil.eraser_status = 3
        self.pencil.write_on_paper(self.paper, 'Bill')
        self.pencil.erase(self.paper,'ill')
        self.assertEqual(self.pencil.erased_position, 1)
        self.assertEqual(self.paper.text, 'B   ')


    def test_erased_position_when_eraser_runs_out(self):
        self.pencil.eraser_status = 2
        self.pencil.write_on_paper(self.paper, 'Bill')
        self.pencil.erase(self.paper,'Bill')
        self.assertEqual(self.pencil.erased_position, 2)
        self.assertEqual(self.paper.text, 'Bi  ')

    def test_text_editing_override_previous_text(self):
        self.pencil.write_on_paper(self.paper, 'hi he')
        self.pencil.erase(self.paper, 'hi')
        self.pencil.edit_text(self.paper,'hello')
        self.assertEqual(self.paper.text, 'hel@@')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
