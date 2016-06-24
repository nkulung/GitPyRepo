import requests
import urllib3
from bs4 import BeautifulSoup as bs


def getInfo():
    un = input('Enter a Github Username: ')
    return un
def getRepos(un):
    url = 'https://github.com/'
    url = url + un + '?tab=repositories'
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    repo = soup.find_all('h3' ,{'class': "repo-list-name"})
    link = []
    for i in range (len(repo)):
        repo[i] = repo[i].text
        repo[i] = repo[i].strip()
        links ='https://github.com/'+un+'/'+repo[i]
        link.append(links)
    return repo, link
        
def displayRepos(repo,link):
    print('')
    print('Repositories')
    print('')
    print('             Name                         Link')
    
    print('--------------------------------------------------')
    for i in range (len(repo)):
        print('#',i+1,' ',repo[i],' ',link[i])

def main():
    un = getInfo()
    repo,link = getRepos(un)
    displayRepos(repo,link)

main()
    
