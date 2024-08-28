import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("</>", "5", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_init(self):
        node = HTMLNode("</>", "5", None, {"href": "https://www.google.com", "target": "_blank"})
        expected_str = "Tag: </>, Value: 5, Children: = None, Props: = {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(str(node), expected_str)


if __name__ == "__main__":
    unittest.main()