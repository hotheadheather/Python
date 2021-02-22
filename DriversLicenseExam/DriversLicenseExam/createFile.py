# Program to write to a file 
# Susan Wilson
# 10/19/20

def main():
    playAgain = 'y'
    employeeFile = init()
    while( playAgain == "y"):
      iName = getName()
      iAge = getAge()
      output (iName, iAge, employeeFile)
      playAgain = input("Would you like to enter another? y/n ")
    closing(employeeFile)

def closing(employeeFile):
    employeeFile.close()

def output(iName, iAge, employeeFile):
    employeeFile.write(format(iName, "20s") +  
                       format(iAge, "2d") + ("\n"))

def getName():
    valid = False
    while valid == False: 
        iName = input("Enter name: ")
        if iName.strip() != "":
            valid = True
        else:
            print("Error. Name Required:")
    return iName 

def getAge():
    valid = False
    while valid == False:
        try:
            iAge = int(input("Enter age: "))
            valid = True
        except:
            print("Error.  Invalid Age.")
    return iAge

def init():    
    try:
        # a = append
        # w = write
        employeeFile = open(r'c:\python03\employee.dat', 'a')
    except IOError:
        print("File Error. Program terminated.")
        exit(0)
    return (employeeFile)

main()










