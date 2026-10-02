"""
Name: Annie Lischer
Peers: N/A
References: N/A
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    
    for idx in range ( len(grades) ):
        #asks for a number
        num=input("Give me the next grade in [0 to 10]:")
        
        #checks if num is a digit. If it is not it prints an error and ends the code
        if num.isdigit()==False:
            print("Error in read_five_ints: input string is not for an integer")
            exit()
        
        #now we know num is a digit so we can cast it as an int
        num=int(num)
        
        #checks if num is in range. If it is not it prints an error and ends the code
        if num>10 or num<0:
            print("Error in read_five_ints: input integer outside of range")
            exit()
        
        #places num into grades
        grades[idx] = num


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    #recieving user input
    choice=input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")
    
    #if user choose "a" it calculates and returns the Mean
    if choice == "a":
        print("picked: Mean")
        avg = statistics.mean(grades)
        return avg
    
    #if user choose "b" it calculates and returns the Median
    elif choice == "b":
        print("picked: Median")
        avg = statistics.median(grades)
        return avg
    
    #if user choose "c" it calculates and returns the Mode
    elif choice == "c":
        print("picked: Mode")
        avg = statistics.mode(grades)
        return avg
    
    #if none of the above apply it returns an error message and ends the code
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        exit()

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    #receiving user input
    option=input("Pick '1' for print average, or '2' for plot average: ")
    
    #if user chooses option 1 calls relevant func
    if option=="1":
        print_list_and_average(average)
    
    #if user chooses option 2 calls relevant func
    elif option=="2":
        plot_grades(average)
    
    #if none of the above apply it returns an error message and ends the code
    else:
        print("Error in pick_visualization: incorrect option picked")
        exit()


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
