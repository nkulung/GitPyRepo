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
    repoClass = soup.find_all('div' , {'class': "d-inline-block mb-1"})
    link = []
    repos = []
    for i in range(len(repoClass)):
        newTest = str(repoClass[i])
        soupe = bs(newTest, "html.parser")
        repo = soupe.find_all('h3')
        repos = repos + repo
        repo[0] = repo[0].text
        repo[0] = repo[0].strip()
        links ='https://github.com/' +un+ '/'+ repo[0]
        link.append(links)
       
    return repoClass, repos, link,


def displayRepos(repoClass,link, repos):
    print('')
    print('')
    print('Repositories')
    print('')
    for i in range (len(repoClass)):
        repos[i] = repos[i].text
        repos[i] = repos[i].split()
        newRepo = repos[i]
        print('---------------------------------------')
        print('#',i+1, str(newRepo[0]))
        print('')
        print(link[i])
        print('')


def main():
    un = getInfo()
    repoClass,repo,link = getRepos(un)
    displayRepos(repoClass,link,repo)



main()
