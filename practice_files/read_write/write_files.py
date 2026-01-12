import os

# Get folder where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build paths to files in the same folder
input_file_path = os.path.join(script_dir, "inputFile.txt")
pass_file_path = os.path.join(script_dir, "passFile.txt")
fail_file_path = os.path.join(script_dir, "failFile.txt")

# open inputFile.txt with the intention of reading it
# open passFile.txt with the intention of writing it
# open failFile.txt with the intention of writing it
with open(input_file_path, "r") as inputFile, \
  open(pass_file_path, "w") as passFile, \
  open(fail_file_path, "w") as failFile:
       
  # loop through each line in inputFile.txt
  for line in inputFile:
      line_split = line.split()
      if line_split[2] == "P":
        passFile.write(line)
      else:
        failFile.write(line)

# files automatically close when using the 'with' block, otherwise close all files i.e. inputFile.close()
