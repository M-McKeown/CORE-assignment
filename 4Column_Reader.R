#Theme, package and data Setup
#----------------------------------------------------
library(ggplot2) #Package to make the histogram
library(gridExtra) #Package for grid arranging
source("https://bit.ly/theme_pub") #Finding the theme
theme_set(theme_pub()) #Set the theme

setwd("/Users/MMckeown/Desktop/Coding/BIOL812") #Absolute directory pathway setup
Data<-read.csv("./Assignment/DNASeq.csv",header=F) #Reading the .csv file containing 4 columns, header = False because we do not have them
#----------------------------------------------------
#Convert columns to proportions (i.e divide each number by the total for each column)
#----------------------------------------------------
Column1<-Data[1]/sum(Data[1]) 
Column2<-Data[2]/sum(Data[2]) 
Column3<-Data[3]/sum(Data[3]) 
Column4<-Data[4]/sum(Data[4])
Proportions<-data.frame(Column1,Column2,Column3,Column4) #Putting back into a data.frame to combine all the columns into one 2D matrix
names(Proportions)<-c("Adenine","Guanine","Cytosine","Thymine") #Create our own headers for each of the 4 columns
#----------------------------------------------------

#Graphing
#----------------------------------------------------
Hist_Col1<-qplot(x=Adenine, data=Proportions) #Making 4 different histograms
Hist_Col2<-qplot(x=Guanine, data=Proportions)
Hist_Col3<-qplot(x=Cytosine, data=Proportions)
Hist_Col4<-qplot(x=Thymine, data=Proportions)
#----------------------------------------------------

#Output to pdf
#----------------------------------------------------
pdf("4-panel graph.pdf")
grid.arrange(Hist_Col1,Hist_Col2,Hist_Col3,Hist_Col4,nrow=2) #Using the gridExtra package to create a 4-panel graph
dev.off()
#----------------------------------------------------





