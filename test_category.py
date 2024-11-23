import unittest # std lib - ja vem instalada com o python

from category import Category

class TestCategory(unittest.TestCase):

    def test_name_is_required(self):
        with self.assertRaises(TypeError):
            Category()

    def test_name_must_have_less_than_255_characters(self):
        with self.assertRaisesRegex(TypeError, "name must have less than 255 characters"):
            Category("a" * 256)


if __name__ == "__main__":
    unittest.main()