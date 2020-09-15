import os, shutil, glob, re, datetime

#Source file

# for loop then I split the names of the image then making new folder
for file_path in glob.glob('../../data/files/**/*.mp3*', recursive=True):
    if "base" not in file_path:
     try:
        temp = re.split('(20\d{2}_\d{2}_\d{2})', file_path, 1) 
        company = re.split('incoming',file_path,0)
        folder = datetime.datetime.strptime(temp[1],'%Y_%m_%d').date().isoformat()	
       
     except Exception:
        try:
           temp = re.split('(20\d{2}\d{2}\d{2})', file_path, 1) 
           company = re.split('incoming',file_path,0)
           folder = datetime.datetime.strptime(temp[1],'%Y%m%d').date().isoformat()	
          
        except Exception:
           continue
       
     folderstr = os.path.join(company[0],"incoming/base",folder)
   # If folder does not exist try making new one
     try:
        os.mkdir(folderstr)
           # except error then pass
     except:
        pass
         # Move the images from file to new folder based on image name
     print("move" + file_path + " to " + os.path.join(folderstr, os.path.basename(file_path)))