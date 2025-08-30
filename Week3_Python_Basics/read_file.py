try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File Contents:\n")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist. Please run write_file.py first.")
