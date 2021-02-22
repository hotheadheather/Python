#Lab 5 - Calculate  the total of a paint job  including cost of paint and square footage
# Author: Heather Whittlesey
#10/7/19

#input is the sq ft of wall space and cost per gallon
#calc the labor cost

 #How many square feet do you want to paint?
 #What is the price per gallon?

 #112sq ft = 8 hr 
 #1hr = 35.00

PAINTLABOR = 35

def main():
    galsNeeded = int(input('How much square footage do you need to paint? '))
    galsNeeded = galsNeeded / 112
    print('The total gallons you need is', format(galsNeeded, ',.2f'))
    paintprice = paint(galsNeeded)
    labor = laborprice(galsNeeded)
    total = paintprice + labor
    print('The total amount of your project will cost $', format(total,',.2f'))





def paint(galsNeeded):
    paintprice = float(input('How much is the price for gallon? '))
    paintprice = paintprice * galsNeeded

    print('The amount you will pay for paint is $', format(paintprice, ',.2f'))
    return paintprice

def laborprice(galsNeeded):
    labor = galsNeeded * 8 * PAINTLABOR
    print('The cost of labor for the project $', format(labor, ',.2f'))
    return labor 


    

    



main()



        



