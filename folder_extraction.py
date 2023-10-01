
import os

# Specify the folder path you want to read
folder_path = 'G:\Certificate'

# List all files in the folder
file_list = os.listdir(folder_path)

# Create a text file to store the list of file names
output_file_path = 'file_list.txt'

# Write the file names (without extensions) to the text file
with open(output_file_path, 'w') as file:
    for filename in file_list:
        name_without_extension, _ = os.path.splitext(filename)
        file.write(name_without_extension + '\n')

print(f'File list (without extensions) has been written to {output_file_path}')
