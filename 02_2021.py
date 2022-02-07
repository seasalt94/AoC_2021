# Day 2: Dive!
# Objectives:
# Part 1:   Calculate the horizontal position and depth you would have after following the planned 
#           course. What do you get if you multiply your final horizontal position by your final 
#           depth?
#               - forward X increases the horizontal position by X units.
#               - down X increases the depth by X units.
#               - up X decreases the depth by X units.
#
# Part 2:   Based on your calculations, the planned course doesn't seem to make any sense. You find 
#           the submarine manual and discover that the process is actually slightly more 
#           complicated.In addition to horizontal position and depth, you'll also need to track a
#           third value, aim, which also starts at 0. The commands also mean something entirely 
#           different than you first thought:
#               - down X increases your aim by X units.
#               - up X decreases your aim by X units.
#               - forward X does two things:
#                   + It increases your horizontal position by X units.
#                   + It increases your depth by your aim multiplied by X.



file=open(r"C:\Users\Garrett\Documents\Python\Advent of Code\AoC_2021\Input_files\02_2021_input.txt","r")

# Function for Part One
def partOne():
    # Initialize positions
    horPos=0
    depth=0

    for line in file:
        line=line.rstrip()
        # Find the number after the space and save it as value
        sPos=line.find(" ")
        value=int(line[sPos+1:])
        # Evaluate new positions
        if line.startswith("forward"):
            horPos=horPos+value
        if line.startswith("down"):
            depth=depth+value
        if line.startswith("up"):
            depth=depth-value
    print("Solutions to Part One:")
    print("Final Depth:",depth)
    print("Final Horizontal distance:",horPos)
    print("Final Depth * Hor:",depth*horPos)

# Function for Part Two
def partTwo():
    # Initialize Variables:
    aim=0
    depth=0
    horPos=0

    for line in file:
        line=line.rstrip()
    #   Find the number after the space and save it as value
        sPos=line.find(" ")
        value=int(line[sPos+1:])

        # Evaluate new positions
        if line.startswith("forward"):
            horPos=horPos+value
            depth=depth+aim*value
        if line.startswith("down"):
            aim=aim+value
        if line.startswith("up"):
            aim=aim-value
    print("Solutions to Part Two:")
    print("Final Depth:", depth)
    print("Final Horizontal Distance:",horPos)
    print("Final Depth * Horizontal Distance:",depth*horPos)

run=int(input('''
Which part would you like solutions for?
Please type 1 or 2.
'''))
if run==1:
    partOne()
if run==2:
    partTwo()
