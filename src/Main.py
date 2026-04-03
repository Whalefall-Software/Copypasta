import os
import shutil
import filecmp

def ValidateDirectory(userDirectoryPath):
    try:
        while os.path.isdir(userDirectoryPath) == False:
            userDirectoryPath = input("Please enter a valid directory: ")
        if os.path.isdir(userDirectoryPath) == True:
            print(f"{userDirectoryPath} is a valid directory!")
    except Exception as e:
        print(f"Error: {e} unexpected error occurred.")

sourceDirectory: str = input("Please enter the directory to copy from: ")
ValidateDirectory(sourceDirectory)

destinationDirectory: str = input("Please enter the destination directory: ")
ValidateDirectory(destinationDirectory)

def CopyDirectory(source, destination):
    try:
        shutil.copytree(source, destination, dirs_exist_ok=True)
    except Exception as e:
        print(f"Error copying directory {source}: {e}")
    else:
        print(f"Copying directory {source} to {destination} was successful.")

def MoveDirectory(source, destination):
    try:
        shutil.copytree(source, destination, dirs_exist_ok=True)
        shutil.rmtree(source)
    except Exception as e:
        print(f"Error moving directory {source}: {e}")
    else:
        print(f"Moving directory {source} to {destination} was successful.")

def ValidateOperation(source, destination):
    try:
        dirDiff = filecmp.dircmp(source, destination)
        if dirDiff.diff_files:
            print(f"Mismatched files: {dirDiff.diff_files}")
        if dirDiff.left_only or dirDiff.right_only:
            print(f"Only in source: {dirDiff.left_only}")
            print(f"Only in destination: {dirDiff.right_only}")
        else:
            print(f"Contents of contents of {source} to {destination} match.")
    except:
        print(f"Error validating contents of {source} to {destination}")
    
def ChooseOperation():
    operationState = input("Enter the function you want to do.\n(C)opy, (M)ove, or (V)alidate: ")
    if operationState == "C" or "c":
        CopyDirectory(sourceDirectory, destinationDirectory)
    elif operationState == "M" or "m":
        MoveDirectory(sourceDirectory, destinationDirectory)
    elif operationState == "V" or "v":
        ValidateOperation(sourceDirectory, destinationDirectory)
        
ChooseOperation()
