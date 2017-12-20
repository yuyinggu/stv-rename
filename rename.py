#coding:utf8
import os
from datetime import timedelta, datetime
from time import sleep
import re

def date_to_folder(date):
    time_str = date.strftime("%Y-%m-%d").split("-")
    time_folder = time_str[0] + "\\"+ time_str[1] + "-"+ time_str[0] + "\\"time_str[2]
    return (time_folder, time_str)

def rename(path, time_str):#time_str[0]: year, time_str[1]:month, time_str[2]:day
    if os.path.exists(path):
        i=1
        filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
        if len(filelist) == 0:
            return
        for files in sorted(filelist):#遍历所有文件
            Olddir=os.path.join(path,files)#原来的文件路径
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                continue
            filename=os.path.splitext(files)[0]#文件名
            filetype=os.path.splitext(files)[1]#文件扩展名
            if files == time_str[2]+"00.flv" or files == time_str[2]+"99.flv" or (re.search('.jpg?',files) is not None): 
                continue
            elif files == "00.flv" or files == "99.flv":
                Newdir=os.path.join(path,time_str[2]+filename+filetype)
                os.rename(Olddir,Newdir)
                continue
            if i < 10 and filetype in ['.flv','.mp4']:
                Newdir=os.path.join(path,time_str[2]+"0"+str(i)+filetype)#新的文件路径
                i=i+1
            elif filetype in ['.flv','.mp4']:
                Newdir=os.path.join(path,time_str[2]+str(i)+filetype)#新的文件路径
                i=i+1
            if os.path.exists(Newdir):
                pass
            else:
                os.rename(Olddir,Newdir)#重命名
    else:
        input("重命名地址错误")
        exit()




if __name__ == '__main__':
       today_folder, timeStr = date_to_folder(datetime.now())

       for i in range(1,9):
              path="\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_0"+str(i)
              rename(path,timeStr)
