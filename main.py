from datetime import datetime

students = {}
bookings = {}
yearly_counters = {
    "students": {},
    "bookings":{}
}

HOURLY_RATE = 50

def validate_appointment(date_input, time_input):

    combined_date = date_input + ":" + time_input
    try:
        appointment = datetime.strptime(combined_date, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Invalid Date or Time. Please use YYYY-MM-DD and HH:MM")
        return False


    today = datetime.now().date()
    now = str(datetime.now().hour) +":"+ str(datetime.now().minute) 

    if appointment < today:
        print(f"You cannot book an appointment in the past. Enter Date Past {today} and a time past {now}")
        return False

    return True


def generate_student_id ():
    year_str = str(datetime.now().year)

    prefix = year_str[0] + year_str[2:]

    count = yearly_counters["students"].get(prefix, 0) + 1

    yearly_counters['students'][prefix] = count

    sequence = str(count + 1).zfill(3)

    return int(prefix + sequence)

def generate_booking_id ():
    year_str = str(datetime.now().year)
    
    prefix = year_str[0] + year_str[2:]
    
    count = yearly_counters["bookings"].get(prefix, 0) + 1
    
    yearly_counters['bookings'][prefix] = count
    
    sequence = str(count + 1).zfill(2)
    
    return int(prefix + sequence)

def add_student(students):

    first_name = input("First name: ")
    last_name = input("Last name: ")
                
    level = input("Level (HS/Uni): ").strip().lower()
    
    if level in ["hs", "high school", "highschool"]:
        level = 'hs'
    
    elif level in ["uni", "university"]:
        level = 'uni'
    
    else:
        print("Invalid education level.")
        return
    
    
    student_id = generate_student_id()
    
    students[student_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "level": level,
    } 
    print(
        f"Student Added Successfully: "
        f"ID #{student_id} {first_name} {last_name}"
    )
    
    return

def calculate_price (hours):
    total = hours * HOURLY_RATE
    return total


def add_booking(students, bookings):

    try:
        student_id = int(input("Please Enter Your Student ID: "))
    except ValueError:
        print("Invalid ID. Please Enter A Number.")
        return 
    
    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print(f"Booking for: {student['first_name']} {student['last_name']}")


    if student["level"] == "hs":
        subjects = ["math", "english", "science"]
    else: 
        subjects = ["dsa", "dta"]


    print("Available subjects:", ", ".join(subjects))
                
    subject = input("Choose a subject: ").strip().lower()
                
    if subject not in subjects:
        print("Invalid subject.")
        return
    
                
    date_input = input("Appointment Date (YYYY-MM-DD): ").strip()
    time_input = input("Appointment Start Time(HH:MM): ").strip()

    if not validate_appointment(date_input, time_input):
        return
    
    
    try:
        duration = float(input("Enter a lesson duration (Min: 1 hour / Max: 2 hours): "))
    except ValueError:
        print("Please enter a valid number!")
        return

    if duration < 1 or duration > 2:
        print("Please Enter Hours No Less Than 1 and No More Than 2: ")
        return

    total_price = calculate_price(duration)

    print(f"\nBooking Summary: \n")
    print(f"Student : {student['first_name']} {student['last_name']}")
    print(f"Subject: {subject}")
    print(f"Date: {date_input}")
    print(f"Start Time: {time_input}")
    print(f"Duration: {duration} hour(s)")
    print(f"Hourly Rate: N${HOURLY_RATE:.2f}")
    print(f"Total Price: N${total_price:.2f}")

    confirmation = input("\nConfirm Booking? (Yes/No): ").strip().lower()

    if confirmation not in ["yes", "y"]:
        print("Booking Cancelled")
        return
                    
    booking_id = generate_booking_id()
    
    bookings[booking_id] = {
        "student_id" : student_id,
        "subject": subject,
        "date": date_input,
        "start_time": time_input,
        "duration": duration,
        "hourly_rate": HOURLY_RATE,
        "total_price": total_price,
        "status": "SCHEDULED"
    }
    
    print(f"Booking Added Successfully: Booking # {booking_id}")



def view_students(students):
    if not students:
        print("No Registered Students!")
        return 

    print("\nRegistered Students: ")
    for student_id, student in students.items():

        print(f"\nStudent ID: {student_id}")
        print(f"Student First Name: {student['first_name']}")
        print(f"Student Last Name: {student['last_name']}")
        print(f"Education Level: {student['level']}")

def view_bookings ():

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
            print(f"Start Time: {booking['start_time']}")
            print(f"Rate: {booking['hourly_rate']:.2f}")
            print(f"Lesson Duration (Hours): {booking['duration']}")
            print(f"Total Due: {booking['total_price']}")
            print(f"Status: {booking['status']}")


def cancel_booking ():
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


while True:
    print("\nWelcome To BookIt")
    print("1. Add a New Student")
    print("2. View Students")
    print("3. Create Booking")
    print("4. View Bookings")
    print("5. Cancel Booking")
    print("6. Exit")

    choice = input("\nSelect an option: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        add_booking(students, bookings)

    elif choice == "4":
        view_bookings()

    elif choice == "5":
        cancel_booking()

    elif choice == "6":
        print("End Of Program")
        break

    else:
        print("Invalid option.")
