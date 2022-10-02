class ParkingGarage():

    def __init__(self):
        self.tickets = 9
        self.parkingSpaces = 9
        self.currentTicket = {}

    def takeTicket(self, name):
        if self.tickets > 0:
            print(f"\nHi {name.title()}! We currently have {self.tickets} spaces available! \n\nPrinting Ticket...You have ticket # {self.tickets}!")
            self.currentTicket[name] = {
                'ticket': self.tickets,
                'paid': False
            }           
            self.tickets += -1
            self.parkingSpaces += -1
        else:
            print("\nSorry we have no parking spaces available at the moment!")

    def payForParking(self, name):
        try:
            ticket = self.currentTicket[name]
            if ticket['paid'] == False:
                paid = input("\nPlease enter 15, to pay for ticket: ")
                if paid == '15':
                    print(f'\nYour ticket # {ticket["ticket"]} has been paid and you have 15 minutes to leave!')
                    ticket['paid'] = True
                    return
                else:
                    print("\nSorry! Invalid Input, please enter 15!")
                    self.payForParking(name)
            else:
                print('\nYour ticket is already paid.')
        except:
            print("\nYou do not currently have a ticket!")
            self.runParkingGarage()

    def leaveGarage(self, name):
        try:
            ticket = self.currentTicket[name]
            if ticket['paid'] == True:
                print('\nThank you, have a nice day!')
                self.tickets += 1
                self.parkingSpaces += 1
                self.currentTicket.pop(name)        
            else:
                print('\nPlease pay for your ticket!')
                self.payForParking(name)
                self.leaveGarage(name)
        except:
            print('\nYou do not currently have your car parked here!')

# ----- Main Program ---------- #

    def runParkingGarage(self):
        while True:
            print(f"\nWelcome to the parking garage!")
            response = input('\nWould you like to get a ticket ("Get"), pay for current ticket ("Pay") or leave ("Leave"): ')
            if response.lower() == 'get':
                name = input('\nWhat is your name? ').lower()
                if name in self.currentTicket:
                    print("\nYou already have a ticket!")
                    likeToPay = input('Would you like to pay? (Y/N) ').lower()
                    if likeToPay == 'y':
                        self.payForParking(name)
                        readyToLeave = input("\nAre you ready to leave as well? (Y/N) ").lower()
                        if readyToLeave == 'y':
                            self.leaveGarage(name)
                        elif readyToLeave == 'n':
                            print("\nYour ticket has been paid, so you are free to leave whenever! Just type 'Leave' at the main console!")     
                        else:
                            print('Invalid response! Try again!')
                    elif likeToPay == 'n':
                        print("\nOk! See you soon! Don't forget to pay!")
                    else:
                        print("Invalid Input! Please enter either 'Y' or 'N'")
                else:
                    self.takeTicket(name)
            elif response.lower() == 'pay':
                response2 = input("\nReady to Leave? (Y/N): ")
                if response2.lower() == 'y':
                    name = input('\nWhat is your name? ').lower()
                    self.payForParking(name)
                    self.leaveGarage(name)
                    continue
                if response2.lower() == 'n':
                    print("\nOk, see you soon!")
                    continue
                else:
                    print("\nInvalid Input! Start again.")
                    continue 
            elif response.lower() == 'leave':
                name = input('\nWhat is your name? ').lower()
                self.leaveGarage(name)
                continue 
            else:
                print("\nInvalid response. Please type either 'Get', 'Pay', or 'Leave'")



            

parkinggarage = ParkingGarage()

parkinggarage.runParkingGarage()
