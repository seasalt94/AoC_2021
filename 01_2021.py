# Day 1: Sonar Sweep
# Objectives:
# Part 1:   The first order of business is to figure out how quickly the depth increases, 
#           just so you know what you're dealing with - you never know if the keys will get 
#           carried into deeper water by an ocean current or a fish or something. To do this, 
#           count the number of times a depth measurement increases from the previous measurement. 
#           (There is no measurement before the first measurement.)
#
# Part 2:   Your goal now is to count the number of times the sum of measurements in this sliding 
#           window increases from the previous sum.

# Initialize variables
count=0
sumCount=0
fList=[]
sumList=[]

# Read from file and generate list
file=open(r"C:\Users\Garrett\Documents\Python\Advent of Code\AoC_2021\Input_files\01_2021_input.txt","r")
for line in file:
    line=line.rstrip()
    fList.append(int(line))

# Loop through list and increase count when the current value is greater than the previous value
for i in range(len(fList)):
    if fList[i]>fList[i-1]:
        count=count+1
#        print(fList[i], "(Increase)")
    else: print(fList[i])
print("Total increases:",count)

# Loop through list and generate new 3-value rolling sums in a new list
# Exclude the last two digits because 
for i in range(len(fList)-2):
    sumList.append(sum(fList[i:i+3]))
    if sumList[i]>sumList[i-1]:
        sumCount=sumCount+1
        print(sumCount,"(Increase)")
    else: print(sumList[i])

print("Total rolling sum increases:", sumCount)