# Program to read from a file 
# Susan Wilson
# 10/19/20

import datetime

# Global Definitions
oDate = ''
cPctr = 0

def main():
    iRec, employeeFile = init()
    while( iRec != ""):
      cWages = calcs(iRec)
      output (iRec, cWages)
      iRec, employeeFile = read(employeeFile)

def output(iRec, cWages):
    iName = iRec[0:20]
    iId = iRec[20:27]
    iCode = iRec[28:29]
    iHrs = int(iRec[29:34])/100
    print (iName)
    print (cWages)
    print("")

def calcs(iRec):
    cCode = iRec[28:29]
    if cCode == 'J':
        cRate = 12.00
    elif cCode == 'M':
        cRate = 50.66
    else:
        cRate = 35.70
    iHrs = int(iRec[29:34])/100
    cWages = iHrs * cRate
    return cWages


def init():
    global oDate
    employeeFile = open(r'c:\python03\employee.dat', 'r')
    oDate = datetime.datetime.today().strftime('%D')
    hdgs()
    iRec, employeeFile = read(employeeFile)
    return (iRec, employeeFile)

def read(employeeFile):
    iRec = employeeFile.readline()
    return iRec, employeeFile

def hdgs():
    global cPctr
    cPctr = cPctr + 1
    print("Date:", oDate, format(" ", "20s"), "ABC Company", 
          format(" ", "20s"), "Page:", format(cPctr, "2d"))
    print(format(" ", "35s"), "Employee Wages\n")
    print("Name", format(" ", "23s"), "ID", format(" ", "10s"),
          'Hours', format(" ", "8s"), "Rate", 
          format(" ", "8s"), "Wages\n")

main()









