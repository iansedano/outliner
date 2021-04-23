from lexing import *
import re

class token2:
	def __init__(
			self,
			tok_type ,
			value ,
			tab_level,
			line_no
			):
		self.tok_type  	= tok_type
		self.value    	= value
		self.tab_level  = tab_level
		self.line_no 	= line_no
		self.next 		= None


# Node Type can be FOLDER, FILE, CONTENT

def parse(root_lex):

	tab_level = 0
	line_no = 1
	tok_type = None
	current_value = None
	prev_tab_level = 0
	file_tab_level = None
	in_file = False
	content_string = []
	prev_tok = None
	root = None

	lex = root_lex
	while lex:

		print("====Starting new lex====")
		print(lex.tok_type, lex.value, end=" ")
		print("line", line_no, "tab", tab_level)

		if in_file == False:

			print("not in file")

			if lex.tok_type == '<ITEM>':
				print("its an <ITEM>")
				if "." in lex.value:
					print("its a <FILE>")
					in_file = True
					tok_type = "<FILE>"
					file_tab_level = tab_level
					print("file tab level", file_tab_level)
				else:
					print("its a <FOLDER>")
					tok_type= "<FOLDER>"
				current_value = lex.value
					
			elif lex.tok_type == '<NEW_LINE>':
				print("its a <NEW_LINE>")
				line_no += 1
				prev_tab_level = tab_level
				tab_level = 0

			elif lex.tok_type == '<TAB>':
				print("its a <TAB>")
				tab_level += 1
			

		elif in_file == True:
			# Do I need to keep track of the first line of content?


			
			if lex.tok_type == '<TAB>':
				if tab_level > file_tab_level + 1:
					content_string.append(lex.value)
				tab_level += 1

			elif tab_level <= file_tab_level:
				print("tab level still indicates we are no longer in a file")
				in_file = False
				current_value = "".join(content_string)
				
				tok_type = "<CONTENT>"
				file_tab_level = None

			elif tab_level > file_tab_level:
				print("we are still in a file")

				if lex.tok_type == '<NEW_LINE>':
					line_no += 1
					prev_tab_level = tab_level
					tab_level = 0

				content_string.append(lex.value)


		if tok_type == "<FILE>" or tok_type == "<FOLDER>" or tok_type == "<CONTENT>":
			print("*creating new token*")
			tok2 = token2(
			tok_type = tok_type,
			value = current_value,
			tab_level = tab_level,
			line_no = line_no
			)
			current_value = None

			if prev_tok is not None:
				prev_tok.next = tok2
			prev_tok = tok2

			if line_no == 1:
				root = tok2

		tok_type = None

		lex = lex.next

	return root
	
def print_lex2(tok):

	while tok:
		print(tok.line_no, tok.tok_type, tok.value, tok.tab_level)
		tok = tok.next

if __name__ == "__main__":
	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')

	second_pass = parse(lexemes2)

	print_lex2(second_pass)
