import time
import os
import shutil

path = input("what is the file you want to delete: ")
days = 30
seconds = time.time() - (days*24*60*60)

if os.path.exists(path): 
    for root_folder, folders, files in os.walk(path):
        if seconds >= getfileorfolderage(root_folder):
            removeFolder(root_folder)
        else:
            for folder in folders:
                folder_path = os.path.join(root_folder, folder)
                if seconds >= getfileorfolderage(folder_path):
                    removeFolder(folder_path)
            for file in files:
                file_path = os.path.join(root_folder, file)
                if seconds >= getfileorfolderage(file_path):
                    removeFolder(file_path)
   
def getfileorfolderage(path):
    ctime = os.stat(path).st_ctime
    return ctime

def removeFolder(path):
    if not shutil.rmtree(path):
        print("path is removed successfully")
    else:
        print("unable to remove the path")