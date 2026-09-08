class Power Mac Center: #Creates a class named "Power Mac Center".
    
    #Creates a function that lists down all the attributes in one function.
    def __init__(self, Color, Type, Color, IsWorking):
        self.__available = Available
        self.__type = Type
        self.__color = Color
        self.__IsWorking = IsWorking
        
    #Creates a function which materializes the method tune() and lets it get called and utilized later on.
    def available(self):
        self.__Availabile = True
        print("Status: Available")

    #Creates a function which checks if the product is working.
      def IsWorking(self):
        self.__IsWorking = True
        print("Status: Working")

    #Creates a function getColor() which calls and displays the attribute "Color".
    def getColor(self):
        return self.__color

    #Creates a function getType() which calls and displays the attribute "Type".
    def getType(self):
        return self.__type

    #Creates a function getAvailable() which calls and displays the attribute "IsTuned".
    def getAvailable(self):
        return self.__Available

    #Creates a function getIsWorking() which calls and displays a private attribute "IsPlayable". 
    def getIsWorking(self):
        return self.__IsWorking


object1 = Instrument("Blue", "iPhone 14", True, False) #Assigns an object named "object1" which contains all of its attributes in one compiled parameter.
object2 = Instrument("Red", "iPhone 13", True, True) #Assigns another object named "object2" which also contains all of its attributes in a compiled parameter.

print("---INITIAL STATE---") #Prints out all of the assigned attributes and calling all of the previous functions of both objects BEFORE the chosen method is performed.
print("OBJECT 1:")
print("Color:", object1.getColor())
print("Type:", object1.getType())
print("Available:", object1.getAvailable())
print("Playable:", object1.getIsWorking())

print("")

print("OBJECT 2:")
print("Color:", object2.getColor())
print("Type:", object2.getType())
print("Available:", object2.getAvailable())
print("Playable:", object2.getIsWorking())

print("")
print("Doing repair() method on OBJECT 1...")
object1.repair() #Calls the method tune() to repair "object1" and perform the assigned task to the function.
print("")

print("---FINAL STATE---") #Prints the final state and attributes of both objects AFTER the method repair() was perfoemd on "object1" whilst leaving "object2" unchanged.    
print("OBJECT 1:")
print("Color:", object1.getColor())
print("Type:", object1.getType())
print("Available:", object1.getAvailable())
print("Playable:", object1.getIsWorking())

print()
