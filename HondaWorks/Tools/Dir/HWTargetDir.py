import os

class HWTargetDir:

    def __init__(self, filePath):
        self.fileList = []
        self.dirList = []
        self.filePath = filePath
        workList = os.listdir(self.filePath)
        for work in workList:
            if os.path.isfile(os.path.join(self.filePath, work)):
                self.fileList.append(work)
            else:
                self.dirList.append(work)

    def getFileList(self):
        return self.fileList
    
    def getDirList(self):
        return self.dirList
    
    def getCurrentPath(self):
        return self.filePath

    def getFilePath(self, fileName):
        return os.path.join(self.filePath, fileName)
    
    def getDirPath(self, dirName):
        return os.path.join(self.filePath, dirName)

#動作確認
if __name__ == '__main__':
    testTargetDir = HWTargetDir("d:\\python\\venv\\310venv\\HondaWorks")
    fileList = testTargetDir.getFileList()
    print(testTargetDir.getCurrentPath())
    for file in fileList:
        print(testTargetDir.getFilePath(file))
    dirList = testTargetDir.getDirList()
    for dir in dirList:
        print(testTargetDir.getDirPath(dir))
