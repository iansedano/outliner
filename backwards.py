from pathlib import Path

def make_outline(
	folder: Path,
	output_file,
	tab_level = 0,
	remove_prefix = False,
	prefix_length = 3
):
	for path in folder.iterdir():
		tabs = "\t" * tab_level
		name = path.parts[-1]
		if remove_prefix:
			name = name[prefix_length:]
		print(tabs + name, file=output_file)
		if path.is_dir():
			make_outline(
				path,
				output_file,
				tab_level + 1,
				remove_prefix = remove_prefix,
				prefix_length = prefix_length
			)
		elif path.is_file():
			with path.open() as text_file:
				for line in text_file.readlines():
					print(tabs + "\t" + line, end="", file=output_file)

root_dir = "D:\\Dropbox\\Desktop\\outliner_backwards_test\\output"
output_file = "D:\\Dropbox\\Desktop\\outliner_backwards_test\\backwards_output.txt"

root_dir = Path(root_dir)
output_file = Path(output_file)

with output_file.open(mode="w") as f:
	make_outline(root_dir, f, remove_prefix = True, prefix_length = 4)



