# This python file contains a class called ParkingGarage
# class ParkingGarage will be used for customers to "take tickets", "pay for parking", and "leave garage"


class ParkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket = False):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        self.tickets -= 1
        self.parkingSpaces -= 1
        print('Please take your ticket. ')
        print('Tickets left: ' + str(self.tickets) + '\nSpaces left: ' + str(self.parkingSpaces))

    def payForParking(self):
        payment = input('Please input the amount you are paying: $5, $10, $20 ')
        if int(payment) == 5 or int(payment) == 10 or int(payment) == 20:
            print('Thank you for your payment! You have 15 minutes to leave the garage. ')
            self.currentTicket = True
        else:
            print('I am sorry, this is not a valid response.')
            print('Please come back when you are ready to pay. :)')
        
    def leaveGarage(self):
        if user_x.tickets == 100:
            print('Have a nice day!')
        elif self.currentTicket == True:
            print('Thank you, have a nice day!')
            self.parkingSpaces += 1
            self.tickets += 1
            self.currentTicket = False
        elif self.currentTicket == False:
            print("I'm sorry, you have not paid your ticket yet.")
            self.payForParking()


user_x = ParkingGarage(100, 100)


def activate_PG():
    while True:
        response = input('What would you like to do? Get Ticket/Pay/Leave Garage/Show or Quit? ')
        if response.lower() == 'quit':
            print('You have now exited the program.')
            break
        elif response.lower() == 'show':
            print('Tickets left: ' + str(user_x.tickets) + '\nSpaces left: ' + str(user_x.parkingSpaces))
        elif response.lower() == 'get ticket':
            user_x.takeTicket()
        elif response.lower() == 'pay':
            if user_x.tickets == 100:
                print('There are no tickets to be paid for.')
            else:
                user_x.payForParking()
        elif response.lower() == 'leave' or response.lower() == 'leave garage':
            user_x.leaveGarage()
        else:
            print("I'm sorry, this is an invalid response. Please try again. ")


activate_PG()