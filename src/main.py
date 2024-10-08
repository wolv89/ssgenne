
from constants import *
from parser import *

from htmlnode import *
from textnode import *


MARKDOWN = """# This is my markdown

### Some secondary header

Bit of text as *some intro* or something?

- Quick
- List
- Of
- Nothing

#### This is **important**

1. Writing this stuff
2. For testing
3. Is dull..."""




def parse_markdown(markdown):
	nodes = []
	blocks = markdown_to_blocks(markdown)

	for block in blocks:
		block_type = block_to_block_type(block)

		if block_type == "heading":
			nodes.append(create_header_node(block))
		elif block_type == "code":
			nodes.append(create_code_node(block))
		elif block_type == "quote":
			nodes.append(create_quote_node(block))
		elif block_type == "unordered_list":
			nodes.append(create_unordered_list_node(block))
		elif block_type == "ordered_list":
			nodes.append(create_ordered_list_node(block))
		else:
			nodes.append(create_paragraph_node(block))

	doc = HTMLNode("div", None, nodes)

	return doc


def create_header_node(block):
	parts = block.split(" ", 1)
	return HTMLNode("h" + str(len(parts[0])), None, text_to_text_nodes(parts[1]))


def create_code_node(block):
	lines = block.split("\n")
	cotent = []
	for line in lines:
		if line == "```":
			continue
		content.append(line)
	code = HTMLNode("code", "\n".join(content))
	return HTMLNode("pre", None, [code])


def create_quote_node(block):
	lines = block.split("\n")
	cotent = []
	for line in lines:
		content.append(line[1:].strip())
	return HTMLNode("blockquote", "\n".join(content))


def create_unordered_list_node(block):
	lines = block.split("\n")
	children = []
	for line in lines:
		line = line[1:].strip()
		nodes = text_to_text_nodes(line)
		children.append(HTMLNode("li", None, nodes))
	return HTMLNode("ul", None, children)


def create_ordered_list_node(block):
	lines = block.split("\n")
	children = []
	for line in lines:
		parts = line.split(".", 1)
		nodes = text_to_text_nodes(parts[1].strip())
		children.append(HTMLNode("li", None, nodes))
	return HTMLNode("ol", None, children)


def create_paragraph_node(block):
	return HTMLNode("p", None, text_to_text_nodes(block))



NODES = parse_markdown(MARKDOWN)

print(NODES)
