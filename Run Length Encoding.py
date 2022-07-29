# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:56:08 2020

@author: AEBEL MATHEW
"""


import cv2
import os
import file

        
class Node:
    def __init__(self,count=None):
        self.count=count
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
# Print the linked list
    def listprint(self):
        printval = self.headval
        printval = printval.nextval
        s=""
        while printval is not None:
            s=s+","+str(printval.count)
            printval = printval.nextval
        return s
    def AtEnd(self,newcount):
        NewNode=Node(newcount)
        ptr=self.headval
        while(ptr.nextval is not None):
            ptr=ptr.nextval
        NewNode.nextval=None
        ptr.nextval=NewNode


pth=get_file()
img=cv2.imread(pth)
dim=img.shape
a=str(dim[1])
for i in range(0,dim[0]):
    R= SLinkedList()
    R.headval = Node(0)
    r=255
    cr=0
    for j in range(0,dim[1]):
        if(img[i][j][0]!=r):
            R.AtEnd(cr)
            r=img[i][j][0]
            cr=0
        cr=cr+1
    R.AtEnd(cr)
    a=a+R.listprint()
file=open('BinaryImage.bin','w+')
file.write(a)
print ("Written to file BinaryImage.bin")
size1 = os. stat(pth).st_size
size2 = os.stat("BinaryImage.bin").st_size
print("Compression ratio = ", (size1-size2)/size1 *100)
