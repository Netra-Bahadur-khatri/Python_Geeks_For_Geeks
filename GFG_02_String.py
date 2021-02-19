# String in python
# Notes: String in python is immutable i.e.it cannot be changed once declared
a = "Netra Bahadur khatri"
print(a)

# Strings are arrays of byte representing an unicode characters.
# Important:--> Python does not have characters data types.
# Individual characters of strings in python can be accessed with the help of indexing i.e. +ve or -ve


# String Slicing in python
# To access the range of characters in the string,for that condition --> Methods of slicing is used.
# Slicing in string is done by using an slicing Operator i.e. colon
name = "Yagya Bahadur Khatri";
print(name[3:13])
print(name[:-2])

# Deletion or updation in the string
# Since string in python is immutable so deletion or updation in the string at python is not allowed.
# but whole string can be delete with the built in delete key i.e. del(). and string can be reassigned to same variables in python.


# Important points:
# Updation of whole string is possible in python
print("\n\n")
string_name = "Netra Bahadur khatri"
print("This will print my name: ")
print(string_name)

print("\n\n")
string_name = "Hello, Yagya Bahadur khatri"
print("This will print my brother name: ")
print(string_name)


# To ignore the escape sequences in the string, we have to used 'r' or 'R', this implies that the string is raw string and escape sequences inside it are be ignored.
print("\n\n")
name_of_my_brother = r"Yagya Bahadur khatri\n\n" # 'r' --> ignored the backslash characters in the string.
print(name_of_my_brother)
print("This will print my brother name as i declare in the string format.")



