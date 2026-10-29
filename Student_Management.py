

class Student_manage:

    # initiate method for repeted object creation 
    def __init__(self):
        self.All_Student=[]

    # Adding new student  
    def Add_Student(self,Std_details):
        self.Std_details=Std_details
        self.All_Student.append(Std_details)
        print("The student Details Added Successfully!...")

    # Display All Student Datas  
    def ViewAll_Student(self):
        print(" --The All Student Database-- ")
        print(self.All_Student)

    # Searching Student and print that Student details
    def Search_Student(self):
        print("Search Student Enter the Student Roll Number")
        self.Srh_Roll=int(input("Rolle Number: "))
        self.found=False
        for student in self.All_Student:
            if self.Srh_Roll == student["Roll_No"]:
                self.found=True
                break
        if self.found:
            print("Yes the Student Data Available!...")
            print(student)
        else:
            print("Student Data Not Available!...")

    # Update perticular Student Datas
    def Update_Student(self):
        print("--Please Enter the Roll Number for which Student Data need to Update--")
        self.Sch_Up_Std=int(input("Roll Number: "))
        self.dfound=False
        for student in self.All_Student:
            if self.Sch_Up_Std == student["Roll_No"]:
                self.dfound=True
                break
        if self.dfound:
            self.U_Std=student
            print("The Student ",self.Sch_Up_Std," is Avilable please check the student details and chhose the ubdate option!...")
            print(self.U_Std)
            print("1. Roll Number \n2. Name \n3. Age \n4. department \n5. Year \n6. Phone ")
            self.Up_Option=int(input("Enter the Option Number: "))
            while self.Up_Option>0 and self.Up_Option<7:
                match self.Up_Option:
                    case 1:
                        self.Up_RollNo=int(input("Enter Update Roll Number: "))
                        self.U_Std["Roll_No"]=self.Up_RollNo
                        print("Check the Updated data ")
                        print(self.U_Std)
                        print("Please Type 'Y'  You Want to Save update. Type 'N' for Again ")
                        self.Save=str(input())
                        if self.Save in'Yy':
                            break
                        else:
                            continue
                    case 2:
                        self.Up_Name=str(input("Enter Update Name: "))
                        self.U_Std["Name"]=self.Up_Name
                        print("Check the Updated data ")
                        print(self.U_Std)
                        print("Please Type 'Y'  You Want to Save update. Type 'N' for Again ")
                        self.Save=str(input())
                        if self.Save in'Yy':
                            break
                        else:
                            continue
                    case 3:
                        self.Up_Age=int(input("Enter Update Age: "))
                        self.U_Std["Age"]=self.Up_Age
                        print("Check the Updated data ")
                        print(self.U_Std)
                        print("Please Type 'Y'  You Want to Save update. Type 'N' for Again ")
                        self.Save=str(input())
                        if self.Save in'Yy':
                            break
                        else:
                            continue
                    case 4:
                        self.Up_Dept=str(input("Enter Update Department: "))
                        self.U_Std["Department"]=self.Up_Dept
                        print("Check the Updated data ")
                        print(self.U_Std)
                        print("Please Type 'Y'  You Want to Save update. Type 'N' for Again ")
                        self.Save=str(input())
                        if self.Save in'Yy':
                            break
                        else:
                            continue
                    case 5:
                        self.Up_Year=int(input("Enter Update Year: "))
                        self.U_Std["Year"]=self.Up_Year
                        print("Check the Updated data ")
                        print(self.U_Std)
                        print("Please Type 'Y'  You Want to Save update. Type 'N' for Again ")
                        self.Save=str(input())
                        if self.Save in'Yy':
                            break
                        else:
                            continue
                    case 6:
                        self.Up_Phone=int(input("Enter Update Phone Number: "))
                        self.U_Std["Phone"]=self.Up_Phone
                        print("Check the Updated data ")
                        print(self.U_Std)
                        print("Please Type 'Y'  You Want to Save update. Type 'N' for Again ")
                        self.Save=str(input())
                        if self.Save in'Yy':
                            break
                        else:
                            continue
        else:
            print("Please Enter Valid Roll Number The Student Data Not Available!...")

    # Delete Perticular Student 
    def Delete_Student(self):
        print("--Please Enter the Roll Number for which Student need to Delete--")
        self.delete_Std=int(input("Roll Number: "))
        self.dfound=False
        for student in self.All_Student:
            if self.delete_Std == student["Roll_No"]:
                self.dfound=True
                break
        if self.dfound:
            self.All_Student.remove(student)
            print("The Student ",self.delete_Std," is Deleted Successfully!...")
        else:
            print("Please Enter Valid Roll Number The Student Data Not Available!...")


# class Object create and calling
Std_Menu=Student_manage()

# Menu Dhashbord
while True:
    print(" --STUDENT MANAGEMENT SYSTEM-- ")
    print("1. Add Student \n2. View All Student \n3. Search Student \n4. Update Student \n5. Delete Student \n6. Exit \nEnter the Menu Number for which Menu you choose...")
    option=int(input("Enter Your Menu: "))
    
    if option>0 and option<7:
        match option:
            case 1:
                    print(" --Please give bellow Details-- ")
                    roll_num=int(input("Roll Number: "))
                    Std_name=str(input("Name: "))
                    Std_age=int(input("Age: "))
                    Std_dept=str(input("Department: "))
                    Std_year=int(input("Year: "))
                    Std_Phone=int(input("Phone Number: "))
                    Std_details={"Roll_No":roll_num,
                                  "Name":Std_name,
                                  "Age":Std_age,
                                  "Department":Std_dept,
                                  "Year":Std_year,
                                  "Phone":Std_Phone}
                    Std_Menu.Add_Student(Std_details)
        
            case 2:
                Std_Menu.ViewAll_Student()
            case 3:
                Std_Menu.Search_Student()
            case 4: 
                Std_Menu.Update_Student()
            case 5:
                Std_Menu.Delete_Student()
            case 6:
                print("Loguot Successfull!...")
                break
        
    else:
        print("Please enter valuable option")
        