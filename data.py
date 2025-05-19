def modify_content(content):
    # Example modification: reverse each line
    lines = content.splitlines()
    reversed_lines = [line[::-1] for line in lines]
    return "\n".join(reversed_lines)

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return

    modified_content = modify_content(content)
    new_filename = "modified_" + filename

    try:
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to '{new_filename}'")
    except IOError:
        print(f"Error: Could not write to the file '{new_filename}'.")

if __name__ == "__main__":
    main()
