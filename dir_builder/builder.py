import outline_parser

from pathlib import Path
import shutil


def build_dir_structure(node, name):
	"""
	TODO - Is this function even needed?
	"""
	path = Path.cwd() / "output" / name
	build_helper(node, path)
	
def build_helper(node, path):
	"""
	"""
	if node.node_type == '<ROOT>':
		for n in node.children:
			build_helper(n, path)

	elif node.node_type == '<FOLDER>':
		folder_path = path / node.value
		if not folder_path.exists():
			Path.mkdir(folder_path, parents=True)
		for n in node.children:
			build_helper(n, folder_path)

	elif node.node_type == '<FILE>':
		file_path = path / node.value
		with open(file_path, 'w') as f:
			for c in node.children:
				if c.node_type != "<CONTENT>":
					raise Exception("invalid content")
				f.write(c.value)

def create_main(source, output_path, number = False):
	"""
	TODO - Does some of this function belong elsewhere?
	"""
	source = Path(source)
	if not Path.is_file(source):
		raise Exception("invalid file")
	
	output_path = Path(output_path)
	if output_path.exists():
		shutil.rmtree(output_path)

	Path.mkdir(output_path)
	
	with open(source) as mydata:
		source_text = mydata.read()
	lexemes = outline_parser.lex(source_text)
	tokens = outline_parser.parse(lexemes)
	tree_root = outline_parser.build_tree(tokens)

	if number == True:
		outline_parser.number_tree(tree_root, 3)

	build_helper(tree_root, output_path)



if __name__ == "__main__":
	
	with open('test_files\\folderstruct1.txt') as mydata:
		data1 = mydata.read()
	with open('test_files\\folderstruct2.txt') as mydata:
		data2 = mydata.read()
	with open('test_files\\folderstruct3.txt') as mydata:
		data3 = mydata.read()
	with open('test_files\\folderstruct4.txt') as mydata:
		data4 = mydata.read()

	lexemes1 = lex(data1)
	lexemes2 = lex(data2)
	lexemes3 = lex(data3)
	lexemes4 = lex(data4)

	second_pass1 = parse(lexemes1)
	second_pass2 = parse(lexemes2)
	second_pass3 = parse(lexemes3)
	second_pass4 = parse(lexemes4)

	tree1 = build_tree(second_pass1)
	tree2 = build_tree(second_pass2)
	tree3 = build_tree(second_pass3)
	tree4 = build_tree(second_pass4)

	print("\n\n=====STARTING=====\n\n")

	build_dir_structure(tree1, "1")
	build_dir_structure(tree2, "2")
	build_dir_structure(tree3, "3")
	build_dir_structure(tree4, "4")