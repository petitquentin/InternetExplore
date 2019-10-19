from bs4 import BeautifulSoup
from urllib.request import urlopen
import copy as cp
from webSite import *
from tldextract import extract

def findNextPage(waitingList, visitedList , result = [None, None, None]):
    i = 0
    while (len(waitingList) != 0) :
        try:
            actualPage = waitingList.pop(0)
            if(actualPage != None):
                visitedList.append(actualPage)
                htmlPage = urlopen(actualPage.url)

                result[0] = True
                result[1] = actualPage
                result[2] = htmlPage
                return
        except:
            i = i + 1
    result[0] = False



def exploreWebPage(webPage: WebSite, htmlPage, waitingList, visitedList):
    t1, t2, t3 = extract(webPage.url)  # prints abc, hostname, com
    if(webPage.url[4] == 's'):
        domain = "https://" + t1 + "." + t2 + "t3"
    else:
        domain = "http://" + t1 + "." + t2 + "t3"
    soup = BeautifulSoup(htmlPage)
    for link in soup.findAll('a'):
        if (link.get('href') is not None and len(link.get('href')) != 0):
            if (link.get('href')[0] == '/'):
                if (webPage.url[-1] == '/'):
                    url = webPage.url + link.get('href')[1:]
                else:
                    url = webPage.url + link.get('href')
            elif(link.get('href')[0] == '.'):
                url = domain + link.get('href')[1:]
            else:
                url = link.get('href')
            newWebPage = WebSite(url, [webPage.url])
            if(newWebPage in visitedList):
                visitedList[visitedList.index(newWebPage)].fusion(newWebPage)
            elif(newWebPage in waitingList):
                waitingList[waitingList.index(newWebPage)].fusion(newWebPage)
            else:
                waitingList.append(cp.copy(newWebPage))
    waitingList.sort()
    waitingList.reverse()
