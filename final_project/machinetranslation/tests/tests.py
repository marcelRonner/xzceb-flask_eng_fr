import unittest

from machinetranslation import translator

class TestTranslation(unittest.TestCase):
    def test_english_to_frenchNull(self):
        self.assertEqual("Text for translation is missing",english_to_french(""))
    
    def test_english_to_french(self):
        self.assertEqual("Bonjour",english_to_french("Hello"))
    
    def test_french_to_english_Null(self):
        self.assertEqual("Text for translation is missing",french_to_english(""))
    
    def test_french_to_english(self):
        self.assertEqual("Hello",french_to_english("Bonjour"))

if __name__ == '__main__':
    unittest.main()