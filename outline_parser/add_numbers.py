"""Stage 4 (Optional)
Takes the root of a tree and numbers all the siblings, eg:

	Root
		01
		02
			01
			02
		03
		04
"""
from utils import Counter

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
