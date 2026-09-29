# This is a simple file management program that allows users to create, read, update, and delete files in the current directory. It uses the `pathlib` module for handling file paths and the `os` module for file operations.
from pathlib import Path
import os

# Function to read all files and folders in the current directory
def readfileandfolder():
    path = Path(".")
    items = list(path.rglob("*"))
    for i, item in enumerate(items):
        print(f"{i + 1}: {item}")


# Function to create a new file
def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to create: ")
        p = Path(name)
        if not p.exists():
          with open(p, 'w') as f:
            data = input("Enter the data you want to write in the file: ")
            f.write(data)
          print(f"File '{name}' created successfully.")
        else:
            print(f"File '{name}' already exists.")


    except Exception as e:
     print(f"An error occurred while creating the file: {e}")


# Function to read a file
def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, 'r') as f:
                data = f.read()
                print(f"Contents of '{name}':\n{data}")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


#  Function to update a file
def updatefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of the file: ")
            print("Press 2 for overwriting the content of the file: ")
            print("Press 3 for appending the content of the file: ")
            choice = int(input("Please Enter your response: "))
            if choice == 1:
                new_name = input("Enter the new name for the file: ")
                p.rename(new_name)
                print(f"File renamed to '{new_name}' successfully.")
            if choice == 2:
                data = input("Enter the new content for the file: ")
                with open(p, 'w') as f:
                    f.write(data)
                print(f"File '{name}' overwritten successfully.")
            if choice == 3:
                data = input("Enter the content to append to the file: ")
                with open(p, 'a') as f:
                    f.write(data)
                print(f"Content appended to '{name}' successfully.")
    except Exception as e:
      print(f"An error occurred while updating the file: {e}")


# Function to delete a file
def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print(f"File '{name}' deleted successfully.")
        else:
            print(f"File '{name}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

print("Press 1 for creating a file: ")
print("Press 2 for reading a file: ")
print("Press 3 for updating a file: ")
print("Press 4 for deletion a file: ")
print("Press 5 for exiting the program: ")

check = int(input("Please Enter your response: "))
if check==1:
    createfile()

if check==2:
    readfile()

if check==3:
    updatefile()

if check==4:
    deletefile()

if check == 5:
        print("Exiting the program. Goodbye!")