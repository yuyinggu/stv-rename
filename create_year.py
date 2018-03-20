from datetime import datetime,timedelta
import os

def date_to_folder(date):
    time_str = date.strftime("%Y-%m-%d").split("-")
    time_folder = time_str[0] + "\\"+ time_str[1] + "\\" + time_str[2] ###修改这里
    return time_folder

def check_next_month(mon=1):
    next_month = (datetime.now() + timedelta(days=30*mon)).strftime("%Y-%m").split("-")
    print(next_month)
    try:
        test_path = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\Source\\"+ next_month[0] + "\\"+ next_month[1]
        #test_path = "C:\\Users\\Andy\\Downloads\\"+ next_month[0] + "\\"+ next_month[1] ###修改这里
    except:
        os.system("pause")
        error = input("地址错误")
        exit()

    if not os.path.exists(test_path):
        start_date = datetime.strptime("-".join(next_month)+"-01","%Y-%m-%d")
        start_mon = int(start_date.strftime("%m"))
        cur_mon = start_mon
        while cur_mon == start_mon:
            fold_str = date_to_folder(start_date)
            for i in range(1,9):
                dir_path = "\\\\vdisk.chineseradio.local\\VideoWork\\OtherVideos\\STPlayer\\Source\\"+ fold_str +"\\segment_0"+ str(i)
                #dir_path = "C:\\Users\\Andy\\Downloads\\" + fold_str +"\\segment_0"+ str(i)
                os.makedirs(dir_path)
            start_date = start_date + timedelta(days=1)
            cur_mon = int(start_date.strftime("%m"))
        print("Next Month Folders Created")

if __name__ == "__main__":
    for i in range(1,13):
        check_next_month(i)
