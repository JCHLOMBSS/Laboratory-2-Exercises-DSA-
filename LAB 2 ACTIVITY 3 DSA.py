side_length = int(input("Please enter the side length of the square: ")) # Asking the user for the side length of the square

def generate_hollow_square(n): # Defining a function that will generate a hollow square
    if n < 2:
        print("The side length should be at least 2.")
        return

    # Outer loop
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

generate_hollow_square(side_length) # Calling the function