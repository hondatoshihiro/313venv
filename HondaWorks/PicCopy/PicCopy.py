import os
import datetime
import shutil
import sys
sys.path.append("../")
from Tools.Dir.HWDirSearch import HWDirSearch
from Tools.IniFile.HWIniFile import HWIniFile
import PicCopy

def main():
    try:
        #設定ファイル(PicCopy.ini)の読み込み
        iniFile = HWIniFile()
        iniFile.readIniFile('PicCopy.ini')
        #入力パス取得
        srcPath = iniFile.getStrValue('FilePath','SrcPath')
        print("入力パス：" + srcPath)

        #出力パス取得
        dstPath = iniFile.getStrValue('FilePath','DstPath')
        print("出力パス：" + dstPath)

        #入力パス配下の写真ファイルを
        #出力パス配下の日付毎のディレクトリにコピーする。
        obj = PicCopy.PicCopy()
        obj.countFiles(srcPath)
        obj.copyPic(srcPath, dstPath)
        obj.printCopyResult()
    except Exception as e:
        print("例外発生!!:"+ e)

if __name__ == '__main__':
    main()

class PicCopy:
    def __init__(self):
        self.fileIndex = 0
        self.dirIndex = 0
        self.allFileCnt = 0
        self.allDirCnt = 0

    def countFiles(self, srcPath):
        dirSearch = HWDirSearch()
        dirSearch.setTargetDir(srcPath)
        fileList = dirSearch.getFileList()
        self.allFileCnt = self.allFileCnt + len(fileList)
        dirList = dirSearch.getDirList()
        self.allDirCnt = self.allDirCnt + len(dirList)
        for dir in dirList:
            self.countFiles(dirSearch.getDirPath(dir))


    def copyPic(self, srcPath, dstPath):

        print("入力パス(copyPic)：" + srcPath)
        dirSearch = HWDirSearch()
        dirSearch.setTargetDir(srcPath)

        fileList = dirSearch.getFileList()
        for file in fileList:
            #画像ファイルに対する処理を書く
            self.fileIndex = self.fileIndex + 1
            print("処理ファイル数：" + str(self.fileIndex) + "/" + str(self.allFileCnt))
        
        dirList = dirSearch.getDirList()
        for dir in dirList:
            self.copyPic(dirSearch.getDirPath(dir), dstPath)
            self.dirIndex = self.dirIndex + 1
            print("処理ディレクトリ数：" + str(self.dirIndex) + "/" + str(self.allDirCnt))
    
    def printCopyResult(self):
        print("処理結果 ディレクトリ総数:" + str(self.allDirCnt) + ",ファイル総数:" + str(self.allFileCnt))
