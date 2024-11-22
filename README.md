This code implements a **student performance tracking system** using Object-Oriented Programming (OOP) in Python. It consists of three main classes: `Student`, `PerformanceTracker`, and `MenuManager`. Here's a detailed explanation of how each part of the code works:

### 1. `Student` Class
The `Student` class is responsible for storing information about individual students, including their roll number, name, marks in computer science (CS) and mathematics, percentage, and grade.

#### Attributes:
- **`roll_number`**: The student's roll number (unique identifier).
- **`name`**: The student's name.
- **`cs_marks`**: Marks obtained in the Computer Science subject (out of 100).
- **`math_marks`**: Marks obtained in Mathematics (out of 100).
- **`percentage`**: The overall percentage of marks, calculated as the average of CS and Math marks.
- **`grade`**: The student's grade based on their percentage.

#### Methods:
- **`__init__()`**: The constructor method initializes the student's details and automatically calculates their percentage and grade.
- **`calc_percentage()`**: Calculates the percentage using the formula:
  \[
  \text{Percentage} = \frac{\text{cs\_marks} + \text{math\_marks}}{200} \times 100
  \]
- **`calc_grade()`**: Determines the student's grade based on the following criteria:
  - **A**: 91-100%
  - **B**: 75-90%
  - **C**: 60-74%
  - **D**: 50-59%
  - **F**: Below 50%

### 2. `PerformanceTracker` Class
The `PerformanceTracker` class manages multiple students. It allows adding, updating, deleting, and displaying student records.

#### Attributes:
- **`students`**: A dictionary that stores student objects using their roll numbers as keys.

#### Methods:
- **`add_student()`**: Adds a new student to the tracker by creating a `Student` object and storing it in the `students` dictionary.
- **`update_student_roll_number()`**: Updates a student's roll number.
- **`update_cs_marks()`**: Updates the CS marks of a student and recalculates their percentage and grade.
- **`update_math_marks()`**: Updates the Math marks of a student and recalculates their percentage and grade.
- **`update_student_info()`**: Updates the percentage and grade after modifying marks.
- **`delete_student()`**: Deletes a student's record based on their roll number.
- **`display_all_students()`**: Displays all student records in a tabular format.
- **`calculate_class_average()`**: Computes the class average percentage.

### 3. `MenuManager` Class
The `MenuManager` class handles the user interface for the performance tracker system. It manages enrolling students, displaying options, and updating student data based on user input.

#### Attributes:
- **`tracker`**: An instance of the `PerformanceTracker` class.

#### Methods:
- **`enroll_students()`**: Allows the admin to enroll up to 5 students initially by taking input from the user.
- **`display_menu()`**: Displays a menu with various options for updating student data, displaying records, and calculating the class average.
- **`update_roll_number()`**: Prompts the user to update a student's roll number.
- **`update_cs_marks()`**: Prompts the user to update a student's CS marks.
- **`update_math_marks()`**: Prompts the user to update a student's Math marks.
- **`delete_student()`**: Prompts the user to delete a student's record.

### 4. `main()` Function
The `main()` function serves as the entry point of the program:
1. It creates an instance of `PerformanceTracker`.
2. It creates an instance of `MenuManager` and uses it to:
   - Enroll students.
   - Display a menu with various options.

### How the Code Works
1. **Enrollment**:
   - The user is prompted to enter details for up to 5 students (roll number, name, CS marks, and Math marks).
   - Each student is stored as an instance of the `Student` class inside the `PerformanceTracker`.

2. **Menu Options**:
   - **1. Update Roll Number**: Allows the user to change a student's roll number.
   - **2. Update CS Marks**: Updates the CS marks for a student and recalculates their percentage and grade.
   - **3. Update Math Marks**: Updates the Math marks for a student and recalculates their percentage and grade.
   - **4. Delete a Student Record**: Removes a student's record based on their roll number.
   - **5. Display Records**: Displays all enrolled students along with their marks, percentage, and grade.
   - **6. Display Class Average**: Calculates and shows the average percentage of all students.
   - **7. Exit**: Ends the program.

### Example Run

```
Welcome to Admin Panel!
Enter the Roll No. of the student: 1
Enter the name of the student: John
Enter the marks of computer science within 100: 85
Enter the marks of Mathematics within 100: 90

Press 'Y' to enroll more students or 'N' to exit enrolling: n

Advance Menu:
1. Update Roll Number
2. Update CS Marks
3. Update Math Marks
4. Delete a Student Record
5. Display Records
6. Display Class Average
7. Exit

Enter your choice: 5

=================================================================================================
|   |Roll Number|   | Student name |   |CS Marks|    |Math Marks|    |Percentage|    |Grade|    |
|-----------------------------------------------------------------------------------------------|
|         1               John             85             90            87.50           B       |
=================================================================================================
```

### Key Features:
- **Object-Oriented Design**: Uses classes to encapsulate student data and functionality.
- **Modular Code**: Separates student management, data storage, and user interaction for easy maintenance.
- **Dynamic Updates**: Supports updating student details and recalculating grades dynamically.

This code is ideal for educational institutions to track student performance and can be extended with additional features like file storage or web integration.
