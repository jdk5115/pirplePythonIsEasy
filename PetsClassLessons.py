'''#Classes - Pets: Lesson A'''

class Pets:
    def __init__(self, n, a, h, p):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    #getters
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful   

    #setters
    def setName(self, x):
        self.name = x

    def setAge(self, Age):
        self.age = Age

    def setHunger(self, hunger):
        self.hunger = hunger

    def setPlayful(self, playful):
        self.playful = playful
    
    def __str__(self):
        return self.name + str(self.playful) + str(self.hunger) + str(self.age)


Pet1 = Pets("Fido", 43, False, True)

print(Pet1.getName())
print(Pet1.getPlayful())
Pet1.setName("Snowball")
print(Pet1.getName())
print(Pet1.name)
Pet1.name = "Jim"
print(Pet1.name)
print(Pet1)