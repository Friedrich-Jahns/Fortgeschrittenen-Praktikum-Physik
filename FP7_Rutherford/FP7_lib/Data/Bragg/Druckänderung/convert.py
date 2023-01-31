import string
import math
import os
data=[]
comment=[]


def readFile(filename):
    del data[:]
    del comment[:]
    infile=open(filename, "r")


    for line in infile:
        if(line[0].isdigit()):
            numbers=string.split(line[:-1], ",")
            for i in numbers:

                data.append(int(i))
                
            
        else:    
            comment.append("#"+line)

    infile.close()




def writeFile(outfilename):


    outfile2=open(outfilename, "w")
    for i in comment:
        
        outfile2.write(i)
    for i  in range(len(data)):
        outfile2.write(str(i)+"\t"+str(data[i])+"\t"+str(math.sqrt(float(data[i])))+"\n")
    outfile2.close()

def dataFilter():
    for i in range(32, len(data)-1, 32):
            data[i]=(data[i-1]+data[i+1])/2






filelist=os.listdir("./")


outfile=open("plot.gpt", "w")

outfile.write("set xrange [2:]\n")

for item in filelist:
    print item
    if (len(item)>4 and item[-4:]==".SPC"):
        print "Processing "+item

        out=item[:-4]+".csv"
		
		
        readFile(item)
        #dataFilter()
        writeFile(out)

        outfile.write("plot \'"+out+"\' using 1:2 title \'"
                      +out[:-4]+"\' with steps\n"
                      +"pause -1\n\n")

        
outfile.close()
                      

