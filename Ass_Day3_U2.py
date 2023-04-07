from fileinput import close, filename
import os
from pathlib import Path
import re

def getNumber(mess):                        # get the number of a string
    regexGetNumber = re.compile(r'\d+')
    number = regexGetNumber.search(mess)
    if number != None:
        return int(number.group())

dirName = 'D:\\MON HOC\\Assignment - FPT\\2_Assignments\\2_Assignments\\find_the_flag'
listOfFile = os.listdir('D:\\MON HOC\\Assignment - FPT\\2_Assignments\\2_Assignments\\find_the_flag')

listOfIndex = list()                # the index of file
for filename in listOfFile:
    fileIndex = getNumber(filename)
    listOfIndex.append(fileIndex)
listOfIndex.sort()                  # sort the list of index

os.chdir(dirName)                   # come to the working folder
# print(Path.cwd())

flagRegex = re.compile(r'. (?=.*This.*file.*?)')
print('Flag: ', end = '')
for index in listOfIndex:
    filename = str(index)+'.txt'
    file = open(filename,'r')
    for line in file:
        flag = flagRegex.search(line)
        if flag != None: 
#            print(filename +':'+ flag.group())
            flagInFile = flag.group().rstrip()
            print(flagInFile, end = '')
    file.close()
