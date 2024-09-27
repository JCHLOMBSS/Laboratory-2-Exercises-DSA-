def compute_cubes(arr): # Function to compute
    cubes = [x**3 for x in arr]
    return cubes

size = int(input("Please enter the size of the array: ")) # Will input for the size of array

elements = list(map(int, input("Please enter the elements separated by space: ").split())) # Will input the elements

if len(elements) != size: #Will ensure that the number of elemenets is match to size
    print("It has an Error, the number of elements does not match the specified size.")
else:
    # Step 3: Display the cube of each element
    cubes = compute_cubes(elements)
    print("The cubes of the elements are:", *cubes)
