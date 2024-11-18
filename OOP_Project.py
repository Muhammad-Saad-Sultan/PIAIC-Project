class Student:
    def __init__(self, roll_number, name, cs_marks, math_marks):
        self.roll_number = roll_number
        self.name = name
        self.cs_marks = cs_marks
        self.math_marks = math_marks
        self.percentage = self.calc_percentage()
        self.grade = self.calc_grade()

    def calc_percentage(self):
        return ((self.cs_marks + self.math_marks) / 200) * 100

    def calc_grade(self):
        wp = self.percentage
        if 91 <= wp <= 100:
            return 'A'
        elif 75 <= wp <= 90:
            return 'B'
        elif 60 <= wp < 75:
            return 'C'
        elif 50 <= wp < 60:
            return 'D'
        else:
            return 'F'


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_number, name, cs_marks, math_marks):
        self.students[roll_number] = Student(roll_number, name, cs_marks, math_marks)

    def update_student_roll_number(self, old_roll, new_roll):
        if old_roll in self.students:
            student = self.students.pop(old_roll)
            student.roll_number = new_roll
            self.students[new_roll] = student
            print("Roll Number updated successfully.\n")
        else:
            print(f"Student with Roll Number {old_roll} not found.")

    def update_cs_marks(self, roll_number, new_marks):
        if roll_number in self.students:
            self.students[roll_number].cs_marks = new_marks
            self.update_student_info(roll_number)
        else:
            print(f"Student with Roll Number {roll_number} not found.")

    def update_math_marks(self, roll_number, new_marks):
        if roll_number in self.students:
            self.students[roll_number].math_marks = new_marks
            self.update_student_info(roll_number)
        else:
            print(f"Student with Roll Number {roll_number} not found.")

    def update_student_info(self, roll_number):
        student = self.students[roll_number]
        student.percentage = student.calc_percentage()
        student.grade = student.calc_grade()

    def delete_student(self, roll_number):
        if roll_number in self.students:
            del self.students[roll_number]
            print("Record deleted successfully.")
        else:
            print(f"Student with Roll Number {roll_number} not found.")

    def display_all_students(self):
        print("=================================================================================================")
        print("|   |Roll Number|   | Student name |   |CS Marks|    |Math Marks|    |Percentage|    |Grade|    |")
        print("|-----------------------------------------------------------------------------------------------|")
        for student in self.students.values():
            print(f"|          {student.roll_number}\t\t {student.name}\t\t {student.cs_marks}\t\t{student.math_marks}\t\t{student.percentage:.2f}\t\t{student.grade}\t|")
        print("=================================================================================================")

    def calculate_class_average(self):
        total_percentage = sum(student.percentage for student in self.students.values())
        return total_percentage / len(self.students) if self.students else 0


class MenuManager:
    def __init__(self, tracker):
        self.tracker = tracker

    def enroll_students(self):
        max_students = 5
        print("\n\tWelcome to Admin Panel!\n")
        for _ in range(max_students):
            roll_number = int(input("Enter the Roll No. of the student: "))
            name = input("Enter the name of the student: ")
            cs_marks = float(input("Enter the marks of computer science within 100: "))
            math_marks = float(input("Enter the marks of Mathematics within 100: "))
            
            self.tracker.add_student(roll_number, name, cs_marks, math_marks)
            
            enroll_more = input("\nPress 'Y' to enroll more students or 'N' to exit enrolling: ").strip().lower()
            if enroll_more != 'y':
                break

    def display_menu(self):
        while True:
            print("\nAdvance Menu:")
            print("1. Update Roll Number")
            print("2. Update CS Marks")
            print("3. Update Math Marks")
            print("4. Delete a Student Record")
            print("5. Display Records")
            print("6. Display Class Average")
            print("7. Exit")

            choice = int(input("\nEnter your choice: "))
            
            if choice == 1:
                self.update_roll_number()
            elif choice == 2:
                self.update_cs_marks()
            elif choice == 3:
                self.update_math_marks()
            elif choice == 4:
                self.delete_student()
            elif choice == 5:
                self.tracker.display_all_students()
            elif choice == 6:
                print(f"Class Average Percentage: {self.tracker.calculate_class_average():.2f}")
            elif choice == 7:
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Try again.")

    def update_roll_number(self):
        old_roll = int(input("Enter the Roll Number of the student to update: "))
        new_roll = int(input("Enter the new Roll Number: "))
        self.tracker.update_student_roll_number(old_roll, new_roll)

    def update_cs_marks(self):
        roll_number = int(input("Enter the Roll Number of the student to update CS marks: "))
        new_marks = float(input("Enter the new CS marks within 100: "))
        self.tracker.update_cs_marks(roll_number, new_marks)

    def update_math_marks(self):
        roll_number = int(input("Enter the Roll Number of the student to update Mathematics marks: "))
        new_marks = float(input("Enter the new Mathematics marks within 100: "))
        self.tracker.update_math_marks(roll_number, new_marks)

    def delete_student(self):
        roll_number = int(input("Enter the Roll Number to delete: "))
        self.tracker.delete_student(roll_number)


def main():
    print("|====================================================|",
          "|                 Final OOP Project                  |",
          "|====================================================|",
          "|       Name       |       Muhammad Saad Sultan      |",
          "|====================================================|",
          "|      Roll No     |           PIAIC245902           |",
          "|====================================================|",
          "|       Batch      |                62               |",
          "|====================================================|", sep="\n")
    tracker = PerformanceTracker()
    menu_manager = MenuManager(tracker)
    menu_manager.enroll_students()
    menu_manager.display_menu()

if __name__ == "__main__":
    main()