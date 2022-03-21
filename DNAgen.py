#Setup
#----------------------------------------------------
import random
import sys

DNA=["A","G","C","T"]   #DNA contains the four possible base pairs
#----------------------------------------------------

#Custom function with FileName and Nb as the parameters
#----------------------------------------------------
def FASTAfile(FileName,Nb:int):
    FileName = "%s.seq" % FileName              #We take user filename input and then replace %s location to create our .seq file.
    outfile = open(FileName, 'w')               #Create and open the file name
    for i in range(Nb):                         #Input from the user descides the length of the Nb sequence
        outfile.write(random.choice(DNA))       #Random.choice comes from "random" package, allows each of DNA base pairs to be randomly selected from the vector with equal probability
    outfile.close()

FASTAfile(FileName=sys.argv[1], Nb=int(sys.argv[2])) #Sys.argv allows us to accept input via bash/shell script
#----------------------------------------------------


#Alternative - User input
#----------------------------------------------------
#FASTAfile(FileName=input("Please enter the file name"), Nb=int(input("Please enter the length of the DNA sequence"))) #Here we are asking user for their input
#----------------------------------------------------

#Summary
#----------------------------------------------------
#We have a custom function with parameters FileName and Nb
#We collect the inputs from the bash/shell script
#The FileName is taken from bash/shell script and becomes overwritten with the "%s.seq" % FileName"
# here we replace the %s with FileName to generate a .seq file
#Nb taken from the user determines the length of the loop and sequence
#The variable "DNA" contains all the possible base pairs to be taken form where random.choice from "random" package
#Picks them with random and equal probability
#----------------------------------------------------
