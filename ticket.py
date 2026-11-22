line = "~~~~~~~~~~~~~"
passenger_name = "John Doe"
destination = "New York"
ticket_price = 450.55
number_of_tickets = 4
is_available = True

print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: $", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Is Available:", is_available)

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(number_of_tickets))
print(type(is_available))


print(line)

total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount

print("\nTotal Cost: $", total_cost)
print("Discount: $", discount)
print("Final Cost: $", final_cost)

print(line)

print("Double the Ticket Price: $", ticket_price * 2)
print("Ticket Price after $50 increase: $", ticket_price + 50)
print("Half the Ticket Price: $", ticket_price / 2)

print(line)

print("\nIs ticket price under $500?", ticket_price < 500)
print("Are more than 3 tickets booked?", number_of_tickets > 3)
print("Is the destination New York?", destination == "New York")
print("Is the final cost more than or equal to $1000?", final_cost >= 1000)

print(line)

travel_message = f"Hello {passenger_name}, your trip to {destination} is confirmed. The total cost for {number_of_tickets} tickets is ${final_cost:.2f}. Thank you for choosing our service!"
print("\nTravel Message:", travel_message)

print("Destination in uppercase:", destination.upper())
print("Passenger name in lowercase:", passenger_name.lower())
print("First letter of destination:", destination[0])
print("Length of passenger name:", len(passenger_name))

print(line)

morning_ticket_price = 650
evening_ticket_price = 800

print("\nBefore swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)

morning_ticket_price, evening_ticket_price = evening_ticket_price, morning_ticket_price

print("\nAfter swapping:")
print("Morning Ticket Price: $", morning_ticket_price)
print("Evening Ticket Price: $", evening_ticket_price)

print(line)

print("\n==================== Ticket Summary ====================")
print("Passenger Name:", passenger_name)
print("Destination:", destination)
print("Ticket Price: $", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Is Available:", is_available)