import os
import datetime

class HWTargetFile:

    #ファイル名を含んだフルパスを引数として渡す
    def __init__(self, fileFullPath):
        self.fileFullPath = fileFullPath

    def isExistTargetFile(self):
        return os.path.isfile(self.fileFullPath)

    def getCreateTimeStr(self):
        mtime = os.stat(self.fileFullPath).st_mtime
        dtTimeStamp = datetime.datetime.fromtimestamp(mtime)
        strTimeStamp = dtTimeStamp.strftime('%Y-%m-%d')
        return strTimeStamp

#動作確認
if __name__ == '__main__':
    fileFullPath = "d:\\python\\venv\\310venv\\HondaWorks\\test.ini"
    testTargetFile = HWTargetFile(fileFullPath)
    print(testTargetFile.isExistTargetFile())
    if testTargetFile.isExistTargetFile():
        print(testTargetFile.getCreateTimeStr())
