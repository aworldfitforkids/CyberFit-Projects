#!/usr/bin/python3

###############################################################
#Let the use know what the program does and what info it needs#
###############################################################
print("Welcome to Mr. BMI")
print("Enter your height. First enter feet then inches")


#########################################################################
#Get height in feet and inches, if it is only inches then put 0 for feet#
#########################################################################
feet= input("Feet: ")
inches= input("Inches: ")


######################
#Get weight in pounds#
######################
print("Enter your weight in pounds")
weight= input("Pounds: ")


############################################
#convert into kilograms and meters  squared#
#1meter=39.3701 inches                     #
#1kg = 2.2 pounds                          #
#use int() to convert string to integer    #
############################################
feet2inches= int(feet) * 12
totalinches= int(inches) +  feet2inches
meters= (totalinches / 39.3701)
kilograms =  int(weight) / 2.2

###############
#calculate bmi#
###############
bmi = kilograms / (meters * meters)

#######################
#round to two decimals#
#######################
bmi = round(bmi,2)


####################################################
#Create a list to hold the different health status'#
####################################################
chartlist = ['Underweight','Healthy','Overweight','Obese','Extreme Obese']


###################################
#Initiate variable for conditional#
###################################
status=''


##########################################
#check bmi condition to get health status#
##########################################
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

		
###################################################################
#print out the results. Make sure to convert integers into strings#
###################################################################
print("Your BMI: " + str(bmi) + " and you are " + status)