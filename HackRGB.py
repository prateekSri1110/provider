#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'mixColors' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY colors
#  2. 2D_INTEGER_ARRAY queries
#

def mixColors(res):
   
    return res
            
        
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    
    dicr={}
    dicb={}
    dicg={}

    for _ in range(n):
        
        a=list(map(int, input().rstrip().split()))
        
        # Pls Help me add try and catch
         
         try:
            
            if(dicr[a[0]][2]>a[1]):
                dicr[a[0]][2]=a[1]
            if(dicr[a[0]][3]>a[2]):
                dicr[a[0]][3]=a[2]
        except:
            dicr[a[0]]=[set([]),set([]),[],[]]
           
            dicr[a[0]][2]=a[1]
            dicr[a[0]][3]=a[2]
            
            
            
        try:
           
            if(dicb[a[1]][2]>a[0]):
                dicb[a[1]][2]=a[0]
            if(dicb[a[1]][3]>a[2]):
                dicb[a[1]][3]=a[2]
        except:
            dicb[a[1]]=[set([]),set([]),[],[]]
            dicb[a[1]][2]=a[0]
            dicb[a[1]][3]=a[2]
        try:
            if(dicg[a[2]][2]>a[0]):
                dicg[a[2]][2]=a[0]
            if(dicg[a[2]][3]>a[1]):
                dicg[a[2]][3]=a[1]
        except:
            dicg[a[2]]=[set([]),set([]),[],[]]
            dicg[a[2]][2]=a[0]
            dicg[a[2]][3]=a[1]
        
        
   
        
        
    # print(dicr,"\n",dicb,"\n",dicg)
            
            

    queries = []
    res=[]
    for iioi in range(q):
        # print(iioi)
        # queries.append(list(map(int, input().rstrip().split())))
        aaaa=list(map(int, input().rstrip().split()))
        
        c=0
        try:
            # print(1)
            ann=(dicr[aaaa[0]][2])
            ann1=(dicr[aaaa[0]][3])
            # print(dic[aaaa[0]][0][0],"  ",aaaa[1],"   ",dic[aaaa[0]][1][0],"  ",aaaa[2])
            
            if(ann<=aaaa[1] and ann1<=aaaa[2]):
                # print(2)
                try:
                    ann2=(dicb[aaaa[1]][2])
                    ann3=(dicb[aaaa[1]][3])
                    
                    # print(3)
                    if(ann2<=aaaa[0] and ann3<=aaaa[2]):
                        # print(4)
                        try:
                            ann4=(dicg[aaaa[2]][2])
                            ann5=(dicg[aaaa[2]][3])
                            
                            # print(5)
                            if(ann4<=aaaa[0] and ann5<=aaaa[1]):
                                # print(6)
                                res.append("YES")
                                c=1
                            else:
                                c=1
                                # print(7)
                                res.append("NO")
                        except:
                            if(c==0):
                                # print(8)
                                res.append("NO")
                                c=1
                    else:
                        if(c==0):
                            # print(9)
                            res.append("NO")
                            c=1
                except:
                    if(c==0):
                        # print(10)
                        res.append("NO")
                        c=1
            else:
                if(c==0):
                    # print(11)
                    res.append("NO")
                    c=1
        except :
            if(c==0):   
                # print(12)
                res.append("NO")
                c=1
        # print(13)

    result = mixColors(res)
    
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
