def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    message_words = [line.split()[1] for line in lines]

    decoded_message = ' '.join(message_words)

    return decoded_message
print(decode('coding_qual_input.txt'))
