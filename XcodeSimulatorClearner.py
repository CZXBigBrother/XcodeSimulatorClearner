#coding: utf-8

__author__ = 'chenzhengxing'

import os
import shutil
import time

computerName = ''
path = []
def getPath():
    return '/Users/{0}/Library/Developer/Xcode/DerivedData/'.format(computerName)

def searchFile(files,path):
    for x in  os.listdir(path):
        if x != '.DS_Store':
            files.append(path + x)
    return files

def isExistsPath():
    return os.path.exists(getPath())

def setPath():
    files = []
    path = ['/Users/{0}/Library/Developer/Xcode/DerivedData/'.format(computerName),'/Users/{0}/Library/Developer/Xcode/Archives/'.format(computerName)]
    for apath in path:
        searchFile(files,apath)
    return files

def deleteFile():
    startTime = time.time()
    files = setPath();
    for afile in files:
        shutil.rmtree(afile,True)
        print '删除:' + afile
    print('删除完毕...耗时:'+ str(time.time() - startTime))
    print('共删除{0}个编译文件'.format(len(files)))

def getCurrentPath():
    return os.path.abspath('.')

def getConfig():
    if os.path.exists(getCurrentPath() + '/config.txt'):
        f = open(getCurrentPath() + '/config.txt', 'r')
        return f.read()
    return ''

def writeConfig(user):
    f = open(getCurrentPath() + '/config.txt', 'w')
    f.write(user)
    f.close()
if __name__ == '__main__':
    isQuit = True
    computerName = 'cheng'
    if getConfig():
        print '是否使用:{0}(y/n)'.format(getConfig())
        if raw_input().lower() == 'y':
            computerName = getConfig()
        else:
            print('请输入您的计算机名称:')
            computerName = raw_input()
    else:
        print('请输入您的计算机名称:')
        computerName = raw_input()
    while isQuit:
        print('检查路径是否存在...')
        if isExistsPath():
            print('检查成功,是否开始删除(y/n):')
            sure = raw_input().lower()
            if sure == 'y':
                writeConfig(computerName)
                deleteFile()
                isQuit = False
            else:
                isQuit = False
        else:
            print('路径错误或者用户名输入错误,或按n退出程序')
            computerName = raw_input().lower()
            if computerName == 'n':
                isQuit = False
