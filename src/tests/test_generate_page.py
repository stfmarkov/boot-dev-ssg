import unittest

from src.functions.generate_page import generate_page


class TestGeneratePage(unittest.TestCase):
    def test_eq(self):

        generate_page("index.md", "template.html", "index.html")



if __name__ == "__main__":
    unittest.main()