# Testing script for Person class
#asjdfoasdfjasodfjaldfjalskd

from person import Person

# Initial amount
print(f"Initial amount: {Person.amount}")

# Create first person
person1 = Person("Alice", 25, 165)
print(f"After creating person1, amount: {Person.amount}")
print(f"Person1: {person1}")
person1.helloWorld()

# Create second person
person2 = Person("Bob", 30, 175)
print(f"After creating person2, amount: {Person.amount}")
print(f"Person2: {person2}")
person2.helloWorld()

# Get older using a specified number of years
print(f"Person1 age before get_older: {person1.age}")
person1.get_older(3)
print(f"Person1 age after get_older(3): {person1.age}")

print(f"Person2 age before get_older: {person2.age}")
person2.get_older(5)
print(f"Person2 age after get_older(5): {person2.age}")

# Delete person1
del person1
print(f"After deleting person1, amount: {Person.amount}")

# Delete person2
del person2
print(f"After deleting person2, amount: {Person.amount}")