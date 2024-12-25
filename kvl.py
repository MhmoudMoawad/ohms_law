#Program will use KVL to find the voltage of all componets in a circuit.
import os


while True:
    os.system("cls")
    print("Hello, welcome to the KVL calculator\n")
    print("What type of circuit are you working with?: ")
    print("1.Series\n")
    print("2.Parellel\n")
    print("3.Series Parellel\n")
    print("0.Exit\n")

    option = int(input("Enter your selection: "))
    
    if option == 1:
        
        #The user will input the values of the componets in the circut
        source = float(input("What is the source value of the circuit ?: ")) 
        print("Source Value = ", source, "V")
        num_resistors = int(input("How many resistors?: "))
        resistor_values = []
        for i in range (1, num_resistors + 1):
            value = float(input(f"\nEnter the value for resistor {i} (in Ω): ")) 
            resistor_values.append(value)
        total_resistance = sum(resistor_values)
        
        
        
        current = input("\nDo you know the current value? Y(y) or N(n): ")
        if current == "Y" or current == "y":
            amp_value = float(input("\nWhat is the current value?: "))
            print ("\nVolatage: ", source,)
            print("Current: ", amp_value)
            print("List of resistors:")
            for idx, value in enumerate(resistor_values, start = 1):
                print(f"{idx}. {value} Ω\n")
            print(f"Total resistance: {total_resistance} Ω")     
            input("Press any key to continue")
        
        
        elif current == "N" or current == "n": 
            print("To calcualte the current we need Voltage(V) divided by Resistance Total(R).")
            print("The formula is I = V/R")
            calc_current = source / total_resistance
            print("Current = ", calc_current, "A\n")
            print("The formula for total resistance: RT = R1 + R2 + R3 ... ")
            print(f"Total resistance: {total_resistance} Ω")
            input("Press any key to continue")
            
              
        #Todo: I will need to add the calculations
        
            
        
    elif option == 2:
        source = float(input("How what is the source value of the circuit?: "))
        print("Source value = ", source, " V")
        
        parellel_res = int(input("How many reisistors are in parellel?: "))
        resistor_values = []
        for i in range (1, parellel_res + 1):
            value = float(input(f"\nEnter the value for resistor {i} (in Ω): ")) 
            resistor_values.append(value)
        #total_resistance = sum(resistor_values)
        total_resistance = 1/sum([1/i for i in resistor_values])
        print("The total resistance for this parellel circuit = ", total_resistance, " Ω")
        
        input("Press any key to continue.")
        
          
    elif option == 3:
        source = float(input("How what is the source value of the circuit?: "))
        num_resistors = int(input("How many resistors?: "))
        print("Source value = ", source, " V")
        
        
        
        
    
    elif option == 0:
        print("Exit")
        break

    
    
    
    
#    source = float(input("How what is the source value of the circuit?: "))
#    num_resistors = int(input("How many resistors?: "))
#    out = [list() for i in range(num_resistors)]
#    val_resistors = float(num_resistors)
#    more_comp = input("Are there any other components? Y(y) or N(n)\n")
#
#    if more_comp == "y" or "Y":
#        print ("What other componets do you have in your circuit?")
#        print("1. Resistor")
#        print("2. Inductor")
#        print("3. Capacitor")
#
#    elif more_comp == "n" or "N":
#        print("We will start calculations")
#
#    else:
#        print("Exit")
    
