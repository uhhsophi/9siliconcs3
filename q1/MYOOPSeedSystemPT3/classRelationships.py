class AppleProduct:
    # Stores the information about each product.
    def __init__(self, color, name, available, working):
        self.__color = color
        self.__name = name
        self.__available = available
        self.__working = working

    # Changes the product's working status.
    def repair(self):
        self.__working = True
        print("Status: Working")

    # Changes the product's availability.
    def make_available(self):
        self.__available = True
        print("Status: Available")

    # Gets the product's color.
    def getColor(self):
        return self.__color

    # Gets the product's name.
    def getType(self):
        return self.__name

    # Gets the availability status.
    def getAvailable(self):
        return self.__available

    # Gets the working status.
    def getIsWorking(self):
        return self.__working


class Customer:
    # Sets the customer's name and starts an empty product list.
    def __init__(self, name):
        self.__name = name
        self.__products = []

    # Gets the customer's name.
    def getName(self):
        return self.__name

    # Adds a product to the customer.
    def add_product(self, product):
        self.__products.append(product)

    # Gets the customer's products.
    def getProducts(self):
        return self.__products


# Creates the customer and the products.
customer = Customer("Liane")

phone = AppleProduct("Blue", "iPhone 14", True, True)
macbook = AppleProduct("Silver", "MacBook Air", True, True)
airpods = AppleProduct("White", "AirPods", True, True)


print("")
print("---BEFORE RELATIONSHIP---")
# Shows the customer before any products are added.

print(f"Customer: {customer.getName()}")
print(f"Products: {len(customer.getProducts())}")


print("")
print("---BUILDING RELATIONSHIP---")
# Connects each Apple product to the customer.

print(f"Adding {phone.getType()}...")
customer.add_product(phone)

print(f"Adding {macbook.getType()}...")
customer.add_product(macbook)

print(f"Adding {airpods.getType()}...")
customer.add_product(airpods)


print("")
print("---AFTER RELATIONSHIP---")
# Shows the customer and the products after they are connected.

print(f"Customer: {customer.getName()}")
print("Products:")

# Goes through the product list and displays each one.
i = 1
for product in customer.getProducts():
    print(f"Product {i}: {product.getType()}")
    i += 1
