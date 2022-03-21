#!/bin/bash/env python

Var1=$1 #Input 1 is to determine file name
Var2=$2 #Input 2 is to determine number of base pairs in the sequence

for Count in {0..100} #For loop to generate 100 input files
do

	python DNAgen.py $Var1$Count $Var2 #Using DNAgen.py to create a FASTA file with Var1 + Var2
	python BASE.py $Var1$Count #Subsequently reading FASTA file via BASE.py to create .count files
done	

cat *.count > $Var1.csv #Compiles all the .count files into 1 .csv

Rscript 4Column_Reader.r #Passing the generated .csv file into R
