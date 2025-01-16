# 1.1
# Calculates arithmetic mean of two integer numbers
def mean(x, y):
    return (x + y) / 2

# takes two numbers from keyboard
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# calculates arithmetic mean and print result
result = mean(n1, n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')

# 1.2
# takes two numbers from keyboard
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# define an anonymous function
mean = lambda x, y: (x + y) / 2

# calculates arithmetic mean and print result
result = mean(n1, n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")


# 1.3
# Function to convert meters per second to kilometers per hour
def ms_to_kmh(ms):
    return ms * 3.6

# Sample usage
ms1 = 10
ms2 = 35

# Convert and print the results
print(f"{ms1} m/s = {ms_to_kmh(ms1)} km/h")
print(f"{ms2} m/s = {ms_to_kmh(ms2)} km/h")

# 1.4
# Define anonymous function to convert meters per second to kilometers per hour
ms_to_kmh = lambda ms: ms * 3.6

# Sample usage
ms1 = 10
ms2 = 35

# Convert and print the results
print(f"{ms1} m/s = {ms_to_kmh(ms1)} km/h")
print(f"{ms2} m/s = {ms_to_kmh(ms2)} km/h")

# 1.5
# Function to calculate the average speed
def avg_speed(distance, hours, minutes):
    total_time_hours = hours + minutes / 60  # Convert minutes to hours and add to hours
    return distance / total_time_hours  # Average speed formula

# Input from the user
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# Calculate and print the average speed
speed = avg_speed(distance, hours, minutes)
print(f"Average speed: {speed:.1f} km/h")

# 1.6
# Define anonymous function to calculate average speed
avg_speed = lambda distance, hours, minutes: distance / (hours + minutes / 60)

# Input from the user
distance = float(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

# Calculate and print the average speed
speed = avg_speed(distance, hours, minutes)
print(f"Average speed: {speed:.1f} km/h")

# 1.7
# Define anonymous function to check if a number is even
is_even = lambda number: number % 2 == 0

# Test the function
number = int(input("Enter a number: "))

# Check if the number is even and print the result
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# 1.8
# Define anonymous function to get initials
initials = lambda name, surname: name[0].upper() + surname[0].upper()

# Test the function
name = input("Enter your first name: ")
surname = input("Enter your surname: ")

# Get and print the initials
print(f"Initials: {initials(name, surname)}")

# 2.2
# Unsorted list
names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry'
]

# Sort the list by the length of the names using a lambda function
sorted_names = sorted(names, key=lambda name: len(name))

# Print the sorted list
print("Sorted list:")
for name in sorted_names:
    print(name)

# 3.1
# List of transaction amounts in Euros
transactions_in_eur = [15.90, 38.47, 4.07, 132.70, 9.15]

# Convert the amounts to Polish zlotys using map() and lambda
transactions_in_pln = list(map(lambda x: x * 4.5, transactions_in_eur))

# Print the transaction amounts in PLN
for transaction in transactions_in_pln:
    print(f"{transaction:.2f}")

# 3.2
# Given sentence
sentence = 'I completely agree with you'

# Split the sentence into words and use map() to calculate the number of letters in each word
result = list(map(lambda word: len(word), sentence.split()))

# Print the result
print(f"Text: {sentence}")
print(f"No. of letters in words: {result}")

# 3.3
# List of products in stock with quantity and unit price
stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# Use map() to calculate the total value for each product and sum() to get the total value of all products
total_value = sum(map(lambda product: product[0] * product[1], stock))

# Print the result
print(f"Products in stock: {stock}")
print(f"Total value: {total_value:.2f}")

# 4.1
# List of employees
employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry",
             "JACKSON Peter", "JOHNSON Rick",
             "LEWIS Terry", "CLARKE Robin"]

# Use filter() to find employees whose surnames start with 'J'. IF surname appeared after firstname e.split()[1][0]
emp_J = list(filter(lambda e: e[0] == 'J', employees))

# Print the filtered list
print("Employees with surnames starting with 'J':")
for emp in emp_J:
    print(emp)

# 4.2
# List of recorded speed values
speed_values = [48, 47, 54, 50, 42, 68, 39, 46]

# Use filter() to find speeds greater than 50 km/h
too_high_speeds = list(filter(lambda speed: speed > 50, speed_values))

# Print the results
print(f"Recorded values: {', '.join(map(str, speed_values))}")
print(f"Speed too high: {', '.join(map(str, too_high_speeds))}")

# 4.3
# List of grades
grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

# Use filter() to exclude grades equal to 2.0
valid_grades = list(filter(lambda grade: grade != 2.0, grades))

# Calculate the arithmetic mean
mean_grade = sum(valid_grades) / len(valid_grades)

# Print the result
print(f"Arithmetic mean for grades <> 2.0 is {mean_grade:.2f}")

# 5.1
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using reduce with an anonymous lambda function to sum the numbers
result = reduce(lambda x, y: x + y, numbers)

# Print the result
print(result)  # Output: 15

# 5.2
from functools import reduce

# List of numbers
numbers = [2, 4, 6, 3, 7, 5]

# Use filter() to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Use reduce() to calculate the sum of even numbers
sum_even_numbers = reduce(lambda x, y: x + y, even_numbers)

# Print the result
print(sum_even_numbers)  # Output: 12

# 6.4
# Create an array containing numbers from 1 to 20
numbers = list(range(1, 21))

# Use map() with an anonymous lambda function to calculate the third power of each number
third_powers = list(map(lambda x: x ** 3, numbers))

# Print the result
print(third_powers)

# 6.5
# Create an array containing numbers from 1 to 20
numbers = list(range(1, 21))

# Use filter() with an anonymous lambda function to filter numbers divisible by both 2 and 3
divisible_by_2_and_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))

