from gui import ui_elec_calc as ui
#
#=======================================================================================================
#
#Program will calcualte current, voltage and resistance
def calc_voltage(current:float, resistance: float)->float:
    """
        This function calculates voltage for a given parameter
    Args:
        current (float): _description_
        resistance (float): _description_

    Returns:
        float: _description_
    """ 
    voltage = current * resistance
    return voltage
#
#-------------------------------------------------------------------------
#
def calc_current(voltage:float, resistance: float)->float:
    """
        this function calculate current for a given parameter
    Args:
        voltage (float): _description_
        resistance (float): _description_

    Returns:
        float: _description_
    """
    current = voltage / resistance
    return current
#
#-------------------------------------------------------------------------
#
def calc_resistance(voltage:float, current:float)->float:
    """
        This function calculates resistance for a given parameter
    Args:
        voltage (float): _description_
        current (float): _description_

    Returns:
        float: _description_
    """
    resistance = voltage / current
    return resistance

def main( ui_mode:str = 'text')->None:
    if ui_mode == 'gui':
        call_back_fns = []
        win_app = ui.WinApp(win_title="Electrical Calculator", call_back_fn = call_back_fns, win_size = '600x400')
        win_app.mainloop()
    elif ui_mode == 'text':
        while True:    
            print("Which value are you trying to calculate? \n")
            print("1.Voltage\n")
            print("2.Current\n")
            print("3.Resistance\n")
            print("0.Exit\n")
            
            
            option = int(input("Enter your selection: "))

            if option == 1:
                #TODO [x] create function for calculating voltage
                c = float(input("\nEnter the Current value (A): "))
                r = float(input("\nEnter the Resistance value: (Ω)"))
                
                # voltage = current * resistance
                v = calc_voltage(current = c, resistance = r)
                print(v , " V")
                answer = v
                break
                
            elif option == 2:
                #TODO [x] create function for calculating current
                v = float(input("\nEnter the Voltage value (V): "))
                r = float(input("\nEnter the Resistance value (Ω): "))
                
                
                # current = voltage / resistance
                c = calc_current(voltage = v, resistance = r)
                print(c , " A" )
                answer = c
                break
                        
            elif option == 3:
                #TODO [x] create function for calculating resistance
                v = float(input("\nEnter the Voltage value (V): "))
                c = float(input("\nEnter the Current value (A): "))
                
                
                # resistance = voltage / current
                r = calc_resistance(voltage=v,current=c)
                print(r , " Ω")
                answer = r
                break

            elif option == 0:
                break

#If the number is in decimal form convert to the closest whole number using scientific notation and eginering notation

if __name__== '__main__':
    main(ui_mode="text")
    
