
from constants import *
from htmlnode import LeafNode

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, node):
		if not self.text == node.text:
			return False
		if not self.text_type == node.text_type:
			return False
		if not self.url == node.url:
			return False
		return True

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type}, {self.url})"

	def to_html(self):
		return text_node_to_html_node(self).to_html()


def text_node_to_html_node(text_node):
	if text_node.text_type == TT_TEXT:
		return LeafNode(None, text_node.text)
	if text_node.text_type == TT_BOLD:
		return LeafNode("b", text_node.text)
	if text_node.text_type == TT_ITALIC:
		return LeafNode("i", text_node.text)
	if text_node.text_type == TT_CODE:
		return LeafNode("code", text_node.text)
	if text_node.text_type == TT_LINK:
		return LeafNode("a", text_node.text, {"href": text_node.url})
	if text_node.text_type == TT_IMG:
		return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
	raise Exception("invalid text type")
