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

    ###BUILD A LIST TO LOOP THROUGH! 
    #[[1,January], [2, February], [3, March], [4, April], [5,May],[6,June],[7,July],[8,August],[9,September],[10,October],[11,November],[12,December]]
    monthly_counter = 1
    monthly_average = 0
    daily_counter = 0

    for line in csvfile: 
        monthly_value = int(line [0])
        daily_value = int(line [1])
        if monthly_value == monthly_counter:
            daily_value += monthly_average
            daily_counter += 1
            #outfile.write(str(daily_value) + '\n')
        else: 
            outfile.write('Month:' + str(monthly_average) + '\n')
            monthly_counter += 1 
    #close the outfile

    outfile.close()

#call main
main()
