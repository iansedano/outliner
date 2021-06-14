import dir_builder

import os
import glob



dir_builder.create_main(
	'tests\\test_input_files\\folderstruct1.txt',
	"tests\\test_output\\1",
	number = False
	)
dir_builder.create_main(
	'tests\\test_input_files\\folderstruct2.txt',
	"tests\\test_output\\2",
	number = False
	)
dir_builder.create_main(
	'tests\\test_input_files\\folderstruct3.txt',
	"tests\\test_output\\3",
	number = False
	)
dir_builder.create_main(
	'tests\\test_input_files\\folderstruct4.txt',
	"tests\\test_output\\4",
	number = False
	)

path = "tests\\test_output"

# Clearing verification file
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

