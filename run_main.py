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
    tmpDir = target_dir 
    searchDir = serialNum + '_' #for scanning for subfolder with underscore runnum
    
    flag = 0

    print(serialNum)
    for root,dirs,files in os.walk(target_dir): ####WGAT IS HPAPENIGN ok so currently this loops and checks through every folder so the make dir thing needs to be after this check
        if (serialNum) in dirs:
            print("folder already exists")
            #tmpDir = tmpDir + '/' + serialNum
            flag = flag + 1
            print(dirs)
    #if no root serial folder make that otherwise just set dir location for next step in finding subfolder 
    if(flag > 0):
        print("folder exists")
        tmpDir = tmpDir + '/' + serialNum
    else:
        os.mkdir(target_dir + '/' + serialNum)
        tmpDir = tmpDir + '/' + serialNum

        #vs 

    rootDirs = os.listdir(tmpDir)
    print(rootDirs)
    if (len(rootDirs == 0)):

        print("aids")
    if (len(rootDirs) > 0):
        print('go to subfolder and find last one')
        runNum = rootDirs[len(rootDirs) - 1][13]
        print(runNum)

    #if rootDirs[len(rootDirs)] 

    
    #a = os.listdir(tmpDir)
    
    #print(a)

    return

# else:
#            if(flag == 0):
#               
#                flag = 1
#
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