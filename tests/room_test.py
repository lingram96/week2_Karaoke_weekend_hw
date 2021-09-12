import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Nothing Else Matters", "Metallica")
        self.guest = Guest("Donald Trump", 50)
        self.guest2 = Guest("Barack Obama", 50)
        self.guest3 = Guest("George Bush", 50)
        self.guest4 = Guest("Bill Clinton", 50)
        self.guest5 = Guest("Ronald Reagan", 50)
        self.room = Room(5, 10)

    def test_room_has_guest(self):
        self.assertEqual("Donald Trump", self.guest.name)

    def test_room_has_song(self):
        self.room.add_song(self.song)
        self.assertEqual("Nothing Else Matters", self.song.title)

    # def test_room_can_add_guest(self):
    #     self.room.add_guest(self.guest)
    #     self.assertEqual(1, len(self.room.guests))

    def test_room_can_remove_guest(self):
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    def test_room_check_capacity(self):
        self.room.check_in(self.guest)
        self.room.check_in(self.guest2)
        self.room.check_in(self.guest3)
        self.room.check_in(self.guest4)
        self.room.check_in(self.guest5)
        self.assertEqual(5, self.room.guest_count())

    def test_room_fee(self):
        self.room.check_in(self.guest)
        self.assertEqual(40, self.guest.money)


 
   
 

