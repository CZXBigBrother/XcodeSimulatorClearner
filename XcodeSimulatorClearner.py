#coding: utf-8

__author__ = 'chenzhengxing'

import os
import shutil
import time
import getpass

computerName = ''
path = []
def getPath():
    return '/Users/{0}/Library/Developer/Xcode/DerivedData/'.format(computerName)

def searchFile(files,path):
    for x in  os.listdir(path):
        print x
        if x != '.DS_Store':
            files.append(path + x)

def isExistsPath():
    return os.path.exists(getPath())

def setPath():
    files = []
    path = ['/Users/{0}/Library/Developer/Xcode/DerivedData/'.format(computerName)]#,'/Users/{0}/Library/Developer/Xcode/Archives/DerivedData/'.format(computerName)
    for apath in path:
        searchFile(files,apath)
    return files

def deleteFile():
    startTime = time.time()
    files = setPath();
    for afile in files:
        print afile
        shutil.rmtree(afile,True)
        print '删除:' + afile
    print('删除完毕...耗时:'+ str(time.time() - startTime))
    print('共删除{0}个编译文件'.format(len(files)))

if __name__ == '__main__':
    isQuit = True
    computerName = getpass.getuser()
    print getpass.getuser()
    while isQuit:
        print('检查路径是否存在...')
        if isExistsPath():
            print('检查成功,是否开始清楚编译缓存(y/n):')
            sure = raw_input().lower()
            if sure == 'y':
                deleteFile()
                isQuit = False
            else:
                isQuit = False
        else:
            print('路径不存在，按n退出程序')
            isQuit = False
