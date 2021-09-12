import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Nothing Else Matters", "Metallica")

    def test_song_has__title(self):
        self.assertEqual("Nothing Else Matters", self.song.title)

    def test_song_has__artist(self):
        self.assertEqual("Metallica", self.song.artist)

    