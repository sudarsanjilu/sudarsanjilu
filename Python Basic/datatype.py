
#: A list is an ordered collection of data with elements separated by a comma
# and enclosed within square brackets. Lists are mutable and can be modified after creation
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
print(list1[3])
print(len(list1))
#A tuple is an ordered collection of data with elements separated by a comma
# and enclosed within parentheses. Tuples are immutable and can not be modified after creation. 
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

sequence1 = range(4,14,2)
for i in sequence1:
    print(i)