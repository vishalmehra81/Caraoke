import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song



class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Bollywood", 3, 5, 10)
        self.room_2 = Room("Tollywood", 5, 10, 20)
        self.guest_1 = Guest("Abhi", 20, 30)
        self.guest_2 = Guest("Rakesh", 29, 20)
        self.guest_3 = Guest("Tarun", 40, 60)
        self.song_1 = Song("Sunoh", "Lucky Ali", 3.25, "Oh Sanam...")
        self.song_2 = Song("Rockstar", "Mohit Chauhan", 4.00, "Saada Haq...")
        self.song_3 = Song("Kedarnath", "Amit", 5.25, "Namo Shankara...")

        def test_room_has_name(self):
            self.assertEqual("Bollywood", self.room.name)

        def test_room_has_min_capacity(self):
            self.assertEqual("3", self.room.min_capacity)
        

        def test_room_has_cost(self):
            self.assertEqual("10", self.room.cost)


        def test_guest_check_in_room(self):
            guest = Guest("Abhi", 20, 30)
            self.room.check_in(guest)
            self.assertEqual(1, self.guest_count())

        def test_guest_check_out_room(self):
            guest = Guest("Abhi", 20, 30)
            self.room.check_in(guest)
            self.room.check_out(guest)
            self.assertEqual(0, self.guest_count())

        def test_room_can_add_a_song(self):
            self.room.add_song(self.song_1)
            self.assertEqual(1, self.room.total_song(self.song_1))

        def test_add_waiting_list(self):
            self.room.add_to_waiting_list(self,guest)
            self.assertequal(1,self.room.waiting_list_length())
            
