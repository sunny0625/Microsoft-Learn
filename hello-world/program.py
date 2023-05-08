# program.py
from datetime import date
sum = 1 + 2
print(sum)
print("show this in the console")
sum = 1 + 2 # 3
product = sum * 2
print(product)
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
type(distance_to_alpha_centauri) ## <class 'float'>
left_side = 10
right_side = 5
print(left_side / right_side) # 2
date.today()
# print(date.today())
# print("Today's date is: " + date.today()) # error
print("Today's date is: " + str(date.today())) # type cast to string