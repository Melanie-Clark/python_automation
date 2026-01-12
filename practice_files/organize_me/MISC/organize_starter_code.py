import os
from pathlib import Path

SUBDIRECTORIES = {
  "DOCUMENTS": ['.pdf','.rtf','.txt'],
  "AUDIOS": ['.m4a','.m4b','.mp3'],
  "VIDEOS": ['.mov','.avi','.mp4'],
  "IMAGES": ['.jpg','.jpeg','.png']
}

def pickDirectory(value):
  for category, suffixes in SUBDIRECTORIES.items():
    if value in suffixes:
      return category
  return "MISC"

# test out the pickDirectory() function
print(pickDirectory(".avi"))

def organizeDirectory(target_folder):
  # for item in os.scandir(): # scans all files & folders in project root directory to see if it's a directory
  
  target_folder = Path(target_folder) # path of target folder organize_me
  
  for item in os.scandir(target_folder):
    if item.is_dir(): # if directory exists, skip over rest of function
      continue
    filePath = Path(item) # filepath is created
    fileType = filePath.suffix.lower() # file type is extracted
    directory = pickDirectory(fileType) 
    
    # directoryPath = Path(directory) # directory path is created
    directoryPath = target_folder / directory  # folder inside target_folder
    
    # create directory if dir path doesn't exist
    if directoryPath.is_dir() != True:
      directoryPath.mkdir() 
      
    filePath.rename(directoryPath / filePath.name)  # move file into new folder

# path to  folder
folder_to_organize = Path("practice_files/organize_me")

# test out the organizeDirectory() function
organizeDirectory(folder_to_organize)
