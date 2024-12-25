#Program will calcualte current, voltage and resistance

while True:    
    print("Which value are you trying to calculate? \n")
    print("1.Voltage\n")
    print("2.Current\n")
    print("3.Resistance\n")
    print("0.Exit\n")
    
    
    option = int(input("Enter your selection: "))

    if option == 1:
        c = float(input("\nEnter the Current value (A): "))
        r = float(input("\nEnter the Resistance value: (Ω)"))
        v = c * r
        print(v , " V")
        answer = v
        break
        
    elif option == 2:
        v = float(input("\nEnter the Voltage value (V): "))
        r = float(input("\nEnter the Resistance value (Ω): "))
        c = v / r
        print(c , " A" )
        answer = c
        break
                
    elif option == 3:
        v = float(input("\nEnter the Voltage value (V): "))
        c = float(input("\nEnter the Current value (A): "))
        r = v / c
        print(r , " Ω")
        answer = r
        break

    elif option == 0:
        break


#If the number is in decimal form convert to the closest whole number using scientific notation and eginering notation
