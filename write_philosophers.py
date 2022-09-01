#this program writes three lines of data to a file. 

def main():
    #open a file named philosophers/txt 
    outfile = open('philosophers.txt', 'w')

    #write the names of three philosophers to the file
    #ERROR: don't add any equal signs when writing to close. parentheses are sufficient!
    #Note: You can either create variables or type the strings directly in here 

    name1 = 'John Locke'
    name2 = 'David Hume'
    name3 = 'Edmund Burke'
    
    outfile.write(name1 + '\n') 
    outfile.write(name2 + '\n')
    outfile.write(name3 + '\n')

    #close the file
    outfile.close()

#call main
main()

#ctrl + alt + n is the hotkey to run the file 