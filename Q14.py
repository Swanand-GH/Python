#14. Remove all items from a dictionary using .clear(), while keeping the dictionary object itself intact
#Given Input: inventory = {"apples": 10, "bananas": 5, "oranges": 8}


inventory = {"apples": 10, "bananas": 5, "oranges": 8}
print("Before clear:", inventory)

inventory.clear()
print("After clear:", inventory)

#The variable still exists as an empty dictionary
print("Type of inventory:", type(inventory))
