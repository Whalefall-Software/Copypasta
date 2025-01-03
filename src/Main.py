from pathlib import Path

inputDirectory = input(Path("Please enter the directory to copy from: "))

print("Input directory is: " + inputDirectory)

print(inputDirectory.exists(inputDirectory))



# def IsValidDirectory(inputDirectory):
#     try: 
#         isdir(inputDirectory)
#     except Exception:
#         print("Invalid directory!")
#         inputDirectory = input("Please enter a valid directory: ")

# if IsValidDirectory(inputDirectory) == True:
#     print("Directory is valid!")
# else:
#     print("Directory is invalid!")

# if IsValidDirectory(inputDirectory) == True:
#     print("Directory input is valid!")
# elif IsValidDirectory(inputDirectory) == False:
#     print("Directory input is not valid!")
    




