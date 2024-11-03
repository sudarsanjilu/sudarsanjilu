country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
country[1]
print(country[1])
print(country[:])
print(country[:-3])

#check for the item
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
    
# check for das brother
brother = ("Jugal", "Ujwal", "bulu", "lilu", "lipu", "silu", "jilu", "sipu")
if "jilu" in brother:
    print(" jilu is family member")
else:
    print("jilu is not family member")
    