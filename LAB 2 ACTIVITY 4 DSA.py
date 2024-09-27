height = int(input("Please enter the height of the triangle: ")) # Asking the user for the height of the triangle

def generate_inverted_triangle(n): # Defining a function to generate an inverted right triangle
    if n < 1:
        print("Height should be at least 1.")
        return
    for i in range(n, 0, -1):     # Loop to iterate
        print('*' * i)

generate_inverted_triangle(height) # Calling the function

