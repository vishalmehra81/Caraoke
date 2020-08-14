import unittest
from classes.song import Song



class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1= Song("Sunoh", "Lucky Ali", 3.25, "Oh Sanam")
        self.song_2 = Song("Rockstar", "Mohit Chauhan", 4.00, "Saada Haq...")
        self.song_3 = Song("Kedarnath", "Amit", 5.25, "Namo Shankara...")
        self.song_4 = Song("Harry Met", "Arijit", 3.16, "Le jayen...")
        self.song_5 = Song("Agni", "Sonu", 4.05, "Abhi Mujh...")
        self.song_6 = Song("Kites", "KK", 6.00, "Zindagi Do...")

        self.song = [self.song_1, self.song_2,self.song_3,self.song_4,self.song_5,self.song_6]

    def test_song_has_name(self):
        self.assertEqual("Sunoh", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Lucky Ali", self.song.artist)

    def test_song_has_duration(self):
        self.assertEqual(3.25, self.song.duration)

    def test_song_has_lyrics(self):
        self.assertEqual("Oh Sanam", self.song.lyrics)