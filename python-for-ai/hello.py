print("Hello, World!")
print("I'm learning Python for AI")
print("My name is [Your Name]")
print("Today is a great day to code!")

import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

# Let's explore interactive mode
name = "Python Learner"
print(f"Hello, {name}!")

# Some data to work with
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Calculate something
total = sum(numbers)
print(f"Total: {total}")

# First, create a variable
message = "Hello"

# Later, use it (even in a different cell)
print(message + " World!")

# Modify it
message = message.upper()
print(message)

name = "Alice"
age = 25
is_student = True

user_name = "Dave"  # lowercase with underscores (Python style)
userName = "Dave"  # camelCase (works but not Python style)
age2 = 30  # numbers are OK (not at start)
_private = "secret"  # underscore at start is OK

# Good Python style
first_name = "Alice"
user_age = 25
is_logged_in = True
shopping_cart_total = 49.99

# Avoid camelCase (this is for other languages)
firstName = "Alice"  # Works, but not Python style
userAge = 25
isLoggedIn = True

# Start with one value
score = 0
print(score)  # Shows: 0

# Change it
score = 10
print(score)  # Shows: 10

# Change it again
score = score + 5
print(score)  # Shows: 15

# This is a comment
print("Hello")  # This is also a comment

# You can have multiple lines
# of comments by starting
# each line with a hash

age = 25  # Store user's age

"""
This is a multi-line comment.
It can span several lines.
Great for longer explanations.
"""


def calculate_tip(bill):
    """
    Calculate 20% tip for a restaurant bill.
    Takes the bill amount and returns the tip.
    """
    return bill * 0.20


# Basic math
print(10 + 3)  # 13 - Addition
print(10 - 3)  # 7  - Subtraction
print(10 * 3)  # 30 - Multiplication
print(10 / 3)  # 3.333... - Division (always gives float)

# Special operators
print(10 // 3)  # 3  - Floor division (rounds down)
print(10 % 3)  # 1  - Modulo (remainder)
print(10**3)  # 1000 - Exponent (power)

result = 2 + 3 * 4  # 14 (not 20!)
result = (2 + 3) * 4  # 20 (parentheses first)

age = 18

print(age == 18)  # True  - Equal to
print(age != 21)  # True  - Not equal to
print(age > 17)  # True  - Greater than
print(age < 20)  # True  - Less than
print(age >= 18)  # True  - Greater than or equal
print(age <= 18)  # True  - Less than or equal

age = 25
has_license = True

# AND - both must be true
can_drive = age >= 16 and has_license
print(can_drive)  # True

# OR - at least one must be true
day = "Saturday"
is_weekend = day == "Saturday" or day == "Sunday"
print(is_weekend)  # True

# NOT - reverses the value
is_adult = age >= 18
is_child = not is_adult
print(is_child)  # False

# AND: Both must be True
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False

# OR: At least one must be True
print(True or False)  # True
print(False or False)  # False

# NOT: Flips the value
print(not True)  # False
print(not False)  # True

# Instead of:
score = score + 10

# Write:
score += 10

# Works with all operators
x = 10
x += 5  # x is now 15
x *= 2  # x is now 30

first_name = "Jane"
last_name = "Doe"

# Using +
full_name = first_name + " " + last_name  # "Jane Doe"

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"

star = "*"
stars = star * 10  # "**********"

separator = "-" * 20  # "--------------------"

text = "Python Programming"

print(text.lower())  # "python programming"
print(text.upper())  # "PYTHON PROGRAMMING"
print(text.title())  # "Python Programming"

messy = "  hello world  "
print(messy.strip())  # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)  # True
print(message.startswith("I"))  # True
print(message.endswith("Python"))  # True

# Find position
print(message.find("Python"))  # 7 (first occurrence)
print(message.count("Python"))  # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

age = 18

if age >= 18:
    print("You can vote!")
    print("You're an adult")

temperature = 25

if temperature > 30:
    print("It's hot!")
else:
    print("Nice weather!")

score = 85

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

age = 25
has_license = True
day = is_weekend

# Both must be True
if age >= 18 and has_license:
    print("You can drive!")


has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the movie!")
    else:
        print("Need adult supervision")
else:
    print("Buy a ticket first")

for i in range(5):
    print("Hello!")

# Print numbers 0 through 4
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

name = "Python"
for letter in name:
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

colors = ["red", "blue", "green"]
for color in colors:
    print(f"I like {color}")

# Output:
# I like red
# I like blue
# I like green

count = 0
while count < 5:
    print(f"Count is {count}")
    count = count + 1  # Increase count by 1

# Output:
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4

# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types OK!

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])  # "apple" (first item)
print(fruits[1])  # "banana"
print(fruits[-1])  # "orange" (last item)
print(fruits[-2])  # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])  # ["banana", "orange"]

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")  # Add to end
fruits.insert(1, "kiwi")  # Insert at position

