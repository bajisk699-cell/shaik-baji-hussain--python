slots=list(map(str,input("slots:").split()))
time_slots=input("time slots:")
print(f"slot already booked"if  time_slots in slots else f"slot is available")