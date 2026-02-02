
weekday = input("Enter the week day for January 1st (MO/TU/WE/TH/FR/SA/SU): ")
leapyear = input("Is it a leap year? (y/n): ")
elif weekday == "FR" and leapyear == "y":
noSaturdays = 52
noSaturdays = 53
if weekday == "SA":
else:
noSaturdays = 53

print("There are",noSaturdays,"Saturdays this year.")


