

class ParkingGarage():

    def __init__(self, name):
        self.tickets = 9
        self.parkingSpaces = 9
        self.currentTicket = {}
        self.name = name

    def takeTicket(self):
        if self.tickets > 0:
            print(f"\nWe currently have {self.tickets} spaces available! \nPrinting Ticket...")
            self.tickets += -1
            self.parkingSpaces += -1
            paid = 'Paid'
            self.currentTicket['Paid'] = False
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
            print(f"\nWelcome to the parking garage, {self.name.title()}!")
            response = input('Would you like to get a ticket ("Get") or pay for current ticket ("Pay") or ("Done") to go about your business: ')
            if response.lower() == 'get':
                self.takeTicket()
            elif response.lower() == 'pay':
                response2 = input("Ready to Leave? (Yes/No): ")
                if response2.lower() == 'yes':
                    self.payForParking()
                    self.leaveGarage()
                    break
                if response2.lower() == 'no':
                    print("Bye! Have a great day!")
                    break
            elif response.lower() == 'done':
                print(self.tickets)
                break
            else:
                print("Invalid response. Please type either 'Get', 'Pay', 'Done'")



            

diante = ParkingGarage('diante')
person2 = ParkingGarage('carla')
person3 = ParkingGarage('steph')
person4 = ParkingGarage('david')

diante.runParkingGarage()
person2.runParkingGarage()
