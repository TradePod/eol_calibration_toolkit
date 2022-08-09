from genericpath import isfile
from ntpath import join
import os
import shutil


delete_files_after_move = False
searchTerm = "ec90"
numFilesForCal = 5
fileCriteria = '.pb.bin'   ##something to qualify it as target filetype for recording (eg. .pb.bin)
download_dir = 'C:/Users/calvi/Downloads/_edge/'
#target_dir = 'G:/Shared drives/Supply Chain and Manufacturing/seat_calibration/seat_calibration_v8/'
target_dir = 'C:/projects/bababoo/'

opMode = {  ###unused currently
    1: "move 5 cal things 2 dir in config",
    2: "idk"
}

###############################################

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
def calFind(dirList,searchStr,fileCriteria):
    #resultIndex = []
    resultStr = []

    for x in dirList:
        index = dirList.index(x) #get curr file index
        #print(x)
        if((searchStr in x) and (fileCriteria in x)):
            #print(x)
            resultStr.append(x)
            #resultIndex.append(index)

    return resultStr #resultIndex

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
    


    ##better subfolder number discovery system 
    subDirs = os.listdir(tmpDir)
    print(subDirs)
    if any(os.scandir(tmpDir)):
        print('noempty')


    subCount = 1 #default underscore start at _1
    for entry in os.scandir(tmpDir):
        if entry.is_dir():
            #print(entry)
            print(entry.name)
            subCount = subCount + 1

<<<<<<< HEAD
    #print(subCount)
=======
    print(subCount)
>>>>>>> 2b32b7da1758e4316ffbd1a6f2d34d32b761eafc

    newDir = tmpDir + serialNum + '_' + str(subCount)
    os.mkdir(newDir)

    ###futurefeature: check if any/prev subfolder is empty in case accidental creatin of too many folders with nothing in it
    # if (len(subDirs) == 0):
    #     #no subfolder yet
    #     os.mkdir(tmpDir + serialNum + '_1') 
    #     runNum = 1
    # if (len(subDirs) > 0):
    #     print('go to subfolder and find last one')
    #     runNum = subDirs[len(subDirs) - 1][13]  #next folder underscore number ###THIS IMPLENTATION DOESN'T SUPPORT DOUBLE DIGIT NUMBERS
    #     runNum = int(runNum) + 1  ###UNCOMMENT BEFORE DPELOY
    #     print(runNum)
    #     os.mkdir(tmpDir + serialNum + '_' + str(runNum ))  ###UNCOMMENT BEFORE DEPLOY


    targetSubfolder = newDir + '/'

    return targetSubfolder

def main():

    fish = dirFiles(download_dir)

    try:
        matchList = calFind(fish, searchTerm, fileCriteria)
        print(matchList)
    except:
        print("Couldn't find all files")
    #dirlist = [ item for item in os.listdir('C:/projects/Casana/test_calibrationdir/') if os.path.isdir(os.path.join('C:/projects/Casana/test_calibrationdir/', item)) ]
    #check if files from seat
    print(len(matchList))
    if(len(matchList) == numFilesForCal):
        dirTarget = makeDir(matchList)
        for a in matchList:     ### why is A length not right

            try:
                print('moving file:' + a)
                #print(download_dir + a)
                sourceFile = download_dir + a
                destination = dirTarget + a
                shutil.copy(sourceFile, destination)

            except shutil.SameFileError:
                print('file already exists')
            
            if delete_files_after_move is True: os.remove(download_dir + a),print('deleting files from originating directory')

        caldirPrint = dirTarget[len(target_dir) + 13:-1] # remove subdir and / 
        print('\nPATH TO COPY TO CAL_DIR: \n' + caldirPrint)    

    else:    
        print('itdontwork')

main()