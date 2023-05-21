# Create the list of planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Prompt the user for the reference planet
user_planet = input("Please enter the name of the planet (with a capital letter to start)")

# Find the location of the selected planet
planet_index = planets.index(user_planet)

# Display planets closer to the sun
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])

# Display planets further
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])