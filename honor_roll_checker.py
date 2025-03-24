# Name: Mohamed Gaballa
# File: honor_roll_checker.py
# Description: This app takes student names and GPAs, and checks if they qualify
# for the Dean's List or the Honor Roll. It stops when the last name 'ZZZ' is entered.

while True:
    last_name = input("Enter the student's last name (or 'ZZZ' to exit): ")
    if last_name == 'ZZZ':
        break
    first_name = input("Enter the student's first name:  ")
    gpa = float(input("Enter the student's GPA: "))

    if gpa >= 3.5:
        print(first_name,last_name, "has made the dean's List.")
    elif gpa >= 3.25:
        print(first_name,last_name, "has made the Honor Roll.")
    else:
        print(first_name, last_name, "did not qualify for the Dean's List or Honor Roll.")







        
    

