import configparser

class HWIniFile:
    def read_inifile(self, inifile_path):
        config = configparser.ConfigParser()
        config.read(inifile_path, encoding='utf-8')
        src_path = config.get('FilePath','SrcPath')
        dst_path = config.get('FilePath','DstPath')
        self.inifile_dict = {}
        self.inifile_dict['SrcPath'] = src_path
        self.inifile_dict['DstPath'] = dst_path
        
    def getvalue(self, key):
        val = self.inifile_dict.get(key)
        return val

#動作確認
if __name__ == '__main__':
    filecopy_inifile = HWIniFile()
    filecopy_inifile.read_inifile('FileCopy.ini')
    print(filecopy_inifile.getvalue('SrcPath'))
    print(filecopy_inifile.getvalue('DstPath'))
