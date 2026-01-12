inputFile = open("inputFile.txt", "r")
# print(inputFile.read())

for line in inputFile:
    drivers_list = line.split() # splits on whitespace by default to create an array
    if drivers_list[2] == 'P':
        print(line)
        
inputFile.close()