# Remove items
fruits.remove("banana")  # Remove by value
last = fruits.pop()  # Remove and return last
del fruits[0]  # Remove by index

numbers = [3, 1, 4, 1, 5, 9]

# Information
print(len(numbers))  # 6 (length)
print(numbers.count(1))  # 2 (count occurrences)
print(numbers.index(4))  # 2 (find position)

# Sorting
numbers.sort()  # Sort in place
print(numbers)  # [1, 1, 3, 4, 5, 9]

numbers.reverse()  # Reverse order
print(numbers)  # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()  # Create a copy

fruits = ["apple", "banana", "orange"]

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")

# Empty dictionary
my_dict = {}

# Dictionary with data
person = {"name": "Alice", "age": 30, "city": "New York"}

# Different ways to create
scores = dict(math=95, english=87, science=92)

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])  # "Alice"
print(person["age"])  # 30

# Safer with get()
print(person.get("job"))  # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)

person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
person["age"] = 31  # Update existing

# Remove items
del person["email"]  # Remove by key
age = person.pop("age")  # Remove and return
person.clear()  # Remove all items

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())  # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())  # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"},
}

# Access nested data
print(students["alice"]["grade"])  # "A"

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = 42  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])  # 3
print(colors[-1])  # "blue"

# Slicing works too
print(colors[0:2])  # ("red", "green")

# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}

colors = {"red", "blue"}

# Add items
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# Remove items
colors.remove("blue")  # Error if not found
colors.discard("yellow")  # No error if not found

# Check membership
if "red" in colors:
    print("Red is available")

names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_names = list(set(names))
print(unique_names)  # ['Alice', 'Bob', 'Charlie']

allowed_users = {"alice", "bob", "charlie"}

if "alice" in allowed_users:  # Very fast!
    print("Access granted")


def greet():
    print("Hello, world!")
    print("Welcome to Python!")


# Call the function
greet()


def function_name():
    # Code goes here
    # Must be indented
    pass


# Good names
def calculate_total():
    pass


def send_email():
    pass


def validate_password():
    pass


# Bad names
def func1():  # Not descriptive
    pass


def Calculate():  # Should be lowercase
    pass


def say_goodbye():
    print("Goodbye!")
    print("See you later!")


# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()


def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")


# Use the function
check_weather()


def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")


calculate_price()  # Total: 110

# This fails - price doesn't exist outside the function
print(price)  # NameError: name 'price' is not defined

discount_rate = 0.15  # Global variable


def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount


result = apply_discount(100)
print(result)  # 85.0

counter = 0  # Global variable


def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1


increment()
increment()
print(counter)  # 2

# Bad - using global variable
total = 0


def add_to_total(amount):
    global total
    total += amount


# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount


total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30


# Without parameters (inflexible)
def greet_alice():
    print("Hello, Alice!")


# With parameters (flexible)
def greet(name):
    print(f"Hello, {name}!")


# Now it works for anyone
greet("Alice")
greet("Bob")
greet("Charlie")


def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")


# Call with values
introduce("Alice", 25)
introduce("Bob", 30)


def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")


# Order matters!
calculate_total(100, 0.08, 10)  # $98


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# Use default
greet("Alice")  # Hello, Alice!

# Override default
greet("Bob", "Hi")  # Hi, Bob!
greet("Charlie", "Hey")  # Hey, Charlie!


def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")


# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)


# This function only prints
def add_print(a, b):
    print(a + b)


# This function returns a value
def add_return(a, b):
    return a + b


# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8


def calculate_area(width, height):
    area = width * height
    return area


# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft


def double(number):
    return number * 2


# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")


def get_min_max(numbers):
    return min(numbers), max(numbers)


# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)


def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays


def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value


# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!


def greet(name):
    print(f"Hello, {name}!")
    # No return statement


result = greet("Alice")  # Prints: Hello, Alice!
print(result)  # None

# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime

today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os

current_dir = os.getcwd()
print(current_dir)

# JSON data
import json

data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)

# Import entire module
import math

result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi

result = sqrt(16)
radius = 5
circle_area = pi * radius**2

# Import with alias
import pandas as pd

df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *

# Web requests
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
# Web requests
import requests

response = requests.get("https://api.example.com/data")
data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["NYC", "LA", "Chicago"],
}
df = pd.DataFrame(data)
print(df)

import requests

# We need coordinates to get weather data
latitude = 48.85  # Paris latitude
longitude = 2.35  # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

import requests


def get_weather(latitude, longitude):
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m"
    )
    data = response.json()
    return data["current"]["temperature_2m"]


# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")

import requests
from datetime import datetime, timedelta

# Calculate dates
today = datetime.now()
week_ago = today - timedelta(days=7)

# Format dates for API (YYYY-MM-DD)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

# Get Paris weather for past week
url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()
print(data)

import pandas as pd

# Extract the daily data
daily_data = data["daily"]

# Create a DataFrame
df = pd.DataFrame(
    {
        "date": daily_data["time"],
        "max_temp": daily_data["temperature_2m_max"],
        "min_temp": daily_data["temperature_2m_min"],
    }
)

# Convert date strings to datetime
df["date"] = pd.to_datetime(df["date"])

print(df)

import matplotlib.pyplot as plt

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")

# Add labels and title
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Paris Weather - Past 7 Days")
plt.legend()

# Rotate x-axis labels for readability
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig("weather_chart.png")
plt.show()

import os

# Create data folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# Save to CSV
df.to_csv("data/paris_weather.csv", index=False)
print("Data saved to data/paris_weather.csv")

# Without classes - data and functions separate
name = "OpenAI"
model = "gpt-4o-mini"


def generate_response(prompt):
    # Process prompt...
    return response


# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def generate_response(self, prompt):
        # Process prompt...
        return response


# main.py - Organized with functions
def setup_api(key):
    return {"key": key, "base_url": "https://api.openai.com"}


def generate_response(api_config, prompt):
    # Make API call
    return response


api = setup_api("sk-...")
result = generate_response(api, "Explain Python")


# api_utils.py
def setup_api(key):
    return {"key": key, "base_url": "https://api.openai.com"}


# main.py
from api_utils import setup_api

api = setup_api("sk-...")


# client.py
class OpenAIClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openai.com"

    def generate(self, prompt):
        # All logic encapsulated here
        return response


# main.py
from client import OpenAIClient

client = OpenAIClient("sk-...")
response = client.generate("Explain Python")


class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name)  # Buddy
print(dog2.breed)  # Beagle


class Dog:
    def __init__(self, name):
        self.name = name  # self.name belongs to this specific dog


# Using positional argument
dog1 = Dog("Buddy")

# Using named argument (same result)
dog2 = Dog(name="Max")

# Each dog has its own name
print(dog1.name)  # Buddy
print(dog2.name)  # Max


class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.base_url = "https://api.openai.com/v1"


# Create different configurations
# Using positional for required arg, named for optional
dev_config = APIConfig("sk-dev-key", max_tokens=50)

# Using all named arguments (clearest)
prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=1000)

# Access the configuration
print(dev_config.model)  # gpt-3.5-turbo
print(prod_config.model)  # gpt-4
print(prod_config.max_tokens)  # 1000

# APIConfig is the class
# config1 and config2 are instances
config1 = APIConfig(api_key="key1", max_tokens=50)
config2 = APIConfig(api_key="key2", max_tokens=200)

# Each instance has its own data
print(config1.max_tokens)  # 50
print(config2.max_tokens)  # 200

# Changing one doesn't affect the other
config1.max_tokens = 75
print(config1.max_tokens)  # 75
print(config2.max_tokens)  # 200 (unchanged)


class APIClient:
    def __init__(self, api_key, base_url):
        self.api_key = api_key  # Each client has its own key
        self.base_url = base_url  # Each client has its own URL
        self.request_count = 0  # Track requests per client


# Creating instances with named arguments
client1 = APIClient(api_key="key1", base_url="https://api1.com")
client2 = APIClient(api_key="key2", base_url="https://api2.com")


