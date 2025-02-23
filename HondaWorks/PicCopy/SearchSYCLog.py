import os

def main():
    collect_log("d:\\work\\test")

def collect_log(target_path):
    print(target_path)
    #target_path探索
    target_list=os.listdir(target_path)
    print(len(target_list))
    for target in target_list:
        print(target)
        target_wkpath = target_path + "\\" + target
        if os.path.isdir(target_wkpath):
            #ディレクトリの場合
            #そのディレクトリを処理する(再帰呼び出し)
            collect_log(target_wkpath)
        else:
            #ファイルの場合
            worklist = target.split(".")
            if worklist[-1] == "lgf":
                #ログファイルの中身を検索する
                search_log(target_wkpath)
            else:
                #*.lgfファイル以外は何もしない
                pass

def search_log(target_path):
    result_file = open("result_log.txt", "a", encoding="utf_8")
    with open(target_path, "r", encoding="utf_8") as target_file:
        for line in target_file:
            #print(line)
            jdg = "★test★" in line
            if jdg == True:
                #結果ファイルに書き込む
                result_file.write(line)
            else:
                #何もしない
                pass
    result_file.close()

if __name__ == '__main__':
    main()
