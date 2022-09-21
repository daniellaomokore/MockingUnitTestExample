from dice import rollDice

def guessNumber(num):
    result = rollDice()    #here the function is calling another function to get it's return value - hence it's dependent on the other function
    if result == num:
        return "You won!"
    else:
        return "You lost!"
   