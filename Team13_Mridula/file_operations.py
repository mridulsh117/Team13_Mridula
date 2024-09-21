import os 
import shutil #Module used for file operations

class FileOperations:
    @staticmethod
    def list_files():
        #Function to list all files in current directory
        try:
            files = [f for f in os.listdir('.') if os.path.isfile(f)]
            if files:
                print("Files in the current directory:")
                for file in files:
                    print(f" - {file}")
            else:
                print("No files found in the current directory.")
        except Exception as e:
            print(f"An error occurred while listing files: {e}")

    @staticmethod
    def list_dirs():
        #Function to list all directories in the current directory
        try:
            dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
            if dirs:
                print("Directories in the current directory:")
                for dir in dirs:
                    print(f" - {dir}")
            else:
                print("No directories found in the current directory.")
        except Exception as e:
            print(f"An error occurred while listing directories: {e}")

    @staticmethod
    def cat_file(filename):
        #Function to display the contents of a file
        try:
            with open(filename, 'r') as file:
                print(f"Contents of {filename}:")
                print(file.read())
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file '{filename}': {e}")

    @staticmethod
    def head_file(filename, lines=5):
        #Function to display the first 5 lines of a file
        try:
            with open(filename, 'r') as file:
                print(f"First {lines} lines of {filename}:")
                for _ in range(lines):
                    print(file.readline(), end='')
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file '{filename}': {e}")

    @staticmethod
    def tail_file(filename, lines=5):
        #Function to display the last 5 lines of a file
        try:
            with open(filename, 'r') as file:
                all_lines = file.readlines()
                print(f"Last {lines} lines of {filename}:")
                for line in all_lines[-lines:]:
                    print(line, end='')
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file '{filename}': {e}")

    @staticmethod
    def copy_file(src, dest):
        #Function to Copy a file from src to dest
        try:
            shutil.copy(src, dest)
            print(f"Successfully copied '{src}' to '{dest}'.")
        except FileNotFoundError:
            print(f"The source file '{src}' does not exist.")
        except Exception as e:
            print(f"An error occurred while copying the file: {e}")

    @staticmethod
    def remove_file(filename):
        #Function to delete a file
        try:
            os.remove(filename)
            print(f"Successfully removed '{filename}'.")
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist.")
        except Exception as e:
            print(f"An error occurred while removing the file '{filename}': {e}")

    @staticmethod
    def empty_file(filename):
        #Function to Empty the contents of a file
        try:
            with open(filename, 'w') as file:
                pass
            print(f"Successfully emptied '{filename}'.")
        except Exception as e:
            print(f"An error occurred while emptying the file '{filename}': {e}")

