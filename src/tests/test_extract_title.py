import unittest

from src.functions.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_eq(self):

        base_case = """ # This is a title 
        
        This is a paragraph
        
        ## This is a subtitle
        """

        h2_is_first = """ ## This is a subtitle
        
        This is a paragraph

        # This is a title
        """

        no_title = """ ## This is a subtitle

        This is a paragraph

        ## This is another subtitle
        """

        title = extract_title(base_case)

        self.assertEqual(title, "This is a title")

        title = extract_title(h2_is_first)

        self.assertEqual(title, "This is a title")

        with self.assertRaises(Exception):
            extract_title(no_title)
            



if __name__ == "__main__":
    unittest.main()