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
        files = os.listdir(source)
        for file in files:
            filePath = os.path.join(source, file)
            if os.path.join(filePath):
                os.remove(filePath)
            elif os.path.isdir(filePath):
                shutil.rmtree(filePath)
            
    except Exception as e:
        print(f"Error moving directory {source}: {e}")
    else:
        print(f"Moving directory {source} to {destination} was successful.")
        
def ValidateOperation(source, destination, depth):
    filecmp.clear_cache() #Used to eliminate cached comparison results that can give innacurate results
    try:
        dirDiff = filecmp.dircmp(source, destination, shallow=depth)
        if dirDiff.diff_files:
            print(f"Mismatched files: {dirDiff.diff_files}")
        elif dirDiff.left_only or dirDiff.right_only:
            print(f"Only in source: {dirDiff.left_only}")
            print(f"Only in destination: {dirDiff.right_only}")
        else:
            print(f"Contents of contents of {source} to {destination} match.")
    except:
        print(f"Error validating contents of {source} to {destination}")
        
sourceDirectory: str = input("Please enter the source directory: ")
ValidateDirectory(sourceDirectory)

destinationDirectory: str = input("Please enter the destination directory: ")
ValidateDirectory(destinationDirectory)
   
def ChooseOperation():
    operationState = ""
    operationState = input("Enter the function you want to do.\n(C)opy, (M)ove, (V)alidate, or (B)yte-by-byte validation: ")
    match operationState.lower():
        case 'c': 
            CopyDirectory(sourceDirectory, destinationDirectory)
        case 'm':
            MoveDirectory(sourceDirectory, destinationDirectory)
        case 'v':
            ValidateOperation(sourceDirectory, destinationDirectory, False)
        case 'b':
            ValidateOperation(sourceDirectory, destinationDirectory, True)
        case _:
            print("Error: Invalid input given!")

ChooseOperation()