import os
import shutil
import filecmp
import click
import Main

def ChooseOperation(sourceDirectory, destinationDirectory):
    operationState = ""
    operationState = input("Enter the function you want to do.\n(C)opy, (M)ove, (V)alidate, or (B)yte-by-byte validation: ")
    match operationState.lower():
        case 'c': 
            Main.CopyDirectory(sourceDirectory, destinationDirectory)
        case 'm':
            Main.MoveDirectory(sourceDirectory, destinationDirectory)
        case 'v':
            Main.ValidateOperation(sourceDirectory, destinationDirectory, False)
        case 'b':
            Main.ValidateOperation(sourceDirectory, destinationDirectory, True)
        case _:
            print("Error: Invalid input given!")

src: str = input("Please enter the source directory: ")
while Main.isValidDir(src) == False:
    src: str = input("Please enter a valid source directory: ")
if Main.isValidDir(src) == True:
    print(f"{src} is a valid directory!")
else:
    Main.isValidDir(src)

dst: str = input("Please enter the destination directory: ")
while Main.isValidDir(dst) == False:
    dst: str = input("Please enter a valid source directory: ")
if Main.isValidDir(dst) == True:
    print(f"{dst} is a valid directory!")
else:
    Main.isValidDir(dst)

ChooseOperation(src, dst)

