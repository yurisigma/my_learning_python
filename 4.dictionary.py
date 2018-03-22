alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium',
    'nile': 'egypt',
    }

print("Alien speed is " +
      alien_0['speed'] +
      ".")

for k, v in alien_0.items():
    print("\nKey: " + k)
    print("Value: " + str(v))


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]

aliens = []
# create aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# change aliens' value
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))


cities = {'Shanghai': {
    'country': 'China',
    'population': 100,
    'fact': 'Q'
}, 'New york': {
    'country': 'US',
    'population': 100,
    'fact': 'W'
}, 'London': {
    'country': 'UK',
    'population': 100,
    'fact': 'E'
}, 'Tokyo': {
    'country': 'Japan',
    'population': 100,
    'fact': 'R'
}}

for city, city_info in cities.items():
    print("\nCity Name: " + city)

    country_name = city_info['country'] + " " + str(city_info['population'])
    country_fact = city_info['fact']
    print("\tCountry Name: " + country_name)
    print("\tCountry Fact: " + country_fact)
