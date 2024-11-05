class College:
    def __init__(self, name, branch,location):
        self.name = name
        self.branch = branch
        self.location = location

obj1 = College("GIFT", "ECE", "Bhubaneswar")
print(obj1.name, "collge have", obj1.branch, "branch")
print(obj1.name, "collge situated in ", obj1.location)