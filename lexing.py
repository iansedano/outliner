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

	lexemes = []
	current_lexeme = []
	current_line = 1;

	for i, c in enumerate(data):

		if i == 0 and c in STRUCTURE_TOKENS:
			current_tok = token(STRUCTURE_TOKENS[c], c, current_line)
			lexemes.append(STRUCTURE_TOKENS[c])
		elif c in STRUCTURE_TOKENS:
			if current_lexeme != []:
				lexemes.append(''.join(current_lexeme).strip())
				current_lexeme = []
			lexemes.append(STRUCTURE_TOKENS[c])
		else:
			current_lexeme.append(c)

		current_line = current_line + 1 if c == '\n' else current_line
		
	return lexemes

if __name__ == "__main__":
	lexemes = lexer('test_files\\folderstruct1.txt')
	print(lexemes)
	lexemes = lexer('test_files\\folderstruct2.txt')
	print(lexemes)
	lexemes = lexer('test_files\\folderstruct3.txt')
	print(lexemes)