#7. Remove all elements from a set using .clear(), while keeping the variable itself intact
#Given Input: colors = {"red", "green", "blue"}


colors = {"red", "green", "blue"}
print("Before clear:", colors)

colors.clear()
print("After clear:", colors)

#The variable still exists as an empty set
print("Type of colors:", type(colors))
