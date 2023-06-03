import os

# Set the directory path where your text files are located
directory = '/home/siddharth/yolo/darknet/data/labels'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        
        # Read the contents of the file
        with open(filepath, 'r') as file:
            lines = file.readlines()

        # Modify the lines by replacing the first number with 0
        modified_lines = ['0 ' + line.split(' ', 1)[1] for line in lines]

        # Write the modified lines back to the file
        with open(filepath, 'w') as file:
            file.writelines(modified_lines)
