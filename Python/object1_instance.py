# create a class a 'blueprint' of information about persons .

class info:
    def __init__(self, FirstName, LastName, Age):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Age = Age

    def fullname(self):
        print(f"My name is {self.FirstName} {self.LastName}.")

    def age(self):
        print(f"I am {self.Age} old.")

# Create an instance of the info class for Sazidul Islam age 22


id_21 = info("Sazidul", "Islam", 22)


# Create an instance of the info class for Belal Hossain age 20

id_12 = info("Belal", "Hossain", 20)


# now its time to interact with  instances.

# Access attributes of sazid

print("Access FirstName of sazid Through thier Method (id_21)=>", id_21.FirstName)
print("Access LastName of sazid Through thier Method (id_21)=>", id_21.LastName)
print("Access Age of sazid Through thier Method (id_21)=>", id_21.Age)


# call Method (id_21)
id_21.fullname()
id_21.age()
