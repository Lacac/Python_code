import csv,json
from pathlib import Path
import pandas as pd
import os
import mimetypes

def jsonTocsv(jsonInput,csvOutput):
    input = open(jsonInput)
    data = json.load(input)
    input.close()
    output = csv.writer(open(csvOutput,'w'))
    output.writerow(data[0].keys())                 # header row
    for row in data:
        output.writerow(row.values())

def csvTojson(inputFile,outputFile):
    csv_data = pd.read_csv(inputFile, sep = ',')
    csv_data.to_json(outputFile, orient = "records")


dirName = 'D:\\MON HOC\\Coursera\\Python\\Python_Code\\file'
listOfFile = os.listdir(dirName)
print(listOfFile)
# application/vnd.ms-excel
# ('application/json', None)

os.chdir(dirName)
print(Path.cwd())
for fileName in listOfFile:
    typeOfFile = mimetypes.guess_type(fileName,strict=True)
    if (typeOfFile[0] == 'application/vnd.ms-excel'):   
        newFile = fileName.split('.')[0]+'.json'
        csvTojson(fileName,newFile)
        os.remove(fileName)
    elif (typeOfFile[0] == 'application/json'):
        newFile = fileName.split('.')[0]+'.csv'
        jsonTocsv(fileName,newFile)
        os.remove(fileName)

print(os.listdir(dirName)) 