class APIClient:
    version = "1.0"  # Same for all clients
    max_retries = 3  # Same for all clients

    def __init__(self, api_key):
        self.api_key = api_key  # Unique to each client


class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self, email):
        if "@" not in email:
            self.errors.append(f"Invalid email: {email}")
            return False
        return True

    def validate_age(self, age):
        if age < 0 or age > 150:
            self.errors.append(f"Invalid age: {age}")
            return False
        return True

    def get_errors(self):
        return self.errors


# Use the validator
validator = DataValidator()

# Notice: we don't pass self, just the email
validator.validate_email(email="bad-email")
validator.validate_age(age=200)

# Or using positional arguments
validator.validate_email("another-bad-email")
validator.validate_age(150)

print(validator.get_errors())
# ['Invalid email: bad-email', 'Invalid age: 200', 'Invalid email: another-bad-email']


# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"


# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())  # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())  # Buddy says woof!


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_pet = True


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Pass name to parent's __init__
        self.breed = breed  # Dog-specific attribute

    def describe(self):
        return f"{self.name} is a {self.breed}"


# Create dogs with breeds - positional arguments
golden = Dog("Buddy", "Golden Retriever")

# Or with named arguments (clearer)
poodle = Dog(name="Max", breed="Poodle")

print(golden.describe())  # Buddy is a Golden Retriever
print(golden.is_pet)  # True (inherited from Animal)


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} barks: Woof!"


class Cat(Animal):
    def make_sound(self):  # Override parent method
        return f"{self.name} meows: Meow!"


# Different animals, different sounds
generic = Animal(name="Something")
dog = Dog(name="Buddy")
cat = Cat(name="Whiskers")

print(generic.make_sound())  # Something makes a sound
print(dog.make_sound())  # Buddy barks: Woof!
print(cat.make_sound())  # Whiskers meows: Meow!


class BaseModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_loaded = False

    def load(self):
        print(f"Loading {self.model_name}...")
        self.is_loaded = True


class TextModel(BaseModel):
    def __init__(self, model_name, max_length=1000):
        super().__init__(model_name)
        self.max_length = max_length

    def process_text(self, text):
        if not self.is_loaded:
            self.load()
        # Truncate if needed
        if len(text) > self.max_length:
            text = text[: self.max_length]
        return f"Processed: {text}"


# Use the model - with named arguments
model = TextModel(model_name="gpt-3.5-turbo", max_length=100)

# Call method - notice no 'self' parameter needed
result = model.process_text(text="Hello world")
print(result)  # Loading gpt-3.5-turbo...
# Processed: Hello world


# Functions operate on data
def clean_text(text):
    return text.strip().lower()


def remove_punctuation(text):
    return text.replace(".", "").replace(",", "")


# Chain functions together
result = remove_punctuation(clean_text("  Hello, World.  "))


# Class bundles data and methods
class TextProcessor:
    def __init__(self, text):
        self.text = text

    def clean(self):
        self.text = self.text.strip().lower()
        return self

    def remove_punctuation(self):
        self.text = self.text.replace(".", "").replace(",", "")
        return self


# Chain methods on object
processor = TextProcessor(text="  Hello, World.  ")
result = processor.clean().remove_punctuation().text

import os

# Read from environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")

print(f"Using database: {database}")

import os

# Method 1: Get with default
api_key = os.environ.get("API_KEY", "demo-key")

# Method 2: Check if exists
if "API_KEY" in os.environ:
    api_key = os.environ["API_KEY"]
else:
    print("No API key found")

# Method 3: Will crash if not found
api_key = os.environ["API_KEY"]  # KeyError if missing!

from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get("API_KEY")
debug = os.environ.get("DEBUG")

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")

# app.py
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.environ.get("OPENAI_API_KEY")

if not API_KEY:
    print("Please set OPENAI_API_KEY in .env file")
    exit(1)

# Use the API
headers = {"Authorization": f"Bearer {API_KEY}"}
# Make your API calls...

import os


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {
        "name": "apple",
        "price": 0.5,
        "quantity": 6,
    },
    {
        "name": "banana",
        "price": 0.3,
        "quantity": 8,
    },
]
print(calculate_total(shopping_cart))


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    print("You choose addition.")
    print(f"Adding {num1} and {num2}...")
    print("Result:", add(num1, num2))
