l = ["one", "two", "three"]
t = ("one", "two", "three")
s = {"one", "two", "three", "one"}

l[0] = "four"
print(l)

l.append("five")
print(l)

l.remove("three")
print(l)

print(s)
#a set will only return unique elements and not duplicates
s.add("four")
print(s)
#a set has an add attribute

t[0] = "four"
print(t)
#this will result in an error because tuples are immutable
#tuple does not have an append attribute
