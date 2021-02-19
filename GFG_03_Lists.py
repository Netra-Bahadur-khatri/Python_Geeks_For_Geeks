# List in python:
# Notes: Similar to arrays in other programming languages.
# list need not to be homogenous always.
# List are mutable i.e. can be altered once declared.

List1 = ["Netra", "Jesis",12,34]
print("Original list is")
print(List1)
List1.append(14)
print("After appending an some values to list: ")
print(List1)

"""
TABLE OF CONTENTS IN LIST:
-> Creating a list:
-> Knowing the size of list:
-> Adding an elements in the list:
    Using an append() method
    Using an insert() method
    Usinga an extend() method
-> Accessing elements from the list:
-> Removing Elements from the list:
    Using an remove() method
    Using pop() method
-> Slicing of a list
-> List Methods.

"""
# Creating a List:
List = ["Netra", 13, "45", "What is your hobby ?"]
print("The elements of first List is: ")
print(List[0])
print(List)


# Knowiong the size of the list:
list_size = ["Netra", "Yagya", "Mummy", "Daddy","Radhika"]
print(len(list_size))


# Adding an elements to the list:
List_add_element = ["Netra", "Khatri", "Babarmhal", "Ktm","Evan"]
List_add_element.append("Chris Evan is my favourite actor in hollyhood")
print(List_add_element)


# Using an insert methods to insert somethings in the list:
# insert methods takes an exact two arguments one for indexing and another for elements to which add
List_insert = [1,2,3,4,5,6,7,8,9,10]
List_insert.insert(3,56768)
print(List_insert)


# Adding an elements into an list using an extend()
List_extend = [1,2,3,4,5,"Netra","khatri", "How are you"]
List_extend.extend([12,23,45,67,89,"What's up guys."])
print(List_extend)

# Accessing an elements from the list using an indexing
list_access_name = ["Netra","The British college"]
print("This will access an first elements from the list: ")
print(list_access_name[0])

# Accessing an elements in the list using an negative indexing:
print("Accessing an elements the list using a negative indexing: ")
print(list_access_name[-1])


# Removing all the elements from the given list:
list_remove = ["Hello", "World","Hello_bash", "Hello_mac"]
print("This will remove all the elements from the list: ")
list_remove.remove("Hello")
print(list_remove)

# Removing an elements from the list using an pop() methods
list_pop = ["Hello", "This is pop method", "Here it is used to remove ", "some elements from the list"]
print(list_pop.pop(2))
