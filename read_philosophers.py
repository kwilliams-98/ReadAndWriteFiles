#This program reads and displays the contents of the philosophers.txt file. 

def main(): 
    #Open a file named philosopers.txt
    infile = open("philosophers.txt", 'r')

    #read the file's contents
    ##file_contents = infile.read() [option one; REMOVE ME TO RUN AND COMMENT OUT CURRENT CODE]

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline().rstrip('\n')
    line3 = infile.readline().rstrip('\n')

    #print the data that was read into memory
    ##print(file_contents) [option one; REMOVE ME TO RUN AND COMMENT OUT CURRENT CODE]
    print(line1)
    print(line2)
    print(line3)

    #call the main function

main()

#Note: no need to close the file since we aren't writing to it. You won't get any errors if you run and leave the file open. 
#Note: when you use readline, you would need to remove the '\n' to not have giant spaces in between each line. Since the object is a string, you can use the string methods!