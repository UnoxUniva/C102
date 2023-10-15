import os
import shutil
from_dir = "C:/Users/User/Desktop/Randofilos"
to_dir = "C:/Users/User/Desktop/Designs"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue;
    if extension in ['.png','.jpg','jpeg']:
        path1 = from_dir + '/' + file_name  
        path2 = to_dir + '/' + "Tfers" 
        path3 = to_dir + '/' + "Tfers" + '/' + file_name   
        if os.path.exists(path2):
            print("Moving " + file_name + "......")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving " + file_name + "......")
            shutil.move(path1, path3)
            