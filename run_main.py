from genericpath import isfile
from ntpath import join
import os
import glob
from subprocess import call
from turtle import xcor

searchTerm = ".png"

download_dir = 'C:/Users/calvi/Downloads'
target_dir = ""

def find(name, path):
    #for finding with fully matched path
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def dirFiles(path):   #check if can use blob instead
    #this is files only excl dirs
    dir_contents = [
        a for a in os.listdir(path) 
            if isfile(join(path, a))
    ]
    return dir_contents


#note: this is currently case sensitive!
def calFind(dirList,searchStr):
    resultIndex = []
    resultStr = []

    for x in dirList:
        index = dirList.index(x) #get curr file index
        #print(x)
        if(searchStr in x):
            #print(x)
            resultStr.append(x)
            resultIndex.append(index)

    print(resultStr)
    print(resultIndex)
    #resultStr = list(filter(lambda x: searchStr in x, dirList))
    #resultStr = [v for v in dirList if searchStr in v]

    #print(resultIndex)
    #print(resultStr)

    return 


def main():
    fish = dirFiles(download_dir)
    #print(fish)

    calFind(fish, searchTerm)

    try:
        #calFind(fish, 'Tolulu')
        print('doneish')
    except:
        print("pok gai")
    #pog

main()