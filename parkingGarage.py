

class ParkingGarage():

    def __init__(self, name):
        self.tickets = 9
        self.parkingSpaces = 9
        self.currentTicket = {}
        self.name = name

    def takeTicket(self):
        if self.tickets > 0:
            print(f"\nWe currently have {self.tickets} spaces available! \n\nPrinting Ticket...You have ticket # {self.tickets}!")
            self.currentTicket[self.tickets] = False            
            self.tickets += -1
            self.parkingSpaces += -1
        else:
            print("\nSorry we have no parking spaces available at the moment!")

    def payForParking(self):
        try:
            if self.currentTicket[self.tickets + 1] == False:
                paid = input("\nPlease enter 15, to pay for ticket: ")
                if paid == '15':
                    print(f'\nYour ticket # {self.tickets + 1} has been paid and you have 15 minutes to leave!')
                    self.currentTicket[self.tickets + 1] = True
                    return
                else:
                    print("\nSorry! Invalid Input, please enter 15!")
                    self.payForParking()
        except:
            print("\nYou do not currently have a ticket!")
            self.runParkingGarage()

    def leaveGarage(self):
        try:
            if self.currentTicket[self.tickets + 1] == True:
                print('\nThank you, have a nice day!')
                self.tickets += 1
                self.parkingSpaces += 1
            elif self.currentTicket[self.tickets + 1] == False:
                print('\nPlease pay for your ticket!')
                self.payForParking()            
            else:
                print('\nPlease pay for your ticket!')
                self.payForParking()
        except:
            print('\nYou do not currently have your car parked here! You are free to leave! Goodbye!')

# ----- Main Program ---------- #

    def runParkingGarage(self):
        while True:
            print(f"\nWelcome to the parking garage, {self.name.title()}!")
            response = input('\nWould you like to get a ticket ("Get"), pay for current ticket ("Pay"), park your car ("Park") or leave ("Leave"): ')
            if response.lower() == 'get':
                self.takeTicket()
            elif response.lower() == 'pay':
                response2 = input("\nReady to Leave? (Yes/No): ")
                if response2.lower() == 'yes':
                    self.payForParking()
                    self.leaveGarage()
                    break
                if response2.lower() == 'no':
                    print("Bye! Have a great day!")
                    break
                else:
                    print("Invalid Input! Please type 'Yes' or 'No'")
                    self.runParkingGarage()
            elif response.lower() == 'park':
                if self.currentTicket:
                    break
                else:
                    print('\nYou have not purschased a ticket yet!')
            elif response.lower() == 'leave':
                self.leaveGarage()
                break
            else:
                print("\nInvalid response. Please type either 'Get', 'Pay', 'Park' or 'Leave'")



            

diante = ParkingGarage('diante')
person2 = ParkingGarage('carla')
person3 = ParkingGarage('steph')
person4 = ParkingGarage('david')

diante.runParkingGarage()
diante.runParkingGarage()


