class ParkingGarage():

    def __init__(self):
        self.tickets = 9
        self.parkingSpaces = 9
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets > 0:
            print(f"\nWe currently have {self.tickets} spaces available! \nPrinting Ticket...")
            self.tickets += -1
            self.parkingSpaces += -1
        else:
            print("Sorry we have no parking spaces available at the moment!")


diante = ParkingGarage()

diante.takeTicket()

