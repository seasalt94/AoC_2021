# Day 3: Binary Diagnostic
# Objectives:
# Part 1:   You need to use the binary numbers in the diagnostic report to generate two new binary 
#           numbers (called the gamma rate and the epsilon rate). The power consumption can then be 
#           found by multiplying the gamma rate by the epsilon rate.
#               - The gamma rate is the collection of most common binVals per bit
#               - The epsilon rate is the collection of least common binVals per bit
#
# Part 2:   Identify the Oxygen Generator Rating and CO2 Scrubber rating by reviewing each line and 
#           determining the most common value for each position.
#               - To find oxygen generator rating, determine the most common value (0 or 1) in the 
#                 current bit position, and keep only numbers with that bit in that position. If 0 
#                 and 1 are equally common, keep values with a 1 in the position being considered.
#               - To find CO2 scrubber rating, determine the least common value (0 or 1) in the 
#                 current bit position, and keep only numbers with that bit in that position. If 0
#                 and 1 are equally common, keep values with a 0 in the position being considered.


valList=[]
# Read from file and generate str list
file=open(r"C:\Users\Garrett\Documents\Python\Advent of Code\AoC_2021\Input_files\03_2021_input.txt","r")
for line in file:
    line=line.rstrip()
    valList.append(line)
# Set binVal equal to the first number in my list so I know length
binVal=valList[0]

def mostCommon(list,pos,type):
    '''
    Returns the most common value for O2 and least common value for CO2 stored in the [pos] 
    position of all values in list.
    Inputs: a list of strings, a column position, and a type for "o"xygen or "c"o2
    '''
    oneCount=0
    zeroCount=0
    for i in range(len(list)):
        value=list[i]
        if value[pos]=="1":
            oneCount+=1
        else:
            zeroCount+=1
    if type=="o":
        if oneCount>=zeroCount:
            return "1"
        elif oneCount<zeroCount:
            return "0"
    else:
        if oneCount>=zeroCount:
            return "0"
        elif oneCount<zeroCount:
            return "1"

# Solution to Part 1
def partOne():
    # Initialize Variables
    gamma=[]
    epsilon=[]
    oneCount=0
    #
    for i in range(len(binVal)):
        oneCount=0
        # For all lines of file, increase oneCount if there's a 1
        for j in range(len(valList)):
            value=valList[j]
            if value[i]=="1":
                oneCount+=1
        # Build out gamma and epsilon lists based on most-common character
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
    print("Epsilon integer:",epsInt,"\n")
    print("Power Consumption:",gamInt*epsInt)
    print("---------------------")

# Solution to Part 2
def partTwo():
    # Generate initial O2 and CO2 lists
    removeList=[]
    oxList=valList
    cList=valList
    remove=0
    # Calculate Oxygen Generator Rating
    for i in range(len(binVal)):
        commonVal=mostCommon(oxList,i,"o")
        #print(f"Column {i}: Common Value: {commonVal}")
        # Loop through file and add values to removeList that should be removed
        for j in range(len(oxList)):
            value=oxList[j]
            if value[i]==str(commonVal):
                #print(f"Row: {j} Value: {value} (keep)")
                continue
            removeList.append(value)
            #print(f"Row: {j} Value: {value} (remove)")
        # Set my new oxList loop to only values that should remain (ie not in removeList)
        oxList=[x for x in oxList if not x in removeList]
        if len(oxList)==1:
            oxRatingStr=oxList[0]
            print(f"Columns needed for complete O2 rating: {i}")
            break

    removeList.clear()
    # Calculate CO2 Generator Rating
    for i in range(len(binVal)):
        commonVal=mostCommon(cList,i,"c")
        #print(f"Column {i}: Common Value: {commonVal}")
        # Loop through file and add values to removeList that should be removed
        for j in range(len(cList)):
            value=cList[j]
            if value[i]==str(commonVal):
                #print(f"Row: {j} Value: {value} (keep)")
                continue
            removeList.append(value)
            #print(f"Row: {j} Value: {value} (remove)")
        # Set my new cList loop to only values that should remain (ie not in removeList)
        cList=[x for x in cList if not x in removeList]
        if len(cList)==1:
            cRatingStr=cList[0]
            print(f"Columns needed for complete CO2 rating: {i} \n")
            break

    print(f"Final O2 rating: {oxRatingStr}")
    print(f"Final CO2 rating: {cRatingStr} \n")
    oxRatingInt=int(oxRatingStr,2)
    cRatingInt=int(cRatingStr,2)

    print("Final O2 * CO2 power consumption:",oxRatingInt*cRatingInt)
    print("---------------------")

partOne()
partTwo()