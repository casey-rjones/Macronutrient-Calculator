# This function adds two numbers 
def maintCalc(x, y):
   return (x * 10) * y

print("Select operation.")
print("1.Calculate Body Weight Maintenance")
print("2.Calculate Macros")

# Take input from the user 
choice = input("Enter choice(1 or 2): ")


 




if choice == '1':
   bodyWeight = int(input("Enter Body Weight (lbs): "))
   gender = (input("Enter Gender (M or F): "))
   height = int(input("Enter Height (inches): "))
   age = int(input("Enter Age: "))
   activityLevel = int(input("Enter Activity Level: "))
   print("Maintenance Calories:", maintCalc(bodyWeight,activityLevel))
elif choice == '2':
   bodyWeight = int(input("Enter Body Weight (lbs): "))
   gender = (input("Enter Gender (M or F): "))
   height = int(input("Enter Height (inches): "))
   age = int(input("Enter Age: "))
   activityLevel = int(input("Enter Activity Level: "))   
   print(num1,"-",num2,"=", subtract(num1,num2))

else:
   print("Invalid input")

