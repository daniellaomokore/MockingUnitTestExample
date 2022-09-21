from unittest import mock, TestCase
from sample import guess_number              # Import the function(s) you are testing from the python file it is in
#  EXAMPLE 1

class TestCorrectGuessNumber(TestCase):
    #  When writing your arguments for @mock.patch(" ")...
    #  You specify Where the function is USED Not Where it was Defined (as they might not be the same place)...
    #  In this case the 'roll_dice' function is Defined in the dice.py file BUT we actually USE it in the sample.py file so we use 'sample.roll_dice' and
    #  NOT 'dice.roll_dice' as the argument for @mock.patch(" ").
    @mock.patch("sample.roll_dice")
    def test_guess_number(self, mock_roll_dice):

        mock_roll_dice.return_value = 3      #  This is ESSENTIAL as you set here what you want your mocked function to return

        assert guess_number(3) == "You won!"           #  Version 1
        self.assertEqual(guess_number(3), "You won!")  #  Version 2
                                                       #  Both Version 1 and Version 2 Work. You can use either format to run your test, you don't need to use both

"""#  EXAMPLE 2

class TestCorrectGuessNumber(TestCase):

    @mock.patch("sample.roll_dice", return_value = 3)  #  Here in example 2 we write the return value directly in the patch thing
    def test_guess_number(self, mock_roll_dice):       #  Even though we wrote the return value directly in the patch thing on line 23 we still need a parameter next to
                                                       # 'self' on line 24 - It can say anything. We wrote : 'mock_roll_dice'

        assert guess_number(3) == "You won!"           #  Version 1
        self.assertEqual(guess_number(3), "You won!")  #  Version 2
                                                       #  Both Version 1 and Version 2 Work. You can use either format to run your test, you don't need to use both
"""

