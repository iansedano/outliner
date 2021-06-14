"""Stage 1
Takes a string and splits it into one of three lexemes:

- New line
- Tab
- Item

Items will later become folders, files or file content.
"""

class Lexeme:
	def __init__(self, tok_type, value, line_no):
		self.tok_type = tok_type
		self.value = value
		self.line_no = line_no
		self.next = None

STRUCTURE_TOKENS = {
	'\n'  :   '<NEW_LINE>',
	'\t'  :   '<TAB>',
}

def lex(data):
	"""Transform string into lexemes
	"""
	i = 0
	line_no = 1
	current_lex = []
	root = None

	while i < len(data):

		char = data[i]

		if char in STRUCTURE_TOKENS:
			if current_lex != []:
				lex = Lexeme(
					tok_type = '<ITEM>',
					value = ''.join(current_lex),
					line_no = line_no
					)
				current_lex = []

				if line_no == 1:
					root = lex
				else:
					previous_tok.next = lex
				
				previous_tok = lex

			current_tok = Lexeme(
				tok_type = STRUCTURE_TOKENS[char],
				value = repr(char),
				line_no = line_no
				)

			previous_tok.next = current_tok
			previous_tok = current_tok

			if char == '\n':
				line_no += 1
		else:
			current_lex.append(char)


		i += 1

	if current_lex != []:
		lex = Lexeme(
			tok_type = '<ITEM>',
			value = ''.join(current_lex),
			line_no = line_no
			)

		previous_tok.next = lex

	return root


def print_lex(tok):

	while tok:
		print(tok.tok_type, tok.value, tok.line_no)
		tok = tok.next
