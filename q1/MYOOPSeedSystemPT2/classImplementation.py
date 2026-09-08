class Power Mac Center:
    # Creates a constructor to initialize the attributes.
    def __init__(self, color, p_type, available, is_working):
        self.__color = color
        self.__type = p_type
        self.__available = available
        self.__is_working = is_working

    # Creates a function to make the product available or repaired.
    def repair(self):
        self.__is_working = True
        print("Status: Working")

    # Creates a function to check if available.
    def make_available(self):
        self.__available = True
        print("Status: Available")

    # Creates a function getColor() which returns the attribute color.
    def getColor(self):
        return self.__color

    # Creates a function getType() which returns the attribute type.
    def getType(self):
        return self.__type

    # Creates a function getAvailable() which returns availability.
    def getAvailable(self):
        return self.__available

    # Creates a function getIsWorking() which returns working status.
    def getIsWorking(self):
        return self.__is_working


# Assigns an object named object1 with initial attributes.
object1 = Power Mac Center("Blue", "iPhone 14", True, False)

# Assigns another object named object2 with initial attributes.
object2 = Power Mac Center("Red", "iPhone 13", True, True)

# Prints out initial state of both objects.
print("---INITIAL STATE---")
print("OBJECT 1:")
print("Color:", object1.getColor())
print("Type:", object1.getType())
print("Available:", object1.getAvailable())
print("Working:", object1.getIsWorking())
print()

print("OBJECT 2:")
print("Color:", object2.getColor())
print("Type:", object2.getType())
print("Available:", object2.getAvailable())
print("Working:", object2.getIsWorking())
print()

# Performs repair method on object1.
print("Doing repair() method on OBJECT 1...")
object1.repair()
print()

# Prints the final state of both objects.
print("---FINAL STATE---")
print("OBJECT 1:")
print("Color:", object1.getColor())
print("Type:", object1.getType())
print("Available:", object1.getAvailable())
print("Working:", object1.getIsWorking())
print()

print("OBJECT 2:")
print("Color:", object2.getColor())
print("Type:", object2.getType())
print("Available:", object2.getAvailable())
print("Working:", object2.getIsWorking())
