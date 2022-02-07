# Day 3: Binary Diagnostic
# Objectives:
# Part 1:   You need to use the binary numbers in the diagnostic report to generate two new binary 
#           numbers (called the gamma rate and the epsilon rate). The power consumption can then be 
#           found by multiplying the gamma rate by the epsilon rate.
#               - The gamma rate is the collection of most common binVals per bit
#               - The epsilon rate is the collection of least common binVals per bit
#
# Part 2:

# Initialize Variables
valList=[]
gamma=[]
epsilon=[]
oneCount=0

# Read from file and generate str list
file=open(r"C:\Users\Garrett\Documents\Python\Advent of Code\AoC_2021\Input_files\03_2021_input.txt","r")
for line in file:
    line=line.rstrip()
    valList.append(line)

# Set binVal equal to the first number in my list so I know length
binVal=valList[0]

 
for i in range(len(binVal)):
    oneCount=0
    # For all lines of file, increase oneCount if there's a 1
    for j in range(len(valList)):
        value=valList[j]
        if value[i]=="1":
            oneCount+=1
    if oneCount>=len(valList)/2:
        gamma.append(1)
        epsilon.append(0)
    else:
        gamma.append(0)
        epsilon.append(1)

# Join gamma and epsilon arrays into string
gamStrings=[str(val) for val in gamma]
gamStr="".join(gamStrings)
epsStrings=[str(val) for val in epsilon]
epsStr="".join(epsStrings)

# Convert binary string to integer values
epsInt=int(epsStr,2)
gamInt=int(gamStr,2)

print("---------------------")
print("Gamma List:",gamma)
print("Gamma String:",gamStr)
print("Gamma Integer:",gamInt,"\n")
print("Epsilon: List",epsilon)
print("Epsilon string:",epsStr)
print("Epsilon integer:",epsInt)
print("Power Consumption:",gamInt*epsInt)
print("---------------------")