#LEVEL 2- FILE HANDLING + OOP

# ===================
# STUDENT CLASS
# ===================

class Student:
    def __init__(self,name,roll_no,age,course,marks):  
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"{self.name},{self.roll_no},{self.age},{self.course},{self.marks}"
    
# =========================
# STUDENT MANAGEMENT CLASS
# =========================

class StudentManagementSystem:
     def __init__(self):
         self.students = []

        # ---------------
        # ADD STUDENT
        # ---------------

     def add_student(self):

         try:
             name = input("Enter student name: ")
             roll_no = int(input("Enter roll no: "))
             age = int(input("Enter age: "))
             course = input("Enter course: ")
             marks = float(input("Enter marks: "))

             student = Student(name, roll_no, age, course, marks)

             self.students.append(student)
             print("Student added successfully! ")

         except ValueError:
             print("Invalid input! ")

         # ----------------------
         # VIEW STUDENTS
         # ----------------------

     def view_students(self):

             if not self.students:
                 print("Student not found! ")
                 return
             print("\n---STUDENT LIST----")

             for student in self.students:
                  print(student)


         # -------------------
         # SEARCH STUDENT
         # -------------------

     def search_student(self):

          try:
               roll_no = int(input("Enter roll_no to search: "))

               for student in self.students:

                    if student.roll_no == roll_no:
                         print("\n student found! ")
                         print(student)
                         return

               print("Student not found! ")

          except ValueError:
               print("Invalid roll number! ")

            # ---------------
            # UPDATE STUDENT
            # ---------------

     def update_student(self):
          try:
               roll_no = int(input("Enter roll no to update: "))
               
               for student in self.students:
                    if student.roll_no == roll_no:
                         print("\n Enter new details! ")
               
                         student.name = input("Enter student name: ")
                         student.age = int(input("Enter age: "))
                         student.course = input("Enter course: ")
                         student.marks = float(input("Enter marks: "))
               
                         print("Student updated successfully! ")
                         return
               
               print("Student not found! ")


          except ValueError:
               print("Invalid input! ")


            # ---------------------
            # DELETE STUDENT
            # ---------------------


     def delete_student(self):

          try:
               roll_no = int(input("Enter roll no to delete: "))

               for student in self.students:

                    if student.roll_no == roll_no:

                         self.students.remove(student)

                         print("Student deleted successfully! ")
                         return

                    print("Student not found! ")

          except ValueError:
               print("Invalid roll number! ")


            # -------------------
            # SAVE TO FILE
            # -------------------

     def save_to_file(self):

          try:
               with open("students.txt", "w")as file:

                    for student in self.students:

                         file.write(f"{student.name}, {student.roll_no}, {student.age}, {student.course}, {student.marks}\n")

                         print("Students saved successfully! ")

          except Exception as e:
               print("Error while saving file:", e)


            # --------------------
            # LOAD FROM FILE
            # --------------------

            
     def load_from_file(self):

          try:
               with open("students.txt", "r") as file:

                    self.students.clear()

                    for line in file:

                         data = line.strip().split(",")

                         if len(data) == 5:
                              name = data[0]
                              roll_no = int(data[1])
                              age = int(data[2])
                              course = data[3]
                              marks = float(data[4])

                              student = Student(name,roll_no,age,course,marks)
                              self.students.append(student)

                    print("Students loaded from file successfully!")


          except FileNotFoundError:
               print("No saved student file found!")

          except Exception as e:
               print("Error while loading file:", e)


# ===============================
# MAIN PROGRAM
# ===============================

system = StudentManagementSystem()

system.load_from_file()  

while True:
        print("\n====================================================")
        print(" STUDENT MANAGEMENT SYSTEM")
        print("======================================================")

        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Students")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
             system.add_student()

        elif choice == "2":
             system.view_students()

        elif choice == "3":
             system.search_student()

        elif choice == "4":
             system.update_student()

        elif choice == "5":
             system.delete_student()

        elif choice == "6":
             system.save_to_file()

        elif choice == "7":
             system.save_to_file()
             print("Thank you for using Student Management System!")
             break

        else:
             print("Invalid choice! Please try again.")