# Task 1: Read a File and Handle Errors



try:
    with open("Sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file Sample.txt was not found.")



