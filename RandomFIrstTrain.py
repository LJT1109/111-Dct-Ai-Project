import os,shutil,random,sys

path = ["train","annotations"]
for i in os.listdir("/".join(path)):
    if(i!= "image_annotation_classes.txt"):
        os.remove("/".join(path)+"/"+i)
        
        
path = ["train","images"]
for i in os.listdir("/".join(path)):
    os.remove("/".join(path)+"/"+i)