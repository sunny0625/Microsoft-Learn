name = 'Earth'
moons = 1

earth_name = 'Earth'
earth_moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get('name'))
# planet['name'] is identical to using planet.get('name')
print(planet['name'])

wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError

planet.update({'name': 'Makemake'})

# No output: name is now set to Makemake.

planet['name'] = 'Makemake'

# No output: name is now set to Makemake.

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

planet['name'] = 'Jupiter'
planet['moons'] = 79

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }
planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }
# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')