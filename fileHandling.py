# file_object = open("filename" , "mode") -opening the file

# file_object.close() - closing the file

# r - reading from a file

# w - for writing to a file

# a - appending to a file

# for reading the file common methods - read() , readline() or readlines()


# example


# with open("example.txt" , "r") as file:
#     content = file.read()
#     print(content)

# it either empties or opens a new file
# with open("sample.txt" , "w") as file:
#     file.write("hello python world")

# appending
# example.txt
with open("/Users/mudit/Desktop/PYTHON/example.txt" , "a") as file:
    file.write("\n hello my name is mudit")


