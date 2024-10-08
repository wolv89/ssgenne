
import unittest

from parser import *


class TestHeaderType(unittest.TestCase):
    def test_header_type_1(self):
        markdown = "# Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")

    def test_header_type_2(self):
        markdown = "## Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")

    def test_header_type_3(self):
        markdown = "### Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")

    def test_header_type_4(self):
        markdown = "#### Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")

    def test_header_type_5(self):
        markdown = "##### Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")

    def test_header_type_6(self):
        markdown = "###### Heading"
        self.assertEqual(block_to_block_type(markdown), "heading")

    def test_header_type_7(self):
        markdown = "####### Not a heading"
        self.assertEqual(block_to_block_type(markdown), "paragraph")

    def test_header_type_0(self):
        markdown = " # Not a Heading"
        self.assertEqual(block_to_block_type(markdown), "paragraph")

    def test_unordered_list(self):
        markdown = "* Some\n* List\n* of\n* Items"
        self.assertEqual(block_to_block_type(markdown), "unordered_list")

    def test_ordered_list(self):
        markdown = "1. Some\n2. List\n3. of\n4. Items"
        self.assertEqual(block_to_block_type(markdown), "ordered_list")



if __name__ == "__main__":
    unittest.main()

