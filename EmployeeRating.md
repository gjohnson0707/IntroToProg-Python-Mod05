### Overview
The Employee Ratings application is a Python-based program designed to manage and process employee performance ratings. This application demonstrates the use of classes and file handling in Python, structured into multiple modules. Users can add new employee ratings, view existing ratings, save ratings to a file, and exit the program.

### Files Included
1. **main.py**- The entry point of the application, managing user interactions and program flow.
2. **presentation_classes.py** - Contains classes for handling user input and output.
3. **data_classes.py** - Defines the data models used in the application.
4. **processing_classes.py** - Includes classes for processing and managing file operations.
5. **test_data_classes.py** - Contains unit tests for the data classes.
6. **test_processing_classes.py** - Contains unit tests for the processing classes.
7. **test_presentation_classes.py** - Contains unit tests for the presentation classes.
### Application Features
1. **Data Management**: Handle employee ratings with validation and error handling.
2. **File Operations**: Read from and write to a JSON file for data persistence.
3. **User Interaction**: Present a menu, handle user input, and display data.
4. **Error Handling**: Provide structured error handling throughout the application.
### Class Descriptions
## `Main`
    *  Purpose: The core of the application, handling the main flow and user interactions.
    *  Key Features:
        *  Loads existing employee data from a JSON file.
        *  Provides a menu for user choices.
        *  Allows users to add new employee ratings, view current data, and save data to a file.
        *  Exits the program based on user input.
## `presentation_classes.py`
    *  IOProcessor:
        *  Purpose: Manages all input and output operations.
        *  Methods:
            *   output_error_message(message: str, exception: Exception = None): Displays error messages.
            *   output_employee_data(employee_data: list): Displays employee data.
            *   output_menu(menu: str): Displays the menu.
            *   input_menu_choice() -> str: Prompts for and validates menu choice input.
            *   input_employee_data(employee_data: list): Prompts for and collects new employee data.
## `data_classes.py`
    *  Person:
        *  Purpose: Base class for storing personal information.
        *  Properties:
            *   first_name: Validates that the name consists of alphabetic characters.
            *   last_name: Validates that the name consists of alphabetic characters.
    *  Employee (inherits from Person):
        *  Purpose: Extends Person with employee-specific details.
        *  Properties:
            *   review_date: Validates that the date is in ISO format.
            *   review_rating: Ensures the rating is an integer between 1 and 5.
    *  Methods:
        *  to_dict(): Converts the employee object to a dictionary.
        *  from_dict(data: dict): Creates an employee object from a dictionary.
## `processing_classes.py`
    *  FileProcessor:
        *  Purpose: Handles reading from and writing to JSON files.
        *  Methods:
            *   read_data_from_file(file_name: str): Reads employee data from a file and returns a list of Employee objects.
            *   write_data_to_file(employee_data: list[data.Employee], file_name: str) -> bool: Writes employee data to a file in JSON format.
### Constants
1. **FILE_NAME**: The name of the JSON file used for data storage ("EmployeeRatings.json").
2. **MENU**: The string displayed to the user for menu options.
### Error Handling
1. **File Errors**: Handles file not found and JSON decoding errors.
2. **User Input**: Validates names, dates, and ratings.
3. **Data Serialization**: Manages issues with converting data to/from JSON.
### Acceptance Criteria
1. **Files Named**: Ensure all required files are included.
2. **Script Header**: Each file should have a header with title, description, change log, and author information.
3. **Constants and Variables**: Define FILE_NAME, MENU, and employee list.
4. **Classes and Methods**: Include FileProcessor, IOProcessor, Person, and Employee classes with required methods.
5. **Validation**: Implement validation for properties.
6. **Functions**: Include specific functions with proper error handling.
7. **Input/Output**: Correctly handle and validate user input and file operations.
8. **Testing**: Ensure all functionality is tested.
### Usage
1. **Run `main.py`**: Start the application.
2. **Choose from the Menu**:
    *  1: Enter new employee rating data.
    *  2: Show current employee rating data.
    *  3: Save data to a file.
    *  4: Exit the program.
### Testing
1. **Unit Tests**: Run `test_data_classes.py`, `test_processing_classes.py`, and `test_presentation_classes.py` to ensure code functionality.
2. **Manual Testing**: Test functionality by interacting with the application through the console or terminal.
