from lexing import *


class node:
	def __init__(
			self,
			name = '',
			node_type = '',
			content = '',
			parent = ''
			):
		self.name       = name
		self.node_type  = node_type
		self.content    = content
		self.parent     = parent

def parse(lexemes):
	print(lexemes)
	root = node(name = 'root')
	i = 0
	tab_level = 0

	while i < len(lexemes):
		lex = lexemes[i]

		if lex == '<ITEM>':
			i++;

			name = lexemes[i]
			node_type = 'file' if '.' in name else 'folder'
			content = ''

			while :

			node(
				name = lexemes[i],
				node_type = 'file' if '.' in lexemes[i] else 'folder',
				)








if __name__ == "__main__":
	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')

	parse(lexemes2)