from lexing import *


class node:
	def __init__(
			self,
			node_type = '',
			content   = '',
			parent    = ''
			):
		self.node_type  = node_type
		self.content    = content
		self.parent     = parent


def parse(root_lex):


	root = node(
		node_type = root_lex.tok_type,
		content = root_lex.value,
		parent = None
		)

	while root_lex:

		if lex == '<ITEM>':

			lex.value








if __name__ == "__main__":
	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')

	parse(lexemes2)