elif choice == "2":
    print("You choose subtraction.")
    print(f"Subtracting {num2} from {num1}...")
    print("Result:", subtract(num1, num2))
elif choice == "3":
    print("You choose multiplication.")
    print(f"Multiplying {num1} and {num2}...")
    print("Result:", multiply(num1, num2))
elif choice == "4":
    print("You choose division.")
    print(f"Dividing {num1} by {num2}...")
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")

import math


def scientific_calculator():
    print("Scientific Calculator")
    print("----------------------")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Square root (√)")
    print("7. Logarithm (log10)")
    print("8. Natural log (ln)")
    print("9. Sine (sin)")
    print("10. Cosine (cos)")
    print("11. Tangent (tan)")
    print("12. Factorial (!)")
    print("0. Exit")

    while True:
        choice = input("\nEnter choice: ")

        if choice == "0":
            print("Exiting calculator.")
            break

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", a + b)
                elif choice == "2":
                    print("Result:", a - b)
                elif choice == "3":
                    print("Result:", a * b)
                elif choice == "4":
                    print("Result:", a / b if b != 0 else "Error: Division by zero")
                elif choice == "5":
                    print("Result:", math.pow(a, b))

            elif choice == "6":
                x = float(input("Enter number: "))
                print("Result:", math.sqrt(x))

            elif choice == "7":
                x = float(input("Enter number: "))
                print("Result:", math.log10(x))

            elif choice == "8":
                x = float(input("Enter number: "))
                print("Result:", math.log(x))

            elif choice == "9":
                x = float(input("Enter angle (degrees): "))
                print("Result:", math.sin(math.radians(x)))

            elif choice == "10":
                x = float(input("Enter angle (degrees): "))
                print("Result:", math.cos(math.radians(x)))

            elif choice == "11":
                x = float(input("Enter angle (degrees): "))
                print("Result:", math.tan(math.radians(x)))

            elif choice == "12":
                x = int(input("Enter integer: "))
                print("Result:", math.factorial(x))

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)


scientific_calculator()

# leetcode problem: Two Sum


def two_sum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []  # fallback (though problem guarantees one solution)


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))

# leetcode problem: Add Two Numbers (using lists to represent linked lists)


def add_two_numbers(l1, l2):
    result = []
    carry = 0

    for i in range(max(len(l1), len(l2))):
        v1 = l1[i] if i < len(l1) else 0
        v2 = l2[i] if i < len(l2) else 0

        total = v1 + v2 + carry
        carry = total // 10
        result.append(total % 10)

    if carry:
        result.append(carry)

    return result


l1 = [2, 4, 3]
l2 = [5, 6, 4]

print(add_two_numbers(l1, l2))

# leetcode problem: Longest Substring Without Repeating Characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# Test the function

print(Solution().lengthOfLongestSubstring("abcabcbb"))


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = sorted(nums1 + nums2)
        n = len(merged)

        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0


nums1 = [1, 3]
nums2 = [2]
print(Solution().findMedianSortedArrays(nums1, nums2))

# leetcode problem: Longest Palindromic Substring


class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, end = 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length

        for i in range(len(s)):
            len1 = expand(i, i)  # odd length
            len2 = expand(i, i + 1)  # even length

            max_len = max(len1, len2)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]


print(Solution().longestPalindrome("babad"))

# leetcode problem: ZigZag Conversion


class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            current_row += 1 if going_down else -1

        return "".join(rows)


print(Solution().convert("PAYPALISHIRING", 3))

# leetcode problem: Reverse Integer


class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_str = str(x_abs)[::-1]
        reversed_int = sign * int(reversed_str)

        # Check for 32-bit signed integer overflow
        if reversed_int < -(2**31) or reversed_int > 2**31 - 1:
            return 0

        return reversed_int


print(Solution().reverse(123))

# leetcode problem: String to Integer (atoi)


class Solution(object):
    def myAtoi(self, s):
        s = s.strip()  # Remove leading/trailing whitespace
        if not s:
            return 0

        sign = 1
        start_index = 0

        if s[0] in ["+", "-"]:
            sign = -1 if s[0] == "-" else 1
            start_index = 1

        result = 0
        for i in range(start_index, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])

        result *= sign

        # Clamp to 32-bit signed integer range
        if result < -(2**31):
            return -(2**31)
        if result > 2**31 - 1:
            return 2**31 - 1

        return result


