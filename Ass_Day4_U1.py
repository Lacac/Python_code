import requests
from bs4 import BeautifulSoup
import os
from pathlib import Path

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.47'}

res = requests.get('https://en.wikipedia.org/wiki/Tenterfield,_New_South_Wales')
try:
    res.raise_for_status()
except:
    print('ERROR!')

mySoup = BeautifulSoup(res.text,'html.parser')
imgTag = mySoup.select('img')                           # Get all the tag <img

folderPath = 'D:\\MON HOC\\Coursera\\Python\\Python_Code\\Pictures'             # create new folder
os.makedirs(folderPath)

def renameFile(fileName):
    specialChac = '\/?:*><|"'
    for char in specialChac:
        if char in fileName:
            fileName = fileName.replace(char,'_')
    return fileName


for img in imgTag:
    if img.get('loading') == 'lazy':                             #  
        imgLink = 'https://en.wikipedia.org/' + img.get('src')
    else:
        imgLink = 'https:' + img.get('src')
    
    imageOpen = requests.get(imgLink, headers=headers)          # open img link
    try:
        imageOpen.raise_for_status()
    except:
        print('ERROR')
 #     print(imageOpen.status_code)

    imageName = imgLink.replace('?', '_').replace('>','_').replace('<', '_')            # 
#    imageName = renameFile(imgLink)
    imageFilePath = Path(folderPath) / os.path.basename(imageName)   # path of file image
    imageFile = open(imageFilePath,'wb')
    imageFile.write(imageOpen.content)
    print('Download')
    imageFile.close()
