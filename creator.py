from lexing import *
from parsing import *
from ast import *

import os


def create(node, name):

	path = os.path.join(os.getcwd(), "output", name)
	
	create_helper(node, path)

	


def create_helper(node, path):

	if node.node_type == '<ROOT>':
		for n in node.children:
			create_helper(n, path)

	elif node.node_type == '<FOLDER>':
		folder_path = os.path.join(path, node.value)
		os.mkdir(folder_path)
		for n in node.children:
			create_helper(n, folder_path)

	elif node.node_type == '<FILE>':
		file_path = os.path.join(path, node.value)
		with open(file_path, 'w') as f:
			for c in node.children:
				if c.node_type != "<CONTENT>":
					raise Exception("invalid content")
				f.write(c.value)


if __name__ == "__main__":
	

	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')
	lexemes4 = lexer('test_files\\folderstruct4.txt')

	second_pass1 = parse(lexemes1)
	second_pass2 = parse(lexemes2)
	second_pass3 = parse(lexemes3)
	second_pass4 = parse(lexemes4)

	tree1 = build_tree(second_pass1)
	tree2 = build_tree(second_pass2)
	tree3 = build_tree(second_pass3)
	tree4 = build_tree(second_pass4)

	print("\n\n=====STARTING=====\n\n")

	create(tree1, "1")

