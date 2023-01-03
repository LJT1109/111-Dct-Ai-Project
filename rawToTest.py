import os,shutil,random,sys

times = int(sys.argv[1])
folder = os.listdir("m_raw")

        
oldpath = ["m_raw"]     
path = ["test","images"]
while(len(os.listdir("/".join(path)))<times):
    rand = random.randint(0,len(folder)-1)
    print(str(len(os.listdir("/".join(path))))+"/"+str(times-1))
    oldpath.append(folder[rand])
    path.append(folder[rand])
    shutil.copy("/".join(oldpath), "/".join(path))
    oldpath.pop()
    path.pop()
    