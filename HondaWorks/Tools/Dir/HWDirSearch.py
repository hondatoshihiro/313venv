import os

class HWDirSearch:

    def __init__(self):
        self.__initialize()

    def setTargetDir(self, dirPath):
        self.__setTargetDir(dirPath)

    #カレントディレクトリが設定済みかどうかを返却する。
    def isSetDir(self):
        return self.isSetDir

    #カレントディレクトリ内のファイルリストを返却する。
    def getFileList(self):
        if self.isSetDir == True:
            return self.fileList
        else:
            return []

    #カレントディレクトリ内のディレクトリリストを返却する。
    def getDirList(self):
        if self.isSetDir == True:
            return self.dirList
        else:
            return []
    
    #カレントディレクトリを返却する。
    def getCurrentPath(self):
        if self.isSetDir == True:
            return self.dirPath
        else:
            return ""

    #カレントディレクトリ＋引数のファイル名でフルパスを作成し、返却する。
    def getFilePath(self, fileName):
        if self.isSetDir == True:
            return os.path.join(self.dirPath, fileName)
        else:
            return ""

    #カレントディレクトリ＋引数のディレクトリ名でフルパスを作成し、返却する。
    def getDirPath(self, dirName):
        if self.isSetDir == True:
            return os.path.join(self.dirPath, dirName)
        else:
            return ""

    #初期化　カレントディレクトリ、ファイルリスト、
    # ディレクトリリスト、カレントディレクトリセットフラグを初期化する。
    def __initialize(self):
        self.dirPath = ""
        self.fileList = []
        self.dirList = []
        self.isSetDir = False

    #カレントディレクトリを設定し、カレントディレクトリ内の
    # ファイルリスト、ディレクトリリストを取得しておく
    def __setTargetDir(self, dirPath):
        self.dirPath = dirPath
        self.isSetDir = True
        workList = os.listdir(self.dirPath)
        for work in workList:
            if os.path.isfile(os.path.join(self.dirPath, work)):
                self.fileList.append(work)
            else:
                self.dirList.append(work)

#動作確認
if __name__ == '__main__':
    targetDir = "d:\hondaworks"
    #searchDir1 = HWDirSearch(targetDir)
    searchDir1 = HWDirSearch()
    searchDir1.setTargetDir(targetDir)
    currentPath = searchDir1.getCurrentPath()
    print("現在のディレクトリ:" + currentPath)
    dirList = searchDir1.getDirList()
    for dir in dirList:
        print("配下のディレクトリ:" + dir)
    fileList = searchDir1.getFileList()
    for file in fileList:
        print("配下のファイル:" + file)

    searchDir2 = HWDirSearch()
    childPath = searchDir1.getDirPath(dir)
    searchDir2.setTargetDir(childPath)
    currentPath = searchDir2.getCurrentPath()
    print("現在のディレクトリ:" + currentPath)
    dirList = searchDir2.getDirList()
    for dir in dirList:
        print("配下のディレクトリ:" + dir)
    fileList = searchDir2.getFileList()
    for file in fileList:
        print("配下のファイル:" + file)
