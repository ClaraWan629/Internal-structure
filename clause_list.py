"""
This program is to extract all the branching structures of all the possible clausal types
18 March 2017
By Clara WAN
"""

import sys
import glob
import nltk
from nltk import FreqDist

# read the files under one directory
path = 'E:\\ICE\\Written\\*.cor'
files = glob.glob(path)
mylist = []
for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()

    for line in text:
        mylist.append(line)
    f.close()

clause_status = 0 # not stimulated when in value 0, stimulated in value > 0: 1-first branching; 2-second branching; 3-third branching; 4-fourth branching; 5-fifth branching
clause_num1 = 0 # for storing the embedding number of the first clause node
clause_num2 = 0 # for storing the embedding number of the 2nd clause node
clause_num3 = 0 # for storing the embedding number of the 3rd clause node
clause_num4 = 0 # for storing the embedding number of the 4th clause node
clause_num5 = 0 # for storing the embedding number of the 5th clause node
clause_num6 = 0 # for storing the embedding number of the 6th clause node
clause_num7 = 0 # for storing the embedding number of the 7th clause node
clause_num8 = 0 # for storing the embedding number of the 7th clause node
clause_num9 = 0 # for storing the embedding number of the 7th clause node
clause_num10 = 0 # for storing the embedding number of the 7th clause node

# marking the A,CL for the first time
cl_list1 = [] # for storing the first selected nodes of A,CL and their internal structures
cl_list2 = [] # for storing the 2nd selected nodes of A,CL and their internal structures
cl_list3 = [] # for storing the 3rd selected nodes of A,CL and their internal structures
cl_list4 = [] # for storing the 4th selected nodes of A,CL and their internal structures
cl_list5 = [] # for storing the 5th selected nodes of A,CL and their internal structures
cl_list6 = [] # for storing the 6th selected nodes of A,CL and their internal structures
cl_list7 = [] # for storing the 7th selected nodes of A,CL and their internal structures
cl_list8 = [] # for storing the 7th selected nodes of A,CL and their internal structures
cl_list9 = [] # for storing the 7th selected nodes of A,CL and their internal structures
cl_list10 = [] # for storing the 7th selected nodes of A,CL and their internal structures

