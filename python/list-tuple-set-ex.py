#Creating a list, called my_list, with 3 numbers, the total of which added together should be 100.
my_list = [31, 32, 37]
print(sum(my_list))

#Creating a tuple, called my_tuple, with a single value/element in it
my_tuple = ("single", )
    #Comma at the end is important to signal that this is a tuple and not a math operation

#Creating a set called set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {5, 443, 77, 123, 9, 12, 678, 9, 320}
set2 = {1, 2, 3, 4, 11, 12, 31, 23, 12, 5, 77, 9, 12}
print(set1.intersection(set2))
