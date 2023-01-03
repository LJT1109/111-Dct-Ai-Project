import csv
import tkinter
import os
#folder = os.scandir(path='.')
from tkinter.filedialog import askdirectory
from PIL import Image
from PIL import ImageDraw,ImageTk

folder = ""
while(folder == ""):
    folder = askdirectory()
folder

infolder = os.listdir(folder)
for i in infolder:
    if(i.find(".csv")>0):
        print("/".join([folder,i]))

csvfile = "/".join([folder,i])

x,y = [],[]

for i in os.listdir("area"):
    rx = int(i.split("_")[1])
    if rx not in x:
        x.append(rx)
    ry = int(i.split("_")[2])
    if ry not in y:
        y.append(ry)

print(x)
#print(y)


m_rows = []
with open(csvfile, newline='') as csvfile:
    rows = list(csv.reader(csvfile, delimiter=':')) 
    
    for row in rows[1:]:
        row=row[0].split(",")
        m_rows.append(row)
        
m_rows

maxscore = 0
score = []
for i in m_rows:
    
    sp = i[0].split("_")
    print(int(sp[1]),min(x),int(sp[2]),min(y))
    bigpos = ((int(sp[1])-min(x))*256,(int(sp[2])-min(y))*256)
    #print(bigpos)
    tmp = [i[0]]
    pos = [int(x) for x in i[3:7]]
    
    area = pos[2] * pos[3]
    tmp.append(area)
    cent = (bigpos[0]+pos[0]+pos[2]/2,bigpos[1]+pos[1]+pos[3]/2)
    tmp.append(cent)
    if(area > maxscore):
        maxscore = area
    score.append(tmp)

for i in range(len(score)):
    score[i].append(score[i][1]/maxscore)
    img = Image
score
    

def drawpeople(img,rect):
    for i in score[0:1]:
        a = ImageDraw.ImageDraw(img)
        a.ellipse(rect, fill = 'blue', outline ='blue' ,  width=10)
        return img
    
img = Image.open("output/area.png")
scale = 500
for i in score:
    #print(i)
    rad = i[3]*scale
    pos = (i[2][0]-rad,i[2][1]-rad,i[2][0]+rad,i[2][1]+rad)
    #print(cent)
    img = drawpeople(img,pos)
img.show()
img.save("output/draw.png")