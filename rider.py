'''class Ride:
    def fare(self):
        print("Fare: 100")
class LuxuryRide(Ride):
    def fare(self):
        print("Fare: 300")
ride_type = input().strip()
if ride_type == "Luxury Ride":
    ride = LuxuryRide()
else:
    ride = Ride()
ride.fare()'''

'''class Student:
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 60")

class AdvancedStudent(Student):
    def placement_status(self):
        print("Placement Eligibility: Assessment Score Above 80")

# Test Case 1: Advanced Student
advanced = AdvancedStudent()
advanced.placement_status()

# Test Case 2: Regular Student
regular = Student()
regular.placement_status()'''


class Subscription:
    def features(self):
        print("Watch videos with advertisements")

class PremiumSubscription(Subscription):
    def features(self):
        print("Watch videos without advertisements")
user_input = input().strip()
if user_input == "Premium Plan":
    plan = PremiumSubscription()
    plan.features()
elif user_input == "Basic Plan":
    plan = Subscription()
    plan.features()