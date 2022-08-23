numbers = {1, 2, 3, 4, 5, 6, 7}
odd = {1, 3, 5, 7}

even = {2, 4, 6}
print(even)
#this is hard-coded

even = numbers.difference(odd)
print(even)
#using set operations

even = odd.difference(numbers)
print(even)
#doing this will have a different result because all elements of 'numbers' are removed in 'odd' which are all of them
#so this will return an empty set

lessthan10 = {1,2,3,4,5}
greaterthan10 = {11,12,13,14,15}

plusorminus5 = lessthan10.union(greaterthan10)
print(plusorminus5)
#joining the two sets

friedchicken_ing = {"chicken", "paprika", "pepper", "salt", "flour", "oil", "chili powder"}
roastedchicken_ing = {"salt", "lemon", "pepper", "oil", "carrots", "chicken", "potato"}

common_ing = friedchicken_ing.intersection(roastedchicken_ing)
print(common_ing)
#finding the intersection of the two sets
