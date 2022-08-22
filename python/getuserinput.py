# Input name
name = input("Enter name: ")
print(name)

# Doing math with input
sq_ft = input("How big is the house (in sq ft)?: ")
sq_m = float(sq_ft) / 10.8
print(f"You know, {name}? The house that is {sq_ft} square feet big is also {sq_m:.2f} square metres big.")
