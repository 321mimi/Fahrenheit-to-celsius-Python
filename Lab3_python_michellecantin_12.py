# TWELVE
# Convert degrees fahrenheit to degrees celsius
# The formula: (°C) = ((°F) - 32) * (5/9)

# Prompts the user to enter degrees in fahrenheit, then converts it to an integer
fahrenheit = int(input("What is the fahrenheit? "))

# Calculates the degrees in celsius, turns it into an integer and turns it into a string
celsius = str(int((fahrenheit - 32) * (5/9)))

# Tells the user the degrees in celsius
print(fahrenheit, "degrees fahrenheit is equal to", celsius, "degrees celsius!")
