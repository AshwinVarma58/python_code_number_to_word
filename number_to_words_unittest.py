
import unittest
import number_to_words

class number_to_word_test(unittest.TestCase):

    def test_decimal(self):
        self.assertEqual(number_to_words.numberToWord(123456.78),'Rs. one Lakh twenty three thousand four hundred and fifty six 78/100 only')

    def test_range(self):
        self.assertEqual(number_to_words.numberToWord(119934578.243),
                         'number out of range')

    def test_integer(self):
        self.assertEqual(number_to_words.numberToWord(1191212), 'Rs. eleven Lakh ninety one thousand two hundred and twelve only')

    def test_format(self):
        self.assertEqual(number_to_words.numberToWord("lknlkjoids"), 'string must be number')

    def test_two_digit_number(self):
        self.assertEqual(number_to_words.numberToWord(99),'Rs. ninety nine only')

    def test_one_digit_number(self):
        self.assertEqual(number_to_words.numberToWord(9),'Rs. nine only')

    def test_three_digit_number(self):
        self.assertEqual(number_to_words.numberToWord(999),'Rs. nine hundred and ninety nine only')

    def test_three_digit__hundred_only_number(self):
        self.assertEqual(number_to_words.numberToWord(900),'Rs. nine hundred only')

if __name__ == '__main__':
    unittest.main()
