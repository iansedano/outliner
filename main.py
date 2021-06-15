import dir_builder

# Insert full Linux (no ~) or Windows (with escaped backslashes) path here 
source_file = "C:\\Dev\\0 Git sync\\react-course\\00-js2-react\\000-temp_outlines\\connect4.txt"
output = "D:\\Dropbox\\Desktop\\test"

# the argument number here is used to number the output folders and files
dir_builder.create_main(source_file, output, number = True)