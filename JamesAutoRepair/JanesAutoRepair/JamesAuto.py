
#Author: Heather Whittlesey 
#11/7/2020
#gui that tallies the services provided by an auto shop



from tkinter import * # highlights the Checkbutton

import tkinter # or ... import tkinter


window = tkinter.Tk() 



# define variables that will hold the checked/unchecked values 


oilJob = IntVar()
lubeJob = IntVar()
radiator= IntVar()
transmission = IntVar()
inspection = IntVar()
exhaust = IntVar()
tires = IntVar()
exit = IntVar()


# define the function which will be invoked when any checkbox is toggled on/off:


def display_totCharges():
    total_charges = oilJob.get() + lubeJob.get() + radiator.get() + transmission.get() + inspection.get() + exhaust.get() + tires.get()
    print("")
    print("TOTAL CHARGES: " + str(total_charges)
  
    )


#visuals in the GUI these are the check boxes

oil_button = Checkbutton(window, text = "Oil Change",                   variable = oilJob,          onvalue = 30,  offvalue = 0, command = display_totCharges, height = 1, width = 20)
lube_button = Checkbutton(window, text = "Lube Job",                    variable = lubeJob,         onvalue = 20,  offvalue = 0, command = display_totCharges, height = 1, width = 20)
radiator_button = Checkbutton(window, text = "Radiator Flush",          variable = radiator,        onvalue = 40,  offvalue = 0, command = display_totCharges, height = 1, width = 20)
transmission_button = Checkbutton(window, text = "Transmission Flush",  variable = transmission,    onvalue = 100, offvalue = 0, command = display_totCharges, height = 1, width = 20)
inspection_button = Checkbutton(window, text = "Inspection",            variable = inspection,      onvalue = 35,  offvalue = 0, command = display_totCharges, height = 1, width = 20)
muffler_button = Checkbutton(window, text = "Muffler Replacement",      variable = exhaust,         onvalue = 200, offvalue = 0, command = display_totCharges, height = 1, width = 20)
tire_button = Checkbutton(window, text = "Tire Rotation",               variable = tires,           onvalue = 20,  offvalue = 0, command = display_totCharges, height = 1, width = 20)
quit_button = Checkbutton(window, text = 'Quit',                        variable = exit,            onvalue = 20,  offvalue = 0, command = window.destroy, height = 3, width = 20)



#pack the buttons

oil_button.pack()
lube_button.pack()
radiator_button.pack()
transmission_button.pack()
inspection_button.pack()
muffler_button.pack()
tire_button.pack()
quit_button.pack()

  


window.mainloop()
