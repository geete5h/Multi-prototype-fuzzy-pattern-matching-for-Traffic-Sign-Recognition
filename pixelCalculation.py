# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:01:44 2017

@author: Geetesh
"""
import numpy as np
import random
from PIL import Image

#Input Getter
def InputCreator(address) :
    clss = []
    url =address  
    img = Image.open(str(url))
    width,height =img.size
    #Calculating white pixels in first quadrant
    white1=0
    for x in range(0,int(width/2)):
        for y in range(0,int(height/4)):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white1 += 1
                
    #Calculating white pixels in second quadrant              
    white2=0    
    for x in range(0,int(width/2)):
        for y in range(int(height/4),int(height/2)):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white2 += 1
    #Calculating white pixels in third quadrant          
    white3=0
    for x in range(0,int(width/2)):
        for y in range(int(height/2),int((3*height)/4)):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white3 += 1

    #Calculating white pixels in fourth quadrant          
    white4=0
    for x in range(0,int(width/2)):
        for y in range(int((3*height)/4),height):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white4 += 1

    #Calculating white pixels in fifth quadrant
    white5=0
    for x in range(int(width/2),width):
        for y in range(0,int(height/4)):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white5 += 1

    #Calculating white pixels in sixth quadrant          
    white6=0
    for x in range(int(width/2),width):
        for y in range(int(height/4),int(height/2)):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white6 += 1
   
    #Calculating white pixels in seventh quadrant          
    white7=0
    for x in range(int(width/2),width):
        for y in range(int(height/2),int((3*height)/4)):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white7 += 1
    #Calculating white pixels in eight quadrant          
    white8=0
    for x in range(int(width/2),width):
        for y in range(int((3*height)/4),height):
            pixel = img.getpixel(( x, y))
            if(pixel==(255,255,255)):
                white8 += 1
                
    clss.append((white1,white2,white3,white4,white5,white6,white7,white8))
    cls=np.array(clss)
    return cls



def ClassCreator(name) :
    clss = []
    for i in range(1,25):
        url =str("D:\\dataset\\"+name+"\\image"+ str(i) +".bmp")  
        print(url)
        img = Image.open(str(url))
        width,height =img.size
        #Calculating white pixels in first quadrant
        white1=0
        for x in range(0,int(width/2)):
            for y in range(0,int(height/4)):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white1 += 1
                    
        #Calculating white pixels in second quadrant          
        white2=0
        for x in range(0,int(width/2)):
            for y in range(int(height/4),int(height/2)):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white2 += 1
           
        #Calculating white pixels in third quadrant          
        white3=0
        for x in range(0,int(width/2)):
            for y in range(int(height/2),int((3*height)/4)):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white3 += 1
            
        #Calculating white pixels in fourth quadrant          
        white4=0
        for x in range(0,int(width/2)):
            for y in range(int((3*height)/4),height):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white4 += 1
            
        #Calculating white pixels in fifth quadrant
        white5=0
        for x in range(int(width/2),width):
            for y in range(0,int(height/4)):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white5 += 1
            
        #Calculating white pixels in sixth quadrant          
        white6=0
        for x in range(int(width/2),width):
            for y in range(int(height/4),int(height/2)):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white6 += 1
           
        #Calculating white pixels in seventh quadrant          
        white7=0
        for x in range(int(width/2),width):
            for y in range(int(height/2),int((3*height)/4)):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white7 += 1
        #Calculating white pixels in eight quadrant          
        white8=0
        for x in range(int(width/2),width):
            for y in range(int((3*height)/4),height):
                pixel = img.getpixel(( x, y))
                if(pixel==(255,255,255)):
                    white8 += 1
              
        clss.append((white1,white2,white3,white4,white5,white6,white7,white8))
    R.append(clss)
    cls=np.array(clss)
    return cls

#Matrix containg all the images pixels
R=[]

#Creating all the classes
cls1=ClassCreator(str("class_1"))
cls2=ClassCreator(str("class_2"))
cls3=ClassCreator(str("class_3"))
cls4=ClassCreator(str("class_4"))
cls5=ClassCreator(str("class_5"))
cls6=ClassCreator(str("class_6"))
cls7=ClassCreator(str("class_7"))
cls8=ClassCreator(str("class_8"))
cls9=ClassCreator(str("class_9"))
cls10=ClassCreator(str("class_10"))
cls11=ClassCreator(str("class_11"))
cls12=ClassCreator(str("class_12"))
cls13=ClassCreator(str("class_13"))
cls14=ClassCreator(str("class_14"))
cls15=ClassCreator(str("class_15"))
cls16=ClassCreator(str("class_16"))
cls17=ClassCreator(str("class_17"))
cls18=ClassCreator(str("class_18"))

cls19=ClassCreator(str("class_19"))
cls20=ClassCreator(str("class_20"))
cls21=ClassCreator(str("class_21"))
cls22=ClassCreator(str("class_22"))
cls23=ClassCreator(str("class_23"))
cls24=ClassCreator(str("class_24"))
cls25=ClassCreator(str("class_25"))
cls26=ClassCreator(str("class_26"))
cls27=ClassCreator(str("class_27"))
cls28=ClassCreator(str("class_28"))
cls29=ClassCreator(str("class_29"))
cls30=ClassCreator(str("class_30"))
cls31=ClassCreator(str("class_31"))
cls32=ClassCreator(str("class_32"))
cls33=ClassCreator(str("class_33"))
cls34=ClassCreator(str("class_34"))
cls35=ClassCreator(str("class_35"))
cls36=ClassCreator(str("class_36"))
#Classes successfullycreated



#Finding the maximum value in the all the images
r=np.array(R)
max=np.amax(r)

#Normalising the class geting values betting 0-1
cls1=np.divide(cls1,max)
cls2=np.divide(cls2,max)
cls3=np.divide(cls3,max)
cls4=np.divide(cls4,max)


cls5=np.divide(cls5,max)
cls6=np.divide(cls6,max)
cls7=np.divide(cls7,max)
cls8=np.divide(cls8,max)
cls9=np.divide(cls9,max)
cls10=np.divide(cls10,max)
clss11=np.divide(cls11,max)
cls12=np.divide(cls12,max)
cls13=np.divide(cls13,max)
cls14=np.divide(cls14,max)
cls15=np.divide(cls15,max)
cls16=np.divide(cls16,max)
cls17=np.divide(cls17,max)
cls18=np.divide(cls18,max)
cls19=np.divide(cls19,max)
cls20=np.divide(cls20,max)
cls21=np.divide(cls21,max)
cls22=np.divide(cls22,max)
cls23=np.divide(cls23,max)
cls24=np.divide(cls24,max)
cls25=np.divide(cls25,max)
cls26=np.divide(cls26,max)
cls27=np.divide(cls27,max)
cls28=np.divide(cls28,max)
cls29=np.divide(cls29,max)
cls30=np.divide(cls30,max)
cls31=np.divide(cls31,max)
cls32=np.divide(cls32,max)
cls33=np.divide(cls33,max)
cls34=np.divide(cls34,max)
cls35=np.divide(cls35,max)
cls36=np.divide(cls36,max)
#Class Matixs created 
gamma = 0.85
alpha = 0.14
csize = 2
dim=8

def distance(inp, c, ngroups, dim):
    dif = np.zeros((ngroups, dim))
    for i in range(ngroups):
        dif[i] = inp - c[i]
    dif = np.square(dif)
    sc = np.sum(dif, axis =1)
    return sc
 
def createGroups(data,alpha,n,gamma):
    datan = set(np.arange(n))
    listofGroups = list()
    while(len(datan)!=0):
        remSet = set()
        s = random.sample(datan,1)
        datan -= set(s)
        grp = set(s)
        for e in datan:
            diff = np.zeros((1,dim))
            diff = data[e] - data[s]
            diff = np.square(diff)
            dis = np.sum(diff,axis =1)
            if((gamma*dis>1)==False):
                score = 1 - gamma*dis
                if(score > alpha):
                    grp.add(e)
                    remSet.add(e)
        datan -= remSet
        listofGroups.append(grp)
    return listofGroups

def createPrototype(listofGroups,data):
    prototypemat = np.zeros((len(listofGroups), dim))
    i = 0
    for grp in listofGroups:
        j=0
        for e in grp:
            prototypemat[i] += data[j]
            j += 1
        prototypemat[i] = prototypemat[i]/j
        i += 1
    return prototypemat

def predictedClass(newData, prototypemat1, prototypemat2,prototypemat3):
    dis1 = distance(newData, prototypemat1, len(prototypemat1),dim)
    dis2 = distance(newData, prototypemat2, len(prototypemat2),dim)
    dis3 = distance(newData, prototypemat3, len(prototypemat3),dim)
    d1 = min(dis1)
    d2 = min(dis2)
    d3 = min(dis3)
    print(d1)
    print(d2)
    print(d3)
    
"""    if(d1<d2 and d1<d3):
            print("Sample belongs to Class 1 ")
    else:
        if(d2<d3):
            print("Sample belongs to Class 2 ")
        else:
            print("Sample belongs to Class 3 ")
    if(d1>d2):
        print("Sample belongs to class 2")
    else:
        print("Sample belongs to class 1")"""


distan=[]
i=1
#CreatingThepredictors
def predictClass(newData, prototypemat):
    global i
    dis1 = distance(newData, prototypemat, len(prototypemat),dim)
    d=min(dis1)
    distan.append(d)
    i=i+1
    

#Creating Class Groups
lGroups1 = createGroups(cls1, alpha, dim, gamma)
lGroups2 = createGroups(cls2, alpha, dim, gamma)
lGroups3 = createGroups(cls3, alpha, dim, gamma)
lGroups4 = createGroups(cls4, alpha, dim, gamma)
lGroups5 = createGroups(cls5, alpha, dim, gamma)
lGroups6 = createGroups(cls6, alpha, dim, gamma)
lGroups7 = createGroups(cls7, alpha, dim, gamma)
lGroups8 = createGroups(cls8, alpha, dim, gamma)
lGroups9 = createGroups(cls9, alpha, dim, gamma)
lGroups10 = createGroups(cls10, alpha, dim, gamma)
lGroups11 = createGroups(cls11, alpha, dim, gamma)
lGroups12 = createGroups(cls12, alpha, dim, gamma)
lGroups13 = createGroups(cls13, alpha, dim, gamma)
lGroups14 = createGroups(cls14, alpha, dim, gamma)
lGroups15 = createGroups(cls15, alpha, dim, gamma)
lGroups16 = createGroups(cls16, alpha, dim, gamma)
lGroups17 = createGroups(cls17, alpha, dim, gamma)
lGroups18 = createGroups(cls18, alpha, dim, gamma)
lGroups19 = createGroups(cls19, alpha, dim, gamma)
lGroups20 = createGroups(cls20, alpha, dim, gamma)
lGroups21 = createGroups(cls21, alpha, dim, gamma)
lGroups22 = createGroups(cls22, alpha, dim, gamma)
lGroups23 = createGroups(cls23, alpha, dim, gamma)
lGroups24 = createGroups(cls24, alpha, dim, gamma)
lGroups25 = createGroups(cls25, alpha, dim, gamma)
lGroups26 = createGroups(cls26, alpha, dim, gamma)
lGroups27 = createGroups(cls27, alpha, dim, gamma)
lGroups28 = createGroups(cls28, alpha, dim, gamma)
lGroups29 = createGroups(cls29, alpha, dim, gamma)
lGroups30 = createGroups(cls30, alpha, dim, gamma)
lGroups31 = createGroups(cls31, alpha, dim, gamma)
lGroups32 = createGroups(cls32, alpha, dim, gamma)
lGroups33 = createGroups(cls33, alpha, dim, gamma)
lGroups34 = createGroups(cls34, alpha, dim, gamma)
lGroups35 = createGroups(cls35, alpha, dim, gamma)
lGroups36 = createGroups(cls36, alpha, dim, gamma)
#Groups Created


#Creating the protoypes for each class
proMat1 = createPrototype(lGroups1, cls1)
proMat2 = createPrototype(lGroups2, cls2)
proMat3 = createPrototype(lGroups3, cls3)
proMat4 = createPrototype(lGroups4, cls4)
proMat5 = createPrototype(lGroups5, cls5)
proMat6 = createPrototype(lGroups6, cls6)
proMat7 = createPrototype(lGroups7, cls7)
proMat8 = createPrototype(lGroups8, cls8)
proMat9 = createPrototype(lGroups9, cls9)
proMat10 = createPrototype(lGroups10, cls10)
proMat11 = createPrototype(lGroups11, cls11)
proMat12 = createPrototype(lGroups12, cls12)
proMat13 = createPrototype(lGroups13, cls13)
proMat14 = createPrototype(lGroups14, cls14)
proMat15 = createPrototype(lGroups15, cls15)
proMat16 = createPrototype(lGroups16, cls16)
proMat17 = createPrototype(lGroups17, cls17)
proMat18 = createPrototype(lGroups18, cls18)
proMat19 = createPrototype(lGroups19, cls19)
proMat20 = createPrototype(lGroups20, cls20)
proMat21 = createPrototype(lGroups21, cls21)
proMat22 = createPrototype(lGroups22, cls22)
proMat23 = createPrototype(lGroups23, cls23)
proMat24 = createPrototype(lGroups24, cls24)
proMat25 = createPrototype(lGroups25, cls25)
proMat26 = createPrototype(lGroups26, cls26)
proMat27 = createPrototype(lGroups27, cls27)
proMat28 = createPrototype(lGroups28, cls28)
proMat29 = createPrototype(lGroups29, cls29)
proMat30 = createPrototype(lGroups30, cls30)
proMat31 = createPrototype(lGroups31, cls31)
proMat32 = createPrototype(lGroups32, cls32)
proMat33 = createPrototype(lGroups33, cls33)
proMat34 = createPrototype(lGroups34, cls34)
proMat35 = createPrototype(lGroups35, cls35)
proMat36 = createPrototype(lGroups36, cls36)
#ProtoType For Class Created


inpt=InputCreator("D:\\dataset\\class_2\\image1.bmp")
inpt=np.divide(inpt,max)
print(inpt)
#inpt=[ 0.55334377 , 0.48646835 , 0.45873406 , 0.65801834 , 0.95325431 , 0.75620667,
#  0.56296131 , 0.62267949]
#input_pattern = np.random.rand(1,int(dim))
#print("Input pattern for test is : ")
#print(input_pattern)

#Creating the pred
predictClass(inpt, proMat1)
predictClass(inpt, proMat2)
predictClass(inpt, proMat3)
predictClass(inpt, proMat4)
predictClass(inpt, proMat5)
predictClass(inpt, proMat6)
predictClass(inpt, proMat7)
predictClass(inpt, proMat8)
predictClass(inpt, proMat9)
predictClass(inpt, proMat10)
predictClass(inpt, proMat11)
predictClass(inpt, proMat12)
predictClass(inpt, proMat13)
predictClass(inpt, proMat14)
predictClass(inpt, proMat15)
predictClass(inpt, proMat16)
predictClass(inpt, proMat17)
predictClass(inpt, proMat18)
predictClass(inpt, proMat19)
predictClass(inpt, proMat20)
predictClass(inpt, proMat21)
predictClass(inpt, proMat22)
predictClass(inpt, proMat23)
predictClass(inpt, proMat24)
predictClass(inpt, proMat25)
predictClass(inpt, proMat26)
predictClass(inpt, proMat27)
predictClass(inpt, proMat28)
predictClass(inpt, proMat29)
predictClass(inpt, proMat30)
predictClass(inpt, proMat31)
predictClass(inpt, proMat32)
predictClass(inpt, proMat33)
predictClass(inpt, proMat34)
predictClass(inpt, proMat35)
predictClass(inpt, proMat36)

#Getting the class index
distanc=np.array(distan)
mini=np.argmin(distanc)

print("Sample belongs to " + str(mini+1))
    






      