for node in mylist:
    if node.find('[')==-1 and node.find('DISMK')==-1 and node.find('PAUSE')==-1 and node.find('PUNC')==-1: # exclude the unimportant information

        space_num = 0
        if node.startswith('PU,'):
            clause_status = 0
            clause_num1 = 0
            clause_num2 = 0
            clause_num3 = 0
            clause_num4 = 0
            clause_num5 = 0
            clause_num6 = 0
            clause_num7 = 0
            clause_num8 = 0
            clause_num9 = 0
            clause_num10 = 0
        if node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 0:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            clause_num1 = space_num # here =0
            clause_status = 1
            cl_list1.append(node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 1:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            clause_num2 = space_num
            clause_status = 2
            cl_list2.append(node)
            if space_num == clause_num1 +1:
                cl_list1.append('*'+node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 2:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num2:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*'+node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 3:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 4:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 5:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num5 and space_num > clause_num4:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
            elif space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num6 = space_num
                clause_status = 6
                cl_list6.append(node)
                if space_num == clause_num5 + 1:
                    cl_list5.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 6:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num6 and space_num > clause_num5:
                clause_num6 = space_num
                clause_status = 6
                cl_list6.append(node)
                if space_num == clause_num5 + 1:
                    cl_list5.append('*' + node)
            elif space_num <= clause_num5 and space_num > clause_num4:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
            elif space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num7 = space_num
                clause_status = 7
                cl_list7.append(node)
                if space_num == clause_num6 + 1:
                    cl_list6.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 7:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num7 and space_num > clause_num6:
                clause_num7 = space_num
                clause_status = 7
                cl_list7.append(node)
                if space_num == clause_num6 + 1:
                    cl_list6.append('*' + node)
            elif space_num <= clause_num6 and space_num > clause_num5:
                clause_num6 = space_num
                clause_status = 6
                cl_list6.append(node)
                if space_num == clause_num5 + 1:
                    cl_list5.append('*' + node)
            elif space_num <= clause_num5 and space_num > clause_num4:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
            elif space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num8 = space_num
                clause_status = 8
                cl_list8.append(node)
                if space_num == clause_num7 + 1:
                    cl_list7.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 8:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num8 and space_num > clause_num7:
                clause_num8 = space_num
                clause_status = 8
                cl_list8.append(node)
                if space_num == clause_num7 + 1:
                    cl_list7.append('*' + node)
            elif space_num <= clause_num7 and space_num > clause_num6:
                clause_num7 = space_num
                clause_status = 7
                cl_list7.append(node)
                if space_num == clause_num6 + 1:
                    cl_list6.append('*' + node)
            elif space_num <= clause_num6 and space_num > clause_num5:
                clause_num6 = space_num
                clause_status = 6
                cl_list6.append(node)
                if space_num == clause_num5 + 1:
                    cl_list5.append('*' + node)
            elif space_num <= clause_num5 and space_num > clause_num4:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
            elif space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num9 = space_num
                clause_status = 9
                cl_list9.append(node)
                if space_num == clause_num8 + 1:
                    cl_list8.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 9:
            for char in node:
                if char == ' ':
                    space_num += 1
                else:
                    break
            if space_num <= clause_num9 and space_num > clause_num8:
                clause_num9 = space_num
                clause_status = 9
                cl_list9.append(node)
                if space_num == clause_num8 + 1:
                    cl_list8.append('*' + node)
            elif space_num <= clause_num8 and space_num > clause_num7:
                clause_num8 = space_num
                clause_status = 8
                cl_list8.append(node)
                if space_num == clause_num7 + 1:
                    cl_list7.append('*' + node)
            elif space_num <= clause_num7 and space_num > clause_num6:
                clause_num7 = space_num
                clause_status = 7
                cl_list7.append(node)
                if space_num == clause_num6 + 1:
                    cl_list6.append('*' + node)
            elif space_num <= clause_num6 and space_num > clause_num5:
                clause_num6 = space_num
                clause_status = 6
                cl_list6.append(node)
                if space_num == clause_num5 + 1:
                    cl_list5.append('*' + node)
            elif space_num <= clause_num5 and space_num > clause_num4:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
            elif space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                clause_num10 = space_num
                clause_status = 10
                cl_list10.append(node)
                if space_num == clause_num9 + 1:
                    cl_list9.append('*' + node)
        elif node.find('A,CL') >= 0 and node.find('PARA,CL') ==-1 and clause_status == 10:
            if space_num <= clause_num10 and space_num > clause_num9:
                clause_num10 = space_num
                clause_status = 10
                cl_list10.append(node)
                if space_num == clause_num9 + 1:
                    cl_list9.append('*' + node)
            elif space_num <= clause_num9 and space_num > clause_num8:
                clause_num9 = space_num
                clause_status = 9
                cl_list9.append(node)
                if space_num == clause_num8 + 1:
                    cl_list8.append('*' + node)
            elif space_num <= clause_num8 and space_num > clause_num7:
                clause_num8 = space_num
                clause_status = 8
                cl_list8.append(node)
                if space_num == clause_num7 + 1:
                    cl_list7.append('*' + node)
            elif space_num <= clause_num7 and space_num > clause_num6:
                clause_num7 = space_num
                clause_status = 7
                cl_list7.append(node)
                if space_num == clause_num6 + 1:
                    cl_list6.append('*' + node)
            elif space_num <= clause_num6 and space_num > clause_num5:
                clause_num6 = space_num
                clause_status = 6
                cl_list6.append(node)
                if space_num == clause_num5 + 1:
                    cl_list5.append('*' + node)
            elif space_num <= clause_num5 and space_num > clause_num4:
                clause_num5 = space_num
                clause_status = 5
                cl_list5.append(node)
                if space_num == clause_num4 + 1:
                    cl_list4.append('*' + node)
            elif space_num <= clause_num4 and space_num > clause_num3:
                clause_num4 = space_num
                clause_status = 4
                cl_list4.append(node)
                if space_num == clause_num3 + 1:
                    cl_list3.append('*' + node)
            elif space_num <= clause_num3 and space_num > clause_num2:
                clause_num3 = space_num
                clause_status = 3
                cl_list3.append(node)
                if space_num == clause_num2 + 1:
                    cl_list2.append('*' + node)
            elif space_num <= clause_num2 and space_num > clause_num1:
                clause_num2 = space_num
                clause_status = 2
                cl_list2.append(node)
                if space_num == clause_num1 + 1:
                    cl_list1.append('*' + node)
            else:
                print('There is still one clause which has not been extracted!')

       #elif node.startswith('PU,'):
            #clause_status = 0
        elif clause_status > 0:
            if clause_status == 1:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num1 + 1:
                    cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 1
###############################################################################################
            elif clause_status == 2:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num2 + 1:
                    cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 1
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 2
###############################################################################################
            elif clause_status == 3:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num3 + 1:
                    cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 1
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 2
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 3
###############################################################################################
            elif clause_status == 4:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num4 + 1:
                    cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 1
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 2
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 3
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 4
###############################################################################################
            elif clause_status == 5:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num5 + 1:
                    cl_list5.append(node)
                elif space_num > clause_num4 and space_num <= clause_num5:
                    clause_status -= 1
                    if space_num == clause_num4 + 1:
                        cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 2
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 3
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 4
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 5
###############################################################################################
            elif clause_status == 6:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num6 + 1:
                    cl_list6.append(node)
                elif space_num > clause_num5 and space_num <= clause_num6:
                    clause_status -= 1
                    if space_num == clause_num5 + 1:
                        cl_list5.append(node)
                elif space_num > clause_num4 and space_num <= clause_num5:
                    clause_status -= 2
                    if space_num == clause_num4 + 1:
                        cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 3
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 4
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 5
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 6
###############################################################################################

            elif clause_status == 7:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num7 + 1:
                    cl_list7.append(node)
                elif space_num > clause_num6 and space_num <= clause_num7:
                    clause_status -= 1
                    if space_num == clause_num6 + 1:
                        cl_list6.append(node)
                elif space_num > clause_num5 and space_num <= clause_num6:
                    clause_status -= 2
                    if space_num == clause_num5 + 1:
                        cl_list5.append(node)
                elif space_num > clause_num4 and space_num <= clause_num5:
                    clause_status -= 3
                    if space_num == clause_num4 + 1:
                        cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 4
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 5
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 6
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 7

###############################################################################################
            elif clause_status == 8:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num8 + 1:
                    cl_list8.append(node)
                elif space_num > clause_num7 and space_num <= clause_num8:
                    clause_status -= 1
                    if space_num == clause_num7 + 1:
                        cl_list7.append(node)
                elif space_num > clause_num6 and space_num <= clause_num7:
                    clause_status -= 2
                    if space_num == clause_num6 + 1:
                        cl_list6.append(node)
                elif space_num > clause_num5 and space_num <= clause_num6:
                    clause_status -= 3
                    if space_num == clause_num5 + 1:
                        cl_list5.append(node)
                elif space_num > clause_num4 and space_num <= clause_num5:
                    clause_status -= 4
                    if space_num == clause_num4 + 1:
                        cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 5
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 6
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 7
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 8
 ###############################################################################################
            elif clause_status == 9:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num9 + 1:
                    cl_list9.append(node)
                elif space_num > clause_num8 and space_num <= clause_num9:
                    clause_status -= 1
                    if space_num == clause_num8 + 1:
                        cl_list8.append(node)
                elif space_num > clause_num7 and space_num <= clause_num8:
                    clause_status -= 2
                    if space_num == clause_num7 + 1:
                        cl_list7.append(node)
                elif space_num > clause_num6 and space_num <= clause_num7:
                    clause_status -= 3
                    if space_num == clause_num6 + 1:
                        cl_list6.append(node)
                elif space_num > clause_num5 and space_num <= clause_num6:
                    clause_status -= 4
                    if space_num == clause_num5 + 1:
                        cl_list5.append(node)
                elif space_num > clause_num4 and space_num <= clause_num5:
                    clause_status -= 5
                    if space_num == clause_num4 + 1:
                        cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 6
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 7
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 8
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 9

###############################################################################################
            elif clause_status == 10:
                for char in node:
                    if char == ' ':
                        space_num += 1
                    else:
                        break
                if space_num == clause_num10 + 1:
                    cl_list10.append(node)
                elif space_num > clause_num9 and space_num <= clause_num10:
                    clause_status -= 1
                    if space_num == clause_num9 + 1:
                        cl_list9.append(node)
                elif space_num > clause_num8 and space_num <= clause_num9:
                    clause_status -= 2
                    if space_num == clause_num8 + 1:
                        cl_list8.append(node)
                elif space_num > clause_num7 and space_num <= clause_num8:
                    clause_status -= 3
                    if space_num == clause_num7 + 1:
                        cl_list7.append(node)
                elif space_num > clause_num6 and space_num <= clause_num7:
                    clause_status -= 4
                    if space_num == clause_num6 + 1:
                        cl_list6.append(node)
                elif space_num > clause_num5 and space_num <= clause_num6:
                    clause_status -= 5
                    if space_num == clause_num5 + 1:
                        cl_list5.append(node)
                elif space_num > clause_num4 and space_num <= clause_num5:
                    clause_status -= 6
                    if space_num == clause_num4 + 1:
                        cl_list4.append(node)
                elif space_num > clause_num3 and space_num <= clause_num4:
                    clause_status -= 7
                    if space_num == clause_num3 + 1:
                        cl_list3.append(node)
                elif space_num > clause_num2 and space_num <= clause_num3:
                    clause_status -= 8
                    if space_num == clause_num2 + 1:
                        cl_list2.append(node)
                elif space_num > clause_num1 and space_num <= clause_num2:
                    clause_status -= 9
                    if space_num == clause_num1 + 1:
                        cl_list1.append(node)
                elif space_num <= clause_num1:
                    clause_status -= 10

#The following section is to transfer the extracted clauses into linear forms'''
all_list = cl_list1+cl_list2+cl_list3+cl_list4+cl_list5+cl_list6+cl_list7+cl_list8+cl_list9+cl_list10

mylist2 = []
for line in all_list:
    if line.find('{') == -1 and line.find('(') == -1:
        mylist2.append(line.strip('\n'))
    elif line.find('{') >= 0 and line.find('(') == -1:
        temp_list = line.split('{')
        mylist2.append(temp_list[0])
    else:
        temp_list = line.split('(')
        mylist2.append(temp_list[0])

#write to a file
output = open('E:\\A-output\\Written_linear.txt', 'w', encoding='utf-8')
for item in mylist2:
    if item.find('*')>=0:
        output.write(item.strip('* ')+'-')
    elif item.find('A,CL') >= 0:
        output.write('\n')
    else:
        output.write(item.strip(' ')+'-')
output.close()

for i in range(10):
    print('*')

#The following section is to calculate the frequency distribution
# read a file
file = open('E:\\A-output\\Written_linear.txt', 'r', encoding='utf-8')
text = file.readlines()
file.close()

fd = nltk.FreqDist(line.strip('-\n') for line in text)
feature_frequency = fd.most_common() # list of tuples (feature,frequency)

#write to a file
out = open('E:\\A-output\\Written_fd.txt', 'w', encoding='utf-8')
for fea,fre in feature_frequency:
    out.write(fea + '\t' + str(fre) + '\n')
out.close()

print('The A,CL_fd file is successfully created.')
