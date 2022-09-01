#this program writes my name to the exisitng philosophers.txt file. 

def main():
    #open a file named philosophers/txt 
    outfile = open('philosophers.txt', 'a')

    #write your name
    outfile.write('Kennedy Williams\n') #take note of this notation...a little different!

    #close the file
    outfile.close()

#call main
main()