print(Solution().myAtoi("   -42"))

# leetcode problem: Palindrome Number


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]


print(Solution().isPalindrome(121))

# leetcode problem: Regular Expression Matching


class Solution(object):
    def isMatch(self, s, p):
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], "."}

        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])


print(Solution().isMatch("aab", "c*a*b"))

# leetcode problem: Container With Most Water


class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# leetcode problem: Integer to Roman


class Solution(object):
    def intToRoman(self, num):
        val = [
            1000,
            900,
            500,
            400,
            100,
            90,
            50,
            40,
            10,
            9,
            5,
            4,
            1,
        ]
        syms = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]
        roman_num = ""
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num


print(Solution().intToRoman(1994))

# leetcode problem: Roman to Integer


class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        prev_value = 0

        for char in s:
            value = roman_numerals[char]
            if prev_value < value:
                total += value - 2 * prev_value
            else:
                total += value
            prev_value = value

        return total


print(Solution().romanToInt("MCMXCIV"))

# leetcode problem: Longest Common Prefix


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))

# leetcode problem: 3Sum


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

# leetcode problem: 3Sum Closest


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float("inf")

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return closest_sum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

# leetcode problem: Letter Combinations of a Phone Number


class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = [""]

        for digit in digits:
            if digit not in phone_map:
                continue
            temp = []
            for combination in result:
                for char in phone_map[digit]:
                    temp.append(combination + char)
            result = temp

        return result


print(Solution().letterCombinations("23"))

# leetcode problem: Valid Parentheses


class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else "#"
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


print(Solution().isValid("()[]{}"))

# leetcode problem: Generate Parentheses


class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(s="", left=0, right=0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        backtrack()
        return result


print(Solution().generateParenthesis(3))

# leetcode problem: Merge k Sorted Lists

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))

        return dummy.next


# Example usage:
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))
lists = [list1, list2, list3]
merged_head = Solution().mergeKLists(lists)

# leetcode problem: Swap Nodes in Pairs


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            # Swap
            current.next, first.next, second.next = second, second.next, first

            # Move to the next pair
            current = first

        return dummy.next


# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
swapped_head = Solution().swapPairs(head)

# leetcode problem: Reverse Nodes in k-Group


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # Reverse group
            prev, current = kth.next, group_prev.next
            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next

    def getKthNode(self, current, k):
        while current and k > 0:
            current = current.next
            k -= 1
        return current


# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
reversed_head = Solution().reverseKGroup(head, k)

# leetcode problem: Remove Nth Node From End of List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next


# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
updated_head = Solution().removeNthFromEnd(head, n)

# leetcode problem: Valid Sudoku


