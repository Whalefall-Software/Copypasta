import os
import shutil
import Gui

Gui.launch()

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

def ChooseOperation():
    operationState = input("Enter the function you want to do.\n(C)opy or (M)ove: ")
    if operationState == "C":
        CopyDirectory(sourceDirectory, destinationDirectory)
    elif operationState == "M":
        MoveDirectory(sourceDirectory, destinationDirectory)
        
ChooseOperation()