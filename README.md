# Techolution Assessment

## Problem Statement

### File Processing System
Write a Python program that reads a series of commands from stdin regarding file operations. 
The commands will be in the format: CREATE filename, DELETE filename, RENAME filename new_filename. 
The program should process these commands and output the current list of files after all operations are complete. 
Use OOP principles to design the file handling system.

Example Input:
```
CREATE file1.txt
RENAME file1.txt file2.txt
CREATE file3.txt
```
Expected Output:
```
file2.txt
file3.txt
```

Evaluation Criteria:
- Correct parsing and processing of input commands.
- Effective use of classes and objects for file management.
- Accurate output of the final state of files.