class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue

                if (
                    num in rows[r]
                    or num in cols[c]
                    or num in boxes[(r // 3) * 3 + (c // 3)]
                ):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[(r // 3) * 3 + (c // 3)].add(num)

        return True


# Example usage:
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", "8", "8", "6", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
is_valid = Solution().isValidSudoku(sudoku_board)

# leetcode problem: Sudoku Solver


class Solution(object):
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for num in "123456789":
                        if self.isValid(board, r, c, num):
                            board[r][c] = num
                            if self.solve(board):
                                return True
                            board[r][c] = "."
                    return False
        return True

    def isValid(self, board, row, col, num):
        for i in range(9):
            if (
                board[row][i] == num
                or board[i][col] == num
                or board[(row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == num
            ):
                return False
        return True


# Example usage:
sudoku_board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", "8", "8", "6", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", "6", "9"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
Solution().solveSudoku(sudoku_board)

# leetcode problem: N-Queens


class Solution(object):
    def solveNQueens(self, n):
        def is_safe(board, row, col):
            # Check this column
            for i in range(row):
                if board[i] == col:
                    return False
            # Check upper left diagonal
            for i in range(row):
                if board[i] == col - (row - i):
                    return False
            # Check upper right diagonal
            for i in range(row):
                if board[i] == col + (row - i):
                    return False
            return True

        def backtrack(board, row):
            if row == n:
                solutions.append(
                    ["." * col + "Q" + "." * (n - col - 1) for col in board]
                )
                return
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1

        solutions = []
        backtrack([-1] * n, 0)
        return solutions


print(Solution().solveNQueens(4))

# leetcode problem: N-Queens II


class Solution(object):
    def totalNQueens(self, n):
        def is_safe(board, row, col):
            for i in range(row):
                if board[i] == col:
                    return False
            for i in range(row):
                if board[i] == col - (row - i):
                    return False
            for i in range(row):
                if board[i] == col + (row - i):
                    return False
            return True

        def backtrack(board, row):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    count += backtrack(board, row + 1)
                    board[row] = -1
            return count

        return backtrack([-1] * n, 0)


print(Solution().totalNQueens(4))

# leetcode problem: valid number


class Solution(object):
    def isNumber(self, s):
        s = s.strip()
        if not s:
            return False

        num_seen = False
        dot_seen = False
        e_seen = False

        for i, char in enumerate(s):
            if char.isdigit():
                num_seen = True
            elif char in ["+", "-"]:
                if i > 0 and s[i - 1] not in ["e", "E"]:
                    return False
            elif char == ".":
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif char in ["e", "E"]:
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False  # reset for exponent part
            else:
                return False

        return num_seen


print(Solution().isNumber("0"))


# leetcode problem: string to integer (atoi)
class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0

        sign = 1
        start_index = 0

        if s[0] in ["+", "-"]:
            sign = -1 if s[0] == "-" else 1
            start_index = 1

        result = 0
        for i in range(start_index, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])

        result *= sign

        if result < -(2**31):
            return -(2**31)
        if result > 2**31 - 1:
            return 2**31 - 1

        return result


print(Solution().myAtoi("   -42"))

# leetcode problem: Text Justification


class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        current_line = []
        num_of_letters = 0

        for word in words:
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    current_line[i % (len(current_line) - 1 or 1)] += " "
                res.append("".join(current_line))
                current_line = []
                num_of_letters = 0
            current_line.append(word)
            num_of_letters += len(word)

        return res + [" ".join(current_line).ljust(maxWidth)]


print(
    Solution().fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16
    )
)

# leetcode problem: Minimum Window Substring


class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        required = len(dict_t)
        formed = 0
        window_counts = {}
        l, r = 0, 0
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


print(Solution().minWindow("ADOBECODEBANC", "ABC"))

# leetcode problem: Longest Substring with At Most K Distinct Characters


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0

        left = 0
        right = 0
        char_count = {}
        max_length = 0

        while right < len(s):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


print(Solution().lengthOfLongestSubstringKDistinct("eceba", 2))

# leetcode problem: Smallest Substring With Identical Characters I


class Solution(object):
    def smallestSubstring(self, s):
        from collections import Counter

        char_count = Counter(s)
        required = len(char_count)
        formed = 0
        window_counts = {}
        l, r = 0, 0
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if (
                character in char_count
                and window_counts[character] == char_count[character]
            ):
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if (
                    character in char_count
                    and window_counts[character] < char_count[character]
                ):
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


print(Solution().smallestSubstring("aabcbcdbca"))

# leetcode problem: Longest Substring with At Most Two Distinct Characters


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        left = 0
        right = 0
        char_count = {}
        max_length = 0

        while right < len(s):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_length = max(max_length, right - left + 1)
            right += 1

        return max_length


print(Solution().lengthOfLongestSubstringTwoDistinct("eceba"))

# leetcode problem: Minimum Moves to Make Array Complementary


class Solution(object):
    def minMoves(self, nums, limit):
        from collections import Counter

        count = Counter()
        n = len(nums)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            count[a + b] += 1
            count[min(a, b) + 1] -= 1
            count[max(a, b) + limit + 1] -= 1

        moves = float("inf")
        current_moves = 0

        for x in range(2, 2 * limit + 1):
            current_moves += count[x]
            moves = min(moves, current_moves)

        return moves


print(Solution().minMoves([1, 2, 4, 3], 4))

import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number!:{secret_number}")
            break
    except ValueError:
        print("Please enter a valid integer.")


# create a simple to-do list application
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added to the list.')

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" removed from the list.')
        else:
            print(f'Task "{task}" not found in the list.')

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")


todo_list = ToDoList()
todo_list.add_task("Buy groceries")
todo_list.view_tasks()
todo_list.add_task("Call Alice")
todo_list.view_tasks()
