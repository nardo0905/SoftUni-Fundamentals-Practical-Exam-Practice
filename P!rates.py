command = input()

cities = {}
# This is going to be a two-key-value-pair dictionary; each key will have another dictionary for value; in this case:
# the key is the city name and the value is the dictionary with tha gold and population keys and values

while not command == 'Sail':

    city_data = command.split('||')
    city = city_data[0]
    population = int(city_data[1])
    gold = int(city_data[2])

    if city not in cities:
        cities[city] = {'population': population, 'gold': gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

    command = input()

event = input()

while not event == 'End':

    event_data = event.split('=>')
    event_type = event_data[0]

    if event_type == 'Plunder':

        town = event_data[1]
        people = int(event_data[2])
        gold = int(event_data[3])

        print(f'{town} plundered! {gold} gold stolen, {people} citizens killed.')
        cities[town]['population'] -= people
        cities[town]['gold'] -= gold

        if cities[town]['population'] <= 0 or cities[town]['gold'] <= 0:
            del cities[town]
            print(f'{town} has been wiped off the map!')

    if event_type == 'Prosper':

        town = event_data[1]
        gold = int(event_data[2])

        if gold < 0:
            print('Gold added cannot be a negative number!')
            event = input()
            continue

        cities[town]['gold'] += gold

        print(f'{gold} gold added to the city treasury. {town} now has {cities[town]["gold"]} gold.')

    event = input()

if not cities:
    print('Ahoy, Captain! All targets have been plundered and destroyed!')
else:
    # noinspection SpellCheckingInspection
    sorted_result = sorted(cities.items(), key=lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))  # Towns sorted by DESCENDING
    # gold value (hence the minus), THEN BY town name in ASCENDING order
    print(f'Ahoy, Captain! There are {len(sorted_result)} wealthy settlements to go to:')
    for city, data in sorted_result:
        print(f'{city} -> Population: {data["population"]} citizens, Gold: {data["gold"]} kg')
