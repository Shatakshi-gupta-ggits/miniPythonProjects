student = {}

while True:
    print("\n----STUDENT MANAGER APP-----")
    print("1. Add Student ")
    print("2. view Student ")
    print("3. Check Resuult ")
    print("4. Exit")
    
    
    choice = input("Enter your choice: ")
    
    #Add Student
    if choice == "1":
        name = input("Enter your choice : ")
        marks = marks(input("Enter marks: "))
        student[name] = marks #rahul 50
        print(f"{name} Successfully Added!")
        
    #view students
    elif choice == "2":
        if not student:
            print("No Student found!")
        else:
            for name, marks in student.items():
                print(name, " : ", marks)
                
    #check result
    elif choice == "3":
        name = input("Enter student name : ")
        
        if name in student:
            marks = student[name]
            
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
                
        else:
            print("studnet Not found")
            
            
    #exit
    elif choice == "4":
        print("Exiting .. .")
        break
    
    else:
        print("In-valid input")
    