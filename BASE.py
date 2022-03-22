#Setup
#----------------------------------------------------
from re import sub
import sys
#----------------------------------------------------

#Custum function that analyzes input from DNAgen.py
#----------------------------------------------------
def BASE(FileName):
    FileName = "%s.seq" % FileName #We take user filename input and then replace %s location to read the .seq file from DNAgen.py.
    infile = open(FileName, 'r')
    for line in infile:
        DNA_data= (line.strip('\n')) #We are takihg the string of base pairs from the FileName and also removing the string \n from the line via .strip()
    infile.close() #Close the file because the information is stored onto the DNA_data

    A = len(sub("[G,C,T]", "", DNA_data)) #Removing the unwated base pairs using regex sub
    G = len(sub("[C,A,T]", "", DNA_data)) #and then taking the length to count the number of desired base pairs
    C = len(sub("[G,A,T]", "", DNA_data))
    T = len(sub("[G,C,A]", "", DNA_data))
    print(str(A) +"," + str(G) + "," + str(C) + "," + str(T)) #Output to the screen the for numbers corresponding to A,G,C,T which is separated by commas

    FileName=FileName.removesuffix(".seq") #Removing the .seq from the previous title so below we can save it as a .count
    FileName = "%s.count" % FileName
    outfile = open(FileName, 'w') #Writing a new file name with the base pairs counted
    outfile.write(str(A) +"," + str(G) + "," + str(C) + "," + str(T) + "\n")
    outfile.close()

BASE(FileName=sys.argv[1]) #Taking the user input from the bash/shell script which we generated in DNAgen.py
#----------------------------------------------------


#Summary
#----------------------------------------------------
#We generated .seq files from DNAgen.py where now we are reading the DNA sequence and storing the string on DNA_data.
#The .seq files is closed, then we scan through the DNA_data for the base pairs. Using sub, each unwanted base pair is removed
#which leaves only the desired base pairs in the string. The length of the leftover/modified string counts the number of base pairs.
#The output is printed and then results saved to a FileName.count script by removing the suffix ".seq" of the FileName
#----------------------------------------------------