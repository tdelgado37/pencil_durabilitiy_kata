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


if __name__ == '__main__':
    unittest.main(warnings='ignore')
