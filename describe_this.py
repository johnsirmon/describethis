import os


#modify this function to count the number of folders and files in the parent folder
def count_folders_files(parent_folder_path):
    folder_count = 0
    file_count = 0
    for root, dirs, files in os.walk(parent_folder_path):
        folder_count += len(dirs)
        file_count += len(files)
    return folder_count, file_count

# Provide the parent folder path using the current directory
parent_folder_path = os.getcwd()


# Call the function to get the folder count and file count
folder_count, file_count = count_folders_files(parent_folder_path)

import matplotlib.pyplot as plt

# Display the results visually using a circle sunburst chart that shows the number of folders and files
# You can use any library you want. An example using matplotlib is below:

def display_results(folder_count, file_count):
    labels = 'Folders', 'Files'
    sizes = [folder_count, file_count]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Files')
    


# Call the function to display the results
display_results(folder_count, file_count)

print(f"Parent Folder: {parent_folder_path}")
print(f"Folder Count: {folder_count}")
print(f"File Count: {file_count}")
