# Step 1: ask user for daily calorie limit
cal_limit = int(input("Enter your daily calorie limit: "))

# Step 2: collect inputs as list 
meals = []
cals = []

while True:
    meal = input("Enter meal name (or type 'done' to finish): ")
    if meal.lower() == "done":
        break
    cal = int(input(f"Enter calories for {meal}: "))

    meals.append(meal)
    cals.append(cal)

# Step 3: compute total & average
total_cal = sum(cals)
avg_cal = total_cal / len(cals) 

# Step 4: show report
print("\n--- Daily Calorie Report ---")
for i in range(len(meals)):
    print(meals[i], ":", cals[i], "kcal")

print("-----------------------------")
print("Total calories   :", total_cal)
print("Average calories :", avg_cal)

# Step 5: warning if limit exceeded
if total_cal > cal_limit:
    print("Warning: Daily calorie limit exceeded!")
else:
    print("Within daily limit.")
#Step 6: to save the session log in plain text file 
f=open("Daily calorie intake.txt","w")
f.write()

