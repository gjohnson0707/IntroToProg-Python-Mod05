# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
# Gjohnson,7/26/2024,Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # changed from list to dictionary on 7/27
students: list = []  # a table of student data
json_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
try:

    # Extract the data from the file
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
    for student in students:
        print(
            f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']} \n")

except FileNotFoundError as e:  # Error handling when file is not found
    print('Text file not found')
    print('---Technical Information---')
    print(e, e.__doc__,type(e),sep='\n')
    print('Creating file as file does not exist')
    open(FILE_NAME, "w")
    json.dump(student_data, file)

except json.decoder.JSONDecodeError as e:  # Error handling when data in file is incorrect
    print('Data in file is invalid')
    print('---Technical Information---')
    print(e, e.__doc__,type(e),sep='\n')
    file = open(FILE_NAME, "w")
    json.dump(student_data, file)

except Exception as e:  # Error handling for all other errors not listed above
    print('Unhandled exception')
    print('---Technical Information---')
    print(e, e.__doc__,type(e),sep='\n')

finally:
    if not file.closed:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:  # Error handling
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student First Name must be alpha characters only")  # Error handling for numerics in name

            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha(): #
                raise ValueError("Student First Name must be alpha characters only")  # Error handling for numerics in name

            course_name = input("Please enter the name of the course: ")

            student_data = {'student_first_name': student_first_name, 'student_last_name': student_last_name, 'course_name': course_name}

            students.append(student_data)

            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            continue

        except ValueError as e:
            print(e)
            print("---Technical Information---")
            print(e, e.__doc__,type(e),sep='\n')

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']} \n")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()

        except TypeError as e: # Error handling for JSON Values
            print('JSON data was malformed')
            print('---Technical Information---')
            print(e, e.__doc__,type(e),sep='\n')

        except Exception as e:  # Error handling exceptions
            print('---Technical Information---')
            print(e, e.__doc__,type(e),sep='\n')

        finally:
            if not file.closed:
                file.close()

        print("The following data was saved to file!")
        for student in students:
            print(f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']} \n")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
