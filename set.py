cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

#add method to add new citi
cities.add("Helsinki")
cities.add("Bangalore")
cities.add("jajpur")
cities.add("Bhubaneswar")
cities.add("ctc")

print(cities)
print("all the city")
print("remove jajpur and bhubaneswar from the list")
#remove Method
cities.remove("jajpur")
#ERROR it will through
#cities.remove("jajpur")
print(cities)
#discard method
cities.discard("ctc")
cities.discard("jajpur")
#No error will throw
print(cities)

#The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error,
# whereas discard() does not raise any error.

country = {"india","Bangalore", "Delhi", "Sa", "nz"}
#set.add() takes exactly one argument
#country.add("SL","pak","Ban","Afg")
country.add("SL")
country.add("pak")
country.add("Ban")
print(country)

country.pop()

#This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However,
# you can access the popped item if you assign the pop() method to a variable.
print(country)
del country
#print(country)


dist ={"jajpur", "puri", "kendrapdaa", "paradip"}
#This method clears all items in the set and prints an empty set.
dist.clear()
print(dist)


info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")