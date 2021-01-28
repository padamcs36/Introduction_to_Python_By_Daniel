#Calculating the BMI
#using formulla weightInKilogram/ Height*height
# one pound = 0.45359237kg
# one inch = 0.0254 meters

OnePoundInKilogram = 0.45359237
OneInchInMeter = 0.0254

weight = eval(input("Enter weight in pounds: "))
height = eval(input("Enter height in inches: "))

weightInKilogram = weight * OnePoundInKilogram
heightInMeter = height * OneInchInMeter

#computing BMI
bmi = weightInKilogram / (heightInMeter * heightInMeter)
print("BMI is: ", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi > 18.5 and bmi < 24.9:
    print("Normal")
elif bmi > 25.0 and bmi < 29.9:
    print("Overweight")
else:
    print("Obese")