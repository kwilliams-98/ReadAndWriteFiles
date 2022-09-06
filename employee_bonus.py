#This program will read the employee pay.csv file and print the details of each employee. 
#Details must include bonus pay (which has to be calculated). The program will pause after each employee. 

#import csv module 
import csv

#define main 
def main():
    
    #open file
    infile = open('EmployeePay.csv', 'r')

    #read contents into a csv object
    csvfile = csv.reader(infile, delimiter = ',')

    #skip the first row
    next(csvfile)

    #build for loop 
    for line in csvfile: 
        print('Employer ID:', line [0])
        print('Full Name:', line[1] + ' ' + line [2])
        print('Salary:', line[3], ',')
        print('Bonus:', line [4])
        totalpay = (float(line[3]) * float(line [4])) + float(line[3])
        print('Total Pay:', format(totalpay, ',.2f'))

        #establish pause
        input()

#call main 
main()