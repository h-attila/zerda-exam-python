# Create a Rocket class.
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9".
# 2nd parameter: the starting fuel level as a number, defaults to 0.
# 3rd parameter: number of launches as a number, defaults to 0.
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 fuels if it's a falcon9.
# it should increment the launches by one if it had enough fuel for the launch.
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9.
# it should return the amount of fuel used for the refill.
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2.
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11, launches: 1"

################################################


class Rocket:

    def __init__(self, rocketType, fuelLevel=0, launches=0):
        self.rocketType = rocketType
        self.fuelLevel = fuelLevel
        self.launches = launches

    def launch(self):
        if self.rocketType == 'falcon1' and self.fuelLevel >= 1:
            self.fuelLevel -= 1
            self.launches += 1

        elif self.rocketType == 'falcon9' and self.fuelLevel >= 9:
            self.fuelLevel -= 9
            self.launches += 1

    def refill(self):
        if self.rocketType == 'falcon1':
            fuelUsed = 5 - self.fuelLevel
            self.fuelLevel = 5
            return fuelUsed

        elif self.rocketType == 'falcon9':
            fuelUsed = 20 - self.fuelLevel
            self.fuelLevel = 20
            return fuelUsed

    def getStats(self):
        return 'name: {}, fuel: {}, launches: {}'.format(self.rocketType, self.fuelLevel, self.launches)


# The following code should work with the class:
falcon1 = Rocket('falcon1')
returned_falcon9 = Rocket('falcon9', 11, 1)

falcon1.refill() # 5
falcon1.launch()

print(falcon1.getStats()) # name: falcon1, fuel: 4, launches: 1
print(returned_falcon9.getStats()) # name: falcon9, fuel: 11, launches: 1
