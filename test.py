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
