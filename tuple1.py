# tuple1 = (1,2,2,3,5,4,6)
# tuple2 = ("Red", "Green", "Blue")
# print(tuple1)
# print(tuple1[2])
# print(tuple2)

# country = ("Spain", "Italy", "India", "England", "Germany")
# if "Germany" in country:
#     print("Germany is present.")
# else:
#     print("Germany is absent.")

# state = ("odisha","karnataka","goa","maharastra","kerala")
# if "odisha" in state:
#     print("odisha is very good in hockey")
    
# else:
#     print("other state are in good in other game")


# Dictionary of states and their literacy rates
# literacy_rates = {
#     "State A": 85,
#     "State B": 78,
#     "State C": 90,
#     "State D": 80,
#     "State E": 75,
#     "State F": 82,
# }

# # Print states with a literacy rate of 80% or more
# print("States with a literacy rate of 80% or more:")
# for state, rate in literacy_rates.items():
#     if rate >= 80:
#         print(state)



class VoterCard:
    def __init__(self, name, age, voter_id):
        self.name = name
        self.age = age
        self.voter_id = voter_id

    def display_info(self):
        print("\nVoter Card Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Voter ID: {self.voter_id}")

def register_voter():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    if age < 18:
        print("You must be at least 18 years old to register.")
        return

    voter_id = input("Enter your voter ID: ")
    
    voter = VoterCard(name, age, voter_id)
    voter.display_info()

if __name__ == "__main__":
    print("Welcome to the Voter Card Registration System")
    register_voter()

