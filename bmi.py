#!/usr/bin/python3
print("Welcome to Mr. BMI")
print("Enter your height. First enter feet then inches")
#
feet= input("Feet: ")
inches= input("Inches: ")

print("Enter your weight in pounds")
weight= input("Pounds: ")


#convert into kilograms and meters  squared
#1meter=39.3701 inches
#1kg = 2.2 pounds
feet2inches= int(feet) * 12
totalinches= int(inches) +  feet2inches
meters= (totalinches / 39.3701)
kilograms =  int(weight) / 2.2

#calculate bmi
bmi = kilograms / (meters * meters)

#round to two decimals
bmi = round(bmi,2)

chartlist = ['Underweight','Healthy','Overweight','Obese','Extreme Obese']

status=''

if bmi<=18:
        status = chartlist[0]
elif bmi>18 and bmi<=24:
        status = chartlist[1]
elif bmi>24 and bmi<=29:
        status = chartlist[2]
elif bmi>29 and bmi<=39:
        status= chartlist[3]
else:
        status = chartlist[4]

print("Your BMI: " + str(bmi) + " and you are " + status)