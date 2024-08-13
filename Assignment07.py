# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using set of data classes
# Change Log: (Who, When, What)
# Gjohnson,8/11/2024,Created Script
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
FILE_NAME: str = "Enrollments.json"

# TODO Create a Person Class
# TODO Add first_name and last_name properties to the constructor (Done)
# TODO Create a getter and setter for the first_name property (Done)
# TODO Create a getter and setter for the last_name property (Done)
# TODO Override the __str__() method to return Person data (Done)

class Person:
    def __init__(self, student_first_name, student_last_name):
        '''
        @param student_first_name:
        @param student_last_name:
        '''
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name
    @property
    def student_first_name(self)->str:
        '''
        Returns the first name of the student.
        @return: first name of student formatted
        '''
        return self._student_first_name.title()

    @student_first_name.setter
    def student_first_name(self, value: str):
        '''
        Sets the first name of the student and does validation.
        @param value: the value to set the first name of the student
        @return:
        '''
        if value.isalpha():
            self._student_first_name = value
        else:
            raise ValueError("Student First Name must be alpha.")

    @property
    def student_last_name(self)->str:
        '''
        Returns the last name of the student.
        @return: last name of the student formatted
        '''
        return self._student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value:str):
        '''
        Sets the last name of the student and does validation.
        @param value: value to set the last name of the student
        @return:
        '''
        if value.isalpha():
            self._student_last_name = value
        else:
            raise ValueError("Student Last Name must be alpha.")

    def __str__(self):
        '''
        String representation of the person.
        @return: returns the string as csv
        '''
        return f"{self.student_first_name} {self.student_last_name}"

# TODO Create a Student class the inherits from the Person class (Done)
# TODO call to the Person constructor and pass it the first_name and last_name data (Done)
# TODO add a assignment to the course_name property using the course_name parameter (Done)
# TODO add the getter for course_name (Done)
# TODO add the setter for course_name (Done)
# TODO Override the __str__() method to return the Student data (Done)

class Student(Person):
    def __init__(self, student_first_name: str, student_last_name:str,course_name:str):
        '''
        @param student_first_name:
        @param student_last_name:
        @param course_name:
        '''
        super().__init__(student_first_name, student_last_name)
        self.course_name = course_name

    @property
    def course_name(self) -> str:
        '''
        Returns the name of the course.
        @return: name of the course
        '''
        return self._course_name.title()

    @course_name.setter
    def course_name(self, value) -> None:
        '''
        Sets the name of the course.
        @param value: name of the course
        @return:
        '''
        self._course_name = value

    def __str__(self):
        '''
        String representation of the person.
        @return: returns the string as csv
        '''
        return f"{super().__str__()} {self.course_name}"




class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str) -> list[Student]:
        '''
        This function reads JSON information from the specified file
        :param FILE_NAME: a string indicating the file name
        :return: The student table which is of type list[dict]
        '''
        file = None
        dict_list: list[Student] = []
        try:
            # Extract the data from the file
            file = open(file_name, "r")
            dict_list = json.load(file)
        except FileNotFoundError as e:  # Error handling when file is not found
            IOProcessor.output_error_message('Text file not found', e)
            IOProcessor.output_error_message('Creating file as file does not exist')
            open(file_name, "w")
            json.dump(dict_list, file)

        except json.decoder.JSONDecodeError as e:  # Error handling when data in file is incorrect
            IOProcessor.output_error_message('JSON data is file is not valid', e)
            IOProcessor.output_error_message('Resetting it...')
            file = open(FILE_NAME, "w")
            json.dump(dict_list, file)

        except Exception as e:  # Error handling for all other errors not listed above
            IOProcessor.output_error_message('Unhandled exception', e)

        finally:
            if not file.closed:
                file.close()
        student_data: list[Student] = []
        for row in dict_list:
            student_data.append(Student(row['student_first_name'], row['student_last_name'], row['course_name']))
        return student_data

    @staticmethod
    def write_data_to_file(student_data: list[Student], file_name: str) -> bool:
        '''
        This function writes data to the specified file
        :param student_data: student table which is of type list[dict]
        :param file_name: a string indicating the file name
        :return: True if the data was written to file, False otherwise
        '''
        file = None
        try:
            dict_table: list[dict] = []
            for student in student_data:
                dict_table.append({'student_first_name':student.student_first_name,
                                   'student_last_name':student.student_last_name,
                                   'course_name':student.course_name
                                   }
                                  )
            file = open(file_name, "w")
            json.dump(dict_table, file)
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
            print(f"Student {student.student_first_name} {student.student_last_name} is enrolled in {student.course_name} \n")
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
    def input_student_data(student_data: list[Student]) -> list[Student]:
        '''
        Gathers information required for each student: first name, last name and course name
        :rtype: object
        :param student_data: Add student table
        :return: the students table which is of type list[dict]
        '''
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''
        student: Student
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
            new_student = Student(
                student_first_name= student_first_name,
                student_last_name=student_last_name,
                course_name=course_name)
            student_data.append(new_student)
        except ValueError as e:
            IOProcessor.output_error_message(str(e), e)

            IOProcessor.output_error_message(str(e), e)
        print(f"You have entered {student_first_name} {student_last_name} for {course_name}.")
        return student_data

    @staticmethod
    def input_data_to_table(student_data: list[Student]) -> list[Student]:
        '''
        Imports to table
        @param student_data:
        @return:
        '''
        return IOProcessor.add_data_to_table(student_data)

    @staticmethod
    def output_data_from_table(student_data: list[Student]):
        '''
        Outputs from table
        @param student_data:
        @return:
        '''
        for student in student_data:
            IOProcessor.output_student_courses(f'{student.student_first_name} {student.student_last_name} is registered for {student.course_name}.')


# Define the Data Variables
students: list[Student] = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


students: list[Student] = FileProcessor.read_data_from_file(file_name=FILE_NAME)

# Display the current student data
IOProcessor.output_student_courses(student_data=students)


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