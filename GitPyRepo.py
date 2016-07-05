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
    repoClass = soup.find_all('div' , {'class': "repo-list-item-public source"})
    
    link = []
    for i in range (len(repo)):
        repo[i] = repo[i].text
        repo[i] = repo[i].strip()
        links ='https://github.com/'+un+'/'+repo[i]
        link.append(links)
    return repo, link


def descTest(un):
    url = 'https://github.com/'
    url = url + un + '?tab=repositories'
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    repoClass = soup.find_all('div' , {'class': "repo-list-item public source"})
    link = []
    desc = []
    repos = []
    for i in range(len(repoClass)):
        newTest = str(repoClass[i])
        soupe = bs(newTest, "html.parser")
        repo = soupe.find_all('h3' ,{'class': "repo-list-name"})
        repos = repos + repo
        repo[0] = repo[0].text
        repo[0] = repo[0].strip()
        links ='https://github.com/' +un+ '/'+ repo[0]
        link.append(links)
        descr = soupe.find_all('p' , {'class': "repo-list-description"})
        try:
            descr[0] = descr[0].text
            descr[0] = descr[0].strip()
            desc.append(descr[0])
        except IndexError:
            desc.append('None')
    return repoClass, repos, link, desc


def displayRepos(repoClass,link, repos, desc):
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
        print('Description:',desc[i])
        print('')
        print(link[i])
        print('')


def main():
    un = getInfo()
    repoClass,repo,link,desc = descTest(un)
    displayRepos(repoClass,link,repo,desc)



main()
