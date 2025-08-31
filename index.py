def read_and_modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
        return
    except IOError:
        print(f"Error: Could not read the file '{input_filename}'.")
        return

    # Example modification: convert all text to uppercase
    modified_lines = [line.upper() for line in lines]

    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)
        print(f"Modified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    input_filename = input("Enter the filename to read: ")
    output_filename = input("Enter the filename to write the modified content: ")
    read_and_modify_file(input_filename, output_filename)