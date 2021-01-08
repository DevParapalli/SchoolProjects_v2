"Write a Program to read data from data file in read mode and "
"append the data in given file in python."

read_data = []
with open('42_read.txt', 'r') as read_file:
    for line in read_file:
        read_data.append(line)
        print(line)

with open('42_append.txt', 'a') as append_file:
    for line in read_data:
        append_file.write(line)


__OUTPUT__ = """
Line 01 *
Line 02 **
Line 03 ***
Line 04 ****
Line 05 *****
"""