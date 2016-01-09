#This file takes an input file "inp.txt" and scramble it using mapping.The scrambled text is written in scrambled_text file.
filename="inp.txt"
outfile=open("scrambled.txt","w")
mapping ={'a':'c','b':'p','c':'q','d':'m','e':'z','f':'y','g':'h','h':'a','i':'s','j':'o','k':'b','l':'t','m':'n','n':'y','o':'u','p':'v','q':'w','r':'i','s':'d','t':'f','u':'e','v':'l','w':'j','x':'k','y':'g','z':'r',' ':' '}


with open(filename) as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    sc = mapping[c]  
    outfile.write(sc)  
 
outfile.close()