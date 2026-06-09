class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name

class Booking:
    def __init__(self, customer, movie_name, ticket_price, number_of_tickets):
        self.customer = customer
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.number_of_tickets = number_of_tickets
        self.total_amount = 0.0

    def calculate_amount(self):
        self.total_amount = self.ticket_price * self.number_of_tickets
        return self.total_amount

    def generate_receipt(self):
        print("==================================================")
        print("              MOVIE BOOKING RECEIPT               ")
        print("==================================================")
        print(f"Customer Name  : {self.customer.customer_name}")
        print(f"Movie Name     : {self.movie_name}")
        print(f"Ticket Price   : {self.ticket_price} rs")
        print(f"Tickets Booked : {self.number_of_tickets}")
        print("--------------------------------------------------")
        print(f"Total Amount   : {self.calculate_amount()} rs")
        print("Booking Status : CONFIRMED")
        print("==================================================")

if __name__ == "__main__":
    c1 = Customer("Noah")
    booking1 = Booking(customer=c1, movie_name="Avengers", ticket_price=200, number_of_tickets=4)
    booking1.generate_receipt()
