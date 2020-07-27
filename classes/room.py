class Room:
    def __init__(self,name, min_capacity, max_capacity, cost):
        self.name = name
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
        self.cost = cost
        self.guest_in_room = []
        self.waiting_list = []
        self.song_list = []

    def guest_count(self):
        return len(self.guest_in_room)

    def check_in(self,guest_to_add_in_room):
        self.guest_in_room.append(guest_to_add_in_room)

    def check_out(self, guest_to_remove_from_room):
        self.guest_in_room.remove(guest_to_add_in_room)

    def add_song(self,song):
        if song in self.song_list:
            self.song_list += 1
        
    def total_song(self,song):
        if song in self.song_list:
            return self.song_list(song)
        else:
            return 0

    def waiting_list_length(self):
        return len(self.waiting_list)
    
    def add_to_waiting_list(self,new_guest):
        self.waitlng_list.append(new_guest)
