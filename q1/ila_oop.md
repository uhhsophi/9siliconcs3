# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by creating a Product class that keeps the product’s data, such as productName, price, and quantity, together with its methods. The properties can be kept private and accessed or modified through methods such as getPrice(), getQuantity(), and updateStock(). This keeps the product’s information organized and prevents other parts of the program from directly changing important data incorrectly.

### 2. Abstraction
Abstraction can be applied by providing simple methods that hide the complicated details of inventory operations. For example, a store employee could call an addProduct() or sellProduct() method without needing to know how the program internally stores or updates the product information. This makes the system easier to use and allows the internal implementation to be changed without affecting the rest of the program.

### 3. Inheritance
Inheritance can be used when different types of products share common properties and behaviors. For example, a general Product class could contain the product name, price, and quantity, while classes such as FoodProduct and HouseholdProduct could inherit these properties and add their own specific information. This reduces repeated code and makes it easier to organize different product categories.

### 4. Polymorphism
Polymorphism can allow different product types to respond differently to the same method. For example, a calculatePrice() method could be defined in the Product class, while FoodProduct and HouseholdProduct could implement the method differently if they have different pricing rules. This allows the inventory system to work with different product types using the same method name, making the program more flexible and easier to expand.

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It keeps important product information such as price and stock organized inside the Product object and prevents it from being changed incorrectly. It also makes the program easier to maintain because the data and the methods that manage it are kept together. Overall, encapsulation would make the inventory system more organized, secure, and manageable as the number of products increases.
