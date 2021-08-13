number_of_cars = int(input())

cars = {}

for i in range(0, number_of_cars):
    car_data = input().split('|')

    car_brand = car_data[0]
    mileage = int(car_data[1])
    fuel = int(car_data[2])

    cars[car_brand] = {'mileage': mileage, 'fuel': fuel}

command = input()

while not command == 'Stop':

    command_data = command.split(' : ')
    command_type = command_data[0]

    if command_type == 'Drive':
        car = command_data[1]
        distance = int(command_data[2])
        fuel = int(command_data[3])

        if cars[car]['fuel'] < fuel:
            print('Not enough fuel to make that ride')
            command = input()
            continue

        cars[car]['mileage'] += distance
        cars[car]['fuel'] -= fuel
        print(f'{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.')

        if cars[car]['mileage'] >= 100000:
            print(f'Time to sell the {car}!')
            del cars[car]

    if command_type == 'Refuel':
        car = command_data[1]
        fuel = int(command_data[2])

        if cars[car]['fuel'] + fuel > 75:
            fuel = 75 - cars[car]['fuel']
            cars[car]['fuel'] = 75
        else:
            cars[car]['fuel'] += fuel

        print(f'{car} refueled with {fuel} liters')

    if command_type == 'Revert':
        car = command_data[1]
        kilometers = int(command_data[2])

        cars[car]['mileage'] -= kilometers

        if cars[car]['mileage'] < 10000:
            cars[car]['mileage'] = 10000
            command = input()
            continue

        print(f'{car} mileage decreased by {kilometers} kilometers')

    command = input()

sorted_result = sorted(cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for car, data in sorted_result:
    print(f'{car} -> Mileage: {data["mileage"]} kms, Fuel in the tank: {data["fuel"]} lt.')
