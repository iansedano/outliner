from o_creator import create_main

# Insert full Linux (no ~) or Windows (with escaped backslashes) path here 
source_file = "/home/i/Dropbox/Desktop/outliner_linux_test/outline.txt"
output = "/home/i/Dropbox/Desktop/outliner_linux_test/output"

# the argument number here is used to number the output folders and files
create_main(source_file, output, number = True)