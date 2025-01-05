import os

def ValidateDirectory(userDirectoryPath):
    try:
        while os.path.isdir(userDirectoryPath) == False:
            userDirectoryPath = input("Please enter a valid directory: ")
            
        if os.path.isdir(userDirectoryPath) == True:
            print(f"{userDirectoryPath} is a valid directory!")

    except Exception as e:
        print(f"Error: {e} unexpected error occurred.")

sourceDirectory = input("Please enter the directory to copy from: ")
ValidateDirectory(sourceDirectory)

destinationDirectory = input("Please enter the destination directory: ")
ValidateDirectory(destinationDirectory)
