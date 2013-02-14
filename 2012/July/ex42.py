#!/usr/bin/python
## exercise 42

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## ??
		super(Empolyee,self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass
 
## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satna")

## Mary is-a Person
mary = Person("Mary")

## Mary has-a Cat called Satan
mary.pet = satan

## frank is-a employee with salary 120000
frank = Employee("Frank",120000)

## frank has-a dog called rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut



