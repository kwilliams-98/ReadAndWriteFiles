# this program will import the customers.csv file, read it, and create 
# a new file that only includes the full customer name, country, and 
# the total number of customers read from the file at the bottom. 

#import csv module

import csv

#call main

def main():

    #open files

    infile = open('customers.csv', 'r')
    outfile = open ('customer_country.csv', 'w')

    #read contents into csv object
    csvfile = csv.reader(infile, delimiter = ',')


    #create header
    outfile.write('Full Name, Country' + '\n')
    

    #skip the first row

    next(csvfile)

    #create for loop
    
    counter = 1

    for line in csvfile:
        #alt: full_name = line[1] + ' ' + line[2]
        #alt: country = record [4]

        outfile.write(line[1]+ ' ' + line[2] + ',' + ' ' + line[4] + '\n')

        #alt: outfile.write (full_ name + ' ' + country + '\n')

        counter += 1

    outfile.write(' ')
    outfile.write('Total customers:' + ' ' + str(counter))

    #close the outfile
    outfile.close()

#call main
main()