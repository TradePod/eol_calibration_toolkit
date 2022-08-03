from genericpath import isfile
from ntpath import join
import os
import glob
from subprocess import call
from turtle import xcor

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

def calFind(dirList,searchStr):
    resultIndex = []
    resultStr = []

    for x in dirList:
        index = dirList.index(x) #get curr file index
        print(index)
        #options: use filter, list compression or idk wtf is a lambda
        if list(filter(lambda x: x.startswith(searchStr),dirList)):
            resultIndex.append(index)
            resultStr.append(dirList[x])

    print(resultIndex)
    print(resultStr)

    return 


def main():
    fish = dirFiles(download_dir)
    #print(fish)
    print("aids")

    try:
        calFind(fish, "to")
    except:
        print("pok gai")
    #pog

main()