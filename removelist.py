colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        #removes the last item of the list by default if we will not pass any valid arguments
print(colors)
colors.pop(0)
print(colors)

#del
colors = ["voilet", "indigo", "blue", "green", "yellow"]
del colors[3]
print(colors)


#emplty list
colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)