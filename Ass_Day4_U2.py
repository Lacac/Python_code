import requests
from bs4 import BeautifulSoup

# request the first link
url = 'https://www.us-cert.gov/ncas/alerts'
res = requests.get(url)
try:
    res.raise_for_status()
except: 
    print('ERROR')
mySoup = BeautifulSoup(res.text, 'html.parser')


# Function count:  count the number of issues each page
def count(mySoup):
    issuedTag = mySoup.select('.views-field.views-field-title')   
    return len(issuedTag)

pageTag = mySoup.select('.pager__item')                 # class = paper__item
setPage = set()
for page in pageTag:
    nextPage = page.select('a')[0].get('href')          # get the link of page 
    setPage.add(nextPage)                               # add the link of page to set()
# print(len(setPage))
# print(setPage)


# https://www.cisa.gov/uscert/ncas/alerts?page=6   : form of full link
countIssue = 0          # Number of all issues
for page in setPage:
    linkNextPage = 'https://www.cisa.gov/uscert/ncas/alerts' + page
#    print(linkNextPage)
    res = requests.get(linkNextPage)
    try: 
        res.raise_for_status()
    except:
        print('ERROR')
    mySoup = BeautifulSoup(res.text,'html.parser')
    print(page,' :',count(mySoup))
    countIssue += count(mySoup)
print('Total: ', countIssue)
