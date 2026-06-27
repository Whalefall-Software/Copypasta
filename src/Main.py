import os
import shutil
import filecmp
import click

def ValidateDirectory(userDirectoryPath): 
    try:
        while os.path.isdir(userDirectoryPath) == False:
            userDirectoryPath = input("Please enter a valid directory: ")
        if os.path.isdir(userDirectoryPath) == True:
            print(f"{userDirectoryPath} is a valid directory!")
            totalBytes = GetSizeOfDirectory(userDirectoryPath)
    except Exception as e:
        print(f"Error: {e} unexpected error occurred.")

def CopyDirectory(source, destination):
    try:
        totalSize = GetSizeOfDirectory(source)
        with click.progressbar(length=totalSize) as bar:

            for dirPath, dirName, files in os.walk(source):

                relativePath = os.path.relpath(dirPath, source)
                targetPath = os.path.join(destination, relativePath)

                os.makedirs(targetPath, exist_ok=True)

                for file in files:

                    sourceFile = os.path.join(dirPath, file)
                    targetFile = os.path.join(targetPath, file)

                    shutil.copy2(sourceFile, targetFile)

                    fileSize = os.path.getsize(sourceFile)
                    bar.update(fileSize)

    except Exception as e:
        print(f"Error copying directory {source}: {e}")
    else:
        print(f"Copying directory {source} to {destination} was successful.")

def MoveDirectory(source, destination):
    try:
        totalSize = GetSizeOfDirectory(source)
        with click.progressbar(length=totalSize) as bar:

            for dirPath, dirName, files in os.walk(source):

                relativePath = os.path.relpath(dirPath, source)
                targetPath = os.path.join(destination, relativePath)

                os.makedirs(targetPath, exist_ok=True)

                for file in files:

                    sourceFile = os.path.join(dirPath, file)
                    targetFile = os.path.join(targetPath, file)

                    shutil.copy2(sourceFile, targetFile)

                    fileSize = os.path.getsize(sourceFile)
                    bar.update(fileSize)

        if not ValidateOperation(source, destination, False):
            print("Copy failed...")
            return

        print("Cleaning up...")

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
    filecmp.clear_cache() # Used to eliminate cached comparison results that can give inaccurate results
    try:
        dirDiff = filecmp.dircmp(source, destination)
        if dirDiff.diff_files:
            print(f"Mismatched files: {dirDiff.diff_files}")
            return False
        elif dirDiff.left_only or dirDiff.right_only:
            print(f"Only in source: {dirDiff.left_only}")
            print(f"Only in destination: {dirDiff.right_only}")
            return False
        else:
            print(f"Contents of contents of {source} to {destination} match.")
            return True
    except Exception as e:
        print(f"Error validating contents of {source} to {destination} \n {e}")
        
def GetSizeOfDirectory(directory):
    totalSize = 0
    for dirPath, dirNames, fileNames in os.walk(directory):
        for file in fileNames:
            filePath = os.path.join(dirPath, file)
            totalSize += os.path.getsize(filePath)

    return totalSize
   
def ChooseOperation(sourceDirectory, destinationDirectory):
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

src: str = input("Please enter the source directory: ")
src: str = src.replace('"', '') 
src: str = src.replace("'", "")
ValidateDirectory(src)

dst: str = input("Please enter the destination directory: ")
dst: str = dst.replace('"', '')
dst: str = dst.replace("'", "")
ValidateDirectory(dst)

ChooseOperation(src, dst)