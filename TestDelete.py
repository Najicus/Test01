# from sys import platform
# from pathlib import Path
# import os

# # mainLog = "/Volumes/IT_Storage/FileSorterlogs/"
# logStorage = Path(r"\\10.0.1.191\IT_Storage\Python_logs\ReviewSessions_Master_V1.log")

# def OSFilePathFilter(logStorage):
#     if platform == "linux" or platform == "linux2":
#         return "/mnt"
#     elif platform == "darwin":
#         # print ("OSX")
#         logStorage = logStorage.with_drive("/Volumes")
#     elif platform == "win32":
#         return "\\10.0.0.1"
#     return logStorage
# # fp = OSFilePathFilter() + Path("/Volumes/IT_Storage/FileSorterlogs/")
# # print (OSFilePathFilter() + str(Path("/Volumes/IT_Storage/FileSorterlogs/")))

# username = "NAJ"
# mainLog = OSFilePathFilter() + str(Path("/IT_Storage/FileSorterlogs/"))
# backupLog = Path(f'/Users/{username}/Desktop/FileSorterLogs/')

# def swapLogDestination(mainLog, backupLog):
#     # lp = "/Users/naj/Desktop/Testing/logs/FileSorter/FileSorter.log"
#     # backupLog = '/Volumes/Graphics/_STUDIO_RESOURCE/_Testing/Naj/Scripts/logs/FileSorter/FileSorter.log'

#     if os.path.exists(mainLog):
#         return mainLog
#     else:
#         return backupLog

# # print (swapLogDestination(mainLog, backupLog))
# # print(mainLog)



# flex = "\\10.0.12.100\flex-Source-Materials_1"


# print (logStorage)

from pathlib import Path
import platform
import os

logStorage = Path("/Volumes/IT_Storage/FileSorterlogs/")
username = "NAJ-VARIBALE-TEST"
mainLog = "/Volumes/IT_Storage/FileSorterlogs/"
backupLog = f'/Users/{username}/Desktop/FileSorterLogs/'
UniFilePathRoot = "/Volumes/flex-Source-Materials_1"
destination_rootFolder = "/Volumes/flex-Source-Materials_1"

def OSFilePathFilter():

    global mainLog, backupLog, UniFilePathRoot, destination_rootFolder
    
    system = platform.system()

    if system == "Linux":
        pass
    elif system == "Darwin":
        pass
    elif system == "Windows":
        mainLog = Path(r"\\10.0.12.100/IT_Storage/FileSorterlogs/")
        backupLog = Path(f'/Users/{username}/Desktop/FileSorterLogs/')
        UniFilePathRoot = Path(r"10.0.12.100/flex-Source-Materials_1")
        destination_rootFolder = Path(r"10.0.12.100/flex-Source-Materials_1")
        # if os.path.exists(mainLog):
        #     return mainLog
        # else:
        #     return backupLog

    return mainLog, backupLog, UniFilePathRoot, destination_rootFolder

def swapLogDestination(mainLog, backupLog):
    # lp = "/Users/naj/Desktop/Testing/logs/FileSorter/FileSorter.log"
    # backupLog = '/Volumes/Graphics/_STUDIO_RESOURCE/_Testing/Naj/Scripts/logs/FileSorter/FileSorter.log'

    if os.path.exists(mainLog):
        return mainLog
    else:
        return backupLog

OSFilePathFilter()


print("OS: " + platform.system())
print("Mainlog: " + str(mainLog))
print("BackupLog: "+ str(backupLog))
print("UniPath: " + str(UniFilePathRoot))
print("DestPath: " + str(destination_rootFolder))