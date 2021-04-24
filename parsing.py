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

	flags = {
		'tok_type': None,
		'current_value': None,
		'in_file': False,
	}

	tab_level = 0
	line_no = 1

	tok_type = None
	current_value = None
	in_file = False

	prev_tab_level = 0

	file_tab_level = None
	file_line_no_start = None

	content_string = []
	prev_tok = None
	root = None

	lex = root_lex
	while lex:

		
		
		

		if in_file == False:

			

			if lex.tok_type == '<ITEM>':
				
				if "." in lex.value:
					
					in_file = True
					tok_type = "<FILE>"
					file_tab_level = tab_level
					file_line_no_start = line_no
					

				else:
					
					tok_type= "<FOLDER>"
				current_value = lex.value
					
			elif lex.tok_type == '<NEW_LINE>':
				
				line_no += 1
				prev_tab_level = tab_level
				tab_level = 0

			elif lex.tok_type == '<TAB>':
				
				tab_level += 1
			

		elif in_file == True:
			# Do I need to keep track of the first line of content?
			
			if line_no == file_line_no_start:
				if lex.tok_type != '<NEW_LINE>':
					raise Exception(f"error on line {line_no}")
				else:
					line_no += 1
					tab_level = 0

			elif lex.tok_type == '<TAB>':
				if tab_level > file_tab_level:
					content_string.append('\t')
				tab_level += 1

			elif tab_level <= file_tab_level:
				
				in_file = False
				

				tok2 = token2(
					tok_type = '<CONTENT>',
					value = "".join(content_string),
					tab_level = file_tab_level + 1,
					line_no = file_line_no_start + 1
				)

				content_string = []

				if prev_tok is not None:
					prev_tok.next = tok2
				prev_tok = tok2

				if line_no == 1:
					root = tok2

				file_tab_level = None


				continue

			elif tab_level > file_tab_level:
				

				if lex.tok_type == '<NEW_LINE>':
					line_no += 1
					prev_tab_level = tab_level
					tab_level = 0
					content_string.append('\n')

				else:
					content_string.append(lex.value)

				if lex.next is None:
					tok2 = token2(
						tok_type = '<CONTENT>',
						value = "".join(content_string),
						tab_level = file_tab_level + 1,
						line_no = file_line_no_start + 1
					)

					if prev_tok is not None:
						prev_tok.next = tok2

					if line_no == 1:
						root = tok2

					break

		# ----

		need_to_create_token = (
			tok_type == "<FILE>" or
			tok_type == "<FOLDER>"
		)

		if need_to_create_token:
			
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

	second_pass = parse(lexemes3)

	print("===========FINAL RESULT===========")
	print_lex2(second_pass)
