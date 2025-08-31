# Plan is to create a BMI calculator for adults that print their health status based on their BMI value.
while True:
    print("Welcome to BMI Calculator")
    weight= float(input("Enter your weight in kg: "))
    height= float(input("Enter you height in meters: "))
    bmi= weight/(height**2)
    print("Your score is: ",bmi)
    if bmi<18.5:
        print("Please eat more, you are underweight")
    elif 18.5 <= bmi < 24.9:
        print("You are healthy, keep it up")
    elif 25 <= bmi < 29.9:
        print("You are overweight, please exercise more")
    break   