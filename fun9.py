def book_flight(name, flight_no, **details):
    print("Booking Confirmation for : ",name)
    print(f"Flight Number: ",flight_no)
    print("-----------------------------")
    for key, value in details.items():
        print(f"{key.capitalize():15}:{value}")
    print("------------------------------")
    print("Flight booked successfully!\n")

# Booking flight with extra info using keyword arguments
book_flight("Bal Krishna yadav", "AI203",
            date="2025-04-15",
            seat="12A",
            destination="Delhi",
            meal_preference="Vegetarian",
            baggage="20kg")

book_flight("Ravina yadav", "AI204",
            date="2025-04-16",
            seat="14C",
            destination="Mumbai",
            baggage="15kg")
