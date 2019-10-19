from bs4 import BeautifulSoup
from urllib.request import urlopen
from webSite import *
from variables import *
from script import *
import time
from multiprocessing import Process

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

if __name__ == '__main__':
    lastUpdateTime = time.time()
    startTime = lastUpdateTime
    visitedList = [WebSite(URLSTART)]
    waitingList = []
    actualPage = WebSite(URLSTART)
    htmlPage = urlopen(actualPage.url)
    resultNextPage = [True, WebSite(URLSTART), urlopen(actualPage.url)]
    exploreWebPage(actualPage, htmlPage, waitingList, visitedList)
    while((NUMBERPAGESVISITED == -1 or NUMBERPAGESVISITED >= len(visitedList)) and len(waitingList) != 0 and resultNextPage[0]):
        if(time.time() - lastUpdateTime > 10):
            lastUpdateTime = time.time()
            print("--------------------------")
            print("len(visitedList) = " + str(len(visitedList)))
            print("len(waitingList) = " + str(len(waitingList)))
            print("Time since start : " + str(int(time.time() - startTime)) + " seconds")


        if(resultNextPage[0]):
            actualPage = resultNextPage[1]
            htmlPage = resultNextPage[2]
            runInParallel(findNextPage(waitingList, visitedList, resultNextPage), exploreWebPage(actualPage, htmlPage, waitingList, visitedList))
            #exploreWebPage(actualPage, htmlPage, waitingList, visitedList)
    print('---- Start write ----')
    print(len(waitingList) + len(visitedList))
    for i in waitingList:
        if(i not in visitedList):
            visitedList.append(i)
        else:
            print("Have a problem")
    visitedList.sort()
    visitedList.reverse()
    print(len(visitedList))
    with open('sortie.txt', 'w') as f:
        for item in visitedList:
            f.write("%s\n\n" % item)
    print("Time : " + str(int(time.time() - startTime)) + " seconds")
