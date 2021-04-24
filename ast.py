from lexing import *
from parsing import *

# I think path here is not needed or its not made use of.
# It could potentially be added to the node so that the next stage would have
# it easy...

class Node:
	def __init__(self, node_type = None, value = None):
		self.node_type = node_type
		self.value = value
		self.children = []

# <ROOT> <FOLDER> <FILE> <CONTENT>
 
def build_tree(tok):

	# I think this is impossible but just in case
	if tok.tok_type == "<CONTENT>":
		raise Exception("Error: Input starts with Content")

	root = Node("<ROOT>", "root")
	current_tab_level = 0

	# print("====ROOT CREATED, STARTING TREE BUILD====")
	root.children, _temp = build_helper(tok, [root])

	return root


def build_helper(tok, path):

	# print("path", [p.value for p in path ])
	# print("Initializing siblings for current token")
	# print(tok.line_no, tok.tok_type, tok.value)
	siblings = []


	while tok:
		
		# print("\n===creating node===\n")
		current_node = Node(tok.tok_type, tok.value)
		# print("node created", current_node.node_type, current_node.value)
		siblings.append(current_node)

		next_token = tok.next

		if next_token is None:
			# print("this is the last token!")
			return siblings, 1

		elif next_token.tab_level < tok.tab_level:
			# print("next token is not a child or sibling")
			return siblings, next_token

		elif next_token.tab_level > tok.tab_level:
			# print("next token is a child of this one")
			path.append(current_node)
			# print("  CALLING FUNCTION RECURSIVELY")
			current_node.children, next_token = build_helper(
				next_token,
				path[:]
			)
			# print("\tRETURNED from Function")
			if next_token != 1 and next_token.tab_level < tok.tab_level:
				return siblings, next_token

		# elif next_token.tab_level == tok.tab_level:
			# print("next token is a sibling!")
			# print("siblings", [s.value for s in siblings])

		if next_token == 1:
			return siblings, 1
		else:
			tok = next_token

def print_children(root, level = 0):

	tab = '\t'*level

	# print(tab, root.node_type, root.value)

	if root.children != []:
		for node in root.children:
			print_children(node, level + 1)




if __name__ == "__main__":
	# print("\n\n=====STARTING=====\n\n")

	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')
	lexemes4 = lexer('test_files\\folderstruct4.txt')

	second_pass1 = parse(lexemes1)
	second_pass2 = parse(lexemes2)
	second_pass3 = parse(lexemes3)
	second_pass4 = parse(lexemes4)

	root = build_tree(second_pass3)

	# print("\n\n STARTING PRINT \n\n")
	print_children(root)
