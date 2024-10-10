
import os, shutil

from constants import *
from parser import *

from htmlnode import *
from textnode import *



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

	doc = ParentNode("div", nodes)

	return doc


def create_header_node(block):
	parts = block.split(" ", 1)
	return ParentNode("h" + str(len(parts[0])), text_to_text_nodes(parts[1]))


def create_code_node(block):
	lines = block.split("\n")
	content = []
	for line in lines:
		if line == "```":
			continue
		content.append(line)
	code = LeafNode("code", "\n".join(content))
	return ParentNode("pre", [code])


def create_quote_node(block):
	lines = block.split("\n")
	content = []
	for line in lines:
		content.append(line[1:].strip())
	return LeafNode("blockquote", "\n".join(content))


def create_unordered_list_node(block):
	lines = block.split("\n")
	children = []
	for line in lines:
		line = line[1:].strip()
		nodes = text_to_text_nodes(line)
		children.append(ParentNode("li", nodes))
	return ParentNode("ul", children)


def create_ordered_list_node(block):
	lines = block.split("\n")
	children = []
	for line in lines:
		parts = line.split(".", 1)
		nodes = text_to_text_nodes(parts[1].strip())
		children.append(ParentNode("li", nodes))
	return ParentNode("ol", children)


def create_paragraph_node(block):
	return ParentNode("p", text_to_text_nodes(block))



# NODES = parse_markdown(MARKDOWN)

# print(NODES)


def copy_dir(dfrom, dto):

	if not os.path.exists(dto):
		os.mkdir(dto)

	for i in os.listdir(dfrom):

		item = os.path.join(dfrom, i)

		if os.path.isfile(item):
			shutil.copy(item, dto)
		else:
			copy_dir(os.path.join(dfrom, i), os.path.join(dto, i))


def generate_pages_recursive(from_path, template_path, dest_path):

	with open(template_path, 'r') as tmp:
		template = tmp.read()

	if not os.path.exists(dest_path):
		os.mkdir(dest_path)

	for i in os.listdir(from_path):

		item = os.path.join(from_path, i)

		if os.path.isfile(item):
			generate_page(item, template, dest_path)
		else:
			generate_pages_recursive(item, template_path, os.path.join(dest_path, i))



def copy_static():

	if os.path.exists("public"):
		shutil.rmtree("public")

	cwd = os.getcwd()

	os.mkdir("public")
	copy_dir(os.path.join(cwd, "static"), os.path.join(cwd, "public"))


def extract_title(markdown):

	for line in markdown.split("\n"):
		if line.startswith("# "):
			return line[2:]

	raise Exception("Markdown does not contain a H1 title")



def generate_page(from_path, template, dest_path):

	print(f"Generating page from {from_path} to {dest_path}")

	with open(from_path, 'r') as mdp:
		markdown = mdp.read()

	md_html = parse_markdown(markdown).to_html()
	title = extract_title(markdown)

	template = template.replace("{{ Title }}", title)
	template = template.replace("{{ Content }}", md_html)

	with open(os.path.join(dest_path, "index.html"), 'w') as out:
		out.write(template)



cw = os.getcwd()

copy_static()
generate_pages_recursive(os.path.join(cw, "content"), os.path.join(cw, "template.html"), os.path.join(cw, "public"))
