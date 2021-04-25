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
		create_path(folder_path)
		for n in node.children:
			create_helper(n, folder_path)

	elif node.node_type == '<FILE>':
		file_path = os.path.join(path, node.value)
		with open(file_path, 'w') as f:
			for c in node.children:
				if c.node_type != "<CONTENT>":
					raise Exception("invalid content")
				f.write(c.value)


def create_folders(source, output_path):

	source = os.path.join(source)
	if not os.path.is_file(source):
		raise Exception("invalid file")

	output_path = os.path.join(output_path)
	create_path(output_path)

	for f in os.listdir(output_path):
		os.remove(os.path.join(output_path, f))

	lexemes = lexer(source)
	tokens = parse(lexemes)
	tree_root = build_tree(tokens)

	create_helper(tree_root, output_path)


def create_path(path):

	path_list = path.split("\\")
	path_list[0] = path_list[0] + "\\"

	is_file = "." in path_list[-1]

	
	if is_file:
		file = path_list.pop(-1)

	path_construct = ""

	for p in path_list:
		path_construct = os.path.join(path_construct, p)
		if not os.path.exists(path_construct):
			print("making directory " + path_construct)
			os.mkdir(path_construct)
		else:
			print(path_construct + " already exists")

	# if is_file:
	# 	path_construct = os.path.join(path_construct, file)
	# 	if not os.path.is_file(path_construct):
			


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

