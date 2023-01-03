import tkinter
import os
from PIL import Image
from PIL import ImageDraw,ImageTk
import csv
import sys
import pygame as pg
from pygame.locals import QUIT
import shutil
import random

#folder = os.scandir(path='.')
from tkinter.filedialog import askdirectory

folder = ""
while(folder == ""):
    folder = askdirectory()



infolder = os.listdir(folder)
for i in infolder:
    if(i.find(".csv")>0):
        print("/".join([folder,i]))

csvfile = "/".join([folder,i])
m_rows = []
with open(csvfile, newline='') as csvfile:
    rows = list(csv.reader(csvfile, delimiter=':')) 
    
    for row in rows[1:]:
        row=row[0].split(",")
        m_rows.append(row)
        
#print(m_rows)


def showimg(row,show=False):
    imgPath = "/".join(["m_raw",row[0]])
    img = Image.open(imgPath)
    a = ImageDraw.ImageDraw(img)
    rect = [int(x) for x in row[3:7]]
    rect = ((rect[0],rect[1]),(rect[2]+rect[0],rect[3]+rect[1]))
    #print(rect)
    a.rectangle(rect,fill=None, outline='red',width=2)
    if(show):
        img.show()
    return img
    
#showimg(m_rows[0])


def pilImageToSurface(pilImage):
    return pg.image.fromstring(
        pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
def placeImage(ind):
    global bg,screen
    bg.blit(pilImageToSurface(showimg(m_rows[ind])), (200,100))
    screen.blit(bg, (0,0))
    pg.display.update()

o = []
x = []
ind = 0

#pygame初始化
pg.init()

#設定視窗
width, height = 640, 480                      
screen = pg.display.set_mode((width, height)) 
pg.display.set_caption("Left=>X Right=>O")        

#建立畫布bg
bg = pg.Surface(((screen.get_size())))
bg = bg.convert()
bg.fill((255,255,255))           #白色
#顯示

nowimg = placeImage(ind)

pg.display.update()

#關閉程式的程式碼
running = True
force = False
last = []
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            force = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                x.append(ind)
                ind+=1
                last.append(1)
                if(ind>=len(m_rows)):
                    running = False
                else:
                    nowimg = placeImage(ind)
                    print(o,x)
                    
            if event.key == pg.K_RIGHT:
                o.append(ind)
                ind+=1
                last.append(-1)
                if(ind>=len(m_rows)):
                    running = False
                else:
                    nowimg = placeImage(ind)
                    print(o,x)
            if event.key == pg.K_UP:
                if(ind>0):
                    if(last[-1]<0):
                        o.pop()
                    else:
                        x.pop()
                    last.pop()
                    ind-=1
                    nowimg = placeImage(ind)
                    print(o,x)

    
    
pg.quit() 

if(force):
    sys.exit()

with open('object.xml','r') as ob:
    ob = ob.read()
    print(ob)
print("\n")
with open('format.xml','r') as xmlformat:
    xmlformat = xmlformat.read()
    print(xmlformat)
    
    
anno = {}
for i in o:
    row = m_rows[i]
    path = row[0]
    
    rect = [int(x) for x in row[3:7]]
    rect = (rect[0],rect[1],rect[2]+rect[0],rect[3]+rect[1])
    xmin,ymin,xmax,ymax = rect[0],rect[1],rect[2],rect[3]
    if(path not in anno):  
        anno[path] = [ob.format(xmin,ymin,xmax,ymax)]
    else:
        anno[path].append(ob.format(xmin,ymin,xmax,ymax))
for i in anno:
    print("\n"+"="*25+i+"="*25+"\n")
    out = ""
    for s in anno[i]:
        out+="\n"+s
    print(xmlformat.format(filename = i,m_object = out))
    #"raw_data/"+ row[0].split("_")[1]+"/"+i
    with open('train/annotations/'+i.replace("png","xml"),'a') as newxml:
        newxml.truncate(0)
        newxml.write(xmlformat.format(filename = row[0],m_object = out))
        newxml.close()
    #i.split("_")[1]
    print("m_raw/"+i)
    shutil.copyfile("m_raw/"+i,"train/images/"+i)
    
    