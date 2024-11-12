

"""
text = "HEllo 2"

file = open("test1.txt", "a")
file.write(text)
file.close()


file = open("test1.txt", "r")
output = file.read()
file.close()
print(output)



with open("test2.special", "w") as f:
    f.writelines(["line1\n", "line2"])


with open("test2.special", "r") as f:
    text = f.readlines()
    print(text)

"""

"""
FILE_PATH = "test1.txt"

f = open(FILE_PATH, "w")
f.write("Hello world I am ales and i want to go home")
f.close()

"""
"""# Define the source and destination file paths
source_file = "source.txt"  # The existing file you want to read from
destination_file = "filtered_words.txt"  # The new file where results will be written

# Open the source file in read mode and the destination file in write mode
with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
    # Read each line in the source file
    for line in src:
        # Split each line into words
        words = line.split()

        # Filter words that have at least 4 letters
        filtered_words = [word for word in words if len(word) >= 4]

        # Write the filtered words to the destination file, joined by a space
        dest.write(" ".join(filtered_words) + "\n")"""


"""
#Task1

existing_FILE_PATH = "test1.txt"
new_file = "filtered_words.txt"

print("ahoj")
print("rrrr")

with open(existing_FILE_PATH) as src, open(new_file, 'w') as dest:
    for line in src:
        words = line.split()

        filtered_words = [word for word in words if len(word) >= 4]

        dest.write(" ".join(filtered_words) + "\n")
"""

#Task9
# Define the path to the file
file_path = "test.txt"

# Open the file in read mode and count the characters
with open(file_path, 'r') as file:
    content = file.read()  # Read the entire file content
    num_characters = len(content)  # Count the characters

print(f"The number of characters in the file is: {num_characters}")


