print("fruits names ")
fruits = ["apple", "banana", "cherry"]

print("Access Items")
print(fruits[0])  # apple (indexing starts at 0)
print(fruits[-1]) # cherry (negative index: from end)

print("Change/Update Items")
fruits[1] = "orange"
print(fruits) #['apple', 'orange', 'cherry']

print("Add Items(append() → Add at the end)")
fruits.append("mango")
print(fruits)

print("insert(index, value) → Add at a specific position")
fruits.insert(1, "grape")
print(fruits)

print("extend() → Add multiple items from another list")
fruits.extend(["kiwi", "melon"])
print(fruits)

print("remove(value) → Removes the first orange")
fruits.remove("orange")
print(fruits)

print("pop(index) → Removes by index (default is last)")
fruits.pop(0) # removes first
print(fruits)

print("List Length")
print(len(fruits))

print("silicing a list")
print(fruits[1:3])   # From index 1 to 2
print(fruits[:2])    # First 2 items
print(fruits[::2])   # Every second item

print("Reverse a list")
fruits.reverse()
print(fruits)

print("sort a list")
fruits.sort()
print(fruits)

print("copy a list")
new_list = fruits.copy()
print(new_list)

print("clear a list")
fruits.clear()
print(fruits)










