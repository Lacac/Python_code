# file : determine the type of file
import magic
import os
import sys


    # without argparse
# python Ass_Day9_U1.py fileName : len >= 2 arg, 0, 1---> len-1
arg = sys.argv
if len(arg) < 2:
    print('You need to add the path of folder/file')
    sys.exit()

inputs = list()          # list of folder/file name
for i in range(len(arg)):
    if i>0:
        inputs.append(arg[i])

for input in inputs:
    if (os.path.isdir(input)):                              # folder
        print(input , ':\t', 'directory')
    elif (os.path.isfile(input)):                           # file
        print(input,':\t',magic.from_file(input))
    else: 
        print(input , ':\t', 'Not exist')
