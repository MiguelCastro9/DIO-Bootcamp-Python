# manipulating text files in python

# To manipulate files in Python, we first need to open them.
# we use the 'open()' function for this. When we finish working with the file, 
# we use the 'close()' function to free up resources.

# There are different modes to open a file, such as read-only ('r'), write ('w') and append ('a'). 
# the opening mode must be chosen according to the operation that we will perform on it.

# a good practice is to handle exceptions when working with files.

try:
    file = open("text_01.txt", "r")
    print(file.read())
    file.close()

    file = open("text_02.txt", "w")
    file.write("writing data to a new file")
    print("text_02 file created and written successfully!")
    file.close()

    file = open("text_03.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError as exc:
    print("file not found for reading.")
    print(exc)

# a good practice tip is also to use 'with' which closes the file automatically after the operation,
# and also use 'encoding' to set the file's encoding.

try:
    with open("text_03.txt", "w", encoding="utf-8") as file:
        file.write("file treated with good practices!")
        file = open("text_03.txt", "r")
        print(file.read())
except IOError as exc:
    print("error opening the file.")