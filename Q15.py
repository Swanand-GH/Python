#15. Combine two dictionaries into a single dictionary.
#    If both dictionaries share a key, the value from the second dictionary takes precedence
#Given Input: dict1 = {"a": 1, "b": 2} and dict2 = {"b": 3, "c": 4}


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

#Combine dict2 into dict1
combined = dict1.copy()
combined.update(dict2)
print("Combined dictionary:", combined)
