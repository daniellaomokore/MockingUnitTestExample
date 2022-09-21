from unittest import mock
from sample import guessNumber

#in your '@mock.patch' you must enter the path of the place where the function is dependend on the other function ratehr than the original fucntion itself

@mock.patch("MockingUnitTestExample.sample.rollDice")
def test_guess_number(mockrollDice):
    mockrollDice.return_value = 3

    assert guessNumber(3) == "You won!"
