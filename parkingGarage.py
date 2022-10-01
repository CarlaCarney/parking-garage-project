class ParkingGarage():

    def __init__(self):
        self.tickets = 9
        self.parkingSpaces = 9
        self.currentTicket = {}

    def runProgram(self):
        pass

    def takeTicket(self):
        if self.tickets > 0:
            print(f"\nWe currently have {self.tickets} spaces available! \nPrinting Ticket...")
            self.tickets += -1
            self.parkingSpaces += -1
        else:
            print("Sorry we have no parking spaces available at the moment!")

    def payForParking(self):
        paid = input("Please enter 15, to pay for ticket: ")
        if paid == '15':
            paid = 'Paid'
            print('Your ticket has been paid and you have 15 minutes to leave!')
            self.currentTicket[paid] = True
            print(self.currentTicket)
        else:
            print("Sorry! Invalid Input, please enter 15!")
            paid = self.payForParking()

    def leaveGarage(self):
        




diante = ParkingGarage()

diante.payForParking()

