import os

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

def lexer(path):
	with open(path) as mydata:
			data = mydata.read()

	i = 0
	line_no = 1
	current_lex = []
	root = None

	while i < len(data):

		char = data[i]

		#print(repr(char), current_lex)

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
