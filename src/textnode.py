
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
