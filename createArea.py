import sys,shutil,os
from PIL import Image

if(not os.path.exists("area")):
    os.mkdir("area")
else:
    for i in os.listdir("area"):
        os.remove("area/"+i)
        
x,y = [],[]

for i in os.listdir("m_raw"):
    rx = int(i.split("_")[1])
    if rx not in x:
        x.append(rx)
    ry = int(i.split("_")[2])
    if ry not in y:
        y.append(ry)
    
for i in x:
    for s in y:
        path = ["m_raw","IMG_{0}_{1}_1.png".format(i,s)]
        if not os.path.exists("/".join(path)):
            #print("/".join(path))
            shutil.copy("empty.png","/".join(path))
#print(x)
#print(y)


x1,x2,y1,y2 = min(x),max(x),min(y),max(y)
mx1,mx2,my1,my2 = 0,0,0,0

def enter(text,range = (0,0)):
    print(text.format(range[0],range[1]))
    a = int(input(""))
    if(a < range[0] or a> range[1]):
        return enter(text,range)
    else:
        return a
        
mx1 = enter("Enter min x (range:{0}~{1})",(x1,x2))
mx2 = enter("Enter Max x (range:{0}~{1})",(mx1,x2))+1
my1 = enter("Enter min y (range:{0}~{1})",(y1,y2))
my2 = enter("Enter Max y (range:{0}~{1})",(my1,y2))+1


#mx1,mx2,my1,my2 = 54720,54730,28283,28293


print(mx1,mx2,my1,my2)
for i in range(mx1,mx2):
    for s in range(my1,my2):
        #print("IMG_{0}_{1}_1.png".format(i,s))
        old = "/".join(["m_raw","IMG_{0}_{1}_1.png".format(i,s)])
        new = "/".join(["area","IMG_{0}_{1}_1.png".format(i,s)])
        shutil.copy(old,new)
        
        
def combine(fdname):
    fd = os.listdir(fdname)
    x,y = [],[]
    for i in fd:
        x.append(int(i.split("_")[1]))
        y.append(int(i.split("_")[2]))
    w,h = max(x)-min(x),max(y)-min(y)
    #print(min(x),max(x),min(y),max(y),w,h)
    imsize = (256,256)
    nsize = imsize[0] *w , imsize[1] * h
    #print(nsize)
    new_image = Image.new('RGB',(nsize[0], nsize[1]), (250,250,250))
    for i in range(min(x),max(x)):
        
        img = [Image.open(fdname+"/"+"IMG_{0}_{1}_1.png".format(i,s)) for s in range(min(y),max(y))]
        
        for s in range(len(img)):
            #img[s].show()
            new_image.paste(img[s],((i-min(x))*imsize[0],s*imsize[1]))
            #print((i-min(x))*imsize[0],s*imsize[1])
    new_image.save("output/"+fdname+".png")
    

    
combine("area")
