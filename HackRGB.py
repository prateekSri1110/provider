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
