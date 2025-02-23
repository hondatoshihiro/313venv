import configparser

class HWIniFile:

    def __init__(self):
        self.config = None
        self.isReadIniFile = False
    
    def readIniFile(self, iniFileFullPath):
        self.config = configparser.ConfigParser()
        self.config.read(iniFileFullPath, encoding='utf-8')
        self.isReadIniFile = True

    def getStrValue(self, section, key):
        if self.isReadIniFile == True:
            return self.config.get(section,key)
        else:
            return ""

    def getIntValue(self,section, key):
        if self.isReadIniFile == True:
            return self.config.getint(section,key)
        else:
            return 0

    def getBoolValue(self,section, key):
        if self.isReadIniFile == True:
            return self.config.getboolean(section,key)
        else:
            return False

#動作確認
if __name__ == '__main__':
    inifile = HWIniFile()
    inifile.readIniFile('./../../PicCopy/PicCopy.ini')
    print(inifile.getStrValue('FilePath','SrcPath'))
    print(inifile.getStrValue('FilePath','DstPath'))
