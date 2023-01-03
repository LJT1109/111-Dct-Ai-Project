import os,shutil,random,sys


persent = float(sys.argv[1])

#persent = 0.1

old = ["train","images"]
new = ["val","images"]
oldx = ["train","annotations"]
newx = ["val","annotations"]


for i in os.listdir("/".join(newx)):
    if(i!= "image_annotation_classes.txt"):
        os.remove("/".join(newx)+"/"+i)
        
        
for i in os.listdir("/".join(new)):
    os.remove("/".join(new)+"/"+i)

folder= os.listdir("/".join(old))
count =len(folder) * persent
while(len(os.listdir("/".join(new)))<count):
    rand = random.randint(0, len(folder)-1)
    old.append(folder[rand])
    oldx.append(folder[rand].replace("png", "xml"))
    new.append(folder[rand])
    newx.append(folder[rand].replace("png", "xml"))
    shutil.copy("/".join(old),"/".join(new))
    shutil.copy("/".join(oldx),"/".join(newx))
    new.pop()
    newx.pop()
    old.pop()
    oldx.pop()