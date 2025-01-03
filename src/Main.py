import os

def ValidDirectory(userDirectoryPath):
    try:
        while os.path.isdir(userDirectoryPath) == False:
            userDirectoryPath = input("Please enter a valid directory: ")
        # raise FileNotFoundError(f"{userDirectoryPath} directory not valid!")
        if os.path.isdir(userDirectoryPath) == True:
            print(f"{userDirectoryPath} is a valid directory!")
# except FileNotFoundError as e:
#     print(e)
    except Exception:
        print(f"{Exception} unexpected error occurred.")

sourceDirectory = input("Please enter the directory to copy from: ")
ValidDirectory(sourceDirectory)

destinationDirectory = input("Please enter the destination directory: ")
ValidDirectory(destinationDirectory)

