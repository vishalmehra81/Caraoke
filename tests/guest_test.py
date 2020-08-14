import unittest

from classes.guest import Guest
from classes.room import Room
from classes.song import Song


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.room = Room("Bollywood", 3, 5, 10)
        self.song = Song("Sunoh", "Lucky Ali", 3.25, "Oh Sanam...")
        self.guest = Guest("Karan", 35, 50)
        # self.guest_2 = Guest("Vijay", 25, 30)
        
    def test_guest_has_name(self):
        self.assertEqual("Karan", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(35, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_entry_fee_reduces_wallet(self):
        self.guest.entry_fee(10)
        self.assertEqual(40, self.guest.wallet)
  
    