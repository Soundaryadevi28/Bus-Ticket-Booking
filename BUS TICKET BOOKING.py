print("\t\t\t\tWELCOME  to  MTC\n",'*'*70)
def bus_ticket_booking():
    stations = {
        'Chromepet': 1, 
        'Tambaram': 2, 
        'Perungalathur': 3, 
        'Vandalur': 4, 
        'Kilambakkam': 5
    }
    
    fare_per_stop = 5 

    print("\nAvailable Stations:", ", ".join(stations.keys()))
    
    start = input("Enter Start Station: ").strip().title()
    end = input("Enter Destination: ").strip().title()

    if start in stations and end in stations:
        no_of_stops = abs(stations[end] - stations[start])
        
        total_fare = no_of_stops * fare_per_stop
        
        age = int(input("Enter age: "))
        if age < 8:
            total_fare = total_fare * 0.8  
            
        print("\n" + "="*20)
        print("   WELCOME TO MTC")
        print("="*20)
        print(f"FROM: {start}")
        print(f"TO:   {end}")
        print(f"Fare: {total_fare} Rs")
        print("="*20)
    else:
        print("\nError: Invalid Station Name.")
        print("Please ensure you spelled it correctly as shown in the list.")

if __name__ == "__main__":
    bus_ticket_booking()
