import numpy as np
import random
import math
from string import maketrans
from random import shuffle,randrange

def score(ciphertext,key,key1,M):
    ciphertext=transform(ciphertext,key,key1)
    size=len(ciphertext)
    scr=0.0
    for i in xrange(size-1):    
        scr=scr+M[d[ciphertext[i]]][d[ciphertext[i+1]]]
    return scr    

def swap(key):
   i=randrange(0,27)
   j=randrange(0,27)
   while i==j:
     j=randrange(0,27)
   key[i],key[j]=key[j],key[i]
   return key



def transform(ciphertext,key,key1):
     key1="".join(key1)
     return ciphertext.translate(maketrans("".join(key),key1))



def search(ciphertext,M,key,key1,trials=10000):
#-------calculate plausability--------------
     m=0
     for k in xrange(trials): 
            oldcipher=ciphertext
            oldscore=score(ciphertext,key,key1,M)
            newkey=swap(key[:])
            newscore=score(ciphertext,newkey,key1,M)
            #print "newscore=",newscore
            #print "oldscore=",oldscore
            if newscore > oldscore:
                key=newkey[:]
            else:
                 val=newscore-oldscore
                 val=min(0,val)
                 toss=math.log(random.random())
                 if val > toss:
                    key=newkey[:]
                 else:
                    ciphertext=oldcipher
            if k==2000*m:
               print transform(ciphertext,key,key1) 
               print "------------------------------------------------------------------------------------------------------------------------------------------"
               m=m+1 
     return key         
      


d={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21
,'w':22,'x':23,'y':24,'z':25,' ':26}

key=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
key1=['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a',' ']

M=np.loadtxt("M.txt")

for i in xrange(27):
     for j in xrange(27):
          if M[i][j]==0:
              M[i][j]=0.0000001
              M[i][j]=math.log(M[i][j])
          else:
              M[i][j]=math.log(M[i][j])


ciphertext=open("scrambled_text","r").readlines()
ciphertext=''.join(ciphertext)
ciphertext=ciphertext.replace('\n',' ')
ciphertext=transform(ciphertext,key,key1)
print "scrambled text=",ciphertext
originalcipher=ciphertext

if __name__=='__main__':
      trials=20000
      bestkey=search(ciphertext,M,key,key,trials)
      plaintext=transform(originalcipher,bestkey,key)
      print plaintext
      

    
