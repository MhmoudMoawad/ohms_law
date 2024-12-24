#Program will use KVL to find the voltage of all componets in a circuit.


print("Hello, welcome to the KVL calculator\n")
print("What type of circuit are you working with?: ")
print("1.Series\n")
print("2.Parrelel\n")
print("3.Series Parelel\n")
print("0.Exit\n")


source = float(input("How what is the source value of the circuit?: "))
num_resistors = int(input("How many resistors?: "))
