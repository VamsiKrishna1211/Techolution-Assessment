import os
from pathlib import Path

# class FileFormatter:

#     @staticmethod
#     def create(file_name) -> str:
#         # return f"File {file_name} created"

#         # Check if file already exists
#         if Path(file_name).is_file():
#             return f"File {file_name} already exists"

#         with open(file_name, "w") as file:
#             file.write("Hello World")
#         return f"File {file_name} successfully created"
    
#     @staticmethod
#     def delete(file_name) -> str:
#         try:
#             os.remove(file_name)
#             return f"File {file_name} deleted"
#         except FileNotFoundError:
#             return f"File {file_name} not found"

#     @staticmethod
#     def rename(file_name, new_file_name) -> str:
#         try:
#             os.rename(file_name, new_file_name)
#             return f"File {file_name} renamed to {new_file_name}"
#         except FileNotFoundError:
#             return f"File {file_name} not found"
    

# if __name__ == "__main__":
#     file = FileFormatter()

#     while True:

#         command = input()
#         if "CREATE" in command:
#             try:
#                 file_name = command.split(" ")[1]
#                 print(file.create(file_name))
#             except IndexError:
#                 print("Please enter a file name")
#                 continue

#         elif "DELETE" in command:
#             try:
#                 file_name = command.split(" ")[1]
#                 print(file.delete(file_name))
#             except IndexError:
#                 print("Please enter a file name")
#                 continue
#         elif "RENAME" in command:
#             try:
#                 file_name = command.split(" ")[1]
#                 new_file_name = command.split(" ")[2]
#                 print(file.rename(file_name, new_file_name))
#             except IndexError:
#                 print("Please enter a file name")
#                 continue
#         elif "EXIT" in command:
#             print("Exiting...")
#             break
        
#         else:
#             print("Invalid command, please enter commands starting with CREATE, DELETE or RENAME.")

class FileManager:
    """
    FileManager class is responsible for managing files in memory.
    """
    def __init__(self):
        """
        Initialize an empty set to store file names.
        """
        self.files = set()

    def create_file(self, file_name: str) -> str:
        """
        Create a file with the given name.
        """
        if file_name in self.files:
            return f"File {file_name} already exists"
        self.files.add(file_name)
        return f"File {file_name} successfully created"
    
    def delete_file(self, file_name: str) -> str:
        """
        Delete a file with the given name.
        """
        if file_name not in self.files:
            return f"File {file_name} not found"
        self.files.remove(file_name)
        return f"File {file_name} deleted"

    def rename_file(self, old_name: str, new_name: str) -> str:
        """
        Rename a file from old_name to new_name.
        """
        if old_name not in self.files:
            return f"File {old_name} not found"
        if new_name in self.files:
            return f"File {new_name} already exists"
        self.files.remove(old_name)
        self.files.add(new_name)
        return f"File {old_name} renamed to {new_name}"

    def list_files(self):
        """
        List all files.
        """
        return self.files


def process_commands():
    """
    Process commands from the user.
    """
    file_manager = FileManager()

    while True:
        command = input("Please enter a command: ").split()
        if not command:
            # print("Please enter a command.")
            continue

        action = command[0].upper()
        if action == "CREATE":
            if len(command) != 2:
                print("Usage: CREATE filename")
                continue
            print(file_manager.create_file(command[1]))

        elif action == "DELETE":
            if len(command) != 2:
                print("Usage: DELETE filename")
                continue
            print(file_manager.delete_file(command[1]))

        elif action == "RENAME":
            if len(command) != 3:
                print("Usage: RENAME old_filename new_filename")
                continue
            print(file_manager.rename_file(command[1], command[2]))

        elif action == "LIST":
            print("Current list of files:")
            for file_name in file_manager.list_files():
                print(file_name)

        elif action == "EXIT":
            break

        else:
            print("Invalid command. Available commands: CREATE, DELETE, RENAME, LIST, EXIT")


if __name__ == "__main__":
    process_commands()
