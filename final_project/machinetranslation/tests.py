import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslationMethods(unittest.TestCase):

    def test_basic_translations(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

    def test_null_inputs(self):
        self.assertEqual(englishToFrench(), " ")
        self.assertEqual(frenchToEnglish(), " ")
    
    def test_using_not_equals(self):
        self.assertNotEqual(englishToFrench("Simple thing"), "Bonjour")
        self.assertNotEqual(frenchToEnglish("Wronge"), "Hello")

if __name__ == '__main__':
    unittest.main()