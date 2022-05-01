import unittest
from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test_translate_eng_to_fr(self):
        """Test to check english to french translation"""
        self.assertEqual(english_to_french("Hello, how are you today?")["translations"][0]["translation"], "Bonjour, comment vous êtes aujourd'hui?")
        
    def test_translate_eng_to_fr_hi(self):
        """Test to check english to french translation Hi"""
        self.assertEqual(english_to_french("Hi")["translations"][0]["translation"], "Salut")
    def test_translate_eng_to_fr_null(self):
        """Test to check english to french translation Null"""
        self.assertEqual(english_to_french(" ")["translations"][0]["translation"], " ")
    
    def test_translate_eng_to_fr_hello(self):
        """Test to check english to french translation Hello"""
        self.assertEqual(english_to_french("Hello")["translations"][0]["translation"], "Bonjour")

class Testfrench_to_english(unittest.TestCase):
    def test_translate_fr_to_eng(self):
        """Test to check french to english translation"""
        self.assertEqual(french_to_english("Bonjour, comment vous êtes aujourd'hui?")["translations"][0]["translation"], "Hello, how are you today?" )
        
    def test_translate_fr_to_eng_hi(self):
        """Test to check french to english translation Hi"""
        self.assertEqual(french_to_english("Salut")["translations"][0]["translation"], "Hi")
    def test_translate_eng_to_fr_null(self):
        """Test to check french to english translation Null"""
        self.assertEqual(french_to_english(" ")["translations"][0]["translation"], " ")
    
    def test_translate_eng_to_fr_hello(self):
        """Test to check french to english translation Hello"""
        self.assertEqual(french_to_english("Bonjour")["translations"][0]["translation"], "Hello")


unittest.main()