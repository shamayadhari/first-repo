# Solar Energy Monitoring and Conservation System

generated = int(input("Enter solar energy generated today (kWh): "))
consumed = int(input("Enter household energy consumed today (kWh): "))

if generated == 0:
    print("Error: Generated energy cannot be zero.")
else:
    # Calculating efficiency
    efficiency = (consumed / generated) * 100
    print(f"\nEnergy Efficiency: {efficiency}%")

    # Giving feedback 
    if efficiency > 90:
        print(" Excellent usage! You are efficiently utilizing solar power.")
    elif 70 <= efficiency <= 90:
        print(" Moderate usage. Try to use more appliances during daytime.")
    else:
        print(" Low efficiency! Consider reducing consumption or cleaning your solar panels.")





        





