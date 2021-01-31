
array = input("Please write the array: ")
search = "a" #initialize the variable search
end = False

while search != "p" and search != "e":
    search = input("Please select if you want to find by position(p) or element(e): ")

#searching by position
if search == "p":
    position = int(input("Please define the position you want to access: "))
    if position < len(array):
        print("The element in this position is:", array[position])
    else:
        print("This position is out of the bounds of the defined array.")

#searching by element
if search == "e":
    element = input("Please define the element you want to access: ")
    position = array.find(element)
    if position == -1:
        print("This element is not present in the defined array.")
    else:
        print("The element is in the position:", position)
