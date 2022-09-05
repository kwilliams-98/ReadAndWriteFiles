#this will print customers and will only advance one you hit the enter key.
# 
#  
#import csv
import csv

#define main

def main():
    #open file
    infile = open('customers.csv', 'r')

    #read contents into csv object
    csvfile = csv.reader(infile, delimiter = ',')
    
    #skip the first row

    next(csvfile)

    #build for loop 
    for record in csvfile: 
        print('ID:', record[0]) 
        print('First Name:', record[1])
        print('Last Name:', record[2])
        print('City:', record[3]) 
        print('Country:', record [4])
        print('Phone', record[5])
        
        #establish input

        input()
#call main 

main()