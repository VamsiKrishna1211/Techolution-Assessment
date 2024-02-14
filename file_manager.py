import os
from pathlib import Path


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
