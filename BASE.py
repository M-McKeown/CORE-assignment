from re import sub
import sys

def BASE(FileName):
    FileName = "%s.seq" % FileName #We take user filename input and then replace %s location to create our .seq file.
    infile = open(FileName, 'r')  #Reading our file name
    for line in infile:
        mydata= (line.strip('\n')) #We are takihg the string of numbers from the file name and also removing the string \n from the line via .strip()
    infile.close()

    A = len(sub("[G,C,T]", "", mydata)) #Here we are removing the other base pairs using regex sub
    G = len(sub("[C,A,T]", "", mydata)) #and then taking the length to count the number of desired base pairs
    C = len(sub("[G,A,T]", "", mydata))
    T = len(sub("[G,C,A]", "", mydata))

    print(str(A) +"," + str(G) + "," + str(C) + "," + str(T)) #Here we are outputting to the screen the for numbers corresponding to A,G,C,T which is separated by commas

    FileName=FileName.removesuffix(".seq") #Removing the .seq from the previous file so below we can save it as a .count
    FileName = "%s.count" % FileName
    outfile = open(FileName, 'w') #Writing a new file name with the base pairs counted
    outfile.write(str(A) +"," + str(G) + "," + str(C) + "," + str(T) + "\n")
    outfile.close()

BASE(FileName=sys.argv[1]) #Asking user input for their file name to analyze
