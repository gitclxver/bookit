from datetime import datetime


def validate_date(date_input):
    try:
        appointment_date = datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        return False

    today = datetime.now().date()

    if appointment_date < today:
        return False

    return True


def validate_time(time_input):
    try:
        appointment_start_time = datetime.strptime(time_input, "%H:%M").time()
    except ValueError:
        return False

    current_time = datetime.now().time().replace(second=0, microsecond=0)

    if appointment_start_time < current_time:
        return False

    return True

def validate_appointment(date_input, time_input):

    combined = date_input + " " + time_input

    appointment = datetime.strptime(combined, "%Y-%m-%d %H:%M")

    print(appointment)

# validate_appointment()
time_input = "22:30"

time = validate_time(time_input)

if time == True:
    print("Booked")
else:
    print("Time Invalid")


now = str(datetime.now().hour) +":"+ str(datetime.now().minute) 
print(now)