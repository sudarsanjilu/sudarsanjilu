cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

#Union
cities3 = cities.union(cities2)
print(cities3)

#Intersection
cities4 = cities.intersection(cities2)
print(cities4)

print("symmentric difference")
citie = {"Tokyo", "Madrid", "Berlin", "Delhi"}
citie2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
citie3 = cities.symmetric_difference(citie2)
print(citie3)

#symmetric_difference_update
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)


#difference
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

#The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present,
# else it returns True.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

citie45 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities46 = {"jajpur", "ctc"}
print(citie45.isdisjoint(cities46))
print(cities46.isdisjoint(citie45))
