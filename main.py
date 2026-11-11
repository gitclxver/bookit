
students = {}
bookings = {}

while True:
    print("\nWelcome To BookIt")
    print("1. Add a New Student Booking")
    print("2. View Existing Bookings")
    print("3. Cancel Booking")
    print("4. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        first_name = input("First name: ")
        last_name = input("Last name: ")

        level = input("Level (HS/Uni): ").strip().lower()

        if level in ["hs", "high school"]:
            subjects = ["math", "english", "science"]

        elif level in ["uni", "university"]:
            subjects = ["dsa", "dta"]

        else:
            print("Invalid education level.")
            continue

        print("Available subjects:", ", ".join(subjects))

        subject = input("Choose a subject: ").strip().lower()

        if subject not in subjects:
            print("Invalid subject.")
            continue

        date = input("Appointment date (YYYY-MM-DD): ")

        student_id = len(students) + 1

        students[student_id] = {
            "first_name": first_name,
            "last_name": last_name,
            "level": level,
        } 

        print(f"Student Added Successfully: {first_name} {last_name}")

        booking_id = len(bookings) + 1

        bookings[booking_id] = {
            "student_id" : student_id,
            "subject": subject,
            "date": date,
            "status": "SCHEDULED"
        }

        print(f"Booking Added Successfully: Booking # {len(bookings)}")
        

    elif choice == "2":
        print("\nExisting Bookings: \n")


        if not bookings:
            print("No Booking's Available! ")

        else:
            for booking_id, booking in bookings.items():
                print(f"Booking Number: # {booking_id}")

                student_id = booking['student_id']
                student = students[student_id]

                print(f"Student: {student['first_name']} {student['last_name']}")
                print(f"Subject: {booking['subject']}")
                print(f"Date: {booking['date']}")
                print(f"Status: {booking['status']}")


    elif choice == "3":
        try:
            booking_id = int(input("\nEnter Booking ID to cancel: "))

            if booking_id not in bookings:
                print("Booking ID does not exist.")

            elif bookings[booking_id]["status"] == "CANCELLED":
                print("This booking is already cancelled.")

            else:
                bookings[booking_id]["status"] = "CANCELLED"
                print(f"Booking # {booking_id} cancelled successfully.")

        except ValueError:
            print("Invalid input. Please enter a numeric booking ID.")

    elif choice == "4":
        print("End Of Program")
        break

    else:
        print("Invalid option.")
