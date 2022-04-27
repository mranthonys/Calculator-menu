#Calculate the Avg and Sum of 3 numbers
def give_avg(val1, val2, val3):
    return(val1+val2+val3)/3 #finds the sum& average of 3 numbers

#Find the Minimum of the three numbers
def give_min(val1, val2, val3):
    if(val1 < val2 and val1 < val3):
        return val1
    elif(val2 < val1 and val2 < val3):
        return val2
    else:
        return val3

#find the max of 3 numbers
def give_max(val1, val2, val3):
    if(val1 > val2 and val1 > val3):
        return val1
    elif(val2 > val1 and val2 > val3):
        return val2
    else: return val3

#Reading 3 Scores:
val1 = int(input("First Score:"))
val2 = int(input("Second Score:"))
val3 = int(input("Third Score:"))

#The Menu Options
print("Average")
print("Biggest")
print("Smallest")
print("Stop")

choice = int(input("Make Selection: "))

while choice!=4:
    if(choice == 1):
        newAvg = give_avg(val1, val2, val3)
        print("The average is:", newAvg)
        break #ends the loop
    
    elif(choice == 2):
        newMax = give_max(val1, val2, val3)
        print("The Biggest is:", newMax)
        break #ends the loop
    
    elif(choice == 3):
        giveSmall = give_min(val1, val2, val3)
        print("The Smallesr is:", giveSmall)
        break #ends the loop
    else:
        choice


#I had difficulty figuring out how to end the loop
# and restart the menu options. I would really appreciate
# some feedback and a solution! 
