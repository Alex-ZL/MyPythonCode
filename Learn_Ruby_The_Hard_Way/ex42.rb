## Animal is-a object look at the extra credit
class Animal
end

## Dog is-a kind of Animal
class Dog < Animal
	def initialize(name)
		## Dog has-a name
		@name = name
	end
end

## Cat is-a kind of Animal
class Cat < Animal
	def initialize(name)
		## Cat has-a name
		@name = name
	end
end

## Person is-a object
class Person
	def initialize(name)
		## Person has-a name
		@name = name

		## Person has -a pet of some kind
		@pet = nil
	end

	attr_accessor :pet
end

## Employee is-a kind of Person
class Employee < Person
	def initialize(name, salary)
		## employee has the same name as a Person???
		super(name)
		## employee has a salary
		@salary = salary
	end
end

## Fish is a Object
class Fish
end

## Salmon is-a kind of Fish
class Salmon < Fish
end

## Halibut is-a kind of Fish
class Halibut < Fish
end

## rover is-a Dog
rover = Dog.new("Rover")

## satan is-a Cat
satan = Cat.new("Satan")

## mary is-a person
mary = Person.new("Mary")

## Mary has-a pet satan
mary.pet = satan

## frank is a employee with salary
frank = Employee.new("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a fish
flipper = Fish.new()

## Crouse is-a Salmon
crouse = Salmon.new()

## harry is-a Halibut
harry = Halibut.new()

