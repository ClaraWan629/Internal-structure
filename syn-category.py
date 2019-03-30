"""
This program is to strip out the syntactic category structural variations
30 July 2018
By Clara WAN
"""
import sys
import glob
import nltk
from nltk import FreqDist

# read a file
file = open('E:\\A-output\\Spoken_linear.txt', 'r', encoding='utf-8')
text = file.readlines()
file.close()

my_syn_cat = []
for line in text:
    newline = line.strip('A,CL:-\n')
    temp_list1 = newline.split('-')
    the_list =[]
    for code in temp_list1:
        temp_list2 = code.split(',')
        the_list.append(temp_list2[0])

    the_line = '-'.join(the_list)
    my_syn_cat.append(the_line)

fd = nltk.FreqDist(line for line in my_syn_cat)
feature_frequency = fd.most_common()

#write to a file
out = open('E:\\A-output\\Spoken_category_fd.txt', 'w', encoding='utf-8')
for fea,fre in feature_frequency:
    out.write(fea + '\t' + str(fre) + '\n')
out.close()

print('The A,CL syntactic category frequency distribution file is successfully created.')