### 1a. What is duck typing, as explained in the video?
#### Duck typing is a programming concept in Python where an object's suitability is determined by the presence of certain methods and properties, rather than its actual class type or inheritance. It follows the saying: "If it walks like a duck and quacks like a duck, then it must be a duck."
### 1b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
#### The Car class simply needed to have the same method name (such as speak()) that the Dog and Cat classes use inside the loop.
---
### 3. How does the code in 2.2 demonstrate polymorphism?
#### The code demonstrates polymorphism because the single function start_trip(vehicle) can accept objects of different, unrelated classes (Car, Boat, and Drone) and call the same move() method on each of them. Even though the method call vehicle.move() looks identical, each object responds in its own unique way depending on its class.
