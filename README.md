# Alfido Tech Internship - Task 1: File Operations in Python

This repository contains the solution for **Task 1** of the Alfido Tech Internship. The project demonstrates fundamental file handling and management operations in Python using the built-in `os` and `shutil` modules.

---

## 🚀 Features

The script automates a complete lifecycle of file management, executing the following operations sequentially:

1. **Create & Write:** Creates a new text file named `sample.txt` and populates it with text.
2. **Read:** Opens and reads the content of the file, displaying it in the console.
3. **Rename:** Changes the file name from `sample.txt` to `renamed_sample.txt`.
4. **Directory Management:** Safely creates a new directory named `backup/` if it does not already exist.
5. **Move:** Relocates the renamed file into the `backup/` directory.
6. **Delete:** Removes the file from the backup directory to clean up the workspace.
7. **Error Handling:** Implements `try-except` blocks to gracefully catch and log `FileNotFoundError` or any other unexpected exceptions.

---

## 🛠️ Prerequisites

To run this script, you only need Python installed on your system. No external third-party libraries are required.

* Python 3.x
