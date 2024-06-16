import random

def character_type_count(nb_chars):
    # Defines the weight for each type of characters in the final generated password.
    lowercase_weight = 35
    uppercase_weight = 35
    digits_weight = 20
    special_chars_weight = 10

    special_chars_count = round(nb_chars * (special_chars_weight/100))
    digits_count = round(nb_chars * (digits_weight/100))
    uppercase_count = round(nb_chars * (uppercase_weight/100))
    lowercase_count = round(nb_chars * (lowercase_weight/100))

    # With rounding, we need to make sure that the total number of characters is what the user asked for.
    # There usually going to be no more than one character difference and we will adjust to it on the uppercase characters count.
    total_chars = special_chars_count + digits_count + uppercase_count + lowercase_count
    while total_chars != nb_chars:
        if total_chars > nb_chars:
            uppercase_count -= 1
        if total_chars < nb_chars:
            uppercase_count += 1
        total_chars = special_chars_count + digits_count + uppercase_count + lowercase_count

    return { 'special_chars': special_chars_count, 'digits': digits_count, 'lowercase': lowercase_count, 'uppercase': uppercase_count }

def get_random_chars(char_type, nb_chars):
    # List of characters we want to use in passwords.
    # We removed alphabet characters that are not in the same spot on a qwerty keyboard and on an azerty keyboard.
    # We removed alphabet characters and digits that can be confusing (like i and 1 or O and 0).
    lowercase_chars = ['e', 'r', 't', 'y', 'u', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'x', 'c', 'v', 'b', 'n']
    uppercase_chars = ['E', 'R', 'T', 'Y', 'U', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'X', 'C', 'V', 'B', 'N']
    digits_chars = ['2', '3', '4', '5', '6', '7', '8', '9']
    special_chars = ['@', '*', '+', '-', '!', '.', '?', ]

    if char_type == 'lowercase':
        return random.choices(lowercase_chars, k = nb_chars)
    elif char_type == 'uppercase':
        return random.choices(uppercase_chars, k = nb_chars)
    elif char_type == 'digits':
        return random.choices(digits_chars, k = nb_chars)
    else:
        return random.choices(special_chars, k = nb_chars)
    
def get_nb_chars():
    nb_chars = 12
    try:
        nb_chars = int(input('How long should the password be ? (min 8 chars, default value is 12 if input is not a number)\n'))
    except:
        pass
    return nb_chars

def main():
    password_chars = []
    nb_chars = get_nb_chars()
    if nb_chars < 8:
        nb_chars = 8
        
    char_count = character_type_count(nb_chars)
    
    for key in char_count:
        password_chars += get_random_chars(key, char_count[key])

    random.shuffle(password_chars)
    
    print(''.join(password_chars))

main()