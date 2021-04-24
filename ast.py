from lexing import *
from parsing import *


class Node:
	def __init__(self, node_type = None, value = None):
		self.node_type = node_type
		self.value = value
		self.children = None


def build_tree(tok):

	# I think this is impossible but just in case
	if tok.tok_type == "<CONTENT>":
		raise Exception("Error: Input starts with Content")

	root = Node("<ROOT>")
	current_tab_level = 0

	print("====ROOT CREATED, STARTING TREE BUILD====")
	root.children, _temp = build_helper(tok, [])

	return root


def build_helper(tok, path):

	print("Initializing siblings for current token")
	print(tok.line_no, tok.tok_type, tok.value)
	siblings = []

	while tok:
		
		print("===creating node===\n")
		current_node = Node(tok.tok_type, tok.value)
		print(current_node.node_type, current_node.value)

		next_token = tok.next

		if next_token is None:
			print("this is the last token!")
			siblings.append(current_node)
			return siblings, 1

		elif next_token.tab_level < tok.tab_level:
			print("next token is not a child or sibling")
			return siblings, next_token

		elif next_token.tab_level > tok.tab_level:
			print("next token is a child of this one")
			current_node.children, next_token = build_helper(
				next_token,
				path.append(current_node)
			)

		elif next_token.tab_level == tok.tab_level:
			print("next token is a sibling!")
			siblings.append(current_node)

		if next_token == 1:
			return siblings, 1
		else:
			tok = next_token

def print_children(root):

	print(root.node_type, root.value)

	if root.children != []:
		for node in root.children:
			print_children(node)




if __name__ == "__main__":
	print("\n\n=====STARTING=====\n\n")

	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')

	second_pass1 = parse(lexemes1)
	second_pass2 = parse(lexemes2)
	second_pass3 = parse(lexemes3)

	root = build_tree(second_pass2)

	print("\n\n STARTING PRINT \n\n")
	print(root.children)
	print_children(root)
