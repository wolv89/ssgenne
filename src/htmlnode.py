
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if self.props is None or len(self.props) <= 0:
			return ""
		atts = ""
		for key, val in self.props.items():
			atts += f" {key}=\"{val}\""
		return atts

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"



class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("leaf nodes must have a value")
		if self.tag is None:
			return self.value
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
	def __init__(self, tag=None, children=None, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if self.tag is None:
			raise ValueError("parent nodes must have a tag")
		if self.children is None or len(self.children) <= 0:
			return ValueError("parent node must have children")
		output = f"<{self.tag}{self.props_to_html()}>"
		for child in self.children:
			output += child.to_html()
		output += f"</{self.tag}>"
		return output
