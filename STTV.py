import subprocess
import os
from datetime import timedelta, datetime
import time
file_count = 0 #counting total video files
total_time = timedelta(0) #total video duration
this_year = (datetime.now()).strftime("%Y")

#######################################################选择1
def options1():
    today_folder, timeStr = date_to_folder(datetime.now(),True)
    for i in range(1,9):
        path="\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_0"+str(i)        
        if not os.path.exists(path):
            os.makedirs(path)           
        rename(path,timeStr)
    result = input("重命名成功")
    

def rename(path, time_str):#time_str[0]: year, time_str[1]:month, time_str[2]:day
    if os.path.exists(path):
        i=1
        filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
        for files in sorted(filelist):#遍历所有文件
            Olddir=os.path.join(path,files)#原来的文件路径
            if os.path.isdir(Olddir):#如果是文件夹则跳过
                continue            
            filename=os.path.splitext(files)[0]#文件名
            filetype=os.path.splitext(files)[1]#文件扩展名
            if files == time_str[2]+"00.flv" or files == time_str[2]+"99.flv":
                continue                
            elif files == "00.flv" or files == "99.flv":
                Newdir=os.path.join(path,time_str[2]+filename+filetype)                                
            elif i < 10 and filetype in ['.jpg''.flv','.mp4']:
                Newdir=os.path.join(path,time_str[2]+"0"+str(i)+filetype)#新的文件路径
                i=i+1
            elif filetype in ['.jpg''.flv','.mp4']:
                Newdir=os.path.join(path,time_str[2]+str(i)+filetype)#新的文件路径
                i=i+1
            if os.path.exists(Newdir):
                pass
            else:
                os.rename(Olddir,Newdir)#重命名		
    else:
        input("重命名地址错误")
        exit()		
#######################################################选择1


        

#######################################################选择2
def getLength(filename):
    result = subprocess.Popen(["ffprobe", filename], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    output = result.stdout.readlines()
    for val in output:
        val = str(val)
        if "Duration" in val:
            return(val[14:22])


def loop_files(dir_path):
    global total_time, file_count    
    os.chdir(dir_path)
    dir_duration = timedelta(0)
    dir_count =[".jpg",".flv", ".mp4",  ".mov"]    
    record_file.write("Folder Path:%s\n" % dir_path)
    
    for f in sorted(os.listdir(dir_path)):           
        for val in file_type:                
            if val in f:
                file_count += 1
                dir_count += 1
                video_length = getLength(f)
                x = video_length.split(":")
                total_time += timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2]))
                dir_duration += timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2]))        
                record_file.write("{0}\t{1}\n".format(f,video_length))
                #print(f)
                #print(video_length)
    record_file.write("Folder Files:%s\n" % str(dir_count))
    record_file.write("Folder Duration:%s\n\n" % str(dir_duration))

    
def date_to_folder(date, getTime = False):
    time_str = date.strftime("%Y-%m-%d").split("-")
    time_folder = time_str[0] + "\\"+ time_str[1] + "\\" + time_str[2]
    if getTime:
        return (time_folder, time_str)
    else:
        return time_folder


def check_next_month():
    next_month = (datetime.now() + timedelta(days=30)).strftime("%Y-%m").split("-")

    try:
        test_path = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\Source\\"+ next_month[0] + "\\"+ next_month[1]
    except:
        os.system("pause")
        error = input("Check Next Month 地址错误")    
        exit()
    
    if not os.path.exists(test_path):
        start_date = datetime.strptime("-".join(next_month)+"-01","%Y-%m-%d")
        start_mon = int(start_date.strftime("%m"))
        cur_mon = start_mon
        while cur_mon == start_mon:
            fold_str = date_to_folder(start_date)
            for i in range(1,9):
                dir_path = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ fold_str +"\\segment_0"+ str(i)                
                os.makedirs(dir_path)
            start_date = start_date + timedelta(days=1)
            cur_mon = int(start_date.strftime("%m"))
        print("Next Month Video Folders Created")
        
def checkLogFolder(year):    
    logPath = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\STPlayerLog\\"+year
    if not os.path.exists(logPath):
        os.makedirs(logPath)
#######################################################选择2

		

        
		

#######################################################选择3
def options3():
	
	path = input("drag or enter file path\n")
	if not os.path.isdir(path):
		choice = input("1:片頭，2:片尾\n")
		if choice == "1":
			os.utime(path,(1330712280, 1330712281))
		elif choice == "2":
			os.utime(path,(18619200000, 1861920001))
        
	else:
		result = input("Path is not a file")
		exit()
	result = input("成功")
#######################################################选择3

	
if __name__ == "__main__":
    options = input("1:重命名并排序文件 2: 创建LOG文件 3:片头片尾时间\n")
    global record_file
    if options == "2":        
        check_next_month()
        checkLogFolder(this_year)
        try:
            record_file = open("\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\STPlayerLog\\"+this_year+"\\%s-record.txt" % str(datetime.now().strftime("%Y-%m-%d")),"w+")
        except:
            error = input("LOG地址错误")
            exit()
        today_folder = date_to_folder(datetime.now())    

        dir_list = ["\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_01",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_02",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_03",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_04",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_05",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_06",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_07",
		"\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ today_folder +"\\segment_08"]
        
        note = "創建LOG文件中"
        sec = int(round(time.time()*1000))
        for dir_path in dir_list:
            if int(round(time.time()*1000))-sec > 800:
                note += "."
                print(note, end="\r")
                mil = int(round(time.time()*1000)) 
            loop_files(dir_path)

        record_file.write("Total Files:%s\n" % str(file_count))
        record_file.write("Total Duration:%s" % str(total_time))
        record_file.close()
        result = input("\nLOG創建成功")
        exit()
    elif options == "1":
        options1()
    elif options == "3":
        options3()
