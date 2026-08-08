#13. Create a dictionary by mapping two equal-length lists, one containing keys
#    and the other containing values
#Given Input: keys = ["name", "age", "city"] and values = ["Bob", 25, "London"]


keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]

result = dict(zip(keys, values))
print("Dictionary:", result)
