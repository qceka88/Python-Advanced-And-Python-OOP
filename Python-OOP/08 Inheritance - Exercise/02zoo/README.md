Problem description

2.	Zoo
Create a zoo project that contains the following classes: 
![img.png](img.png)

Submit in judge a zip file of the project, containing a
separate file for each of the classes using the structure shown below:

![img_1.png](img_1.png)


Follow the diagram and create all the classes. Except for the Animal class, 
each class should inherit from another class, as shown in the diagram. 
The Animal class should receive a name - string upon initialization.
Every class should have a constructor, which accepts one parameter: name


_______________________________________________
Example

Test Code	(no input data in this task)

 
mammal = Mammal("Stella")

print(mammal.__class__.__bases__[0].__name__)

print(mammal.name)

lizard = Lizard("John")

print(lizard.__class__.__bases__[0].__name__)

print(lizard.name)

_______________________________________________
Output

Animal

Stella

Reptile

John
_______________________________________________
