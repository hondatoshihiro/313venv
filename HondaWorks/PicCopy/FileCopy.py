#写真の移動コピー(日付毎のフォルダに分類)
#D:\Python\venv\309venv\PythonStudy01\FileCopy.iniの設定を変更(入出力設定)
#PS D:\Python\venv\309venv>cd .\.309venv\Scripts
#PS D:\Python\venv\309venv\.309venv\Scripts>./Activate.ps1
#PS D:\Python\venv\309venv\.309venv\Scripts>cd ..\..
#PS D:\Python\venv\309venv\PythonStudy01>py FileCopy.py
import os
import logging
import datetime
import shutil
import HWIniFile
import HWLog
import traceback

def main():
    try:
        #ログ
        current_path = os.getcwd()
        hwlog = HWLog.HWLog(current_path +'\\FileCopy.log', logging.DEBUG)
        hwlog.open()
        hwlog.log_info('start FileCopy')
        #ファイルコピーツールIniファイル読み込み
        hwinifile = HWIniFile.HWIniFile()
        hwinifile.read_inifile('FileCopy.ini')
        hwlog.log_info('read FileCopy.ini')
        #コピー元ディレクトリ情報取得
        srcpath=hwinifile.getvalue('SrcPath')
        hwlog.log_info('SrcPath:' + hwinifile.getvalue('SrcPath'))
        #コピー先ディレクトリ情報取得
        dstpath=hwinifile.getvalue('DstPath')
        hwlog.log_info('DstPath:' + hwinifile.getvalue('DstPath'))

        #SrcPath探索 ファイル数カウント
        filecount = 0
        filecount = count_targetfile(srcpath, filecount)
        hwlog.log_info('TargetFile:' + str(filecount))
        #SrcPath探索 ファイルコピー
        fileindex = 0
        copy_targetfile(srcpath, dstpath, filecount, fileindex, hwlog)
        hwlog.log_info('end FileCopy')
    except Exception:
        #すべての例外をキャッチ
        hwlog.log_error('エラー情報:' + traceback.format_exec())
        print("エラー情報:\n" + traceback.format_exec())

def count_targetfile(search_path, filecount):
    #SrcPath探索
    target_list=os.listdir(search_path)
    for target in target_list:
        target_path = search_path + "\\" + target
        if os.path.isdir(target_path):
            #ディレクトリの場合
            #そのディレクトリを処理する(再帰呼び出し)
            filecount = count_targetfile(target_path, filecount)
        else:
            #ファイルの場合
            #ファイルプロパティ取得
            #mtime = os.stat(target_path).st_mtime
            #strtimestamp = datetime.datetime.fromtimestamp(mtime)
            filecount = filecount+1
            #フォルダ作成
            #ファイル存在確認
            #ファイルコピー
    return filecount

def copy_targetfile(search_path, copy_path, filecount, fileindex, hwlog):
    #search_path探索
    target_list=os.listdir(search_path)
    for target in target_list:
        target_path = search_path + "\\" + target
        if os.path.isdir(target_path):
            #ディレクトリの場合
            #そのディレクトリを処理する(再帰呼び出し)
            fileindex = copy_targetfile(target_path, copy_path, filecount, fileindex, hwlog)
        else:
            #ファイルの場合
            #ファイルプロパティ取得
            mtime = os.stat(target_path).st_mtime
            dttimestamp = datetime.datetime.fromtimestamp(mtime)
            strtimestamp = dttimestamp.strftime('%Y-%m-%d')
            copy_dir = strtimestamp[0:10]
            if os.path.exists(copy_path + "\\" + copy_dir) == False:
                #フォルダ作成
                #フォルダ作成に失敗した場合は？
                os.makedirs(copy_path + "\\" + copy_dir)
            #ファイル存在確認
            if os.path.exists(copy_path + "\\" + copy_dir + "\\" + target) == True:
                #リネーム
                index = 1
                copy_file = rename(copy_path + "\\" + copy_dir, target, index)
            else:
                copy_file = target 
            #ファイルコピー
            #ファイルコピーに失敗した場合は？
            shutil.copy2(search_path+ "\\" + target, copy_path + "\\" + copy_dir + "\\" + copy_file)
            fileindex = fileindex + 1
            hwlog.log_info('src:' + search_path+ "\\" + target)
            hwlog.log_info('dst:' + copy_path + "\\" + copy_dir + "\\" + copy_file)
            print("処理中:{}/{} {}%".format(fileindex, filecount, int((fileindex/filecount)*100)))
    return fileindex

def rename(target_path, target_file, index):
    #ファイルリネーム
    filename_list = target_file.split(".")
    index_str = str(index)
    #後ろから2つ目のファイル名成分に
    filename_list[-2] = filename_list[-2] + "_" + index_str.zfill(2)
    rename_file = ""
    for filename_div in filename_list:
        if rename_file != "":
            rename_file = rename_file + "." + filename_div
        else:
            rename_file = filename_div
    #ファイル存在確認
    if os.path.exists(target_path + "\\" + rename_file) == True:
        index = index + 1
        #リネーム
        #リネームに失敗した場合は？
        try:
            rename_file = rename(target_path, target_file, index)
        except OSError as e1:
            raise e1
        except FileExistsError as e2:
            raise e2
        except IsADirectoryError as e3:
            raise e3
        except NotADirectoryError as e4:
            raise e4
    return rename_file

if __name__ == '__main__':
    main()
