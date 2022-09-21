from dice import roll_dice


def guess_number(num):
    result = roll_dice()  # here the function is calling another function to get its return value - hence it's dependent on the other function
    if result == num:
        return "You won!"
    else:
        return "You lost!"


