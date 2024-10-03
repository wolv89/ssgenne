
from constants import *
from parser import *
from textnode import TextNode

sample = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

nodes = text_to_text_nodes(sample)

for node in nodes:
	print(node)