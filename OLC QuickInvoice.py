import openpyxl as excel
import tkinter
import os
from TutorialWindow import DisplayTutorial

# DisplayTutorial()

# Name:                             C10
# Address Line 1:                   D11
# Address Line 2:                   D12
# Phone:                            I10
# Email:                            I11
# Current Date (Month Day, Year):   C15
# Course:                           B24
# Cohort Number:                    B25
# Amount:                           G23

workbookObject = excel.load_workbook('TestBook.xlsx')
sheet = workbookObject.active

while True:
    try:
        print("Please enter the reviewer information. If there is a '*' by it, the field is required, if it does not, only enter information if not known.")
        print("If information is not known, just hit 'enter'\n")
        fullName = input("\tReviewer's Full Name*: ")
        reviewerFileName = fullName.split(" ")
        fullName = fullName[1] + ", " + fullName[0]
        course = input("\tCourse Name* (in the format of 'ABCD 1234'): ")
        courseRep = input("\tCourse Representative*: ")
        courseName = course + " - " + courseRep
        amount = float(input("\tPlease enter the reviewer amount*: "))
        break
    except:
        print("\nInvalid input. Please try again.\n")

try:
    informationKnown = True
    while informationKnown:
        choice = input("\n\tIs there more information known? (Y/N): "); choice.lower()
        if choice == "y":
            addressLine1 = input("\tReviewer's Address Line 1 (if known): ")
            addressLine2 = input("\tReviewer's Address Line 2 (if known): ")
            phone = input("\tReviewer's Phone Number (if known): ")
            email = input("\tReviewer's Email (if known): ")
            print("Values: ", fullName, courseName, amount, addressLine1, addressLine2, phone, email)
            break
        elif choice == "n":
            informationKnown = False
            print("Values: ", fullName, courseName, amount)
            break
        else:
            print("\nInvalid input. Please try again.")
except:
    print("\nThere was an error")

# Name:                             C10
# Address Line 1:                   D11
# Address Line 2:                   D12
# Phone:                            I10
# Email:                            I11
# Current Date (Month Day, Year):   C15
# Course:                           B24
# Cohort Number:                    B25
# Amount:                           G23

try:
    if informationKnown:
        sheet['C10'] = fullName
        sheet['D11'] = addressLine1
        sheet['D12'] = addressLine2
        sheet['I10'] = phone
        sheet['I11'] = email
        sheet['C15'] = "Month Day, Year"
        sheet['B24'] = courseName
        sheet['B25'] = "Cohort Number"
        sheet['G23'] = amount
    else:
        sheet['C10'] = fullName
        sheet['C15'] = "Month Day, Year"
        sheet['B24'] = courseName
        sheet['B25'] = "Cohort Number"
        sheet['G23'] = amount
except:
    print("There was an error appending the file.")

try:
    workbookObject.save('TestBook.xlsx')
except:
    print("There was an error saving the file.")