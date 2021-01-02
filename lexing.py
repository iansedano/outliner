"""
If there is an asterisk anywhere unexpected it will not
produce the right result
"""

import os

class token:
	def __init__(self, tok_type, value, line_no):
		self.tok_type = tok_type
		self.value = value
		self.line_no = line_no
		self.next = None

STRUCTURE_TOKENS = {
	'\n'  :   '<NEW_LINE>',
	'\t'  :   '<TAB>',
	# Will interpret any * as ITEM even though may be part of content.
	'*'   :   '<ITEM>' 
}

def lexer(path):
	with open(path) as mydata:
			data = mydata.read()

	current_lexeme = []
	current_line = 1
	root_set = False

	for i, c in enumerate(data):

		if c in STRUCTURE_TOKENS:
			if current_lexeme != []:

				# Create trailing lexeme token
				lexeme_tok = token(
					'<STRING>',
					''.join(current_lexeme).strip(),
					current_line
					)

				previous_tok.next = lexeme_tok
				previous_tok = lexeme_tok
				current_lexeme = []

			# Create structure token
			current_tok = token(
				STRUCTURE_TOKENS[c],
				repr(c),
				current_line
				)

			# Set root if not set, else link to previous
			if current_line == 1 and root_set == False:
				root = current_tok
				root_set = True
				previous_tok = root
			else:
				previous_tok.next = current_tok

		else:
			current_lexeme.append(c)

		previous_tok = current_tok
		current_line = current_line + 1 if c == '\n' else current_line

	# Deal with the last line since no EOF detection
	if current_lexeme != []:

		lexeme_tok = token(
			'<STRING>',
			''.join(current_lexeme).strip(),
			current_line
			)

		previous_tok.next = lexeme_tok
		
	return root

def print_lex(tok):

	while tok:
		print(tok.tok_type, tok.value, tok.line_no)
		tok = tok.next


# Test cases
if __name__ == "__main__":
	print("======================================")
	lexemes = lexer('test_files\\folderstruct1.txt')
	print_lex(lexemes)
	print("======================================")
	lexemes = lexer('test_files\\folderstruct2.txt')
	print_lex(lexemes)
	print("======================================")
	lexemes = lexer('test_files\\folderstruct3.txt')
	print_lex(lexemes)
