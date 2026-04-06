import os
import shutil
import filecmp

def ChooseOperation():
    operationState = ""
    operationState = input("Enter the function you want to do.\n(C)opy or (M)ove: ")
    # match operationState.lower():
    #     case 'c': 
    #         CopyDirectory(sourceDirectory, destinationDirectory)
    #     case 'm':
    #         MoveDirectory(sourceDirectory, destinationDirectory)
    #     case _:
    #         print("Error: Invalid input given!")

    if operationState == "C" or "c":
        CopyDirectory(sourceDirectory, destinationDirectory)
    elif operationState == "M" or "m":
        MoveDirectory(sourceDirectory, destinationDirectory)

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

sourceDirectory: str = input("Please enter the source directory: ")
ValidateDirectory(sourceDirectory)

destinationDirectory: str = input("Please enter the destination directory: ")
ValidateDirectory(destinationDirectory)

ChooseOperation()
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
