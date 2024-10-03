
import re

from constants import *
from textnode import TextNode




def text_to_text_nodes(text):
	nodes = [TextNode(text, TT_TEXT)]
	nodes = split_nodes_delimiter(nodes, "**", TT_BOLD)
	nodes = split_nodes_delimiter(nodes, "*", TT_ITALIC)
	nodes = split_nodes_delimiter(nodes, "`", TT_CODE)
	nodes = split_nodes_image(nodes)
	nodes = split_nodes_link(nodes)
	return nodes



def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_list = []
	for node in old_nodes:
		if node.text_type != TT_TEXT:
			new_list.append(node)
			continue
		delims = node.text.count(delimiter)
		if delims == 0:
			new_list.append(node)
			continue
		if delims % 2 != 0:
			raise Exception("bad markdown")
		parts = node.text.split(delimiter)
		in_delim = False
		for part in parts:
			if part:
				if in_delim:
					new_list.append(TextNode(part, text_type))
				else:
					new_list.append(TextNode(part, TT_TEXT))
			in_delim = not in_delim
	return new_list


def split_nodes_image(old_nodes):
	new_list = []
	for node in old_nodes:
		if node.text_type != TT_TEXT:
			new_list.append(node)
			continue
		images = extract_markdown_images(node.text)
		if len(images) == 0:
			new_list.append(node)
			continue
		old_text = node.text
		for image in images:
			parts = old_text.split(f"![{image[0]}]({image[1]})", 1)
			if len(parts) != 2:
				raise Exception("you dun goofed")
			if parts[0] != "":
				new_list.append(TextNode(parts[0], TT_TEXT))
			new_list.append(TextNode(image[0], TT_IMG, image[1]))
			old_text = parts[1]
		if old_text != "":
			new_list.append(TextNode(old_text, TT_TEXT))
	return new_list



def split_nodes_link(old_nodes):
	new_list = []
	for node in old_nodes:
		if node.text_type != TT_TEXT:
			new_list.append(node)
			continue
		links = extract_markdown_links(node.text)
		if len(links) == 0:
			new_list.append(node)
			continue
		old_text = node.text
		for link in links:
			parts = old_text.split(f"[{link[0]}]({link[1]})", 1)
			if len(parts) != 2:
				raise Exception("you dun goofed")
			if parts[0] != "":
				new_list.append(TextNode(parts[0], TT_TEXT))
			new_list.append(TextNode(link[0], TT_LINK, link[1]))
			old_text = parts[1]
		if old_text != "":
			new_list.append(TextNode(old_text, TT_TEXT))
	return new_list


def extract_markdown_images(text):
	return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
	return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
