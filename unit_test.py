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
        str_text_to_write = "hello world"
        self.pencil.set_text_to_write(str_text_to_write)
        self.assertEqual(self.pencil.text_to_write, str_text_to_write)

    def test_get_letters_until_dull(self):
        self.assertEqual(self.pencil.letters_until_dull, 10)

    def test_white_space_does_not_dull_pencil(self):
        str_text_to_write = " "
        self.pencil.set_text_to_write(str_text_to_write)
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.pencil.letters_until_dull, 10)

    def test_writing_after_pencil_is_dull_will_write_white_space(self):
        str_text_to_write = "hello world!"
        self.pencil.set_text_to_write(str_text_to_write)
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.paper.text, "hello world ")

    def test_newline_does_not_dull_pencil(self):
        str_text_to_write = '\n'
        self.pencil.set_text_to_write(str_text_to_write)
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.pencil.letters_until_dull, 10)

    def test_writing_upper_case_letter_takes_two_points_off_dull(self):
        str_text_to_write = 'H'
        self.pencil.set_text_to_write(str_text_to_write)
        self.pencil.write_on_paper(self.paper)
        self.assertEqual(self.pencil.letters_until_dull, 8)




if __name__ == '__main__':
    unittest.main(warnings='ignore')
