user_input = ''

while user_input.lower() != 'done':
    user_input = input('Enter a new value, or done when done')

# Create the variable for user input
user_input = ''

# Create the list to store the values
inputs = []

# The while loop
while user_input.lower() != 'done':
    # Check if there's a value in user_input
    if user_input:
        # Store the value in the list
        inputs.append(user_input)
    # Prompt for a new value
    user_input = input('Enter a new value, or done when done')

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is ", planets[0])
print("The second planet is ", planets[1])
print("The third planet is ", planets[2])

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")

from time import sleep

countdown = [4, 3, 2, 1, 0]

for number in countdown:
    print(number)
    sleep(1)  # Wait 1 second
print("Blast off!! 🚀")