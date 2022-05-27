cardipt = input('Введите карту: ')

def card_save(card):
    return '*' * len(card[:-4]) + card[-4:]

print(card_save(cardipt))