secret_message = input()

command = input()

while not command == 'Reveal':
    command_data = command.split(':|:')
    instruction = command_data[0]

    if instruction == 'InsertSpace':
        index = int(command_data[1])

        first_part = secret_message[:index]
        second_part = secret_message[index:]

        secret_message = first_part + ' ' + second_part

        print(secret_message)

    if instruction == 'Reverse':
        substring = command_data[1]

        if substring in secret_message:
            secret_message = secret_message.replace(substring, '', 1)
            secret_message = secret_message + substring[::-1]
        else:
            print('error')
            command = input()
            continue

        print(secret_message)

    if instruction == 'ChangeAll':
        substring = command_data[1]
        replacement = command_data[2]

        secret_message = secret_message.replace(substring, replacement)

        print(secret_message)

    command = input()

print(f'You have a new text message: {secret_message}')
