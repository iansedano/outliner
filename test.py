import os

cwd = os.getcwd()

path = os.path.join(cwd, "test", "child")

print(path)

path_list = path.split("\\")

path_list[0] = path_list[0] + "\\"

path_construct = ""

for p in path_list:
	path_construct = os.path.join(path_construct, p)
	if not os.path.exists(path_construct):
		print("making directory " + path_construct)
		os.mkdir(path_construct)
	else:
		print(path_construct + " already exists")



def create_path_if_exist(path):

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
			