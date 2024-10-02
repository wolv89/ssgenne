
from textnode import TextNode
from htmlnode import HTMLNode

node = TextNode("This is a text node", "bold", "https://www.boot.dev")

hnode = HTMLNode("div", "Some text")

print(hnode)