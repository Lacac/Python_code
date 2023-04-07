# ls command + size

import os
import sys
import argparse
from pathlib import Path

if len(sys.argv) > 2:
    print('Too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('No file/folder')
    print(len(sys.argv))
    print(sys.argv)
    sys.exit()

input_path = sys.argv[1]

if not os.path.isdir(input_path):
    if not os.path.isfile(input_path):
        print('The path specified does not exist')
    #print(input_path)
    else:
        print(input_path,'is a file \t ', os.path.getsize(input_path))
    sys.exit()


for file in os.listdir(input_path):
    print(file,'\t',os.path.getsize(input_path+ '\\' +file))
