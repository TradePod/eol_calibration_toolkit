from genericpath import isfile
from ntpath import join
import os
from re import M
import shutil


delete_files_after_move = False

searchTerm = "ec90"
numFilesForCal = 5
fileCriteria = '34#a'   ##something to qualify it as target filetype for recording
download_dir = 'C:/Users/calvi/Downloads/'
target_dir = 'C:/projects/bababoo'

opMode = {
    1: "move 5 cal things 2 dir in config",
    2: "idk"
}

def find(name, path):
    #for finding with fully matched path NO IDEA IF THIS WORKS PROPERLY USE DIRFILES FOR NOW
    result = []
    print(name)
    for root, dirs, files in os.walk(path):
        if name in files:
            print('found in file')
            result.append(os.path.join(root, name))
        if name in dirs:
            print('found in dir')
            result.append(os.path.join(root, name))
    return result

def dirFiles(path):   #check if can use blob instead
    #this is files only excl dirs
    dir_contents = [
        a for a in os.listdir(path) 
            if isfile(join(path, a))
    ]
    return dir_contents


#note: this is currently case sensitive
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

    return resultStr, resultIndex

def makeDir(matchList):
    serialNum = matchList[0][:12]
    #print(serialNum)
    #find(serialNum, target_dir)
    for root, dirs, files in os.walk(target_dir): ####WGAT IS HPAPENIGN
        if (serialNum) in dirs:
            print("folder already exists")
        else:
            print("folder doesn't exist")
    

    return



def main():
    fish = dirFiles(download_dir)
    #print(fish)
    #probs dont need match index
    try:
        matchList, matchIndex = calFind(fish, searchTerm)
    except:
        print("pok gai")
    #dirlist = [ item for item in os.listdir('C:/projects/Casana/test_calibrationdir/') if os.path.isdir(os.path.join('C:/projects/Casana/test_calibrationdir/', item)) ]
    #check if files from seat
    if(len(matchList) == numFilesForCal):
        makeDir(matchList)
        for a in matchIndex:
            #print(a)
            #target_dir = target_dir + '/'
            #print(matchList[a])
            #print(matchList[a][:29])

            #shutil.copy(download_dir + a, target_dir)
            #os.mkdir(target_dir + '/aids')
            if delete_files_after_move is True: os.remove(download_dir + matchList[a])

    else:    
        print('itdontwork')

main()