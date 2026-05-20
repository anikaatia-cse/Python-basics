#1. Accessing items(The 'Address' system):
grades = [90, 80, 70, 60, 50, 40]
print(grades[0])     # the first item/90
print(grades[1])     # the second item/80
print(grades[2])     # the third item/70
print(grades[5])     # the sixth item/40

#2. Negative Indexing:
print(grades[-1])    # the last item/40
print(grades[-2])    # the second last item/50
print(grades[-3])    # the third last item/60
print(grades[-6])    # the sixth last item/90

#3. Slicing:
print(grades[0:3])   # the first three items/90, 80
print(grades[3:6])   # the last three items/60, 50, 40
print(grades[:3])    # the first three items/90, 80, 70
print(grades[3:])    # the last three items/60, 50, 40
print(grades[:])     # all items/90, 80, 70, 60, 50, 40

#4. Modifying items:
grades[0] = 95      # change the first item to 95
print(grades)       # [95, 80, 70, 60, 50, 40]
grades[1:3] = [85, 75]   # change the second and third items to 85 and 75
print(grades)       # [95, 85, 75, 60, 50, 40]
grades[3:6] = [65, 55, 45]   # change the last three items to 65, 55, and 45
print(grades)       # [95, 85, 75, 65, 55, 45]

#5. Adding items(The .append() method):
grades.append(35)   # add 35 to the end of the list
print(grades)       # [95, 85, 75, 65, 55, 45, 35]
grades.append(25)   # add 25 to the end of the list
print(grades)       # [95, 85, 75, 65, 55, 45, 35, 25]

#6. Removing items(The .remove() method):
grades.remove(45)   # remove the first occurrence of 45
print(grades)       # [95, 85, 75, 65, 55, 35, 25]
grades.remove(25)   # remove the first occurrence of 25
print(grades)       # [95, 85, 75, 65, 55, 35]

#7. changing an item(updating):
grades[0] = 100     # change the first item to 100
print(grades)       # [100, 85, 75, 65, 55, 35]
grades[1:3] = [90, 80]   # change the second and third items to 90 and 80
print(grades)       # [100, 90, 80, 65, 55, 35]
grades[3:6] = [70, 60, 50]   # change the last three items to 70, 60, and 50
print(grades)       # [100, 90, 80, 70, 60, 50]

#8. Length of a list(The len() function):
print(len(grades))   # using len(list_name) to see how many items are inside/6
print(len([]))       # an empty list has 0 items/0
print(len([40]))   # add 40 to the end of the list and check the length/7
print(len(grades))   # check the length of the list again/6
print(len(str(grades[-1])))  # convert 50 to "50" to count its digits/2
#zero-indexing and negative indexing do not affect the length of the list, they are just different ways to access items in the list.
