import os
from HWTargetDir import HWTargetDir

class HWInDir(HWTargetDir):

    def __init__(self, filePath):
        #HWTargetDirのコンストラクタ
        super().__init__(filePath)
        #独自のコンストラクタの処理

    def recursiveDir(self):
        dirList = self.getDirList()
        for dir in dirList:
            dirFullPath = os.path.join(self.filePath, dir)
            print(dirFullPath)
            #ディレクトリに対する処理
            hwInDir = HWInDir(dirFullPath)
            hwInDir.recursiveDir()
        fileList = self.getFileList()
        for file in fileList:
            #ファイルに対する処理
            fileFullPath = os.path.join(self.filePath, file)
            print(fileFullPath)


#動作確認
if __name__ == '__main__':
    targetDir = "d:\\python\\venv\\310venv\\HondaWorks"
    testInDir = HWInDir(targetDir)
    testInDir.recursiveDir()