import os
from HWTargetDir import HWTargetDir

class HWOutDir(HWTargetDir):

    def __init__(self, filePath):
        #HWTargetDirのコンストラクタ
        super().__init__(filePath)
        #独自のコンストラクタの処理

    def makeDir(self, makeDir):
        makeFullPath = os.path.join(self.filePath, makeDir)
        try:
            os.makedirs(makeFullPath)
        except FileExistsError:
            pass
        return makeFullPath
    
    def isExistDir(self, targetDir):
        targetFullPath = os.path.join(self.filePath, targetDir)
        return os.path.exists(targetFullPath)
