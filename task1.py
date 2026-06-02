import os
import shutil

try:
    # Create file and write data
    with open("sample.txt", "w") as file:
        file.write("Hello Alphido Tech Internship")

    print("File created successfully")

    # Read file
    with open("sample.txt", "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

    # Rename file
    os.rename("sample.txt", "renamed_sample.txt")
    print("\nFile renamed successfully")

    # Create backup folder
    if not os.path.exists("backup"):
        os.mkdir("backup")

    # Move file
    shutil.move(
        "renamed_sample.txt",
        "backup/renamed_sample.txt"
    )

    print("File moved successfully")

    # Delete file
    os.remove("backup/renamed_sample.txt")

    print("File deleted successfully")

except FileNotFoundError:
    print("File not found")

except Exception as e:
    print("Error:", e)