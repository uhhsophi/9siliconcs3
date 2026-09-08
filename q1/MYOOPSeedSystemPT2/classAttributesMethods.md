# Class Attributes and Methods
## Previous Design
Link to my previous activity:
[My Previous Activity](../MYOOPSeedSystemPT1)
## Design Revision
No changes were made, nor were needed in my previous design.
## Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|Available|Boolean|Private|Prevents unauthorized status changes unless handled by the store's check-in system|
|Type|String|Private|Keeps the product classification consistent and prevents accidental overwriting|
|Color|String|Private|Protects the product detail from being changed without tracking the modification.|
|IsWorking|Boolean|Private|Enforces safety soa broken product can only be marked active via repair method.|
## Updated UML Class Diagram
![Class Diagram](images/classDiagram.png)
## Python Implementation

[View Python Source](classImplementation.py)
## Test Run
![Test Run](images/classTestRun.png)
## Object Diagram
![Object Diagram](images/objectDiagram.png)
## Analysis
### Why did you make your chosen attribute private?
It protects the data from being directly altered or corrupted by external code.
### Which method changes the state of your object?
Repair changes the state of IsWorking; toggleAvailability changes the state of Available; updateType changes the state of Type.
### How did your two objects demonstrate that instances are independent?
When I put the method repair() on Object 1, Object 2 still had its original attributes and remained whilst Object 1's "IsWorking" attribute turned into True.
### What is the difference between your class diagram and your object diagram?
The class diagram shows the design, whilst the object diagram shows the actual instances and how their data changed after running the method.
