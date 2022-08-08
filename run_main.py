from genericpath import isfile
from ntpath import join
import os
from re import M
import shutil


delete_files_after_move = False

searchTerm = "cf10"
numFilesForCal = 5
fileCriteria = '.pb.bin'   ##something to qualify it as target filetype for recording (eg. .pb.bin)
download_dir = 'C:/Users/calvi/Downloads/_edge'
target_dir = 'C:/projects/bababoo/'

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
    tmpDir = target_dir 
    searchDir = serialNum + '_' #for scanning for subfolder with underscore runnum
    
    #flag = 0

    print(serialNum)
    print(os.listdir(target_dir))
    if(serialNum in os.listdir(target_dir)):
        print('folder exists')
    else:
        print('folder doesnt exist, creating first')
        os.mkdir(target_dir + serialNum)
    tmpDir = tmpDir + serialNum + '/'
    
    subDirs = os.listdir(tmpDir)
    print(subDirs)

    ###futurefeature: check if any/prev subfolder is empty in case accidental creatin of too many folders with nothing in it


    if (len(subDirs) == 0):
        #no subfolder yet
        os.mkdir(tmpDir + serialNum + '_1') 
    if (len(subDirs) > 0):
        print('go to subfolder and find last one')
        runNum = subDirs[len(subDirs) - 1][13]  #next folder underscore number
        #runNum = int(runNum) + 1  ###UNCOMMENT BEFORE DPELOY
        print(runNum)
        #os.mkdir(tmpDir + serialNum + '_' + str(runNum ))  ###UNCOMMENT BEFORE DEPLOY

    targetSubfolder = tmpDir + serialNum + '_' + str(runNum)

    return targetSubfolder

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
        dirTarget = makeDir(matchList)
        for a in matchIndex:
            
            #target_dir = target_dir + '/'
            print(matchList[a])
            #print(matchList[a][:29])

            try:
                print('moving file:' + a)
                print(download_dir + a)
                shutil.copy(download_dir + a, dirTarget)

            except:
                print('file already exists')

            #shutil.copy(download_dir + a, target_dir)
            #os.mkdir(target_dir + '/aids')
            if delete_files_after_move is True: os.remove(download_dir + matchList[a])

    else:    
        print('itdontwork')

main()