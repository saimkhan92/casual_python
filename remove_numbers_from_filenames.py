#This python program removes numbers from the filenames of all files in a directory eg: 1saimfile43==saimfile
# 1) store all file names in a list
# 2)for all the stored elements : rename the file

import os

path="/Users/saimkhan/Desktop"
os.chdir(path)
print("original file names")
print(os.listdir(path))
print("")

def eliminate_numbers_from_filename(filename):
    new_filename=filename.translate(None,"0123456789")            
    return new_filename

def main():
    new_filelist=[]
    file_list=os.listdir(path)
    for filename in file_list:
        new_filename=eliminate_numbers_from_filename(filename)
        new_filelist.append(new_filename)
    print("modified file names")
    print(new_filelist)

if __name__=="__main__":
    main()
