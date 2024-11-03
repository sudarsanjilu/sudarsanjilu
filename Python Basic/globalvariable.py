icecream = "Vanilla"    #global variable
def foods():
    vegetable = "Potato"    #local variable
    fruit = "Lichi"         #local variable
    print(vegetable + " is a local variable value.")

foods()
print(icecream + " is a global variable value.")
print(fruit + " is a local variable value.")