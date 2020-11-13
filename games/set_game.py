import random


NUMBERS = [1, 2, 3]
SYMBOLS = ["DIAMOND", "SQUIGGLE", "OVAL"]
SHADINGS = ["STRIPPED", "SOLID", "OPEN"]
COLORS = ["RED", "GREEN", "PURPLE"]


class Card:
    def __init__(self, number, symbol, shading, color):
        if any([
            number not in NUMBERS,
            symbol not in SYMBOLS,
            shading not in SHADINGS,
            color not in COLORS
        ]):
            raise ValueError("Неправильные параметры карты")

        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color


def check_set(cards):
    color = []
    number = []
    symbol = []
    shading = []
    for card in cards:
        color.append(card.color)
        number.append(card.number)
        symbol.append(card.symbol)
        shading.append(card.shading)
    if color_check(color) and symbol_check(symbol) and shading_check(shading) and number_check(number):
        return True
    else:
        return False


def color_check(color_set):
    if len(set(color_set)) == 1 or len(set(color_set)) == 3:
        return True


def symbol_check(symbol_set):
    if len(set(symbol_set)) == 1 or len(set(symbol_set)) == 3:
        return True


def shading_check(shading_set):
    if len(set(shading_set)) == 1 or len(set(shading_set)) == 3:
        return True


def number_check(number_set):
    if len(set(number_set)) == 1 or len(set(number_set)) == 3:
        return True


def generate_3card(NUMBERS, SYMBOLS, SHADINGS, COLORS):
    cards = []
    for i in range(3):
        i = Card(random.choice(NUMBERS), random.choice(SYMBOLS), random.choice(SHADINGS), random.choice(COLORS))
        cards.append(i)
    return cards


print(check_set(generate_3card(NUMBERS, SYMBOLS, SHADINGS, COLORS)))
