#this program will read the steps.csv file, calculate the average number of steps in a given month, and output 
#the average steps per month and the month name in a new csv file. 

#import csv module 
import csv

#call main
def main():

    #open files
    infile = open('steps.csv', 'r')
    outfile = open('avg._steps.csv', 'w')

    #read contents into csv object
    csvfile = csv.reader(infile, delimiter = ',')

    #skip first row 
    next(csvfile)

    #build for loop 
    
    months = [['1','January'], ['2', 'February'], ['3', 'March'], ['4', 'April'], ['5','May'],['6','June'],['7','July'],['8','August'],['9','September'],['10','October'],['11','November'],['12','December']]

    monthly_counter = 0
    monthly_bin = 0
    daily_counter = 0
    average = 0

    for line in csvfile: 
        monthly_value = line [0]
        daily_value = line [1]
        if monthly_value == months[int(monthly_counter)][0]: 
            monthly_bin = int(daily_value) + monthly_bin
            daily_counter += 1
        else: 
            average = int(monthly_bin) // int(daily_counter) 
            outfile.write(months[monthly_counter][1] + ':' + ' ' + str(average) + '\n')
            monthly_counter += 1
            daily_counter = 0
            average = 0
            monthly_bin = 0

    
    #close the outfile
    outfile.close()

#call main
main()
