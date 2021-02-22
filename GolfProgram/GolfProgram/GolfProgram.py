#Program that reads each player's name and golf score as input
#Save to golf.txt

print(
"""
        ~~  Spring Fork Golf Club  ~~

Save golfers name to a record in a file read the name and golf score into a file. 
Then golfers will be printed for your convenience.
     
      """
      )


outfile = open('golf.dat', 'w')

#Enter input, leave blank to quit program
while True:
    name = input("Player's name(leave blank to quit):")
    if name == "":
        break
    score = input("Player's score:")

#write to file golf.dat
    outfile.write(name + "\n")

    outfile.write(str(score) + "\n")

outfile.close() 



#Golf Scores

# main module/function
def main():

# opens the "golf.txt" file created in the Golf Player Input python
# in read-only mode
    infile = open('golf.txt', 'r')

# reads the player array from the file
    name = infile.readline()

    while name != '':

# reads the score array from the file
        score = infile.readline()

# strip newline from field
        name = name.rstrip('\n')
        score = score.rstrip('\n')
# prints the names and scores
        print(name + " scored a " + score)

# read the name field of next record
        name = infile.readline()

# closes the file    
    infile.close()

# calls main function
main()