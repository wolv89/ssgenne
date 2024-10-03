
import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.test.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.test.com\"")



class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode("a", "link", {"href": "https://www.test.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.test.com\">link</a>")


if __name__ == "__main__":
    unittest.main()

