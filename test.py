from o_lexer import lex
from o_parser import parse
from o_ast import build_tree
from o_creator import create
import os
import glob



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

create(tree1, "1")
create(tree2, "2")
create(tree3, "3")
create(tree4, "4")


path = "output"

# for root, subdirs, files in os.walk(path):

# 	for subdir in subdirs:
# 		new path

open('test_files\\verifier.txt', 'w').close()

with open('test_files\\verifier.txt', 'a') as f:
	for filename in glob.iglob(path + '**/**', recursive=True):
		f.write(filename)
		f.write('\n')
		if os.path.isfile(filename):
			with open(filename) as c:
				f.writelines(c)
				f.write('\n')


with open('test_files\\verifier.txt', 'r') as v:
	with open('test_files\\verifier_master.txt', 'r') as m:
		if v.read() != m.read():
			raise Exception("Verification Failed!")

print("\n\n=====================\n\nverification success!")

