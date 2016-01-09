#This file parse the input file "corpus.txt" provided in the folder and calculate the character statistics from the provided corpus. The statistics is written to "M.txt" file.
#The parsed text is written to parsed.txt file.

import numpy as np


filew=open("parsed.txt","w")
filer=open("corpus.txt","r")

text=filer.readlines()
text=''.join(text)
#print text
#text="ab ab bc"
punctuation = '!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`1234567890'
for marker in punctuation:
      text = text.replace(marker, "").lower()
      text=text.replace('\n',' ')
      text=text.replace('  ',' ')

#-------------converting into bigrams----------------------------------------
bigrams=[]
for i in xrange(len(text)-1):
    bigram=text[i]+text[i+1]
    bigrams.append(bigram)
   


#print bigrams

dict={0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',
11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v'
,22:'w',23:'x',24:'y',25:'z',26:' '}

M=np.zeros(shape=(27,27))

#------------------------calculate transition matrix--------------
for i in xrange(27):
    for j in xrange(27):
         char1=dict[i]
         char2=dict[j]
         #print char1,char2
         elem=char1+char2
         #print elem
         count1=0
         count2=0
         for k in bigrams:
             if k==elem:
                #print k,"yes"
                count1=count1+1
             if k[0]==char1:
                #print k[0],"yes"
                count2=count2+1
         if count1==0 or count2==0:     
             M[i][j]=0
         else:     
             M[i][j]=float(count1)/count2;


np.savetxt('M.txt',M,fmt='%.8f')
filew.write(text);


