
import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "link", None, {"href": "https://www.test.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.test.com\"")


if __name__ == "__main__":
    unittest.main()

