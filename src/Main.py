import os
import shutil
import filecmp
import click

def isValidDir(userDirectoryPath):
    try:
        while os.path.isdir(userDirectoryPath) == False:
            return False
        if os.path.isdir(userDirectoryPath) == True:
            return True
    except Exception as e:
        return e
    
def ValidateDirectory(userDirectoryPath):
    try:
        isValidDir: bool = os.path.isdir(userDirectoryPath)
        while isValidDir == False:
            return isValidDir
        if isValidDir == True:
            totalBytes = GetSizeOfDirectory(userDirectoryPath)
            return isValidDir
    except Exception as e:
        validateDirMessage: str = f"Error: {e} unexpected error occurred."
        return validateDirMessage

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
        copyDirMessage: str = f"Error copying directory {source}: {e}"
        return copyDirMessage
    else:
        copyDirMessage: str = f"Copying directory {source} to {destination} was successful."
        return copyDirMessage

def MoveDirectory(source, destination):
    try:
        copyFailed: bool = False 
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
            copyFailed = True
            return copyFailed 

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
   