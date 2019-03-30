import sys
import glob
import nltk
from nltk import FreqDist

# read the files under one directory
path = 'E:\\ICE\\Spoken\\*.cor'
files = glob.glob(path)

i = 0
for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()
    for line in text:
        if line.find('PU,') >= 0:
            i += 1
    f.close()

print('the number of parsing units are:', i)

# read the files under one directory
path = 'E:\\ICE\\Written\\*.cor'
files = glob.glob(path)

j = 0
for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()

    for line in text:
        if line.find('PU,') >= 0:
            j += 1
    f.close()
print('the number of parsing units are:', j)
'''
# read the files under one directory
path = 'E:\\ICE_FourRegisters\\3NewsReportage\\*.cor'
files = glob.glob(path)

for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()
    m = 0
    for line in text:
        if line.find('PU') >= 0:
            m += 1
    f.close()

print('the number of parsing units are:', m)

# read the files under one directory
path = 'E:\\ICE_FourRegisters\\4Academic\\*.txt'
files = glob.glob(path)

for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()
    n = 0
    for line in text:
        if line.find('PU')>=0:
            n += 1
    f.close()

print('the number of parsing units are:', n)
'''
