weight = int(input("enter your weight"))
height = int(input("enter your height"))

BMI = (weight)/(height/100)**2

print("your BMIZ is " , BMI)

if (BMI < 18.4):
    print("you are under weiht")
elif (BMI <= 24.9):
    print("you are healthy") 
elif (BMI <= 29.9):
    print("you are overweight")
elif (BMI <= 34.9):
    print("you are obese")
elif (BMI <= 39.9):
    print("you are sererly obese")
     

 
