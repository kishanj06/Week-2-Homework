#problem 4-1 (chapter 4)
pizzas = ['hawaiian', 'pepperoni', 'cheese']
for pizza in pizzas:
    print(pizza)

pizzas = ['hawaiian', 'pepperoni', 'cheese']
for pizza in pizzas:
    print(f"{pizza.title()} pizza is my favorite!")

print("Hawaiian pizza is a 10/10")
print("Pepperoni pizza is a 10/10")
print("Cheese pizza is a 10/10")
print("I really love pizza!")

#problem 4-2 (chapter 4)
animals = ['dolphins', 'whales', 'sharks']
for animal in animals:
    print(animal)

animals = ['dolphins', 'whales', 'sharks']
for animal in animals:
    print(f"{animal.title()} would make great pets.")

print("All of these animals live underwater")
print("Any of these animals would make a great pet")

#problem 4-3 (chapter 4)
for value in range(1,21):
    print(value)

#problem 8-1 (chapter 8)
def display_message():
    """Display a simple message"""
    print("In this chapter I'll be learning about functions")

display_message()

#problem 8-2 (chapter 8)
def favorite_book(title):
    """Display favorite book"""
    print(f"One of my favorite books is, {title.title()}!")

favorite_book("Lord of the Flies")

#problem 8-3 (chapter 8)
def make_shirt(shirt_size, shirt_message):
    """Dispplay information about a shirt"""
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"The {shirt_size} shirt will say {shirt_message.title()}.")

make_shirt('small', 'Coding is Awsome!')
make_shirt(shirt_size='small', shirt_message='Coding is Awesome')

#problem 8-4 9(chapter 8)
def make_shirt(shirt_size, shirt_message= 'I love Python'):
    """Dispplay information about a shirt"""
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"The {shirt_size} shirt will say {shirt_message.title()}.")

make_shirt(shirt_size= 'large')

def make_shirt(shirt_size, shirt_message= 'I love Python'):
    """Dispplay information about a shirt"""
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"The {shirt_size} shirt will say {shirt_message.title()}.")

make_shirt(shirt_size= 'medium')

def make_shirt(shirt_size, shirt_message= 'Pineapple belongs on pizza!'):
    """Dispplay information about a shirt"""
    print(f"\nThe size of the shirt is a {shirt_size}.")
    print(f"The {shirt_size} shirt will say {shirt_message.title()}.")

make_shirt(shirt_size= 'extra small')

#problem 8-5 (chpater 8)
def describe_city(city_name, country_name= 'Jamaica'):
    """Display information about country"""
    print(f"{city_name.title()} is in {country_name.title()}.")

describe_city(city_name= 'Kingston')

def describe_city(city_name, country_name= 'Jamaica'):
    """Display information about country"""
    print(f"{city_name.title()} is in {country_name.title()}.")

describe_city(city_name= 'Montego Bay')

def describe_city(city_name, country_name= 'England'):
    """Display information about country"""
    print(f"{city_name.title()} is in {country_name.title()}.")

describe_city(city_name= 'London')

#problem 8-6 (chapter 8)
def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return(city.title() + "," + country.title())
city = city_country('santiago', 'chile')
print(city)
city = city_country('tokyo', 'japan')
print(city)
city = city_country('madrid', 'spain')
print(city)