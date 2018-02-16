from random import randint

def roll(dice_expression):
    """
    1d20+1d4-3
    => 5+2-3 (4)
    """
    if dice_expression.find('+') != -1 or dice_expression.find('-') != -1:
        return roll_multi(dice_expression)
    return str(partial_roll(dice_expression))

def roll_multi(dice_expression):
    partial_rolls = list()
    operations = list()
    total = 0
    # Split in parts
    while dice_expression:
        plus = dice_expression.find('+')
        minus = dice_expression.find('-')
        if (plus != -1 and plus < minus) or (plus != -1 and minus == -1):
            partial = dice_expression[:plus]
            dice_expression = dice_expression[plus+1:]
            operations.append('+')
        elif minus != -1:
            partial = dice_expression[:minus]
            dice_expression = dice_expression[minus+1:]
            operations.append('-')
        else:
            partial = dice_expression # only a number left
            dice_expression = None
            assert partial.isdigit()

        # roll
        if partial.find('d') != -1:
            partial_rolls.append(partial_roll(partial))
        else:
            partial_rolls.append(int(partial))

    # Add and subtract each part
    result = ""
    while partial_rolls:
        if operations:
            result += "{}{}".format(partial_rolls.pop(0), operations.pop(0))
        else:
            result += "{}".format(partial_rolls.pop(0))
    result += " ({})".format(eval(result)) # Should be secure, since we have washed the input quite nicely
    return result

def partial_roll(dice_expression):
    number, dice_type = dice_expression.split('d')

    assert number.isdigit()
    assert dice_type.isdigit()

    result = 0
    dice_type = int(dice_type)
    for dice in range(int(number)):
        result += randint(1, dice_type)
    return result

# Test
if __name__ == '__main__':
    print("mult: {}".format(roll('1d20+1d4-3')))
    print("mult: {}".format(roll('1d6-4')))
    print("single: {}".format(roll('1d20')))
