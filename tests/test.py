import os
import glob

import outline_parser
import dir_builder


with open('tests\\test_input_files\\folderstruct1.txt') as mydata:
	data1 = mydata.read()
with open('tests\\test_input_files\\folderstruct2.txt') as mydata:
	data2 = mydata.read()
with open('tests\\test_input_files\\folderstruct3.txt') as mydata:
	data3 = mydata.read()
with open('tests\\test_input_files\\folderstruct4.txt') as mydata:
	data4 = mydata.read()

lexemes1 = outline_parser.lex(data1)
lexemes2 = outline_parser.lex(data2)
lexemes3 = outline_parser.lex(data3)
lexemes4 = outline_parser.lex(data4)

second_pass1 = outline_parser.parse(lexemes1)
second_pass2 = outline_parser.parse(lexemes2)
second_pass3 = outline_parser.parse(lexemes3)
second_pass4 = outline_parser.parse(lexemes4)

tree1 = outline_parser.build_tree(second_pass1)
tree2 = outline_parser.build_tree(second_pass2)
tree3 = outline_parser.build_tree(second_pass3)
tree4 = outline_parser.build_tree(second_pass4)

dir_builder.builder.build_dir_structure(tree1, "1")
dir_builder.builder.build_dir_structure(tree2, "2")
dir_builder.builder.build_dir_structure(tree3, "3")
dir_builder.builder.build_dir_structure(tree4, "4")


path = "tests\\test_output"

# for root, subdirs, files in os.walk(path):

# 	for subdir in subdirs:
# 		new path

open('tests\\test_verification_files\\verifier.txt', 'w').close()

with open('tests\\test_verification_files\\verifier.txt', 'a') as f:
	for filename in glob.iglob(path + '**/**', recursive=True):
		f.write(filename)
		f.write('\n')
		if os.path.isfile(filename):
			with open(filename) as c:
				f.writelines(c)
				f.write('\n')


with open('tests\\test_verification_files\\verifier.txt', 'r') as v:
	with open('tests\\test_verification_files\\verifier_master.txt', 'r') as m:
		if v.read() != m.read():
			print("=====================\nVerification Failed!\n=====================")

print("=====================\nVerification Success!\n=====================")

