def caesar_cipher(text, shift_steps, alphabets, direction):
    result = []
    for char in text:
        for alphabet in alphabets:
            if char in alphabet:
                place = alphabet.index(char)
                if direction.lower() == 'шифровать':
                    index = (place + shift_steps) % len(alphabet)
                else:
                    index = (place - shift_steps) % len(alphabet)
                result.append(alphabet[index])
                break
        else:
            result.append(char)
    return ''.join(result)

def brut_force(text, alphabets):
    for shift in range(1, len(alphabets[0])):
        decrypted = caesar_cipher(text, shift, alphabets, direction = 'дешифровать')
        print(f'Сдвиг {shift}: {decrypted}')

def get_alphabet(language):
    alphabets_dict = {'русский': ['абвгдежзийклмнопрстуфхцчшщъыьэюя', 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЬЫЭЮЯ'], 'английский': ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']}
    alphabets = alphabets_dict.get(language)
    if alphabets is None:
        print('Ошибка! Неправильно указан язык.')
        exit()
    return alphabets

def input_direction():
    while True:
        direction = input('Что вам нужно сделать с текстом (шифровать или дешифровать)? \n').strip().lower()
        if direction in ['шифровать', 'дешифровать']:
            return direction
        print('Ошибка! Введите "шифровать" или "дешифровать".')
        
def input_shift():
    shift = input('Какой шаг сдвига вправо будет? \n').strip()
    while not (shift.isdigit() and int(shift) >= 0):
        print('Ошибка! Нужно ввести число 0 или больше.')
        shift = input('Попробуйте снова: \n').strip()
    return int(shift)

direction = input_direction()
language = input('На каком языке будет слово? \n').strip().lower()
text = input('Ведите ваше слово: \n')
shift_steps = input_shift()
alphabets = get_alphabet(language)

if direction.lower() == 'дешифровать' and shift_steps == 0:
    print('\nВарианты расшифровки перебором сдвигов:')
    brut_force(text, alphabets)
else:
    encrypted_text = caesar_cipher(text, shift_steps, alphabets, direction)
    print(f'Результат: ({direction}): {encrypted_text}')