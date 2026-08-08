#6. Create a set, add a new element to it, remove an element using remove(),
#   and discard an element using discard()
#Given Input: fruits = {"apple", "banana", "cherry"}


fruits = {"apple", "banana", "cherry"}
print("Initial set:", fruits)

fruits.add("orange")
print("After adding orange:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

fruits.discard("apple")
print("After discarding apple:", fruits)
