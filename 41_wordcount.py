"Write a Program to read data from data file in read mode and count the particular "
"word occurrences in given string, number of times in python."

import re

words1 = []

def clean_word(unclean_word: str) -> str:
    return re.sub('[._, ?]', "", unclean_word.lower())


with open('41_read_file.txt', 'r') as file:
    for line in file:
        for word in line.split(): # auto concat to string
            words1.append(clean_word(word.lower()))
            
common_not_words = [] # we exclude these words as they are very commonly used and do not represent the actual context


# We create a seperate words list 
words2 = [clean_word(i) for i in words1 if i.lower() not in common_not_words] # add cleaned words to the list
counting_dict = {}
for word in words2:
    if word not in counting_dict.keys():
        counting_dict[word] = 1
    elif word in counting_dict.keys():
        counting_dict[word] = counting_dict[word] + 1

# now we create a list with tuples in them and sort based on the counts
ranking_list = []
for key in counting_dict:
    ranking_list.append((key, counting_dict[key]))

sorted_ranking = sorted(ranking_list, key=lambda x: -1 * x[1]) # we multiple by -1 to make them in the reverse order


print(sorted_ranking[0:5]) # gets the top most 5 in order


__OUTPUT__ = """
[('to', 22), ('your', 21), ('the', 16), ('account', 10), ('and', 8)]
"""