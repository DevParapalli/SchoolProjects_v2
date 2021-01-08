"Write a Program to read data from data file in append mode and "
"use writeLines function utility in python."
__lines = [
    "Line 01 *\n"
    "Line 02 **\n",
    "Line 03 ***\n",
    "Line 04 ****\n",
    
]

with open('40_append_file.txt', 'a') as file:
    file.writelines(__lines)

__OUTPUT__ = """

"""