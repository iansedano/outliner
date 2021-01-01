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
	'*'   :   '<ITEM>'
}

def lexer(path):
	with open(path) as mydata:
			data = mydata.read()

	current_lexeme = []
	current_line = 1;

	for i, c in enumerate(data):

		if i == 0 and c in STRUCTURE_TOKENS:
			current_tok = token(STRUCTURE_TOKENS[c], repr(c), current_line)
			root = current_tok # If the first character is not a STRUCTURE_TOKEN this program will break
		elif c in STRUCTURE_TOKENS:
			if current_lexeme != []:
				lexeme_tok = token('<STRING>', ''.join(current_lexeme).strip(), current_line)
				previous_tok.next = lexeme_tok
				previous_tok = lexeme_tok
				current_lexeme = []
			current_tok = token(STRUCTURE_TOKENS[c], repr(c), current_line)
			previous_tok.next = current_tok
		else:
			current_lexeme.append(c)

		previous_tok = current_tok
		current_line = current_line + 1 if c == '\n' else current_line

	if current_lexeme != []:
		lexeme_tok = token('<STRING>', ''.join(current_lexeme).strip(), current_line)
		previous_tok.next = lexeme_tok
		
	return root

def print_lex(tok):

	while tok:
		print(tok.tok_type, tok.value, tok.line_no)
		tok = tok.next


if __name__ == "__main__":

	lexemes = lexer('test_files\\folderstruct2.txt')
	print_lex(lexemes)
