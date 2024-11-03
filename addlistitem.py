colors = ["voilet", "indigo", "blue"]
colors.append("green")
colors.append("pink")
colors.append("grey")
colors.remove("blue")
print(colors)
print(" all colors are great")
print("replace new color white instead of green")
colors.insert(0,"white")
print(colors)

#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)

#concat
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
