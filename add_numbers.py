from lexing import lexer
from parsing import parse
from ast import *
from counter import Counter

def number_tree(root, pad):
	folders = []
	files = []

	if root.node_type == '<ROOT>':
		
		for n in root.children:
			if n.node_type == '<FOLDER>':
				folders.append(n)
			elif n.node_type == '<FILE>':
				files.append(n)
	else:
		raise Exception("invalid root")

	print(folders)
	number_folders(folders, pad)
	number_files(files, pad)

	return root

def number_folders(folders, pad):
	if len(folders) == 0:
		return

	counter = Counter(0, pad = pad)
	files = []
	for n in folders:
		n.value = counter.i() + n.value
		sub_folders = []
		sub_files = []
		for child in n.children:
			if child.node_type == '<FOLDER>':
				sub_folders.append(child)
			elif child.node_type == '<FILE>':
				sub_files.append(child)
		number_folders(sub_folders, pad)
		number_files(sub_files, pad)


def number_files(files, pad):
	if len(files) == 0:
		return
	counter = Counter(0, pad = pad)
	for n in files:
		n.value = counter.i() + n.value


if __name__ == "__main__":
	# print("\n\n=====STARTING=====\n\n")

	lexemes1 = lexer('test_files\\folderstruct1.txt')
	lexemes2 = lexer('test_files\\folderstruct2.txt')
	lexemes3 = lexer('test_files\\folderstruct3.txt')
	lexemes4 = lexer('test_files\\folderstruct4.txt')

	second_pass1 = parse(lexemes1)
	second_pass2 = parse(lexemes2)
	second_pass3 = parse(lexemes3)
	second_pass4 = parse(lexemes4)

	root1 = build_tree(second_pass1)
	root2 = build_tree(second_pass2)
	root3 = build_tree(second_pass3)
	root4 = build_tree(second_pass4)

	Nroot1 = number_tree(root1, 3)
	Nroot2 = number_tree(root2, 3)
	Nroot3 = number_tree(root3, 3)
	Nroot4 = number_tree(root4, 3)

	print_children(Nroot3)
	
