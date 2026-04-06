def add_student():
    try:
        with open("student_records.txt", "a") as f:
            sid = input("Enter ID: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")

            f.write(f"{sid},{name},{marks}\n")
            print("✅ Student record added")

    except PermissionError:
        print("❌ File write permission denied")

    except Exception as e:
        print("❌ Error:", e)
def view_students():
    try:
        with open("student_records.txt", "r") as f:
            data = f.read()

            if data == "":
                print("⚠️ No records found")
            else:
                print("📄 Student Records:")
                print(data)

    except FileNotFoundError:
        print("❌ File not found")

    except Exception as e:
        print("❌ Error:", e)
def search_student():
    try:
        sid = input("Enter ID to search: ")
        found = False

        with open("student_records.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")

                if data[0] == sid:
                    print("✅ Student Found:")
                    print("ID:", data[0])
                    print("Name:", data[1])
                    print("Marks:", data[2])
                    found = True
                    break

        if not found:
            print("❌ Student not found")

    except FileNotFoundError:
        print("❌ File does not exist")

    except Exception as e:
        print("❌ Error:", e)
        
##Main menu controler 
while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("👋 Exiting program")
        break
    else:
        print("❌ Invalid choice")
