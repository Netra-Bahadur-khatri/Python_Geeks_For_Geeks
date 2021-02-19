

# Taking an multiple inputs in python 
# Geeks for Geeks
x,y,z = input("Enter three values ").split()
print("The number of boys in Sec F is ",x )
print("The number of boys in Sec F is ",y)
print("The total number of students in Sec F ",z)
print()

# Taking an multiple inputs in python 
# and type casting using an list function i.e. list()

a = list(map(int, input("Enter any numbers: ").split()))
print("The list of students in The British college is ",a)


# taking an multiple inputs from an users using an List Comprehension:
m,n,o = [int(a) for a in input("Enter three numbers ").split()]
print("The first Number is {}, the second number is {}, and the last one third Number is {}".format(m,n,o))
print()


# Taking an multiple inputs from an users and returning this into an List
q = [int(y) for y in input("Enter multiple number to store into an list: ").split()]
print("The multiple numbers in the list format is ",q)

# Takinga n multiple inputs or numbers from an users and printing them in list format with comma separated
p = [int(d) for d in input("Enter number from 1 to 10: ").split(",")]
print("The number in list format with comma separated is ")
print(p)