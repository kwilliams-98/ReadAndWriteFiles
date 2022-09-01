#this file reads the clients.txt file and prints each client one at a time with a sequence number. 

def main(): 
    #Open the file named clients.txt
    infile = open('clients.txt', 'r') #Note: you don't need to use the readline for this. if you use the for loop, it will go through the whole file. 

    #set up your loop 
    seq = 1

    for line in infile: 
        #print(seq, '.', line.rstrip('\n'), sep=''); Note: this was the in-class example! Either one works :) 
        print(str(seq) + '.' + line.rstrip('\n'), sep='')
        seq += 1
    
    #call main 

main()