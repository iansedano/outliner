"""Stage 3
Takes Tokens from previous stage and builds a tree representing the folder
structure and the files and their contents.
"""

# I think path here is not needed or its not made use of.
# It could potentially be added to the node so that the next stage would have
# it easy...

from outline_parser.parser import token

class Node:
	def __init__(self, node_type = None, value = None):
		self.node_type = node_type
		self.value = value
		self.children = []

# <ROOT> <FOLDER> <FILE> <CONTENT>
 
def build_tree(tok: token):

	root = Node("<ROOT>", "root")
	current_tab_level = 0

	root.children, _temp = build_helper(tok, [root])
	
	return root


def build_helper(tok, path):

	siblings = []


	while tok:
		current_node = Node(tok.tok_type, tok.value)
		siblings.append(current_node)

		next_token = tok.next

		if next_token is None:
			return siblings, 1

		elif next_token.tab_level < tok.tab_level:
			return siblings, next_token

		elif next_token.tab_level > tok.tab_level:
			path.append(current_node)
			current_node.children, next_token = build_helper(
				next_token,
				path[:]
			)
			if next_token != 1 and next_token.tab_level < tok.tab_level:
				return siblings, next_token

		if next_token == 1:
			return siblings, 1
		else:
			tok = next_token

def print_children(root, level = 0):

	tab = '\t'*level

	print(tab, root.node_type, root.value)

	if root.children != []:
		for node in root.children:
			print_children(node, level + 1)

