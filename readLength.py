import subprocess
import os
from datetime import timedelta, datetime
import time
file_count = 0 #counting total video files
total_time = timedelta(0) #total video duration
this_year = (datetime.now()).strftime("%Y")

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
    dir_count = 0
    file_type = [".flv", ".mp4", ".mov", ".jpg"]    
    record_file.write("Folder Path:%s\n" % dir_path)
    
    for f in sorted(os.listdir(dir_path)):           
        for val in file_type:                
            if val in f:
                file_count += 1
                dir_count += 1
                if file_type != ".jpg":
                    video_length = getLength(f)
                    x = video_length.split(":")
                    total_time += timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2]))
                    dir_duration += timedelta(hours=int(x[0]), minutes=int(x[1]), seconds=int(x[2]))        
                    record_file.write("{0}\t{1}\n".format(f,video_length))
                else:
                    record_file.write("{0}\t\n".format(f))
                #print(f)
                #print(video_length)
    record_file.write("Folder Files:%s\n" % str(dir_count))
    record_file.write("Folder Duration:%s\n\n" % str(dir_duration))


def date_to_folder(date):
    time_str = date.strftime("%Y-%m-%d").split("-")
    time_folder = time_str[0] + "\\"+ time_str[1] + "\\" + time_str[2]
    return time_folder


def check_next_month():
    next_month = (datetime.now() + timedelta(days=30)).strftime("%Y-%m").split("-")

    try:
        test_path = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\STPlayerLog\\"+ next_month[0]
    except:
        os.system("pause")
        error = input("next month地址错误")    
        exit()
    
    if not os.path.exists(test_path):
        start_date = datetime.strptime("-".join(next_month)+"-01","%Y-%m-%d")
        start_mon = int(start_date.strftime("%m"))
        cur_mon = start_mon
        while cur_mon == start_mon:
            fold_str = date_to_folder(start_date)
            for i in range(1,9):
                dir_path = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ fold_str +"\\segment_0"+ str(i)
                try:
                    os.makedirs(dir_path)
                except:
                    pass
            start_date = start_date + timedelta(days=1)
            cur_mon = int(start_date.strftime("%m"))
        print("Next Month Video Folders Created")
        
def checkLogFolder(year):    
    logPath = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\STPlayerLog\\"+year
    if not os.path.exists(logPath):
        os.makedirs(logPath)


		
	
if __name__ == "__main__":
    #options = input("1: 创建LOG文件 2:重命名并排序文件 3:片头片尾时间\n")
    global record_file
    #if options == "1":        
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
 #   elif options == "2":
#        options2()
#    elif options == "3":
#        options3()
