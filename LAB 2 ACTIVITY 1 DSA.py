base = int(input("Please enter the base: ")) # Asking the user for base and exponent inputs
exponent = int(input("Please enter the exponent: "))

def power(base, exponent): # Recursive function to calculate powers
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

result = power(base, exponent)# Calling the recursive function

print(f"The Answer of {base}^{exponent} is: {result}")# Answer