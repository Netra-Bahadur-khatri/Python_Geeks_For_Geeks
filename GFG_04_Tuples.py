# Tuples in python:
# Notes:Immutable python Objects i.e. cannot be changed once declared.
# Most Important: tuples are usually faster than list.
# Indexing present

tuple1 = ("Netra", "jesis", 14,16)
print(tuple1)
print("Printing the first values of the tuples.")
print(tuple1[0])


# Notes: Creation of python tuples without the use of parenthesis is known an Tuple Packing.
# Tuples can be of any datatypes or mixed datatypes.


# Creating an Tuples with the use of the for loop
Tuple1 = ('Geeks')
n = 5
for a in range(int(n)):
    Tuple1 = (Tuple1, )
    print(Tuple1)


 
# Concatenation of tuples
# Slicing of tuples
Tuple2 = (12,13,145,37)
print(Tuple2[::-1])

# Deletion of Tuples
Tuple3 = (0,1,2,3,4,5,6,7,8,9,10)
del Tuple3

print(Tuple3) #this will give an error because Tuple3 has been deleted.


