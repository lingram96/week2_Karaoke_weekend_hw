from src.guest import Guest


class Room:
    
    def __init__(self, capacity, fee):
        self.songs = []
        self.guests = []
        self.capacity = capacity
        self.fee = fee 

    def guest_count(self):
        return len(self.guests)

    def check_in(self, guest):
        if len(self.guests) <= self.capacity:
            self.guests.append(guest)
            guest.money -= self.fee

    def add_song(self, song):
        self.songs.append(song)

    # def add_guest(self, new_guest):
    #     self.guests = []
    #     self.guests.append(new_guest)

    def remove_guest(self, guest):
        if guest == guest.name:
         self.guests.remove(guest)



        
        
