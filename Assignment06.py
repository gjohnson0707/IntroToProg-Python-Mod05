# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using dictionaries, files, exception handling,and adds the use of functions,
# classes, and using the separation of concerns pattern
# Change Log: (Who, When, What)
# Gjohnson,8/03/2024,Created Script
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

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.

class FileProcessor:
    '''FileProcessor contains all functions that read and or write to the file'''
    @staticmethod
    def read_data_from_file(file_name: str) -> [dict]:
        '''
        This function reads JSON information from the specified file
        :param FILE_NAME: a string indicating the file name
        :return: The student table which is of type list[dict]
        '''
        file = None
        student_data: list[dict] = []
        try:
            # Extract the data from the file
            file = open(file_name, "r")
            student_data += json.load(file)
            file.close()
            for student in students:
                IOProcessor.output_student_courses(
                    f"Student [{student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']}] \n")

        except FileNotFoundError as e:  # Error handling when file is not found
            IOProcessor.output_error_message('Text file not found', e)
            IOProcessor.output_error_message('Creating file as file does not exist')
            open(file_name, "w")
            json.dump(student_data, file)

        except json.decoder.JSONDecodeError as e:  # Error handling when data in file is incorrect
            IOProcessor.output_error_message('JSON data is file is not valid', e)
            IOProcessor.output_error_message('Resetting it...')
            file = open(FILE_NAME, "w")
            json.dump(student_data, file)

        except Exception as e:  # Error handling for all other errors not listed above
            IOProcessor.output_error_message('Unhandled exception', e)

        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(student_data: list[dict], file_name: str) -> bool:
        '''
        This function writes data to the specified file
        :param student_data: student table which is of type list[dict]
        :param file_name: a string indicating the file name
        :return: True if the data was written to file, False otherwise
        '''
        file = None
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            IOProcessor.output_error_message("The following data was saved to file!")
            IOProcessor.output_student_courses(student_data)
            file.close()
            return True

        except TypeError as e:  # Error handling for JSON Values
            IOProcessor.output_error_message('JSON data was malformed', e)
        except Exception as e:  # Error handling exceptions
            IOProcessor.output_error_message('Unhandled exception', e)
        finally:
            if not file.closed:
                file.close()
        return False

class IOProcessor:
    '''IOProcessor contains all functions that prints to user including print statements and error handling'''
    @staticmethod
    def output_error_message(message: str, exception: Exception = None):
        '''
        This function prints out the specified message
        :param message: the message to print
        :param exception: the exception to print
        '''
        print(message)
        if exception is not None:
            print('---Technical Information---')
            print(exception, exception.__doc__, type(exception), sep='\n')

    @staticmethod
    def output_student_courses(student_data: list[dict]) -> None:
        '''
        Displays information regarding students
        :param student_data: The list of students data
        '''
        for student in student_data:
            print(f"Student {student['student_first_name']} {student['student_last_name']} is enrolled in {student['course_name']} \n")
        print("-" * 50)

    @staticmethod
    def output_menu(menu: str) -> str:
        '''
        This function returns the menu options entered by the user
        :param menu: the menu options entered by the user
        :return: the menu options entered by the user
        '''
        menu_choice = input(menu)
        while menu_choice not in ("1", "2", "3", "4"):
            IOProcessor.output_error_message('please enter an option 1,2,3,4')
            menu_choice = input(menu)
        return menu_choice

    @staticmethod
    def get_input(message: str) -> str:
        '''
        Gets the input from the user
        :param message: the messages to print
        :return: users input
        '''
        return input(message)

    @staticmethod
    def input_student_data(student_data: list[[dict]]) -> list[dict]:
        '''
        Gathers information required for each student: first name, last name and course name
        :rtype: object
        :param student_data: Add student table
        :return: the students table which is of type list[dict]
        '''
        try:  # Error handling
            student_first_name = IOProcessor.get_input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError(
                    "Student First Name must be alpha characters only")  # Error handling for numerics in name

            student_last_name = IOProcessor.get_input("Enter the student's last name: ")
            if not student_last_name.isalpha():  #
                raise ValueError(
                    "Student First Name must be alpha characters only")  # Error handling for numerics in name

            course_name = IOProcessor.get_input("Please enter the name of the course: ")
            new_student = {'student_first_name': student_first_name, 'student_last_name': student_last_name,
                            'course_name': course_name}
            student_data.append( new_student)
        except ValueError as e:
            IOProcessor.output_error_message(str(e), e)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        return student_data

students = FileProcessor.read_data_from_file(FILE_NAME)

IOProcessor.output_student_courses(students)

while True:
    menu_choice = IOProcessor.output_menu(MENU)

    if menu_choice == "1":  # This will not work if it is an integer!
        try:  # Error handling
            students = IOProcessor.input_student_data(student_data=students)

        except ValueError as e:
            IOProcessor.output_error_message(e)
        except Exception as e:  # Catch any other unexpected exceptions
            IOProcessor.output_error_message("An unexpected error occurred", e)

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        IOProcessor.output_student_courses(student_data=students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(student_data=students, file_name=FILE_NAME)

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        IOProcessor.output_error_message("Please only choose option 1, 2, or 3")

print("Program Ended")