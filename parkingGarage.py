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

    def payForParking(self):
        paid = input("Please enter 15, to pay for ticket: ")
        if paid == '15':
            paid = 'Paid'
            print('Your ticket has been paid and you have 15 minutes to leave!')
            self.currentTicket[paid] = True
        else:
            print("Sorry! Invalid Input, please enter 15!")
            paid = self.payForParking()

    def leaveGarage(self):
        if self.currentTicket.values():
            print('Thank you, have a nice day!')
            self.tickets += 1
            self.parkingSpaces += 1
        else:
            print('Please pay for your ticket!')
            paid = self.payForParking()

# ----- Main Program ---------- #

    def runParkingGarage(self):
        while True:
            print("\nWelcome to the parking garage!")
            response = input('Would you like to purchase a ticket? (Y/N): ')
            if response.lower() == 'y':
                self.takeTicket()
            if response.lower() == 'n':
                print("Bye! Have a great day!")
                break
            else:
                print("Invalid response. Please type either 'Y' or 'N' ")
                self.runParkingGarage()


            

diante = ParkingGarage()

diante.takeTicket()


