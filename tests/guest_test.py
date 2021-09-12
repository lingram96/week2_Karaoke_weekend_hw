import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Donald Trump", 500)

    def test_guest_has__name(self):
        self.assertEqual("Donald Trump", self.guest.name)

    def test_guest_has__money(self):
        self.assertEqual(500, self.guest.money)

    # def test_guest_has__favourite_song(self):
    #     self.assertEqual("Mamma Mia", self.guest1.favourite_song)