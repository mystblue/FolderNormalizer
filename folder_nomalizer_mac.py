# coding: utf-8

"""
カレントフォルダ直下にある「aaa - bbb 01」形式のフォルダを
「[aaa] bbb 01」形式に変更する
"""

__author__  = 'mystblue'
__version__ = '0.0.1'
__date__    = '2013/11/12'

import os
import Tkinter
import tkMessageBox

class FolderNormalizer():
    def __init__(self):
        self.counter = 0

    def get_new_name(self, file_name):
        file_name = file_name.replace(u"第".encode("utf-8"), "")
        file_name = file_name.replace(u"巻".encode("utf-8"), "")
        #print file_name
        return file_name

    def rename(self):
        """
        カレントフォルダ直下のフォルダをリネームする
        """
        rootDir = "."
        file_list = os.listdir(rootDir)
        for file_name in file_list:
            path = os.path.join(rootDir, file_name)
            # ファイルは処理しない
            if not os.path.isdir(path):
                continue
            new_name = self.get_new_name(file_name)
            print file_name + " -> " + new_name
            if not file_name == new_name:
                os.rename(file_name, new_name)
                self.counter = self.counter + 1
    
    def show_message(self):
        """
        メッセージを出力する
        """
        root = Tkinter.Tk()
        root.withdraw()

        if self.counter ==0:
            tkMessageBox.showinfo("終了", "フォルダが見つかりませんでした。")
        else:
            tkMessageBox.showinfo("終了", str(self.counter) + "個のフォルダをリネームしました。")

if __name__ == "__main__":
    fnr = FolderNormalizer()
    fnr.rename()
    fnr.show_message()