# Print the result
print(divisible_by_2_and_3)

# 6.6
# List of employee data
employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
             ("Jackson","Peter"),("Johnson","Rick"),
             ("Lewis","Terry"),("Clarke","Robin")]

# Use map() to format the data with last names in capital letters followed by first names
formatted_employees = list(map(lambda e: f"{e[0].upper()}, {e[1]}", employees))

# Print the result
for emp in formatted_employees:
    print(emp)

# 6.7
# List of ratings by 5 judges for each competitor
ratings = [(17,15,16,17,15),
          (16,18,19,17,19),
          (19,15,15,19,18),
          (18,17,19,15,16)]

# Use map() to calculate the total points for each competitor
total_points = list(map(lambda scores: sum(scores) - min(scores) - max(scores), ratings))

# Print the result
print(total_points)

# 6.8
# List of student scores
scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

# Higher order function that returns a lambda function for checking if a score is above the limit
def min_pts(limit):
    return lambda pts: pts >= limit

# Filtering the scores based on different limits
min_70 = list(filter(min_pts(70), scores))
min_40 = list(filter(min_pts(40), scores))
min_30 = list(filter(min_pts(30), scores))

# Display the results
print(f"Min 70 pts: {min_70}")
print(f"Min 40 pts: {min_40}")
print(f"Min 30 pts: {min_30}")

# 6.9
# Dictionary with city names and their recorded temperatures
temperatures = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}

# Using filter() and lambda to select cities with positive temperatures
positive_temp_cities = list(filter(lambda city: temperatures[city] > 0, temperatures))

# Display the result
print("Cities with positive temperatures:", " ".join(positive_temp_cities))

# 6.10
import matplotlib.pyplot as plt

# Dictionary with city names and their recorded temperatures
temperatures = {
    "Krakow": 7,
    "Warszawa": -2,
    "Sopot": 4,
    "Koszalin": -1,
    "Opole": 3
}

# Use map to create two arrays: one for city names and one for temperatures
cities = list(map(lambda city: city, temperatures.keys()))
temp_values = list(map(lambda city: temperatures[city], temperatures.keys()))

# Create a bar chart
plt.bar(cities, temp_values, color='blue')

# Add title and axis labels
plt.title("Temperatures Recorded in Cities")
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# Show the chart
plt.show()

# 6.11
# List of students and their test results
test_results = [
   {"name": "Peter", "result": 27},
   {"name": "Anna", "result": 63},
   {"name": "Robert", "result": 92},
   {"name": "Paul", "result": 46},
   {"name": "Barbara", "result": 52}
]

# Filter students with results between 50 and 70
filtered_students = list(filter(lambda student: 50 <= student["result"] <= 70, test_results))

# Display the filtered list of students
for student in filtered_students:
    print(f"{student['name']} - {student['result']} points")

# 6.12
# List of countries and their medal counts
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Filter countries with at least 10 medals
countries_with_10_or_more_medals = list(filter(lambda country: (country["gold"] + country["silver"] + country["bronze"]) >= 10, medal_data))

# Display the countries and their medal counts
print("COUNTRIES WITH AT LEAST 10 MEDALS")
for country in countries_with_10_or_more_medals:
    print(f"{country['country']}: {country['gold']},{country['silver']},{country['bronze']}")

# 6.13
import matplotlib.pyplot as plt

# List of countries and their medal counts
medal_data = [
    {"country": "Denmark", "gold": 2, "silver": 4, "bronze": 6},
    {"country": "Finland", "gold": 5, "silver": 0, "bronze": 4},
    {"country": "USA", "gold": 12, "silver": 5, "bronze": 11},
    {"country": "Peru", "gold": 0, "silver": 1, "bronze": 7}
]

# Extract countries and their total medal counts using map()
countries = list(map(lambda x: x["country"], medal_data))
total_medals = list(map(lambda x: x["gold"] + x["silver"] + x["bronze"], medal_data))

# Create the bar chart
plt.bar(countries, total_medals, color="skyblue")

# Add a title and axis descriptions
plt.title("Total Medals Won by Country (Olympic Games)", fontsize=14)
plt.xlabel("Countries", fontsize=12)
plt.ylabel("Total Medals", fontsize=12)

# Show the chart
plt.show()

# 6.14
# Data
bottle_capacity = 500
tolerance = 0.02
fillings = [508, 500, 512, 499, 492, 511, 503, 476, 501, 509]

# Tolerance range
min_fill = bottle_capacity * (1 - tolerance)
max_fill = bottle_capacity * (1 + tolerance)

# Higher-order function to check if a bottle is filled correctly
def is_incorrect_fill(fill):
    return not (min_fill <= fill <= max_fill)

# Use filter() to find incorrectly filled bottles
incorrect_fills = list(filter(is_incorrect_fill, fillings))

# Calculate the percentage of incorrectly filled bottles
percentage_incorrect = (len(incorrect_fills) / len(fillings)) * 100

# Display the result
print(f"Bottle capacity:    {bottle_capacity}ml")
print(f"Filling tolerance:  {int(tolerance * 100)}%")
print(f"Filled bottles:     {', '.join(map(str, fillings))}")
print(f"Incorrectly filled: {int(percentage_incorrect)}%")




