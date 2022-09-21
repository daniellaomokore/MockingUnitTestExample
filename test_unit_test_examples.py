from unittest import mock
from unittest import TestCase, main
from unit_test_examples import increment_line_number



class TestIncrementLineNumber(TestCase):
    #Note-- @mock.patch('[insert name of python file the function you are testing from is called].[Insert name of the function you are using mock/fake data from is called]')
    @mock.patch('unit_test_examples.get_file_content')
    def test_mock_file_read_function(self, mock_get_file_content):

        content = [
            '1. Hello',
            '2. Hi',
            '3. Good morning',
            ]

        mock_get_file_content.return_value = content
        self.assertEqual(increment_line_number('some_file'),4)


if __name__ == '__main__':
    main()



