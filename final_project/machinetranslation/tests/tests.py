import unittest
from translator import english_to_french
from translator import french_to_english

class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Hello > Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Hello !-> Hello
        self.assertNotEqual(english_to_french('Hello'), 'Hello')
        # feeling good > se sentir bien
        self.assertEqual(english_to_french('feeling good'), 'Sensation de bien')
        # non-string entity > same number as string
        self.assertEqual(english_to_french(0), '0')

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        # Bonjour -> Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Bonjour !-> Bonjour
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')
        # None !> empty string
        self.assertNotEqual(french_to_english("None"), '')
        # non-string entity > same number as string
        self.assertEqual(french_to_english(0),'0')

unittest.main()



