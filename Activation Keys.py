key = input()

command = input()

while not command == 'Generate':

    command_list = command.split('>>>')
    main_command = command_list[0]

    if main_command == 'Contains':
        substring = command_list[1]
        if substring in key:
            print(f'{key} contains {substring}')
        else:
            print('Substring not found!')

    if main_command == 'Flip':
        case = command_list[1]
        start_index = int(command_list[2])
        end_index = int(command_list[3])

        first_part = key[:start_index]
        change_part = key[start_index:end_index]
        last_part = key[end_index:]

        if case == 'Upper':
            change_part = change_part.upper()
        elif case == 'Lower':
            change_part = change_part.lower()

        key = first_part + change_part + last_part

        print(key)

    if main_command == 'Slice':
        start_index = int(command_list[1])
        end_index = int(command_list[2])

        first_part = key[:start_index]
        last_part = key[end_index:]

        key = first_part + last_part

        print(key)

    command = input()

print(f'Your activation key is: {key}')
