import pickle

def create_records():
    file = open("students.dat", "wb")
    
    for i in range(10):
        print(f"\nEnter details for student {i+1}")
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        
        student = [roll, name, marks]
        pickle.dump(student, file)
    
    file.close()
    print("\n10 records saved successfully!")

def load_records():
    file = open("students.dat", "rb")
    
    print("\nStudent Records:\n")
    
    try:
        while True:
            student = pickle.load(file)
            print(f"Roll: {student[0]}, Name: {student[1]}, Marks: {student[2]}")
    
    except EOFError:
        file.close()
        print("\nAll records loaded.")

# Main program
create_records()
load_records()
