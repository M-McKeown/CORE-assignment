import random
import sys

def FASTAfile(FileName,Nb:int):                 #The custom function with FileName and Nb as the parameters
    FileName = "%s.seq" % FileName              #We take user filename input and then replace %s location to create our .seq file.
    outfile = open(FileName, 'w')               #Create file name
    DNA=["G","C","A","T"]                       #Four possible DNA base pairs to choose from
    for i in range(Nb):                         #Input from the user descides the length of the Nb sequence
        outfile.write(random.choice(DNA))       #Random.choice comes from "random" package, allows each of DNA base pairs to be randomly selected from the vector with equal probability
    outfile.close()                             #Close the file
FASTAfile(FileName=sys.argv[1], Nb=int(sys.argv[2])) #Sys.argv allows us to control input via bash/shell script
#Alternative: FASTAfile(FileName=input("Please enter the file name"), Nb=int(input("Please enter the length of the DNA sequence"))) #Ask user input in Python

#To summarize above:
#We have a custom function with parameters FileName and Nb
#We input the FileName and number of base pairs through bash script
#The FileName is taken from the bash script and becomes overwritten with the "%s.seq" % FileName"  where we replace the %s with FileName to generate a .seq file
#Nb taken from the user determines the length of the loop
#The variable "DNA" contains all the possible base pairs to be taken form where random.choice from "random" package picks them with random and equal probability
